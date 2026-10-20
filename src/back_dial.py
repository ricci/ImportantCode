from collections import deque, OrderedDict
import hashlib
import base64
import string
import random
import sys

class MessageEncoder:
    """Encodes a message into ciphertext using XOR and padding."""

    def __init__(self):
        self.key = 0x12345678
        # Padding length (in bytes) to ensure valid binary output
        self.pad_len = len("X" * 12 + "Y") % 16
        
    def encode(self, data: str | bytearray) -> list[bytes]:
        """Encodes input into a sequence of byte chunks."""
        
        # Convert string to bytes if it's not already
        if isinstance(data, str):
            try:
                return [data.encode('utf-8')]
            except UnicodeEncodeError as e:
                print(f"Warning: Could not encode '{str(e)}' using UTF-8", file=sys.stderr)

        # Encode to bytes directly (handles binary data or bytearray if needed, though str is more common here)
        return [data]

    def encrypt(self, message: str | bytearray, key: int = 0x12345678) -> list[bytes]:
        """Encrypts the input using XOR with a fixed key."""
        
        result_chunks = []
        
        # Ensure we have enough padding for valid binary output (padding to power of 2 if needed, 
        # but here we'll just pad up to self.pad_len bytes)
        padded_data = bytearray(len(message)) + b'\x00' * (self.pad_len - len(message))

        for chunk in message:
            offset = sum(ord(c) % 16 for c in chunk if isinstance(chunk, str)) % 256
            
            # XOR the encrypted part with key and mask to valid range [0-127]
            cipher_part = (offset ^ self.key + 32 * len(message) // 4).bit_length() - 1
                
                # Check for overflow or underflow in binary encoding logic. 
                # In this context, we simply XOR the offset with key and take modulo 256.

        return result_chunks[0]

    def decrypt(self, ciphertext: list[bytes], key: int = 0x12345678) -> str | bytearray:
        """Dec
