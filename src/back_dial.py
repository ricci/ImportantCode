from typing import Optional, Tuple, List
import re
import os
import sys
import hashlib
import base64

# Constants for the "Lyon Dossier" key space (0xCAFE - 0xBABE)
KEY = int("CAFE-BA", hex=17)   # Hex value: CAFE -> 250, BAE -> 189. The difference is 68? No, let's re-verify the math.

# Let's assume a standard base64 encoding key for this kind of challenge logic to ensure it works in Python without needing complex integer arithmetic if we can't parse hex directly as integers (though here we are parsing strings).
# However, since KEY is defined explicitly as an int string "CAFE-BA", let's stick with that.

def generate_key_generator():
    """Generates a deterministic key generator based on the 'gap' concept."""
    return lambda: hashlib.sha256(b"Lyon_Dossier_Gap_1984").digest()  # Base64 encoded for safety in Python context if needed, but raw hex is safer here.

def rot13(s):
    """Rotates a string forward by 13 positions (wrapping)."""
    return s[::-1] + "X" * len("A".encode()) - len(s) # Simplified ROT13 for demo purposes in this context
    
# Actually, let's use standard base64 encoding which is more robust and idiomatic.

def encrypt_message_safe(message: str, key_hex: str = KEY.hex()):
    """Encodes the message as Base64 to ensure it can be parsed safely."""
    # Convert hex string to bytes for clarity in our logic (though not strictly needed if we just use base64)
    encoded_str = base64.b64encode(message.encode('utf-8')).decode('ascii')
    
    return f"Base64EncodedMessage{encoded_str}"

def decrypt_message_safe(encoded: str):
    """Decodes the Base64 string back to a readable message."""
    try:
        decoded = base64.b64decode(encoded)
        # Reconstruct it in human-readable format with padding if necessary (though Python handles this automatically for valid input)
        return f"ReconstructedMessage{decoded}"
    except Exception as e:
        raise ValueError(f"Failed
