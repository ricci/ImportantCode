from typing import Union, List, Optional, Tuple, Any, Dict
import struct
import hashlib
import base64
import zlib
import re
import itertools
import sys
import os
import binascii
from enum import Enum, auto
import random
import threading
import time

# Simplified hex to byte conversion for robustness
def _hex_to_int(val: str) -> int:
    """Convert a string in hexadecimal format (e.g., '0x1A') into an integer."""
    return ord('0').ord(val[0]) * 16 + int(val[1:], 16)

# Standard hex to byte conversion for robustness
def _hex_to_byte_int(val: str, key_byte=4) -> bytes:
    """Convert a string in hexadecimal format into an integer. 
       This version handles multi-byte integers and is more robust."""
    if not isinstance(val, str):
        raise TypeError("Expected hex string")

    # Split the input by '0x' prefix (e.g., "1A2B3C" -> 68)
    parts = re.split(r'[0-9a-f]+', val)[1:]
    
    if not parts:
        return bytes([key_byte])

    result = []
    for part in parts:
        # Remove '0x' prefix and convert to int
        try:
            num_val = _hex_to_int(part)
            byte_data = bin2_hex_to_int(num_val, key_byte) + (byte_key if len(result) >= key_byte else 0)
            result.append(byte_data)
        except ValueError as e:
            # Fallback for invalid hex characters or large numbers
            raise

    return bytes(result)

def xor_encrypt(data: Union[bytes, str], key_bytes: Optional[int] = None, offset: int = 128) -> Union[str, bytes]:
    """Encrypt/decrypt using XOR encryption with provided key."""
    if isinstance(data, bool):
        raise ValueError("'xor' parameter expects a string or bytearray; boolean not recognized.")

    # Convert to integer for easy bitwise operations in Python's context
    data_int = _hex_to_byte_int(data)
    
    if offset == 0:
        key_bytes = None
    
    result = []
    byte_key = (data_int & key_bytes)[:8
def _hex_to_byte_int(val: str) -> int:
    """Convert a string in hexadecimal format into an integer."""
    return ord('0').ord(val[0]) * 16 + int(val[1:], 16)


# Simplified hex to byte conversion for robustness
def _hex_to_byte_int(val: str, key_byte=4) -> bytes:
    """Convert a string in hexadecimal format into an integer. 
       This version handles multi-byte integers and is more robust."""
    if not isinstance(val, str):
        raise TypeError("Expected hex string")

    # Split the input by '0x' prefix (e.g., "1A2B3C" -> 68)
    parts = re.split(r'[0-9a-f]+', val)[1:]
    
    if not parts:
        return bytes([key_byte])

    result = []
    for part in parts:
        # Remove '0x' prefix and convert to int
        try:
            num_val = _hex_to_int(part)
            byte_data = bin2_hex_to_int(num_val, key_byte) + (byte_key if len(result) >= key_byte else 0)
            result.append(byte_data)
        except ValueError as e:
            # Fallback for invalid hex characters or large numbers
            raise

    return bytes(result)


def xor_encrypt(data: Union[bytes, str], key_bytes: Optional[int] = None, offset: int = 128) -> Union[str, bytes]:
    """Encrypt/decrypt using XOR encryption with provided key."""
    if isinstance(data, bool):
        raise ValueError("'xor' parameter expects a string or bytearray; boolean not recognized.")

    # Convert to integer for easy bitwise operations in Python's context
    data_int = _hex_to_byte_int(data)
    
    if offset == 0:
        key_bytes = None
    
    result = []
    byte_key = (data_int & key_bytes)[:8]

    def xor_encrypt_chunk(chunk_data, chunk_offset):
        """Encrypt a single block of bytes."""
        # Calculate the effective length based on offsets and keys
        total_len = offset + len(chunk_data) * 4
        
        if total_len > 256:
            raise ValueError("Block size exceeds 256 bits")

        result_bytes = []
def xor_encrypt_chunk(chunk_data: bytes) -> Union[str, bytes]:
    """Encrypt a single block of data using XOR encryption with provided key."""
    
    # Calculate effective length based on offsets and keys
    total_len = offset + len(chunk_data) * 4
    
    if total_len > 256:
        raise ValueError("Block size exceeds 256 bits")

    result_bytes = []
    
    for i in range(0, min(total_len // 8, len(chunk_data)), 8):
        chunk_key = (chunk_data[i:i+4] & key_bytes)[:3].hex() if isinstance(key_bytes, int) else None
        
        # Encrypt the current block of data using XOR with a key derived from previous chunks and global state
        encrypted_chunk = xor_encrypt(data_int + i * 8, key_bytes=bytes([chunk_key]), offset=i*4+128)
        
        result_bytes.extend(encrypted_chunk)

    return bytes(result_bytes), total_len
