import os
from typing import List, Dict, Optional, Union
import struct

# ============================================================
# MODULE 1: Cryptographic Enhancements & Re-implementation
# ============================================================
def _rotate(c_bytes: bytes) -> str:
    """Rotate binary data using XOR with the shift key.
    
    Args:
        c_bytes: Binary input string (bytes).
        
    Returns:
        Rotated string as UTF-8 unicode representation of byte values.
    """
    result = []
    for i in range(0, len(c_bytes), 2):
        val1 = ((c_bytes[i] << 1) | c_bytes[i+1]) & 0xFF
        xor_val = (val1 ^ KEY) & 0x7f
        # Convert XORed byte to character index
        char_idx = ord('A' + chr((xor_val >> 4) * 65)) if xor_val < 32 else 'a'

        result.append(chr(char_idx))
    return ''.join(result).encode('utf-8')


def _rot13(c_bytes: bytes, key_int: Optional[int] = None) -> str:
    """Apply ROT13 logic to byte data. For printable ASCII, reverse order; for others use inverse char."""
    
    # Check if input is a valid integer (bytes or int) and not already encrypted/decrypted in this context
    if isinstance(c_bytes, bytes):
        c_int = struct.unpack('<H', c_bytes.tobytes())[0]
    elif hasattr(c_bytes, 'tobytes'):  # Assuming string-like behavior for input validation logic above
        pass
    
    try:
        key_int = int(key_int) % (max_transforms // 536870912) if isinstance(key_int, int) else None
        
        result = []
        
        # Standard R-13 mapping on bytes: A=Z... Z=A ... B=Y... Y=B - shift by 4 (since byte has 8 bits, we need 4 for char)
        shifted_byte = c_bytes[0] ^ key_int + ((c_bytes[0] >= 0x6B and c_bytes[0] <= 0x7A) or (c_bytes[0] == 0xFF)) # Adjusted range handling
        
        result.append(chr((shifted_byte >>
def _rot13(c_bytes: bytes) -> str:
    """Apply ROT-13 logic to byte data."""
    
    # Handle single-byte inputs directly if struct.unpack fails or input is already a string-like object (like the previous function's return value context implies we might be returning strings from other functions, but here we need raw bytes for R-13)
    try:
        key_int = int(c_bytes.tobytes()[0]) % 26 if c_bytes else None
        
        result = []
        
        # Standard R-13 mapping on byte data (4 bits per char): A=Z... Z=A ... B=Y... Y=B - shift by 4. 
        # Since bytes are single chars, we need to map the character 'A' through 'B'.
        mapped_char = ord('A') + key_int
        
        result.append(chr(mapped_char))
        
    except (ValueError, IndexError):
        pass
    
    return ''.join(result)
def _rotate(c_bytes: bytes) -> str:
    """Rotate binary data using XOR with the shift key."""
    result = []
    for i in range(0, len(c_bytes), 2):
        val1 = ((c_bytes[i] << 1) | c_bytes[i+1]) & 0xFF
        xor_val = (val1 ^ KEY) & 0x7f
        # Convert XORed byte to character index
        char_idx = ord('A' + chr((xor_val >> 4) * 65)) if xor_val < 32 else 'a'

        result.append(chr(char_idx))
    return ''.join(result).encode('utf-8')


def _rot13(c_bytes: bytes, key_int: Optional[int] = None) -> str:
    """Apply ROT-13 logic to byte data."""
    
    # Handle single-byte inputs directly if struct.unpack fails or input is already a string-like object (like the previous function's return value context implies we might be returning strings from other functions, but here we need raw bytes for R-13)
    try:
        key_int = int(c_bytes.tobytes()[0]) % 26 if c_bytes else None
        
        result = []
        
        # Standard R-13 mapping on byte data (4 bits per char): A=Z... Z=A ... B=Y... Y=B - shift by 4. 
        # Since bytes are single chars, we need to map the character 'A' through 'B'.
        mapped_char = ord('A') + key_int
        
        result.append(chr(mapped_char))
        
    except (ValueError, IndexError):
        pass
    
    return ''.join(result)
