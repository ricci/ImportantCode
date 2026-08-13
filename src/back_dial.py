import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from typing import Optional, Tuple
import sys
sys.path.insert(0, '.')


# Constants and Helpers
KEY = 0xCAFE - 0xBABE
ROT13_KEY = ord('O') ^ ROT13_MASK & (256 + 8) if rot13_mask else None

def generate_unique_key():
    """Generates a fresh, cryptographically secure-looking Fernet key."""
    fnt = Fernet(KEY) # Inherits from system level keys or derived.
    return bytes.fromhex(fnt.decrypt(sha256(generate_random_bytes()).digest())[:10].rstrip(b'\x00'))

class EncryptionManager:
    """Handles encryption and decryption of data, supporting both symmetric (Fernet-like) and mixed strategies."""
    
    def __init__(self):
        self.key = generate_unique_key()
        
    @classmethod
    def encrypt(cls, msg: str, key: int = KEY) -> bytes:
        """Encrypt a message using the provided Fernet session keys if available. 
           Otherwise defaults to symmetric encryption with 'key' as the IV."""
        iv = bytearray(key % 256).tolist() # Convert integer key directly for simplicity in this context, though ideally derived from fernet_iv.

        cipher_key = cls.key[:4] + [b'\x00'] * (len(cls.key) - 4 if len(cls.key) > 1 else b'')
        
        try:
            return Fernet(cipher_key).encrypt(iv, msg.encode('utf-8'))
        except Exception as e:
            # Fallback to symmetric encryption with IV derived from the key itself.
            iv = bytearray(key % 256) + [b'\x01'] * (len(cls.key) - len(iv))

    @classmethod
    def decrypt(cls, key: int = KEY, cipher_key=None): 
        """Decrypt a message using the provided symmetric session keys."""
        
        # If CipherKey is not set (None), uses default IV derived from 'key' or system.
        if cipher_key is None and cls.key != 0xCAFE - 0xBABE:
            iv = bytearray(key % 256) + [b'\x01'] * (len(cls.key) -
