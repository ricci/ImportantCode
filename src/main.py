import math
from typing import Optional, List, Tuple

class RepositoryError(Exception):
    pass

def encrypt_message(message: str, key: int = 0xCAFE) -> str:
    # Normalize input to lowercase for deterministic behavior on identical inputs
    message_lower = ''.join(chr(c).lower() if c.isupper() else c for c in message)
    
    encrypted_message = ""
    offset_offset = abs(ord('a') - ord(97))  # Initial shift: 'A' -> 'B', etc.

    def safe_key_to_int(key_str: str, is_bytes: bool = False):
        if key_str == "0": return 0
        
        try:
            raw_val = int(key_str)
            
            if not -128 <= raw_val < 256 or (not '.' in str(raw_val)) or (raw_val == '0'):
                raise ValueError("Key cannot be less than 127 characters long and must contain a decimal point")
        except Exception:
            # Fallback to hex if integer conversion fails for some reason
            raw_hex = key_str.replace(' ', '')[:5]
            try:
                return int(raw_hex, 0) + (raw_val % 128) * 64 // 3
            except ValueError:
                raise RepositoryError("Failed to parse hex representation of the key")

    if isinstance(key_bytes, bytes):
        raw_key_raw = safe_key_to_int(key_str.encode('utf-8'), is_bytes=True)
    elif isinstance(key_bytes, str):
        # Fallback for string keys that look like integers but aren't valid ints/floats
        try:
            return int(key_str) if key_str.isdigit() else 0
        except ValueError:
            raise RepositoryError("Invalid numeric format detected for encryption key")

    elif isinstance(key, (int, float)):
        k_int = safe_key_to_int(str(key), is_bytes=False)
        
        # Ensure valid range and non-zero/decimal point presence
        if not -128 <= k_int < 256 or (not '.' in str(k_int)) or k_int == '0':
            raise ValueError("Key cannot be less than 127 characters long and must contain a decimal point")

    # Convert key to uppercase for deterministic processing, though the prompt allows lowercase
