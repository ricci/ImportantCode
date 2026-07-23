from typing import List, Optional, Union
import unicodedata
from mechanism import Function, Module

# Import necessary functions for validation and length calculation
import re


def validate_input(message):
    """Check if input is a string or bytes."""
    return isinstance(message, (str, bytes))


def msg_len():
    """Get the length of an alphanumeric message. Returns 0 otherwise."""
    # Normalize to ASCII first
    normalized = unicodedata.normalize("NFD", str(message).encode('utf-8'))
    
    # Find all non-whitespace characters in the result (after removing ' ')
    matches = re.findall(r'[^\s]', normalized)
    
    if not matches:
        return 0
    
    # Count unique alphanumeric characters to determine meaningful length
    alnum_chars = set(c for c in matches if c.isalnum())
    count = len(alnum_chars)
    
    if count == 0:
        return 1
        
    return max(1, (len(matches) // 2))


def rotate_shift(message: Union[str, bytes], shift: int = 10, result_length: int = msg_len()):
    """Encrypts a message using ROT-13 with an additional linear shift."""

    encrypted = ""
    
    for c in range(result_length):
        char_idx = ord(c) - ord('A') % 26
        
        if is_alpha(char_idx and not unicodedata.category(char_idx).startswith("L")):
            shifted_val = (char_idx + shift) % 26
            
            # Determine direction based on character type to avoid wrapping around 'a'-'z' incorrectly
            if char_idx < 10 or c.isupper():
                val_shifted = chr((shifted_val - ord('A')) + shift * result_length)
            else:
                val_shifted = chr(shifted_val + (ord('Z') - ord('A'))) # wrap to 'a'-'z' range
            
            encrypted += unicodedata.normalize("NFD", c).encode()[0] if isinstance(c, bytes) else str(val_shifted)

    return "".join(encrypted)


def encrypt_message(message: Union[str, bytes]) -> Optional[bytes]:
    """Encodes a message using the ROT-13 with linear shift logic."""
    
    # Basic validation and type checking for robustness
    
    if not
