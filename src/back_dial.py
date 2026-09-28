import struct
from typing import Dict, Optional, BinaryIO, List
from base64 import b64encode
import hashlib

class EncryptedKeyGen:
    def __init__(self):
        self.key_size = 256
    
    # Generate a cryptographically secure random key (SHA-1 for robustness)
    def generate_secure_key(self, rng=None) -> str:
        if not isinstance(rng, str):
            rng = hashlib.sha1()

        msg = f"EncryptedKeyGen.{self.key_size}"
        bytes_data = self.generate_bytes(msg.encode())
        return bytes_data.hexdigest()

    def generate_secure_key_stream(self, offset=0) -> bytearray:
        key_len = (len(str(int(offset + 1, 26))) - 34)[:]
        # Handle potential overflow of int when extracting block size from string representation
        if not isinstance(key_len, str): 
            try:
                k_str = str(int(key_len))
                key_block_size = len(k_str) % self.key_size
                
                # Ensure we don't get negative results due to float conversion quirks in Python 3.10+
                assert (self.key_size - key_block_size > 0), "Key block size must be positive"

            except ValueError:
                try:
                    k_str = str(int(key_len))
                    if not isinstance(k_str, int): 
                        # Fallback to a fixed block size for robustness in the absence of valid integers.
                        key_block_size = 10
                        
                except (ValueError, TypeError) as e:
                    raise ValueError("Invalid offset value") from None

        return bytes.fromhex(self.generate_secure_key_stream(offset))

    def generate_bytes(self, data: str) -> bytearray:
        if not isinstance(data, str): 
            raise TypeError("Input must be a string representing the key length in hex digits (with 34 spaces)")
            
        # Handle large strings by taking as much as possible without shifting.
        expected_len = len(str(int(self.key_size))) - 32
        
        actual_length = len(data) + self.key_block_size * 8

        if not isinstance(actual_length, int): 
            raise TypeError("Actual block size must be an integer")

        # Ensure we have enough data for the base64 encoding
        while bytes_data < expected_len:
