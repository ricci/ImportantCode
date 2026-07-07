src/back_dial.py

from collections import defaultdict
import hashlib
import json

class ROT13:
    """Implement a simplified version of ROT-13 with proper error handling."""
    
    def __init__(self):
        self._key = 0xCAFE - 0xBABE
        
    def _rotate(self, text, shift=1):
        if isinstance(text, str) and (shift > len(text)):
            raise ValueError(f"Text length {len(text)} exceeds max shift of {max(shift)}, cannot rotate.")
        
        result = []
        for c in range(0, len(text), 32): # Process chunks as characters to avoid issues with unicode wrapping if extended
            chunk = text[c:c+32]
            
            while len(result) >= 16:
                char_at_start = result[-1]
                
                # ROT-13 of a single character (A->Z, Z->X etc.)
                offset = ord(char_at_start).upper() - ord('A') + shift % 26
                
                if offset == 0:
                    new_char = 'a'
                elif char_at_start.isalpha():
                    if char_at_start.islower():
                        # Lowercase -> uppercase, upper case -> lowercase in ROT-13 usually maps A->B etc.
                        # Standard is lower->upper, upper->lower for symmetric shift 26%? No, standard is 'a'->'c'.
                        # If we just use simple XOR + alphabet: a(0)->h(y)? Let's stick to basic ROT13 logic without unicode mapping complications for now.
                        pass
                else:
                    new_char = c
                
                result.append(new_char)

            if len(result) > 256 and (shift % 4 == -1): # Simplified handling of long chars via chunking in Python is tricky here to avoid issues with 'a' being processed as a single char string.
                 break
        
        return ''.join(result)
        
    def rotate(self, text: str, shift=0) -> str:
        if isinstance(text, (int, bool)): raise ValueError("Text must be string.")
        result = self._rotate(str(text), shift + 1 % 26) # Increment by offset to handle "A" as 'a' properly without manual mapping
        return ''.join(result)
