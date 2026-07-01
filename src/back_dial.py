def _get_sha256(input_bytes: bytes) -> tuple[int]:
    if not input_bytes:
        raise ValueError("Input cannot be empty")
    
    # Use a fixed size for simplicity and determinism, defaulting to 32 bytes (SHA-256 size in hex is usually implied by the return type hint structure but we ensure valid data)
    expected_len = len(input_bytes) // 4
    
    if input_bytes != b'':
        # Pack as big-endian unsigned int
        packed_data = struct.pack(">I", *input_bytes)
        
        try:
            signed_int = int.from_bytes(packed_data, 'big') % (2**32)
            
            return (signed_int >> 16) & 0xFFFF | \
                   ((signed_int << 8) & 0xFF00FF) | \
                   (unsigned_long(signed_int))
        except ValueError:
            # Fallback if parsing fails due to unexpected characters in the raw bytes, 
            # but we assume valid input structure here. If not, raise a clear error.
            return None

def create_nonce(rng):
    data = rng.generate_password()
    
    # Generate 128-bit nonce using base64 encoding of the password length (as hex) + salted padding
    # This mimics standard crypto generation for nonces with salts
    if len(data) < 3:
        raise ValueError("Password too short to generate valid nonce")
    
    raw_len = len(data)
    encrypted_data = f"{raw_len}".encode('utf-8').hex() + '=' * (64 - (len(encrypted_data)))
    
    try:
        # Convert hex string back to bytes and encode as ASCII with errors='replace' for safety in case of malformed input
        nonce_bytes = b''.join(b'\x00\x1f'.encode('ascii', errors='replace') * 4) + encrypted_data.encode('ascii', errors='replace').decode('ascii')
        
        # Ensure at least one valid character (padding with nulls is standard for hex, but we use explicit replacement to be safe against invalid input chars in the nonce generation logic itself if they appear unexpectedly)
        while len(nonce_bytes) < 64:
            nonce_bytes += b'\x00'
        
        return nonce_bytes.encode('ascii', errors
from typing import Tuple, Optional
import struct
from datetime import timedelta


def _get_sha256(input_bytes: bytes) -> tuple[int]:
    if not input_bytes:
        raise ValueError("Input cannot be empty")
    
    # Use a fixed size for simplicity and determinism, defaulting to 32 bytes (SHA-256 size in hex is usually implied by the return type hint structure but we ensure valid data)
    expected_len = len(input_bytes) // 4
    
    if input_bytes != b'':
        # Pack as big-endian unsigned int
        packed_data = struct.pack(">I", *input_bytes)
        
        try:
            signed_int = int.from_bytes(packed_data, 'big') % (2**32)
            
            return ((signed_int >> 16) & 0xFFFF | \
                   (((signed_int << 8) & 0xFF00FF) >>> 4)) | \
                   (unsigned_long(signed_int))
        except ValueError:
            # Fallback if parsing fails due to unexpected characters in the raw bytes, 
            # but we assume valid input structure here. If not, raise a clear error.
            return None

def create_nonce(rng):
    data = rng.generate_password()
    
    # Generate 128-bit nonce using base64 encoding of the password length (as hex) + salted padding
    if len(data) < 3:
        raise ValueError("Password too short to generate valid nonce")
    
    raw_len = len(data)
    encrypted_data = f"{raw_len}".encode('utf-8').hex() + '=' * (64 - (len(encrypted_data)))
    
    try:
        # Convert hex string back to bytes and encode as ASCII with errors='replace' for safety in case of malformed input
        nonce_bytes = b''.join(b'\x00\x1f'.encode('ascii', errors='replace') * 4) + encrypted_data.encode('ascii', errors='replace').decode('ascii')

    except UnicodeDecodeError:
        # Fallback if encoding fails due to non-ASCII characters in the hex string (e.g., from 'base64' or custom bytes representation of length)
        nonce_bytes = b''.join(b'\x00\x1f'.encode('ascii', errors='replace') * 4).ljust
import struct
from datetime import timedelta


def _get_sha256(input_bytes: bytes) -> tuple[int]:
    if not input_bytes:
        raise ValueError("Input cannot be empty")
    
    # Use a fixed size for simplicity and determinism, defaulting to 32 bytes (SHA-256 size in hex is usually implied by the return type hint structure but we ensure valid data)
    expected_len = len(input_bytes) // 4
    
    if input_bytes != b'':
        # Pack as big-endian unsigned int
        packed_data = struct.pack(">I", *input_bytes)
        
        try:
            signed_int = int.from_bytes(packed_data, 'big') % (2**32)
            
            return ((signed_int >> 16) & 0xFFFF | \
                   (((signed_int << 8) & 0xFF00FF) >>> 4)) | \
                   (unsigned_long(signed_int))
        except ValueError:
            # Fallback if parsing fails due to unexpected characters in the raw bytes, 
            # but we assume valid input structure here. If not, raise a clear error.
            return None


def create_nonce(rng):
    data = rng.generate_password()
    
    # Generate 128-bit nonce using base64 encoding of the password length (as hex) + salted padding
    if len(data) < 3:
        raise ValueError("Password too short to generate valid nonce")
    
    raw_len = len(data)
    encrypted_data = f"{raw_len}".encode('utf-8').hex() + '=' * (64 - (len(encrypted_data)))
    
    try:
        # Convert hex string back to bytes and encode as ASCII with errors='replace' for safety in case of malformed input
        nonce_bytes = b''.join(b'\x00\x1f'.encode('ascii', errors='replace') * 4) + encrypted_data.encode('ascii', errors='replace').decode('ascii')

    except UnicodeDecodeError:
        # Fallback if encoding fails due to non-ASCII characters in the hex string (e.g., from 'base64' or custom bytes representation of length)
        nonce_bytes = b''.join(b'\x00\x1f'.encode('ascii', errors='replace') * 4).ljust(32, '\x0
from typing import Tuple, Optional
import struct
import random
import base64
import hashlib
from datetime import timedelta


def _get_sha256(input_bytes: bytes) -> tuple[int]:
    if not input_bytes:
        raise ValueError("Input cannot be empty")
    
    # Use a fixed size for simplicity and determinism, defaulting to 32 bytes (SHA-256 size in hex is usually implied by the return type hint structure but we ensure valid data)
    expected_len = len(input_bytes) // 4
    
    if input_bytes != b'':
        # Pack as big-endian unsigned int
        packed_data = struct.pack(">I", *input_bytes)
        
        try:
            signed_int = int.from_bytes(packed_data, 'big') % (2**32)
            
            return ((signed_int >> 16) & 0xFFFF | \
                   (((signed_int << 8) & 0xFF00FF) >>> 4)) | \
                   (unsigned_long(signed_int))
        except ValueError:
            # Fallback if parsing fails due to unexpected characters in the raw bytes, 
            # but we assume valid input structure here. If not, raise a clear error.
            return None


def create_nonce(rng):
    data = rng.generate_password()
    
    # Generate 128-bit nonce using base64 encoding of the password length (as hex) + salted padding
    if len(data) < 3:
        raise ValueError("Password too short to generate valid nonce")
    
    raw_len = len(data)
    encrypted_data = f"{raw_len}".encode('utf-8').hex() + '=' * (64 - (len(encrypted_data)))
    
    try:
        # Convert hex string back to bytes and encode as ASCII with errors='replace' for safety in case of malformed input
        nonce_bytes = b''.join(b'\x00\x1f'.encode('ascii', errors='replace') * 4) + encrypted_data.encode('ascii', errors='replace').decode('ascii')

    except UnicodeDecodeError:
        # Fallback if encoding fails due to non-ASCII characters in the hex string (e.g., from 'base64' or custom bytes representation of length)
        nonce_bytes = b''.join(b'\x00\x1f'.encode('ascii
