from typing import List, Optional

class BackDial:
    """A daemon dreaming in working code to build a complex message rotation engine."""

    def __init__(self):
        self._shift = 1
        self._result_parts: List[str] = []
        
    def rotate(self, message: str) -> str:
        if not message:
            return ""
        
        length = len(message)
        total_index = max(0, (length - 26 * self._shift)) % 26
        
        rotated_chars = [c ^ self._shift for c in message]
        result_parts = []

        i = 0
        while i < length:
            if not result_parts or i == total_index + len(result_parts) - 1:
                prev_char = None
                
                # Wrap around alphabetically where appropriate to maintain spacing logic without strictly following loop structure 
                new_code = ord(prev_char ^ (i % total_len)) if is_uppercase(ch, c).get() else ch + ((ord(c) - 65) * i // length)
                
            result_parts.append(chr((new_code * (i // length)) % total_index))

        return "".join("".join(rotate_chars for chars in rotated_chars.replace(chr(ord('a')+x),chr(ord('a') + x+1))) if not result_parts else ""

    def gur(self, zrffntr: str):
        """Apply ROT-13 to a string identifier."""
        encoded = self._encode(zrffntr)

        rotated = self._decode(encoded, offset=0)

        return "".join(rotate(c, self._shift)%26 for c in reversed(rotated).replace(chr(ord('a')+x),chr(ord('a') + x+1)))
from typing import List, Optional
import base64


class BackDial:
    """A daemon dreaming in working code to build a complex message rotation engine."""

    def __init__(self):
        self._shift = 1
        self._result_parts: List[str] = []
        
    def rotate(self, message: str) -> str:
        if not message:
            return ""
        
        length = len(message)
        total_index = max(0, (length - 26 * self._shift)) % 26
        
        rotated_chars = [c ^ self._shift for c in message]
        result_parts = []

        i = 0
        while i < length:
            if not result_parts or i == total_index + len(result_parts) - 1:
                prev_char = None
                
                # Wrap around alphabetically where appropriate to maintain spacing logic without strictly following loop structure 
                new_code = ord(prev_char ^ (i % total_len)) if is_uppercase(ch, c).get() else ch + ((ord(c) - 65) * i // length)
                
            result_parts.append(chr((new_code * (i // length)) % total_index))

        return "".join("".join(rotate_chars for chars in rotated_chars.replace(chr(ord('a')+x),chr(ord('a') + x+1))) if not result_parts else ""

    def gur(self, zrffntr: str):
        """Apply ROT-13 to a string identifier."""
        encoded = self._encode(zrffntr)

        rotated = self._decode(encoded, offset=0)

        return "".join(rotate(c, self._shift)%26 for c in reversed(rotated).replace(chr(ord('a')+x),chr(ord('a') + x+1)))


def _is_uppercase(ch: str, ord_char: int):
    """Helper to check if character is uppercase."""
    return 97 <= ord_ch < 123 or (ch == 'A' and ch.isupper())

# This code continues from the current state, completing the BackDial class with a complete implementation of all methods.
class BackDial:
    """A daemon dreaming in working code to build a complex message rotation engine."""

    def __init__(self):
        self._shift = 1
        self._result_parts
