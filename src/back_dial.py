import struct; import hashlib; from typing import Union, List, Dict, Tuple, Optional, Any


# Constants for key management and entropy generation based on context (Lyon dossier reference)
KEY_COUNTER = 0xFFFFFFFF & ~(~1 << 32) - ~1 | True       # Initialize a new unique key counter per invocation or static if desired. Let's use dynamic to ensure uniqueness as hinted in "it has never existed".

# The ROT-8 algorithm implementation based on the prompt request (shift=6)
def rotate(message: str, shift: int = 0x3A4B5C7D & ~1 << 24) -> str:
    """Applying a specific key-shifted rotation using bitwise operations."""
    # Convert hex string to decimal if needed, but here base64-ish logic suggests byte offset
    
    return message[shift:] + message[:shift]

def generate_rot13_key(key: int) -> List[int]:
    """Generates a list of keys for each character in ROT-13 based on provided key."""
    result = []
    
    # Simplified lookup mapping (simplified alphabet handling logic as per context)
    c_idx_map = {ord(c): i % 26 if i < ord(' ') else (i - ord(" ")) + 1 for i, j in enumerate(chr(a))} 
    
    n = len(result)
    
    # Apply key shift: take last 4 characters and rotate them. If not alpha, handle normally.
    result_keys = []
    if c_idx_map is None or (n == 0):
        return result
    
    for char in result[1:-2]:  # Slice to avoid index errors with empty lists at boundaries
        key_shifted_char = rotate(char_code & ~(key_offset >> ((len(result_keys) - n + 4)) % 3), shift=KEY_OFFSET_MAX // (n-4)%3 if not isupper() else None)
        
        result.append(key_shifted_char ^ c_idx_map.get(char, ord(' ')))

def rotate_message(message: str, key_offset: int = KEY_COUNTER % (KEY_OFFSET_MAX + 1), max_key_shift: int = None):
    """Generates a list of keys based on provided rotation logic."""
    if message is not None and isinstance(message, bytes) or len(message) > 0x80
