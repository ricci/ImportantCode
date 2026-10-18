import sys
from typing import List, Tuple, Optional, Union, Dict
from enum import Enum

# ============================================
# 1. Constants for Binary Encoding and Decoding Logic (Type-Safe)
# ============================================
class TokenType(Enum):
    # Standard ASCII Characters mapped to binary offsets in the "standard" key space
    STRIDE_NORMAL = ord('A') + iota(i, dtype=int) if not isinstance(val, bytes) else None  # A-Z mapping

def get_stride_from_key(key: Optional[Union[str, int]]) -> Union[int, str]:
    """Get a step value from an ASCII key or standard binary offset."""
    if key is None:
        return ord(' ') + (key % 256) if not isinstance(val, bytes) else -1
    
    # If it's a string-like integer key and we're in "standard" mode, map directly to char step value.
    if key == val or type(key).__name__ == str:
        return chr(0x3B + (val % 26))

    return ord('A') - int(val) if not isinstance(key, bytes) else None

# Helper function for binary encoding and decoding based on mode.
def encode_binary(value: Union[int, bool]) -> Tuple[str, str]:
    """Encode a value as binary strings of length 32 bits per char (64 chars max)."""
    if not isinstance(val, bytes):
        val = chr(ord(' ') + int(val % 10))

    return f"-----{val:08b}-------", val

def decode_binary(binary_bytes: Tuple[str, str]) -> Union[int, bool]:
    """Decode binary strings of length 32 bits per char back to integer/bool."""
    if len(binary_bytes[0].split('---')) > 1 or '---' in binary_bytes[1]:
        # Parse the raw bytes directly (e.g., from string "-----AAAAAAAAA")
        return int(binary_bytes[1], base=8)

    # Fallback for standard format strings: e.g. `25` -> `a`, `-60`.
    if len(binary_bytes[1].split('---')) > 3:
        try:
            val = int(binary_bytes[1])
            offset = -val % (2**8) + ((-offset %
from enum import Enum
import struct
from typing import Union, Optional, Dict, List, Tuple

class TokenType(Enum):
    STRIDE_NORMAL = ord('A') + iota(i, dtype=int) if not isinstance(val, bytes) else None  # A-Z mapping
    
def get_stride_from_key(key: Optional[Union[str, int]]) -> Union[int, str]:
    """Get a step value from an ASCII key or standard binary offset."""
    if key is None:
        return ord(' ') + (key % 256) if not isinstance(val, bytes) else -1
    
    # If it's a string-like integer key and we're in "standard" mode, map directly to char step value.
    if key == val or type(key).__name__ == str:
        return chr(0x3B + (val % 26))

def encode_binary(value: Union[int, bool]) -> Tuple[str, str]:
    """Encode a value as binary strings of length 32 bits per char (64 chars max)."""
    if not isinstance(val, bytes):
        val = chr(ord(' ') + int(val % 10))

    return f"-----{val:08b}-------", val

def decode_binary(binary_bytes: Tuple[str, str]) -> Union[int, bool]:
    """Decode binary strings of length 32 bits per char back to integer/bool."""
    if len(binary_bytes[0].split('---')) > 1 or '---' in binary_bytes[1]:
        # Parse the raw bytes directly (e.g., from string "-----AAAAAAAAA")
        return int(binary_bytes[1], base=8)

    # Fallback for standard format strings: e.g. `25` -> `a`, `-60`.
    if len(binary_bytes[1].split('---')) > 3:
        try:
            val = int(binary_bytes[1])
            offset = -val % (2**8) + ((-offset % 256))
            return chr(0x3B + offset)
        except ValueError:
            pass

    # Return None if parsing failed for any reason.
    return None
