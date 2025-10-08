#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Structure to represent a mapping from character to Morse code
typedef struct {
    char character;
    char* morse_code;
} MorseMapping;

// Array of mappings (our "map" equivalent)
MorseMapping morse_map[] = {
    {'A', ".-"}, {'B', "-..."}, {'C', "-.-."}, {'D', "-.."}, {'E', "."}, {'F', "..-."},
    {'G', "--."}, {'H', "...."}, {'I', ".."}, {'J', ".---"}, {'K', "-.-"}, {'L', ".-.."},
    {'M', "--"}, {'N', "-."}, {'O', "---"}, {'P', ".--."}, {'Q', "--.-"}, {'R', ".-."},
    {'S', "..."}, {'T', "-"}, {'U', "..-"}, {'V', "...-"}, {'W', ".--"}, {'X', "-..-"},
    {'Y', "-.--"}, {'Z', "--.."},
    {'1', ".----"}, {'2', "..---"}, {'3', "...--"}, {'4', "....-"}, {'5', "....."},
    {'6', "-...."}, {'7', "--..."}, {'8', "---.."}, {'9', "----."}, {'0', "-----"},
    {' ', "/"}, {'.', ".-.-.-"}, {',', "--..--"}, {'?', "..--.."}, {'!', "-.-.--"},
    {'(', "-.--."}, {')', "-.--.-"}, {'&', ".-..."}, {':', "---..."}, {';', "-.-.-."},
    {'+', ".-.-."}, {'-', "-....-"}, {'/', "-..-."}, {'=', "-...-"}
};

// Get the size of our mapping array
const int MORSE_MAP_SIZE = sizeof(morse_map) / sizeof(morse_map[0]);

// Function to find a morse code for a given character
char* find_morse_code(char c) {
    c = toupper(c); // Convert to uppercase
    
    for (int i = 0; i < MORSE_MAP_SIZE; i++) {
        if (morse_map[i].character == c) {
            return morse_map[i].morse_code;
        }
    }
    return NULL; // Character not found
}

// Function to encrypt text to Morse code
void morse_encrypt(char* text, char* result, int max_result_size) {
    int result_index = 0;
    
    for (int i = 0; text[i] != '\0'; i++) {
        char* morse = find_morse_code(text[i]);
        
        if (morse != NULL) {
            int morse_len = strlen(morse);
            
            // Check if we have enough space in result buffer
            if (result_index + morse_len >= max_result_size - 1) {
                printf("Warning: Result buffer too small, truncating output\n");
                break;
            }
            
            // Copy morse code to result
            strcpy(result + result_index, morse);
            result_index += morse_len;
            
            // Add a space between codes (if not the last character)
            if (text[i+1] != '\0') {
                result[result_index++] = ' ';
            }
        }
    }
    
    result[result_index] = '\0'; // Ensure null termination
}

int main() {
    char input[100];
    char result[500]; // Morse code can be much longer than the input
    
    printf("Input the text: ");
    fgets(input, sizeof(input), stdin);
    
    // Remove trailing newline if present
    size_t len = strlen(input);
    if (len > 0 && input[len-1] == '\n') {
        input[len-1] = '\0';
    }
    
    morse_encrypt(input, result, sizeof(result));
    printf("%s\n", result);
    
    return 0;
}