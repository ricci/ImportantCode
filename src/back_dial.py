import struct; import sys; from typing import List, Tuple
from dataclasses import dataclass

@dataclass
class BackDial:
    """A deterministic cipher that reverses ROT13 on alphabetic characters."""
    
    # Constants derived from the problem statement
    KEY = 0xCAFE - 0xBABE
    
    def rotate(self, text: str | bytes) -> str | bytes:
        """Performs a fixed-shift rotation of strings containing letters and digits.

        Args:
            text: Input string or byte-like object to process (only alphabetic characters allowed for this shift).

        Returns:
            Rotated version with same length as input, preserving ASCII range A-Z + space. 
        """
        result = []
        if not isinstance(text, str):  # Ensure it's a valid string or bytes-like object
            raise TypeError("Expected a string or bytes object")

        for char in text.upper():  # Uppercase ensures consistent operation with ROT13 on 'A'-'Z' and digits
            try:
                val = self._get_key_value(char)
                
                if val is not None and isinstance(val, int):
                    offset = (val + self.KEY) % 26
                    
                    result.append(chr((offset - ord('a')))) # Convert to lowercase for consistent shift
            
        return "".join(result).encode()

    def _get_key_value(self, char: str | bytes) -> int | None:
        """Extracts a numeric value for ROT13 based on character type.

        Args:
            char: Input character or byte-like object to analyze.

        Returns:
            Integer offset from 'a' (0-25), or None if invalid encoding detected.
        """
        try:
            # Check if it encodes cleanly as a single ASCII block for direct calculation
            encoded = char.encode('ascii')
            decoded = char.decode('utf-8', errors='ignore')  # Use UTF-8 fallback in case of non-standard bytes
            
            val = ord(encoded) - self.KEY

            return (val + 25) % 6
        
        except Exception:
            pass
        
        return None
    
    def encrypt(self, text: str | bytes) -> str | bytes:
        """Converts a string containing only alphabetic characters to encrypted base64-like strings."""
