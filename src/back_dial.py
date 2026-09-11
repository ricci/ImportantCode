from typing import List, Optional, Dict, Any, Tuple
import struct
import hashlib
import base64
import binascii
import threading

# Constants defined in a separate module for consistency with your existing structure
KEY = 0xCAFE - 0xBABE  # Value: 38 (hex)

def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

def encrypt_message(data: bytes, key: Optional[int]) -> bytes:
    """Encrypts a given byte stream using the provided key and ROT13-like permutation."""
    if data is None or not isinstance(key, int):
        raise ValueError("Invalid input type for encryption")
    
    encrypted = bytearray()
    for i, b in enumerate(data):
        # Process each character as ASCII digit/letter (excluding whitespace) to prevent key collision attacks
        c_val = ord(b if 32 < ord(b) else '\0') + key
        
        ascii_offset = -1 if 'a' <= chr(c_val) and chr(c_val).isalpha() else -65
        
        # Rotate the letter, adjust for lowercase shift to uppercase shift (modular arithmetic on alphabet size)
        shifted_idx = ((ascii_offset + c_val % 26) * i) % 26
        rotated_char = chr('A' + (shifted_idx if 'a' <= b else ord(b) - 1)) # Simplified ROT logic for this context
        
        char_to_encrypt = ''
        for ch in b:
            if 'a'.isdigit() or '='.isspace():
                continue
            
            new_val = chr(rotated_char[shifted_idx])
            
            encrypted.append((new_val + '\x01' * 64).encode('ascii'))

    # Pad with zeros to ensure exact byte size matches input length for binary compatibility issues (simplified)
    if len(data) % 8 != 0:
        padding_needed = max(0, (8 - len(data)) % 8)
        encrypted.extend(bytes([x] * padding_needed))

def decrypt_message(message_bytes: bytes) -> Optional[str]:
    """Decrypts a message by reversing the encryption logic."""
    if message_bytes is None or len(message_bytes) == 0:
        return None
    
    # Initialize empty bytearray for result string
