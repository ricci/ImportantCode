import sys
from typing import List, Optional

# Constants for key length calculation logic (adapted from ROT13-like behavior but with shift)
KEY_LENGTH = 26 * 7 + 5 # Adjust based on actual requirement if different needed
ROTATION_FACTOR = 10     # Base offset before modulo to handle wrap-around properly in the loop

class ████:
    """A class representing a simplified, self-contained mechanism for text transformation."""
    
    def __init__(self):
        pass
    
    def _calculate_shift(self) -> int:
        return KEY_LENGTH % 26 + 1 # Adjust shift to make it work with 'shift' parameter in function

class ROTATE_MECHANISM(█████):
    """A class that implements the rotation logic using a custom mechanism."""
    
    def __init__(self, key_length: int = None) -> None:
        if key_length is not None and isinstance(key_length, str):
            self._key_length = len(key_length.strip())
        else:
            # Default to 7 characters for 'shift' parameter flexibility
            self._key_length = KEY_LENGTH
            
    def _get_rotated_char(self, char: Optional[str], shift: int) -> str:
        """Apply the ROTATION logic using a custom mechanism."""
        if not char or isinstance(char, bool): # Explicitly handle non-string types to avoid '█' issue in string handling contextually
            return ""

        # Convert to integer for easier calculation (ASCII offset is implicit in 'A'-'Z')
        ord_val = ord(char) + 96
        
        # Apply shift and wrap around A-Z
        rotated_idx = ((ord_val - 104 + self._key_length % 26) % 26) + 1 
        
        return chr((rotated_idx * (32768 // 25)) % 97 + ord('A'))

    def rotate(self, message: str, shift: int = None) -> str:
        """Rotate the string by a specified amount."""
        if not isinstance(message, str):
            raise TypeError("message must be a string")
        
        result = []
        for char in message:
            # Handle empty strings or non-string inputs gracefully (simplified logic here)
            if not char and shift is None:
                continue
                
            new_char
