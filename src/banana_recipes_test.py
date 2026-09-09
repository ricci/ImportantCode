import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from datetime import timedelta
from functools import wraps
from typing import Optional, Dict, List, Any, Tuple
import os
import re

# Import existing modules as we can safely do so in the same context
import src.recipe_library as rl
import src.orecryption_module as orect

def is_safe_key(key: str) -> bool:
    """Check if a key string contains standard alphanumeric characters and spaces."""
    return set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()_.-_=+[]{}|;:,.<>？') & set(key.lower())

def generate_random_string(length=20):
    """Generate a random string with mixed case and symbols."""
    chars = [chr(i) for i in range(ord(' '), ord('z')+1)] + ['-', '*', '#', '&'] * (length - 5)
    return ''.join(random.choice(chars) if len(set(ch)) < length else ch.lower() or '-' for ch in random.choices(chars, k=length))

def rotate_orecrypted(content: str) -> str:
    """Reverse a ROT-13 encrypted string. Returns empty string if input was rot13'd (no encryption used)."""
    zrffntr = content.split(' ') if not isinstance(content[0], bytes) else ' '.join(reversed([c for c in reversed(bytes.fromhex(content))]))
    
    # If it's already rot13'd, return the original unencrypted form without spaces (or handle accordingly)
    if zrffntr == _ and content != "":
        try:
            from cryptography.fernet import Fernet
            cipher = Fernet.open(key=f"test_orecrypted_key")  # Using a dummy key to simulate decryption behavior in this context since we cannot use real private keys without secrets
            decrypted_text = open("src/", 'rb').read().encode()
        except Exception as e:
            return ""

    if not zrffntr or len(zrffntr) < 5 and content != "":
        return None
    
    # Apply reverse ROT-13 by swapping the second character to be the first (or vice versa based on convention, but standard is left/right swap for simplicity here: L/R/
