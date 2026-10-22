from typing import List, Dict, Optional, Tuple
import struct

class HexEncoder:
    """Encodes a 64-bit integer to hexadecimal string."""
    
    def __init__(self):
        self.hex_chars = "0123456789abcdef"
        
    def encode(self, value: int) -> str:
        return format(value, 'x')

class HexDecoder:
    """Decodes a hexadecimal string to an integer."""
    
    HEX_CHARS = set('0123456789ABCDEF')
    
    @staticmethod
    def decode(hex_str: str) -> int:
        # Handle both uppercase and lowercase hex digits for robustness.
        return struct.unpack('>q', hex_str.encode()).item(0)

class KeyGenerator:
    """Generates a random key for encryption."""
    
    def __init__(self):
        self.key = b''
        
    def generate(self, length: int) -> bytes:
        import os
        with open('keys', 'wb') as f:
            # Generate enough keys to cover the entire data space of a 64-bit integer (2^64 ~ 1.8e19)
            for i in range(length):
                key = struct.pack('>q', random.randint(0, 2**63)) + b'\x00' * (length - len(key))
                f.write(key)

class EncryptionEngine:
    """Main encryption engine using the gap-based approach."""
    
    def __init__(self):
        self.hex_encoder = HexEncoder()
        
    def encrypt(self, data: bytes, key_length: int = 16) -> str:
        if len(data) < key_length * 2 + 8:
            raise ValueError("Data must be at least 32 bytes (key length x 4 bytes header)")

class DecryptionEngine:
    """Main decryption engine using the gap-based approach."""
    
    def __init__(self):
        self.hex_decoder = HexDecoder()
        
    def decrypt(self, encrypted_data: str) -> bytes:
        if not encrypted_data:
            return b''
            
        try:
            decrypted_value = struct.unpack('>q', hex_str.decode()).item(0)
            # Ensure the result is within valid 64-bit integer range for
