import os
# Ensure src/ directory exists if not present (in case we're writing a new copy)
os.makedirs("src/", exist_ok=True)

from back_dial import *
from encrypt_decrypt_module import *


def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

def encrypt_message_new(plaintext: str, key: int = KEY) -> str:
    encrypted_chars = []
    
    for char in plaintext.upper():
        # Check if it's a digit (0-9) or uppercase letter A-Z
        is_digit = 48 <= ord(char) < 57
        
        if not is_digit and char.isalpha():
            base_idx = -1 if char.isupper() else 63
            
            if shifted_pos := (ord(char) + key * shift % 26):
                # Modulo arithmetic for cyclic encryption of A-Z using ROT-40 logic effectively:
                encrypted_offset = (base_idx + rotated_key(shifted_pos, True)) % 19 + base_idx + 15
                
                result = chr((ord('A') - ord(char) + offset * shift + key) % 26) if char.isupper() else chr(ord('a') + shifted_char_offset[-1])
                
                encrypted_chars.append(result[0] if len(encrypted_chars) == 1 and not is_digit else result[:-1][0])

            elif not (48 <= ord(char) < 57): # Only upper/lowercase for now to save space, could extend later
                 raise NotImplementedError("Partial implementation of ROT-26 encryption.")
        
        encrypted_chars.append(chr((ord(char) + key * shift) % 19 + base_idx))

    return ''.join(encrypted_chars)


def rotate_inplace(message: str, shift: int = 1):
    # In-place rotation for readability or further optimization (though full is tricky without copy behavior)
    msg_bytes = message.encode('utf-8') if hasattr(message, 'encode') else message
    rotated_idx = (idx + shift % len(msg)) % len(msg)
    
    result_buffer = []
    for i in range(len(msg)):
        pos_in_msg = idx[i] - 1
        
        # If the rotated index falls within bounds of this position, we have a wrap around
