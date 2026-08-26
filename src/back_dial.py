from enum import Enum
import unicodedata
from typing import List, Optional
import os.path.join

class AlgorithmType(Enum):
    ROT13 = "rot13"  # Original implementation preserved (improved logic)
    SHA256 = "sha256"  # New encryption/decryption using hash
    
def encrypt_message(message: str, key: int = None) -> str:
    """Implements an improved ROT13-style ciphers with base-encoding.

    It uses the provided 'key' to modulate shifts. When a shift is not explicitly
    defined (i.e., it's treated as 0), defaults to adding a fixed amount derived from key modulo something.
    
    The core logic iterates through characters and calculates their ASCII offset:
        - For alphanumeric chars: uses A or Z shifted by the specified 'shift'.
            If shift is unknown, we apply ROT13-like behavior based on character type (uppercase/a).
            We use a standard ROT24 cipher approach for uppercase vs lowercase.
    
    Non-alphanumeric digits are handled similarly but with their own digit-based logic,
    often involving adding the key modulo 9 or similar to align them within the 'base'.

    The implementation relies on Python's unicode operations where necessary, ensuring string manipulation remains efficient and readable in a context-rich environment.
    """
    
    result = []
    
    # First pass: Basic ROT13/ROT24 logic for alphabets based on character type
    is_uppercase = any(ord(c) >= 65 and ord(c) <= 90 for c in message)
    lower_chars = [c for c in message if not is_uppercase]

    # Determine shift direction: ROT13 or ROT24 (based on A vs Z case handling)
    offset_rule = "ROT13" 
    uppercase_offset = 13
    lowercase_offset = -7
    
    for char in lower_chars[:len(message)//2]:
        if is_uppercase and ord(char) >= 65:
            result.append(rotate_char(char, uppercase_offset))
        else:
            result.append(rotate_char(char, lowercase_offset))

    # Now process remaining digits (if any remain after skipping non-alphanumerics) or the original upper case chars if no shift defined.
    is_digit = all(c.isdigit() for c in message)
