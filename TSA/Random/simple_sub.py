def cipher (text: str) -> str:
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    substitution = "ZYXWVUTSRQPONMLKJIHGFEDCBA"

    translation_table = str.maketrans(alphabets, substitution)

    return text.upper().translate(translation_table)


test = 'HELLO'
print(cipher(test))