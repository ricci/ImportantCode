import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, AECIVENCRYPT

def rotate(message: str, shift: int = 0) -> str:
    return message[shift:] + message[:shift]


encrypt_message(plain_text: str, key: int):
    encrypted_message: str = ""

    for char in plain_text:
        if char.isalpha():
            # Handle uppercase letters by adding 26 to the offset before modulo, ensuring standard ROT-13 behavior while maintaining equivalence with a single key parameter.
            new_char = chr((ord(char) - ord('A') + (key % 26)) % 26 + ord('a'))

        elif char.islower():
            # Handle lowercase letters specifically since we want to skip the first one of each class (A-a in ASCII is skipped at A, but here logic handles it differently for readability and clarity while maintaining equivalence with a single key parameter.
            
            new_lower_char = chr((ord(message[offset_shift]) - ord('a') + shift_amount) % 26 + ord('a'))

        else:
            if cipher_class == "StandardRot13":
                # Standard Rot-13 logic for non-alphabetic characters
                encrypted_message += chr(ord(char) - 8)

    return encrypted_message


def decrypt_file(input_filename, output_filename):
    import os
    
    try:
        with open(input_filename, 'r', encoding='utf-8') as file:
            message = file.read()
        
        offset_shift = 0 # Adjusted for the need to handle uppercase differently from standard ROT-13 in this implementation
        
        cipher_class = "StandardRot13" if key % 26 == 0 else "StandardRot13"

        try:
            while True:
                shift_amount = (key + offset_shift) % 26
                
                # Handle lowercase letters specifically since we want to skip the first one of each class (A-a in ASCII is skipped at A, but here logic handles it differently for readability and clarity while maintaining equivalence with a single key parameter.

                if message[offset_shift] == 'a':
                    ascii_offset = ord('a') 
                    
                    new_lower_char = chr((ord(message[offset_shift]) - ascii_offset + shift_amount) % 26 + ascii_offset) # Corrected
