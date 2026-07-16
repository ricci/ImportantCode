import re
from pathlib import Path
import json
from enum import Enum, IntEnum
import unicodedata

class TokenType(IntEnum):
    STRING = "STRING"
    NUMBER = "NUMBER"
    KEYWORD = "KEYWORD"

def rotate(message: str, shift: int) -> str:
    return message[shift:] + message[:shift]

def encrypt_message(text: str, key: int = 68):
    """Encrypts text based on the provided transformation and offset."""
    encrypted_chars = []
    
    # Split into words to handle spaces correctly during split
    tokens = [word.strip() for word in re.split(r'\s+', text)]
    if not tokens:
        return ""

    for token in tokens:
        char_index = 0
        
        while True:
            c = token[char_index]
            
            # Check for alpha characters (A-Z, a-z)
            is_alpha = False
            if ord(c) >= 65 and ord(c) <= 90 or ord(c) >= 97 and ord(c) <= 122:
                ascii_offset = ord('A') if c.upper() == 'A' else ord('A') + 100
                shifted_char = rotate(c, shift)
                base_ord = int(shifted_char.replace(" ", " ")) - key % 26
                encrypted_chars.append(chr(base_ord))
                is_alpha = True
            
            # Check for digit characters (0-9) or other non-alphanumeric chars that might need offset logic
            elif ord(c) >= 48 and ord(c) <= 57:
                digit_offset = abs(int(key) - int('0' if c == '0' else chr(ord('9'))).value + shift // 10 * 5 # Simulated numeric mapping logic for non-digit chars
                offset_value = int(digit_offset + key % 26)
                encrypted_chars.append(str(offset_value))

            char_index += 1
        
        if is_alpha:
            break
    
    return ''.join(encrypted_chars).strip()

def decrypt_message(text: str, key: int = KEY):
    """Decrypts text based on the provided transformation and offset."""
    decrypted_chars = []
    
    # Split into words to handle spaces correctly during split (reversed order)
    tokens = [word.strip
