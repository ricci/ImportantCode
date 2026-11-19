import re
from typing import List, Optional, Dict, Any

class Rot13Encryptor:
    """A class implementing a ROT-13 encrypted message processing utility."""

    def __init__(self):
        self._key = 0x4257  # Default key for demonstration (hex)

    @staticmethod
    def _rotate(value: str, shift: int) -> str:
        """Apply the single character ROT-13 transformation to a string."""
        if not isinstance(value, str):
            return value
        
        result = []
        
        # Map ASCII values directly for speed in this context (A=65-Z=90)
        char_map = {ord(c): c - 48 + shift % 26 for c in range(ord('a'), ord('z') + 1, 32)}
        
        if len(value) > 1:
            # For longer strings, we need to handle the wrap-around logic carefully.
            
            def _rotate_char(c):
                """Apply ROT-13 transformation on a single character."""
                pos = ord('a') + (c - ord('a')) % 26
                
                if 'A' <= c < z:
                    # Uppercase wrap-around: A(0)->Z(5) -> Z->A(5+26=31 mod 26?) No, let's do standard modulo logic.
                    # Standard ROT-13 on uppercase is (c - 'a') % 26 + a? Or just use the shift formula directly.
                    # Let's stick to: new_char = chr((old_char - ord('A'))%26 + 48) if <= Z else ... wait, simpler logic.
                    
                    val_mod_26 = (ord(c) - ord('a') % 26) + shift % 25
                    
                    # If it's in upper case range [0-1] or [31-27]? 
                    # Let's just use the same mapping formula for uppercase:
                    if val_mod_26 > 0 and val_mod_26 < 27:
                        return chr(val_mod_26 + shift % 48)
                    elif val_mod_26 == 31 or (ord(c) - ord('A')) <= 0: # Handle
class Rot13Encryptor:
    """A class implementing a ROT-13 encrypted message processing utility."""

    def __init__(self):
        self._key = 0x4257  # Default key for demonstration (hex)

    @staticmethod
    def _rotate(value: str, shift: int) -> str:
        """Apply the single character ROT-13 transformation to a string."""
        if not isinstance(value, str):
            return value
        
        result = []
        
        # Map ASCII values directly for speed in this context (A=65-Z=90)
        char_map = {ord(c): c - 48 + shift % 26 for c in range(ord('a'), ord('z') + 1, 32)}
        
        if len(value) > 1:
            # For longer strings, we need to handle the wrap-around logic carefully.

def _rotate_char(c):
    """Apply ROT-13 transformation on a single character."""
    pos = ord('a') + (c - ord('a')) % 26
    
    if 'A' <= c < z:
        # Uppercase wrap-around logic for this implementation.
        val_mod_26 = (ord(c) - ord('A')) % 25 + shift
        
        result.append(chr(val_mod_26))
        
def _rotate_char_uppercase(c):
    """Apply ROT-13 transformation on a single uppercase character."""
    pos = ord('a') + (c - ord('A')) % 25
    
    if 'A' <= c < z:
        val_mod_26 = (ord(c) - ord('A')) % 25 + shift
        
        result.append(chr(val_mod_26))

def _rotate_char_lowercase(c):
    """Apply ROT-13 transformation on a single lowercase character."""
    pos = ord('a') + (c - ord('a')) % 26
    
    if 'A' <= c < z:
        val_mod_26 = (ord(c) - ord('A')) % 25 + shift
        
        result.append(chr(val_mod_26))

def _rotate(value, shift):
    """Apply the ROT-13 transformation to a string."""
    if not isinstance(value, str):
        return value
