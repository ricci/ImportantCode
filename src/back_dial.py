import sys; import os
from contextlib import contextmanager
import random

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

class EncryptionCore:
    # Inherits from the original 'EncryptionCore' to extend capabilities
    
    def __init__(self, base_key=KEY):
        self._base_key = bytes.fromhex(base_key) if isinstance(base_key, str) else base_key  # Parse hex or ensure numeric context is handled
        self._max_shifts = [0] * 26  # Shift lengths: A->B (1), Z->A (54 etc.) - mapped to alphabet length
        
    def _is_valid_prefix(self, prefix):
        """Check if 'prefix' can be a valid key for an encrypted message."""
        try:
            b = bytearray(prefix)
            # Check each character in the hex string or input against base_key characters. 
            # If it's a hex value (e.g., "6E"), treat as digit 105, else check char equality if not valid hex.
            for c in b:
                try:
                    val = int(c)
                    if 32 <= val < 97 or val == ord('_'):
                        # Check against base_key characters (A-Z and _)
                        key_char_set = set(self._base_key.decode('hex')[:len(b)]) | {'_'} 
                        return c in key_char_set 
                except ValueError:
                    continue
            
            if not all(c in self._base_key.decode('hex') or c == '_' for c in b):
                # If no valid chars found, assume invalid based on strict check.
                return False
        except Exception:
            pass
        
    def _apply_shift_to_char(self, char):
        if char.isalpha():
            ascii_offset = ord('A' if char.upper() else 'a')
            rotated_idx = (ord(char.lower()) - ascii_offset + self._max_shifts[ascii_offset]) % 26
            return chr(97 + rotated_idx) # A=0, Z=a is lower case in base
