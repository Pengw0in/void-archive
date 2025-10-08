#include <iostream>
#include <cryptopp/rsa.h>
#include <cryptopp/osrng.h>
#include <cryptopp/files.h>
#include <cryptopp/cryptlib.h>
#include <cryptopp/base64.h>
#include <cryptopp/hex.h>
#include <cryptopp/aes.h>
#include <cryptopp/modes.h>
#include <cryptopp/filters.h>

using namespace CryptoPP;
using namespace std;

int main() {
    AutoSeededRandomPool rng;

    // === Generate RSA key pair
    InvertibleRSAFunction params;
    params.GenerateRandomWithKeySize(rng, 2048);
    RSA::PrivateKey rsaPrivate(params);
    RSA::PublicKey rsaPublic(params);

    // === Generate AES key and IV
    SecByteBlock aesKey(AES::DEFAULT_KEYLENGTH); // 16 bytes
    rng.GenerateBlock(aesKey, aesKey.size());

    SecByteBlock iv(AES::BLOCKSIZE); // 16 bytes IV
    rng.GenerateBlock(iv, iv.size());

    // === Encrypt AES key with RSA
    RSAES_OAEP_SHA_Encryptor rsaEncryptor(rsaPublic);
    string encryptedAesKey;
    StringSource ss1(aesKey, aesKey.size(), true,
        new PK_EncryptorFilter(rng, rsaEncryptor,
            new StringSink(encryptedAesKey)
        )
    );

    // === Encrypt message using AES
    string plaintext = "This is a secret message!";
    string ciphertext;
    CBC_Mode<AES>::Encryption aesEncryptor;
    aesEncryptor.SetKeyWithIV(aesKey, aesKey.size(), iv);

    StringSource ss2(plaintext, true,
        new StreamTransformationFilter(aesEncryptor,
            new StringSink(ciphertext)
        )
    );

    // === Decrypt AES key with RSA
    SecByteBlock decryptedAesKey(AES::DEFAULT_KEYLENGTH);
    RSAES_OAEP_SHA_Decryptor rsaDecryptor(rsaPrivate);
    StringSource ss3(encryptedAesKey, true,
        new PK_DecryptorFilter(rng, rsaDecryptor,
            new ArraySink(decryptedAesKey, decryptedAesKey.size())
        )
    );

    // === Decrypt message with AES
    string recovered;
    CBC_Mode<AES>::Decryption aesDecryptor;
    aesDecryptor.SetKeyWithIV(decryptedAesKey, decryptedAesKey.size(), iv);

    StringSource ss4(ciphertext, true,
        new StreamTransformationFilter(aesDecryptor,
            new StringSink(recovered)
        )
    );

    // === Output
    cout << "Original: " << plaintext << endl;
    cout << "Recovered: " << recovered << endl;

    return 0;
}
