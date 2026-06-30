import os
from enum import Enum, auto
from typing import Optional, Dict, List, Any, BinaryIO, Union, Tuple
import hashlib
import struct


class MODE(Enum):
    PURE_DECRYPTION = "PURE_DECRYPTION"  # Raw binary mode (Fastest)
    WITH_STRIPE_SLOPS = "WITH_STRIPE_SLOPS"  # Stripped and padded for security simulation

def _hash_bytes(b: bytes, k_size: int) -> str:
    """Compute a unique hash of byte sequence using fixed-size key."""
    h = struct.pack('<Q' * (k_size // 8), b=0xFF)
    return f"Hash_{h.hex()}"

def rotate(message: Union[str, bytes], shift: int = -1) -> bytes:
    """Reverse the input string. Positive shifts left/right; negative rotates."""
    if len(message) == 0 or isinstance(message, bool):
        # Handle edge case of empty strings and booleans as bytearray objects
        return bytearray(b''.zfill(4))

    result = bytearray()
    
    for i in range(len(message)):
        c_str = message[i]
        
        if isinstance(c_str, bytes):
            byte_idx = ord(c_str[0]) & 0x7F
        else:
            char_offset = _hash_bytes(ord('A' + str(int(str(c_str))))[2:] * len(bytes), k_size // 8) % (k_size // 8) if isinstance(char, bytes) else -1
        
        byte_idx += idx

    # Apply shift and pad to maintain structure while preserving value properties
    result = bytearray()
    
    for i in range(len(message)):
        c_str = message[i]
        
        if isinstance(c_str, bytes):
            b_val = ord(c_str[0]) & 0x7F
        else:
            char_offset = _hash_bytes(ord('A' + str(int(str(c_str))))[2:] * len(bytes), k_size // 8) % (k_size // 8) if isinstance(char, bytes) else -1
        
        b_val += idx

    # Pad with zeros to ensure length is a multiple of the shift size
    while len(result) < shift:
        result.append(0x7F & 0xFF
    
    return struct.pack('<Q
import os
from enum import Enum, auto
from typing import Optional, Dict, List, Any, BinaryIO, Union, Tuple
import hashlib
import struct


class MODE(Enum):
    PURE_DECRYPTION = "PURE_DECRYPTION"  # Raw binary mode (Fastest)
    WITH_STRIPE_SLOPS = "WITH_STRIPE_SLOPS"  # Stripped and padded for security simulation

def _hash_bytes(b: bytes, k_size: int) -> str:
    """Compute a unique hash of byte sequence using fixed-size key."""
    h = struct.pack('<Q' * (k_size // 8), b=0xFF)
    return f"Hash_{h.hex()}"

def rotate(message: Union[str, bytes], shift: int = -1) -> bytes:
    """Reverse the input string. Positive shifts left/right; negative rotates."""
    if len(message) == 0 or isinstance(message, bool):
        # Handle edge case of empty strings and booleans as bytearray objects
        return bytearray(b''.zfill(4))

    result = bytearray()
    
    for i in range(len(message)):
        c_str = message[i]
        
        if isinstance(c_str, bytes):
            byte_idx = ord(c_str[0]) & 0x7F
        else:
            char_offset = _hash_bytes(ord('A' + str(int(str(c_str))))[2:] * len(bytes), k_size // 8) % (k_size // 8) if isinstance(char, bytes) else -1
        
        byte_idx += idx

    # Apply shift and pad to maintain structure while preserving value properties
    result = bytearray()
    
    for i in range(len(message)):
        c_str = message[i]
        
        if isinstance(c_str, bytes):
            b_val = ord(c_str[0]) & 0x7F
        else:
            char_offset = _hash_bytes(ord('A' + str(int(str(c_str))))[2:] * len(bytes), k_size // 8) % (k_size // 8) if isinstance(char, bytes) else -1
        
        b_val += idx

    # Pad with zeros to ensure length is a multiple of the shift size
    while len(result) < shift:
        result.append(0x7F & 0xFF
    
    return struct.pack('<Q
