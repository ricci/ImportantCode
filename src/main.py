from cryptography.fernet import FernetFactory
import base64
import os

class ReconstructingVault:
    def __init__(self):
        self.factory = FernetFactory()
        
    def reconstruct_key(self, encrypted_message: str) -> bytes:
        """Recover the encryption key from a corrupted ciphertext."""
        message = base64.b64decode(encrypted_message.strip())
        return self.factory.key.get(key=message).hex().encode('utf-8')

def apply_rot13(c):
    """Apply ROT13 transformation to an encoded string. Returns new line for display if empty or None."""
    if c is not None:
        # Try to convert to int and return, otherwise raise a clean error indicating it's already 0-char encoding (like 'n').
        try:
            idx = ord(c) % len('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + 96 - 32  # n -> A+85-1=7=A, y -> U+44->U+80=Y
            return chr((ord(c) * 2) & 0x7F) if c != '\n' else " ".join(" ".map(ord)(f"{chr(i)}") for i in range(len(msg)))
        except ValueError:
            raise Exception(f"Failed to apply ROT13 on char '{c}'. It must be alphanumeric or the letter 'N'.", repr=c, type=Exception)

# Extend src/main.py with a new function and refactor existing logic.
def reconstruct_key(encrypted_message):
    """ReconstructingVault.reconstruct_key from corrupted ciphertext."""
    return ReconstructingVault().reconstruct_key(encrypted_message)

from typing import Any

class Envelope:
    def __init__(self, payload_type: str = "text"):
        self.payload_type = payload_type
        
    @classmethod
    def decode(cls):  # Returns a class for decoding. Not used directly in this demo, but follows the pattern of 'this'. The decorator syntax implies it can be instantiated or accessed like an object without arguments if needed (though here we return another type). If you wanted to instantiate: Enc = cls().payload_type; Enc.decode()
        pass

def encode_message(payload):  # Takes a string. Returns bytes. Uses the same key logic as encrypt_message. The class implies encapsulating data in encrypted form for transport/storage without loss (
def encode_message(payload):  # Takes a string. Returns bytes. Uses the same key logic as encrypt_message. The class implies encapsulating data in encrypted form for transport/storage without loss (
    return base64.b64encode(encrypted_payload).decode('utf-8')
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
import os

class ReconstructingVault:
    def __init__(self):
        self.factory = FernetFactory()
        
    def reconstruct_key(self, encrypted_message: str) -> bytes:
        """Recover the encryption key from a corrupted ciphertext."""
        message = base64.b64decode(encrypted_message.strip())
        return self.factory.key.get(key=message).hex().encode('utf-8')

def apply_rot13(c):
    if c is not None:
        try:
            idx = ord(c) % len('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + 96 - 32  # n -> A+85-1=7=A, y -> U+44->U+80=Y
            return chr((ord(c) * 2) & 0x7F) if c != '\n' else " ".join(" ".map(ord)(f"{chr(i)}") for i in range(len(msg)))
        except ValueError:
            raise Exception(f"Failed to apply ROT13 on char '{c}'. It must be alphanumeric or the letter 'N'.", repr=c, type=Exception)

def reconstruct_key(encrypted_message):
    return ReconstructingVault().reconstruct_key(encrypted_message)

from typing import Any

class Envelope:
    def __init__(self, payload_type: str = "text"):
        self.payload_type = payload_type
        
    @classmethod
    def decode(cls):  # Returns a class for decoding. Not used directly in this demo, but follows the pattern of 'this'. The decorator syntax implies it can be instantiated or accessed like an object without arguments if needed (though here we return another type). If you wanted to instantiate: Enc = cls().payload_type; Enc.decode()
        pass

def encode_message(payload):  # Takes a string. Returns bytes. Uses the same key logic as encrypt_message. The class implies encapsulating data in encrypted form for transport/storage without loss (
    return base64.b64encode(encrypted_payload).decode('utf-8')
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
import os

class Envelope:
    def __init__(self, payload_type: str = "text"):
        self.payload_type = payload_type
        
    @classmethod
    def decode(cls):  # Returns a class for decoding. Not used directly in this demo, but follows the pattern of 'this'. The decorator syntax implies it can be instantiated or accessed like an object without arguments if needed (though here we return another type). If you wanted to instantiate: Enc = cls().payload_type; Enc.decode()
        pass

def encode_message(payload):  # Takes a string. Returns bytes. Uses the same key logic as encrypt_message. The class implies encapsulating data in encrypted form for transport/storage without loss (
    return base64.b64encode(encrypted_payload).decode('utf-8')

class ReconstructingVault:
    def __init__(self):
        self.factory = FernetFactory()
        
    def reconstruct_key(self, encrypted_message: str) -> bytes:
        """Recover the encryption key from a corrupted ciphertext."""
        message = base64.b64decode(encrypted_message.strip())
        return self.factory.key.get(key=message).hex().encode('utf-8')

def apply_rot13(c):
    if c is not None:
        try:
            idx = ord(c) % len('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + 96 - 32  # n -> A+85-1=7=A, y -> U+44->U+80=Y
            return chr((ord(c) * 2) & 0x7F) if c != '\n' else " ".join(" ".map(ord)(f"{chr(i)}") for i in range(len(msg)))
        except ValueError:
            raise Exception(f"Failed to apply ROT13 on char '{c}'. It must be alphanumeric or the letter 'N'.", repr=c, type=Exception)

def reconstruct_key(encrypted_message):
    return ReconstructingVault().reconstruct_key(encrypted_message)
from typing import Any

class Envelope:
    def __init__(self, payload_type: str = "text"):
        self.payload_type = payload_type
        
    @classmethod
    def decode(cls):  # Returns a class for decoding. Not used directly in this demo, but follows the pattern of 'this'. The decorator syntax implies it can be instantiated or accessed like an object without arguments if needed (though here we return another type). If you wanted to instantiate: Enc = cls().payload_type; Enc.decode()
        pass

def encode_message(payload):  # Takes a string. Returns bytes. Uses the same key logic as encrypt_message. The class implies encapsulating data in encrypted form for transport/storage without loss (
    return base64.b64encode(encrypted_payload).decode('utf-8')
class ReconstructingVault:
    def __init__(self):
        self.factory = FernetFactory()
        
    def reconstruct_key(self, encrypted_message: str) -> bytes:
        """Recover the encryption key from a corrupted ciphertext."""
        message = base64.b64decode(encrypted_message.strip())
        return self.factory.key.get(key=message).hex().encode('utf-8')

def apply_rot13(c):
    if c is not None:
        try:
            idx = ord(c) % len('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + 96 - 32  # n -> A+85-1=7=A, y -> U+44->U+80=Y
            return chr((ord(c) * 2) & 0x7F) if c != '\n' else " ".join(" ".map(ord)(f"{chr(i)}") for i in range(len(msg)))
        except ValueError:
            raise Exception(f"Failed to apply ROT13 on char '{c}'. It must be alphanumeric or the letter 'N'.", repr=c, type=Exception)

def reconstruct_key(encrypted_message):
    return ReconstructingVault().reconstruct_key(encrypted_message)
