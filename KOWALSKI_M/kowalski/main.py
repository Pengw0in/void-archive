import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord import app_commands
import random
import os
import base64
import hashlib
import string
from cryptography.fernet import Fernet


# Load environment variables from .env file
load_dotenv()
token = os.getenv("BOT_TOKEN")


intents = discord.Intents.all()
bot = commands.Bot(
    command_prefix="/",  # Change to desired prefix
    heartbeat_timeout=150.0,
  intents=intents #intents
)
   
@bot.event
async def on_ready():
    await bot.tree.sync()
    custom_status = discord.CustomActivity(name="Encrypting your texts!")
    await bot.change_presence(status=discord.Status.online, activity=custom_status)
    print(f'We have logged in as {bot.user}')


# Replace slash command with hybrid command
@bot.hybrid_command(name="about", description="Get information about this bot.")
async def about(ctx):
    embed = discord.Embed(
        title="Purpose of This Guardian",
        description="A steadfast guardian of your messages, dedicated to the encryption and decryption of text. With unwavering precision, I ensure your communications remain secure, accessible only to those you trust.",
        color=discord.Color.dark_gold()
    )
    await ctx.send(embed=embed)  # Use ctx.send for compatibility
    
# Morse code dictionary with letters, numbers, and additional symbols
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', '@': '.--.-.', '!': '-.-.--', ':': '---...',
    '=': '-...-', '+': '.-.-.', '&': '.-...'
}

# Reverse the Morse code dictionary to handle decoding
MORSE_TO_TEXT_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

# Function to convert text to Morse code (encryption)
def text_to_morse(text):
    morse_code = []
    for char in text:
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        elif char == ' ':
            morse_code.append('/')  # Use '/' to separate words in Morse
        else:
            morse_code.append('?')  # Unknown characters become '?'
    return ' '.join(morse_code)

# Function to convert Morse code to text (decryption)
def morse_to_text(morse):
    words = morse.split(' / ')
    decoded_message = []
    for word in words:
        decoded_word = []
        for code in word.split():
            decoded_word.append(MORSE_TO_TEXT_DICT.get(code, '?'))
        decoded_message.append(''.join(decoded_word))
    return ' '.join(decoded_message)

# Caesar Cipher functions
def caesar_encrypt(text, shift):
    encrypted = []
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted.append(chr((ord(char) - shift_amount + shift) % 26 + shift_amount))
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def caesar_decrypt(text, shift):
    decrypted = []
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted.append(chr((ord(char) - shift_amount - shift) % 26 + shift_amount))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# Binary encoding/decoding
def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    try:
        return ''.join(chr(int(b, 2)) for b in binary.split())
    except ValueError:
        return "Invalid binary input!"

# Base64 Encryption (Encoding)
def base64_encrypt(message: str) -> str:
    encoded_bytes = base64.b64encode(message.encode('utf-8'))
    return encoded_bytes.decode('utf-8')

# Base64 Decryption (Decoding)
def base64_decrypt(encoded_message: str) -> str:
    decoded_bytes = base64.b64decode(encoded_message.encode('utf-8'))
    return decoded_bytes.decode('utf-8')

# Base16 (Hexadecimal) Encryption (Encoding)
def base16_encrypt(message: str) -> str:
    encoded_hex = message.encode('utf-8').hex()
    return encoded_hex

# Base16 (Hexadecimal) Decryption (Decoding)
def base16_decrypt(encoded_hex: str) -> str:
    decoded_bytes = bytes.fromhex(encoded_hex)
    return decoded_bytes.decode('utf-8')

# Vigenère cipher encryption/decryption
def vigenere_encrypt(text, key) -> str:
    encrypted = []
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            shift_amount = 65 if char.isupper() else 97
            encrypted.append(chr((ord(char) - shift_amount + shift) % 26 + shift_amount))
            key_index += 1
        else:
            encrypted.append(char)
    return ''.join(encrypted)

def vigenere_decrypt(text, key) -> str:
    decrypted = []
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            shift_amount = 65 if char.isupper() else 97
            decrypted.append(chr((ord(char) - shift_amount - shift) % 26 + shift_amount))
            key_index += 1
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# rotn Cipher encryption
def rotn_encryption(text, n):
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    
    # Create translation tables
    shifted_upper = alphabet_upper[n:] + alphabet_upper[:n]
    shifted_lower = alphabet_lower[n:] + alphabet_lower[:n]
    
    translation_table = str.maketrans(alphabet_upper + alphabet_lower, shifted_upper + shifted_lower)
    
    return text.translate(translation_table)

#rotn Cipher decryption
def rotn_decryption(text , n):
    return rotn_encryption(text, -n)
        

# Reverse text function
def reverse_text(text):
    return text[::-1]

# Hashing functions (MD5 and SHA-256)
def hash_md5(text):
    return hashlib.md5(text.encode()).hexdigest()

def hash_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Function to generate a key for AES encryption
def generate_aes_key():
    return Fernet.generate_key()

# AES encryption and decryption
def aes_encrypt(text, key):
    fernet = Fernet(key)
    return fernet.encrypt(text.encode()).decode()

def aes_decrypt(token, key):
    fernet = Fernet(key)
    return fernet.decrypt(token.encode()).decode()

#Combined Analysis
def combined_analysis(message: str):
    # Text Analysis
    char_count = len(message)
    word_count = len(message.split())

    # Frequency Analysis
    frequency = {}
    for char in message:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return char_count, word_count, frequency


# Hash comparison function
def calculate_similarity(hash1, hash2):
    """Calculate the similarity percentage between two hashes."""
    # Initialize a counter for matching characters
    matches = 0
    
    # Compare each character in both hashes
    for i in range(min(len(hash1), len(hash2))):
        if hash1[i] == hash2[i]:
            matches += 1

    # Calculate similarity percentage
    similarity_percentage = (matches / max(len(hash1), len(hash2))) * 100
    return similarity_percentage


# Function to generate a random substitution cipher
def random_substitution_cipher(text):
    alphabet = string.ascii_letters  # Includes both upper and lower case letters
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    cipher_map = str.maketrans(alphabet, ''.join(shuffled))
    return text.translate(cipher_map)

# Function for salted hashing
def salted_hash(message):
    salt = os.urandom(16).hex()  # Generate a random salt
    salted_message = message + salt
    hashed_message = hash_sha256(salted_message)  # Use SHA-256 from previous functions
    return f"{hashed_message}:{salt}"  # Return hash and salt



# Commands

# Morse Code encryption and decryption
@bot.hybrid_command(name='me', description='Converts text to Morse code.')
async def morse_encrypt(ctx, message: str):
    morse_code = text_to_morse(message)
    embed = discord.Embed(
        title="Morse Code Encryption",
        description=f"**Text**: {message}\n**Morse Code**: {morse_code}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

@bot.hybrid_command(name='md', description='Converts Morse code back to text.')
async def morse_decrypt(ctx, message: str):
    text_message = morse_to_text(message)
    embed = discord.Embed(
        title="Morse Code Decryption",
        description=f"**Morse Code**: {message}\n**Decoded Message**: {text_message}",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

# Caesar cipher encryption and decryption
@bot.hybrid_command(name='ce', description='Encrypts text using the Caesar Cipher.')
async def caesar_encrypt_command(ctx, message: str, shift: int):
    encrypted_message = caesar_encrypt(message, shift)
    embed = discord.Embed(
        title="Caesar Cipher Encryption",
        description=f"**Text**: {message}\n**Shift**: {shift}\n**Encrypted Message**: {encrypted_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

@bot.hybrid_command(name='cd', description='Decrypts a Caesar Cipher text.')
async def caesar_decrypt_command(ctx, message: str, shift: int):
    decrypted_message = caesar_decrypt(message, shift)
    embed = discord.Embed(
        title="Caesar Cipher Decryption",
        description=f"**Encrypted Message**: {message}\n**Shift: {shift}**\n**Decrypted Message**: {decrypted_message}",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

# Binary encryption and decryption
@bot.hybrid_command(name='b2e', description='Converts text to binary format.')
async def binary_encrypt_command(ctx, message: str):
    binary_message = text_to_binary(message)
    embed = discord.Embed(
        title="Binary Encryption",
        description=f"**Text**: {message}\n**Binary Message**: {binary_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

@bot.hybrid_command(name='b2d', description='Converts binary back to text.')
async def binary_decrypt_command(ctx, message: str):
    text_message = binary_to_text(message)
    embed = discord.Embed(
        title="Binary Decryption",
        description=f"**Binary Message**: {message}\n**Text**: {text_message}",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

# Base64 Command for Encryption
@bot.hybrid_command(name='b64e', description='Encodes text using Base64.')
async def base64_encrypt_command(ctx, message: str):
    encoded_message = base64_encrypt(message)
    embed = discord.Embed(
        title="Base64 Encryption",
        description=f"**Text**: {message}\n**Encoded Message**: {encoded_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# Base64 Command for Decryption
@bot.hybrid_command(name='b64d', description='Decodes a Base64-encoded message.')
async def base64_decrypt_command(ctx, encoded_message: str):
    try:
        decoded_message = base64_decrypt(encoded_message)
        embed = discord.Embed(
            title="Base64 Decryption",
            description=f"**Encoded Message**: {encoded_message}\n**Decoded Message**: {decoded_message}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Base16 Command for Encryption
@bot.hybrid_command(name='b16e', description='Encodes text using hexadecimal.')
async def base16_encrypt_command(ctx, message: str):
    encoded_hex = base16_encrypt(message)
    embed = discord.Embed(
        title="Base16 (Hexadecimal) Encryption",
        description=f"**Text**: {message}\n**Encoded Hex**: {encoded_hex}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# Base16 Command for Decryption
@bot.hybrid_command(name='b16d', description='Decodes a hexadecimal-encoded message.')
async def base16_decrypt_command(ctx, encoded_hex: str):
    try:
        decoded_message = base16_decrypt(encoded_hex)
        embed = discord.Embed(
            title="Base16 (Hexadecimal) Decryption",
            description=f"**Encoded Hex**: {encoded_hex}\n**Decoded Message**: {decoded_message}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Vigenère cipher encryption
@bot.hybrid_command(name='ve', description='Encrypts text using the Vigenère cipher.')
async def vigenere_encrypt_command(ctx, key: str, message: str):
    encrypted_message = vigenere_encrypt(message, key)
    embed = discord.Embed(
        title="Vigenère Cipher Encryption",
        description=f"**Text**: {message}\n**Encrypted Message**: {encrypted_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# Vigenère cipher decryption
@bot.hybrid_command(name='vd', description='Decrypts a Vigenère cipher text.')
async def vigenere_decrypt_command(ctx, key: str, message: str):
    decrypted_message = vigenere_decrypt(message, key)
    embed = discord.Embed(
        title="Vigenère Cipher Decryption",
        description=f"**Encrypted Message**: {message}\n**Decrypted Message**: {decrypted_message}",
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

# rotn encryption
@bot.hybrid_command(name='re', description='Encrypts text using rotn.')
async def rotn_command(ctx, message: str, n: int):
    transformed_message = rotn_encryption(message, n)
    embed = discord.Embed(
        title="rotn",
        description=f"**Text**: {message}\n**Transformed Message**: {transformed_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

#rotn decryption
@bot.hybrid_command(name='rd', description='Decrypts text using rotn.')
async def rotn_command(ctx, message: str, n: int):
    transformed_message = rotn_decryption(message, n)
    embed = discord.Embed(
        title="rotn",
        description=f"**Text**: {message}\n**Transformed Message**: {transformed_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# Reverse text command
@bot.hybrid_command(name='reverse', description='Reverses the given text.')
async def reverse_command(ctx, message: str):
    reversed_message = reverse_text(message)
    embed = discord.Embed(
        title="Reverse Text",
        description=f"**Text**: {message}\n**Reversed Message**: {reversed_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# Hashing (MD5 and SHA-256)
@bot.hybrid_command(name='hashmd5', description='Generates an MD5 hash of the text.')
async def hash_md5_command(ctx, message: str):
    hashed_message = hash_md5(message)
    embed = discord.Embed(
        title="MD5 Hash",
        description=f"**Text**: {message}\n**MD5 Hash**: {hashed_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

@bot.hybrid_command(name='hashsha256', description='Generates a SHA-256 hash of the text.')
async def hash_sha256_command(ctx, message: str):
    hashed_message = hash_sha256(message)
    embed = discord.Embed(
        title="SHA-256 Hash",
        description=f"**Text**: {message}\n**SHA-256 Hash**: {hashed_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# Random Substitution Cipher
@bot.hybrid_command(name='rsc', description='Encrypts text using a random substitution cipher.')
async def random_substitution_cipher_command(ctx, message: str):
    ciphered_message = random_substitution_cipher(message.lower())
    embed = discord.Embed(
        title="Random Substitution Cipher",
        description=f"**Text**: {message}\n**Ciphered Text**: {ciphered_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# Salted Hash command
@bot.hybrid_command(name='sh', description='Generates a salted SHA 256 hash')
async def salted_hash_command(ctx, message: str):
    salted_hashed_message = salted_hash(message)
    embed = discord.Embed(
        title="Salted Hash",
        description=f"**Text**: {message}\n**Salted Hash**: {salted_hashed_message}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# AES encryption command
@bot.hybrid_command(name='aese', description='Encrypts text using AES encryption.')
async def aes_encrypt_command(ctx, message: str):
    key = generate_aes_key()  # Generate a new AES key
    encrypted_message = aes_encrypt(message, key)
    embed = discord.Embed(
        title="AES Encryption",
        description=f"**Original Text**: {message}\n**Encrypted Message**: {encrypted_message}\n**Key**: {key.decode()}",
        color=discord.Color.dark_teal()
    )
    await ctx.send(embed=embed)

# AES decryption command
@bot.hybrid_command(name='aesd', description='Decrypts an AES-encrypted message.')
async def aes_decrypt_command(ctx, key: str, token: str):
    try:
        decrypted_message = aes_decrypt(token, key)
        embed = discord.Embed(
            title="AES Decryption",
            description=f"**Encrypted Message**: {token}\n**Decrypted Message**: {decrypted_message}",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Combined command for Text & Frequency Analysis
@bot.hybrid_command(name='analysis', description='Performs a text and frequency analysis of the message.')
async def combined_analysis_command(ctx, message: str):
    char_count, word_count, frequency = combined_analysis(message)
    
    # Formatting frequency analysis output
    freq_list = "\n".join([f"{char}: {count}" for char, count in frequency.items()])
    
    # Create an embed message with both results
    embed = discord.Embed(
        title="Text & Frequency Analysis",
        description=f"**Text**: {message}\n\n"
                    f"**Character Count**: {char_count}\n"
                    f"**Word Count**: {word_count}\n\n"
                    f"**Character Frequencies**:\n{freq_list}",
        color=discord.Color.dark_teal()
    )
    
    await ctx.send(embed=embed)

# Hash comparison command
@bot.hybrid_command(name='ch', description='Compares two hashes and calculates the similarity percentage.')
async def compare_hashes(ctx, hash1: str, hash2: str):
    """Compare two hashes and provide similarity percentage."""
    similarity_percentage = calculate_similarity(hash1, hash2)

    # Format the output with a pipe separator
    result_message = f"**Hashes**: {hash1} | {hash2}\n"
    result_message += f"**Similarity**: {similarity_percentage:.2f}%"

    # Create an embed for the output
    embed = discord.Embed(
        title="Hash Comparison Result",
        description=result_message,
        color=discord.Color.red()
    )
    await ctx.send(embed=embed)

# Combined Encryption/Decryption command
@bot.hybrid_command(name='combo', description='Applies multiple encryption/decryption methods to the text.')
async def combo(ctx, methods: str, message: str):
    try:
        method_list = methods.split(' ')
        current_text = message
        description = f"**Original Text**: {message}\n"
        for method in method_list:
            if method == 'ce':
                current_text = caesar_encrypt(current_text)
                description += f"**Caesar Cipher**: {current_text}\n"
            elif method == 'cd':
                current_text = caesar_decrypt(current_text)
                description += f"**Caesar Cipher Decryption**: {current_text}\n"
            elif method == 'b64e':
                current_text = base64_encrypt(current_text)
                description += f"**Base64 Encoding**: {current_text}\n"
            elif method == 'b64d':
                current_text = base64_decrypt(current_text)
                description += f"**Base64 Decoding**: {current_text}\n"
            elif method == 'b16e':
                current_text = base64.b16encode(current_text.encode()).decode()
                description += f"**Base16 Encoding**: {current_text}\n"
            elif method == 'b16d':
                current_text = base64.b16decode(current_text.encode()).decode()
                description += f"**Base16 Decoding**: {current_text}\n"
            elif method == 'b2e':
                current_text = text_to_binary(current_text)
                description += f"**Binary Encoding**: {current_text}\n"
            elif method == 'b2d':
                current_text = binary_to_text(current_text)
                description += f"**Binary Decoding**: {current_text}\n"
            elif method == 'me':
                current_text = text_to_morse(current_text)
                description += f"**Morse Code Encoding**: {current_text}\n"
            elif method == 'md':
                current_text = morse_to_text(current_text)
                description += f"**Morse Code Decoding**: {current_text}\n"
            elif method == 'reverse':
                current_text = reverse_text(current_text)
                description += f"**Reverse text**: {current_text}\n"
        embed = discord.Embed(
            title="Combo",
            description=description,
            color=discord.Color.dark_teal()
        )
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

bot.remove_command('help')
# Custom Help Command
@bot.hybrid_command(name='help', description='Displays the list of available commands.')
async def help_command(ctx):
    embed = discord.Embed(
        title="Help - Command List",
        description="Here are the available commands and their descriptions:",
        color=discord.Color.dark_gold()
    )
    
    # Adding command explanations
    embed.add_field(
        name="Morse Code Encryption (`/me`)", 
        value="Converts text to Morse code.\nUsage: `/me <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Morse Code Decryption (`/md`)", 
        value="Converts Morse code back to text.\nUsage: `/md <morse>`", 
        inline=False
    )
    
    embed.add_field(
        name="Caesar Cipher Encryption (`/ce`)", 
        value="Encrypts text using the Caesar Cipher.\nUsage: `/ce <message> <shift>`", 
        inline=False
    )
    
    embed.add_field(
        name="Caesar Cipher Decryption (`/cd`)", 
        value="Decrypts a Caesar Cipher text.\nUsage: `/cd <encrypted_message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Binary Encryption (`/b2e`)", 
        value="Converts text to binary format.\nUsage: `/b2e <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Binary Decryption (`/b2d`)", 
        value="Converts binary back to text.\nUsage: `/b2d <binary_message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Base64 Encryption (`/b64e`)", 
        value="Encodes text using Base64.\nUsage: `/b64e <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Base64 Decryption (`/b64d`)", 
        value="Decodes a Base64-encoded message.\nUsage: `/b64d <encoded_message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Base16 (Hex) Encryption (`/b16e`)", 
        value="Encodes text using hexadecimal.\nUsage: `/b16e <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Base16 (Hex) Decryption (`/b16d`)", 
        value="Decodes a hexadecimal-encoded message.\nUsage: `/b16d <encoded_hex>`", 
        inline=False
    )
    
    embed.add_field(
        name="Vigenère Cipher Encryption (`/ve`)", 
        value="Encrypts text using the Vigenère cipher.\nUsage: `/ve <key> <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Vigenère Cipher Decryption (`/vd`)", 
        value="Decrypts a Vigenère cipher text.\nUsage: `/vd <key> <encrypted_message>`", 
        inline=False
    )
    
    embed.add_field(
        name="rotn Cipher encryption (`/re`)", 
        value="Encrypts text using rotn.\nUsage: `/rotn <message> <shift>`", 
        inline=False
    )

    embed.add_field(
        name="rotn Cipher decryption (`/rd`)", 
        value="Decrypts text using rotn.\nUsage: `/rotn <message> <shift>`", 
        inline=False
    )
    
    embed.add_field(
        name="Reverse Text (`/reverse`)", 
        value="Reverses the given text.\nUsage: `/reverse <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="MD5 Hashing (`/hashmd5`)", 
        value="Generates an MD5 hash of the text.\nUsage: `/hashmd5 <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="SHA-256 Hashing (`/hashsha256`)", 
        value="Generates a SHA-256 hash of the text.\nUsage: `/hashsha256 <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Random Substitution Cipher (`/rsc`)", 
        value="Encrypts text using a random substitution cipher.\nUsage: `/rsc <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Salted Hashing (`/sh`)", 
        value="Generates a salted SHA-256 hash of the text.\nUsage: `/sh <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="AES Encryption (`/AESe`)", 
        value="Encrypts text using AES encryption.\nUsage: `/AESe <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="AES Decryption (`/AESd`)", 
        value="Decrypts an AES-encrypted message.\nUsage: `/AESd <key> <token>`", 
        inline=False
    )
    
    embed.add_field(
        name="Text & Frequency Analysis (`/analysis`)", 
        value="Performs a text and frequency analysis of the message.\nUsage: `/analysis <message>`", 
        inline=False
    )
    
    embed.add_field(
        name="Hash Comparison (`/CH`)", 
        value="Compares two hashes and calculates the similarity percentage.\nUsage: `/CH <hash1> <hash2>`", 
        inline=False
    )
    
    embed.add_field(
        name="Combined Encryption/Decryption (`/combo`)", 
        value="Applies multiple encryption/decryption methods to the text.\nUsage: `/combo <method1,method2,...> <message>`", 
        inline=False
    )

    # Send the embed to the Discord channel
    await ctx.send(embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} You do not have permission to use this command.")
    elif isinstance(error, commands.NotOwner):
        await ctx.send(f"{ctx.author.mention} Only the owner of the bot can use this command.")

# Run the bot with your token
bot.run(token)
