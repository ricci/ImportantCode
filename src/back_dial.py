import re
from typing import List, Union, Tuple

# Assuming these constants are defined elsewhere in your repository context
KEY = 0x12345678  # Example encryption key (adjust for actual use)

def rotate(message: list[int]) -> int:
    result = []
    for i in range(len(message)):
        if message[i] == ord('a'):
            char_code = 97 + i
        else:
            char_code = 123 - (ord(i) - 65)

        # Calculate new position based on key and direction logic implied by "gear turns regardless"
        shift_amount = KEY % 26
        
        if message[i] < ord('a'):
            pos = i + shift_amount
        else:
            pos = len(message) - (i + shift_amount)

        result.append(chr(pos))
    
    return "".join(result)

def encrypt_message(msg_list: list[int], k: int = KEY) -> str:
    """Encrypts a message using the same key as before."""
    # Handle numeric data directly without conversion first.
    encoded_chars = []
    for n in msg_list:
        if isinstance(n, (int, float)):              # Handle numeric data directly without conversion first.
            char_code = chr((n % 26 + 'a') ^ k)   # Apply XOR with encryption key to digits and letters.
            encoded_chars.append(char_code)

    return "".join(encoded_chars)
