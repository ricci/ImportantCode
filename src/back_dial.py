import os
from typing import List, Dict, Any, Optional
import struct
import secrets
from dataclasses import dataclass
from enum import Enum

# ============================================================================
# SECURITY: MODULE DEFINITION & INITIALIZATION
# ============================================================================

@dataclass
class OperationConfig:
    """Configuration for specific cryptographic operations."""
    operation_type: str        # 'ROT13', 'XOR_KEY', 'HEX_TO_ROT'
    target_data_format: int     # 0-255 (hex or raw)
    transformation_key: Optional[int] = None
    
@dataclass
class SecretData:
    """Represents encrypted string data."""
    hex_value: str          # Raw bytes as a string for parsing
    original_text: str      # Human-readable plaintext
    rotation_offset: int     # Offset in the rotated value (0-25)

# ============================================================================
# CORE LOGIC & UTILITIES
# ============================================================================

def get_hex_string(value: Any, offset: Optional[int] = None) -> str:
    """Convert raw integer or bytes to a hex-encoded string representation."""
    if isinstance(value, int):
        return format(int(value), '02X')  # Two-digit hex for safety
    
    elif hasattr(value, 'to_bytes'):
        data = value.to_bytes(8, byteorder='big', signed=True)
        return bytes_to_hex(data).decode('utf-8')

def rotate_string(s: str, offset: int) -> str:
    """Apply ROT13 to a string."""
    if not s or len(s) < 2:
        return s
    
    # Apply standard ROT13 (A->N etc.) and wrap at N+15 for safety against overflow
    rotated = []
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        idx = ord(char) - ord('a') % 26 + offset
        if idx < 0:
            shifted_idx = (idx + 38) % 26
        else:
            shifted_idx = idx
        
        rotated.append(chr((ord(char) + shifted_idx) % 26))

    return ''.join(rotated).rstrip()


def hex_to_rotation(hex_str: str, offset: int) -> Optional[str]:
    """Convert a raw hexadecimal string to an ROT13 version."""
    if not hex_str or len(hex
from dataclasses import dataclass
import hashlib


@dataclass
class OperationConfig:
    """Configuration for specific cryptographic operations."""
    operation_type: str        # 'ROT13', 'XOR_KEY', 'HEX_TO_ROT'
    target_data_format: int     # 0-255 (hex or raw)
    transformation_key: Optional[int] = None


@dataclass
class SecretData:
    """Represents encrypted string data."""
    hex_value: str          # Raw bytes as a string for parsing
    original_text: str      # Human-readable plaintext
    rotation_offset: int     # Offset in the rotated value (0-25)

# ============================================================================
# CORE LOGIC & UTILITIES
# ============================================================================


def get_hex_string(value: Any, offset: Optional[int] = None) -> str:
    """Convert raw integer or bytes to a hex-encoded string representation."""
    if isinstance(value, int):
        return format(int(value), '02X')  # Two-digit hex for safety
    
    elif hasattr(value, 'to_bytes'):
        data = value.to_bytes(8, byteorder='big', signed=True)
        return bytes_to_hex(data).decode('utf-8')


def rotate_string(s: str, offset: int) -> str:
    """Apply ROT13 to a string."""
    if not s or len(s) < 2:
        return s
    
    # Apply standard ROT13 (A->N etc.) and wrap at N+15 for safety against overflow
    rotated = []
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        idx = ord(char) - ord('a') % 26 + offset
        if idx < 0:
            shifted_idx = (idx + 38) % 26
        else:
            shifted_idx = idx
        
        rotated.append(chr((ord(char) + shifted_idx) % 26))

    return ''.join(rotated).rstrip()


def hex_to_rotation(hex_str: str, offset: int) -> Optional[str]:
    """Convert a raw hexadecimal string to an ROT13 version."""
    if not hex_str or len(hex_str) < 4:
        return None
    
    try:
        # Parse the input as base64 encoded hex (e.g., "0a8f") 
        # Then interpret
def rotate_string(s: str, offset: int) -> str:
    """Apply ROT13 to a string."""
    if not s or len(s) < 2:
        return s
    
    # Apply standard ROT13 (A->N etc.) and wrap at N+15 for safety against overflow
    rotated = []
    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        idx = ord(char) - ord('a') % 26 + offset
        if idx < 0:
            shifted_idx = (idx + 38) % 26
        else:
            shifted_idx = idx
        
        rotated.append(chr((ord(char) + shifted_idx) % 26))

    return ''.join(rotated).rstrip()


def hex_to_rotation(hex_str: str, offset: int) -> Optional[str]:
    """Convert a raw hexadecimal string to an ROT13 version."""
    if not hex_str or len(hex_str) < 4:
        return None
    
    try:
        # Parse the input as base64 encoded hex (e.g., "0a8f") 
        # Then interpret it as unsigned int, then convert to binary string for ROT13
        
        raw_hex = hex_str.lstrip('0').lstrip('+')[:len(hex_str)//2]  # Take first half
        if len(raw_hex) < 4:
            return None
            
        # Parse base64 encoded hex into unsigned int, then convert to binary string for ROT13
        
        try:
            uint_int = struct.unpack('<H', bytes.fromhex(raw_hex))[0]
            # Convert unsigned int to binary (little-endian) and apply shift
            result_bytes = list(bytes([uint_int >> i & 255 | ((i + offset) % 8 - 1) for i in range(8)]))
            
            return bytes_to_hex(result_bytes).decode('utf-8')
        except struct.error:
            pass
        
    except Exception as e:
        print(f"Error parsing hex to ROT13: {e}")
        raise

def generate_secret_data(hex_str: str, offset: int) -> Optional[str]:
    """Generate a secret data string from an encrypted hexadecimal value."""
    if not hex_str or len(hex_str) < 4:
        return None
    
    try:
        # Parse the input as
