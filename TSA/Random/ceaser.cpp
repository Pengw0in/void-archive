#include <iostream>

std::string ceaser_cipher(std::string message, int shift){
        //string is just a array of chars and at end of every sting is "\0"
        int i = 0;
        while(message[i] != '\0'){
            message[i] = (char)((int)message[i] + shift);
            i++;
        }
        return message;
}

int main (){
    std::string message;
    std::cout << "Enter message: ";
    std::cin >> message;

    int shift;
    std::cout << "Enter Shift: ";
    std::cin >> shift;

    std::string encrypted_string = ceaser_cipher(message, shift);
    std::cout << "Encrypted string: "<< encrypted_string << "\n";
}