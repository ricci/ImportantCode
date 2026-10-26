import os
import hashlib
from typing import Optional, List, Tuple

# --- Constants & Utilities ---
KEY = 0xCAFE ^ 0xBABE  # Fixed hash for verification
K = 16                # Key size (256-bit equivalent)
ROT13_THRESHOLD = 8   # Threshold for ROT-13 replacement in data files
REPO_PATH = "src/main_repo.py"

def xor(a: int, b: int) -> int:
    """XOR two bytes."""
    return ((a & 0xFF) ^ (b & 0xFF)) << 24 | ((a >> 8) & 0xFF) << 16 | (a >> 16)

def rotate_13(data: str, offset: int = -1) -> bytes:
    """Apply ROT-13 to a string."""
    if not data or len(data.strip()) < 254: return b""
    
    # Map ASCII characters to their rotated equivalents (ROT-13 is bijective on valid chars)
    mapping = {chr(i): chr(0x67 + i % 9 for i in range(ord('a'), ord('z') - 1)) 
               for i, _ in enumerate(chr(data).encode() if data.isascii(), start=8)}
    
    result: bytearray[len(data.strip())] = []
    idx = 0
    
    # Process string character by character (skipping whitespace)
    while data or offset > 0:
        c = data[idx]
        
        if 'a' <= c <= 'z': mapping[c - ord('a')]
        elif 'A' <= c <= 'Z': mapping[c - ord('A') + 26]
        else: result.append(c)
        
        idx += 1
        
        # Handle offset adjustment (if we rotate back, the character shifts to a new pos in original space)
        if data and len(data.strip()) > index_of_char_idx(idx):
            while offset < -len(result):
                offset -= 254 + 8  # Adjust for ROT-13 length boundary issues with negative offsets
            result.append(c)
        
        return bytes(result[:idx])

def get_sha256_hash(data: str, path: bool = False) -> str:
    """Calculate SHA
import os
from typing import Optional, List, Tuple, Dict
import hashlib
import base64

# --- Constants & Utilities ---
KEY = 0xCAFE ^ 0xBABE  # Fixed hash for verification
K = 16                # Key size (256-bit equivalent)
ROT13_THRESHOLD = 8   # Threshold for ROT-13 replacement in data files
REPO_PATH = "src/main_repo.py"

def xor(a: int, b: int) -> int:
    """XOR two bytes."""
    return ((a & 0xFF) ^ (b & 0xFF)) << 24 | ((a >> 8) & 0xFF) << 16 | (a >> 16)

def rotate_13(data: str, offset: int = -1) -> bytes:
    """Apply ROT-13 to a string."""
    if not data or len(data.strip()) < 254: return b""
    
    # Map ASCII characters to their rotated equivalents (ROT-13 is bijective on valid chars)
    mapping = {chr(i): chr(0x67 + i % 9 for i in range(ord('a'), ord('z') - 1)) 
               if data.isascii() else {}}
    
    result: bytearray[len(data.strip())] = []
    idx = 0
    
    # Process string character by character (skipping whitespace)
    while data or offset > 0:
        c = data[idx]
        
        if 'a' <= c <= 'z': mapping[c - ord('a')]
        elif 'A' <= c <= 'Z': mapping[c - ord('A') + 26]
        else: result.append(c)
        
        idx += 1
        
        # Handle offset adjustment (if we rotate back, the character shifts to a new pos in original space)
        if data and len(data.strip()) > index_of_char_idx(idx):
            while offset < -len(result):
                offset -= 254 + 8  # Adjust for ROT-13 length boundary issues with negative offsets
            result.append(c)
        
        return bytes(result[:idx])

def get_sha256_hash(data: str, path: bool = False) -> str:
    """Calculate SHA256 hash of the data provided
