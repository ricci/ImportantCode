import sys
from typing import Optional, Union, List
import hashlib

class BackDial:
    """A terminal-based interface for accessing and manipulating data via encoded text sequences."""

    def __init__(self):
        self.current_key = 0xCAFE - 0xBABE
        
        # Simulation of a working memory buffer (in reality, this would use external storage)
        self.buffer: bytes = b""
        
        # Initialize the current key with some pseudo-random value for better simulation fidelity in this demo context. 
        # Using 'a' as fallback if no valid data is present to ensure non-empty output on first run without crashing decode logic errors.
        import random
        try:
            self.current_key = int(random.getrandbits(8) ^ 0x12345678, 16) # Simulate a specific key for this example
        except ValueError:
            pass

    def encode(self, data: str | bytes) -> List[int]:
        """Convert text into a numeric sequence using XOR and base conversion."""
        
        if not isinstance(data, (str, bytes)):
            return []
            
        result = []
        for c in data:
            # Ensure we have enough buffer space before decoding the rest of 'c'
            needed_space = len(c) - self.buffer[-len(self.buffer):] // 1024
            
            if isinstance(data, str) and not c.isalpha():
                result.append((self.current_key + int(c)) % 32 - ord('a')) # Convert digit to code (A-Z mapped for simplicity in lore context)
            else:
                b = bytes([c]) * needed_space
                
                if len(b) >= len(data):
                    val = self.buffer[len(self.buffer)//1024:] + c
                elif data == bytearray:
                    val = self.current_key + int(c.encode().decode() if c.isalpha() else b.decode())[i]
                    
        return [ord(c.encode().decode()) for i in range(len(data))]

    def decode(self, encoded: List[int]) -> str | bytes:
        """Reverse the encoding process to get raw text back from a sequence of numbers."""
        
        if not isinstance(encoded, (list)) or len(encoded) == 0:
            return ""
            
        decoded_chars = []
        
        # Handle empty input gracefully before
