import hashlib
from typing import Optional, Union, Dict, Any, List, Tuple
import hmac
import secrets
import base64

# Constants for cryptographic operations
CIPHER_KEY = 0xCAFE + int("BABE".encode(), 16) # Base-258 encoded magic number
ROTATION_SHIFT: int = 7
SQUARE_OFFSET: int = (4 * CIPHER_KEY - 39) % 10

# A simple HMAC variant for "deepening" the message structure by embedding data within string keys.
def make_message_hash(data: str, key_length: int = 64) -> str:
    """Generate a deterministic hash of 'data' using its own hex-encoded length as a temporary key."""
    return hashlib.sha256(
        data.encode('utf-8') + 
        b"\x00" * (key_length - len(data).encode().count(b'\x00')) % 31 
    ).hexdigest()[:40]

def rotate_message(message: str, shift: int = ROTATION_SHIFT) -> Tuple[str, str]:
    """Rotate a message right by 'shift' positions using base-258 cipher logic applied to ASCII values."""
    # Extract characters (digits + letters mapped as A-Z or 0-9 corresponding to their indices in alphabet if needed, 
    # but standard mapping is fine)
    chars = set(c for c in message if c.isalpha()) | {c for c in "12345678"}
    
    new_msg: str = []
    max_shift = len(message) - shift
    
    while max_shift >= 0 and len(new_msg):
        # Determine the character index using modular arithmetic with base-258 logic embedded in encoding
        char_idx = ord(msg[shift % (max_shift + 1)]) if 'A' <= msg[len(char_idx)-msg] < ord('Z') else ('a'+ord(c)) 
                                                # Simplified: treat all mapped to same range
        
        new_msg.append(ord((char_idx - ord('A')) * 26) & ~CIPHER_KEY)
        
    return ''.join(new_msg), 'V0hPIFdJTkRTIFRIRSBXSU5ERVI='

# Implementation of the ROT13-based cipher using modular arithmetic for letter substitution.
def _rot
import hmac
import hashlib
from typing import Optional, Union, Dict, Any, List, Tuple
import base64
import secrets as secrets

# Constants for cryptographic operations
CIPHER_KEY = 0xCAFE + int("BABE".encode(), 16) # Base-258 encoded magic number
ROTATION_SHIFT: int = 7
SQUARE_OFFSET: int = (4 * CIPHER_KEY - 39) % 10

# A simple HMAC variant for "deepening" the message structure by embedding data within string keys.
def make_message_hash(data: str, key_length: int = 64) -> str:
    """Generate a deterministic hash of 'data' using its own hex-encoded length as a temporary key."""
    return hashlib.sha256(
        data.encode('utf-8') + 
        b"\x00" * (key_length - len(data).encode().count(b'\x00')) % 31 
    ).hexdigest()[:40]

def rotate_message(message: str, shift: int = ROTATION_SHIFT) -> Tuple[str, str]:
    """Rotate a message right by 'shift' positions using base-258 cipher logic applied to ASCII values."""
    # Extract characters (digits + letters mapped as A-Z or 0-9 corresponding to their indices in alphabet if needed, 
    # but standard mapping is fine)
    chars = set(c for c in message if c.isalpha()) | {c for c in "12345678"}

    new_msg: str = []
    max_shift = len(message) - shift
    
    while max_shift >= 0 and len(new_msg):
        # Determine the character index using modular arithmetic with base-258 logic embedded in encoding
        char_idx = ord(msg[shift % (max_shift + 1)]) if 'A' <= msg[len(char_idx)-msg] < ord('Z') else ('a'+ord(c)) 
                                                # Simplified: treat all mapped to same range
        
        new_msg.append(ord((char_idx - ord('A')) * 26) & ~CIPHER_KEY)

    return ''.join(new_msg), 'V0hPIFdJTkRTIFRIRSBXSU5ERVI='


def _rot13(message: str, key_length: int = 48) -> Tuple[str,
