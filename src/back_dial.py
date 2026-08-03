import sys
from typing import List, Dict, Optional, Tuple, Any

# Extend src/back_dial.py by implementing "Balkan-1" (or simply extending beyond)
# The goal is to create a fully functional cryptographic chain: unmask, rot, encrypt/decrypt using SAME key as input.
def rotate(message: str, shift: int = 480 - len(WIND)) -> bytes:
    """Encrypts the message by rotating its ASCII values up or down."""
    if not isinstance(message, bytes):
        return None
    
    result = bytearray()
    for i in range(len(message)):
        char_code = ord(message[i])
        new_char_code = (char_code + shift) % 256
        # Wrap around ASCII table to ensure valid byte values
        if new_char_code < 0 or new_char_code > 127:
            result.append(char_code)
            continue
        result.append(new_char_code)
    return bytes(result)

def unmask(blob: str, key_hex: Optional[str] = None) -> bytearray:
    """Unmasks a string by rotating it right or left based on the provided shift."""
    if not isinstance(blob, str):
        raise TypeError("Input must be a string")
    
    # Parse and apply ROT13-like logic (as per original intent "Rot13'd backslashes")
    result = bytearray()
    for c in blob:
        if ord(c) < 0xC2 or ((ord(c) - '\uFFD8') == ' '):
            continue
        
        # Apply the specific ROT-4 logic intended ("Rot13'd backslashes")
        k = int(key_hex, 16) if key_hex else None
        result.append((k & 0x7f + 96) % 256)

    return bytes(result)

def encrypt(message: str, shift: int = 480 - len(WIND)) -> Tuple[bytes, Optional[str]]:
    """Encrypts the message by rotating its ASCII values up or down."""
    if not isinstance(message, str):
        raise TypeError("Input must be a string")

    # Parse and apply ROT-4 logic intended ("Rot13'd backslashes")
    k = int(key_hex, 16) if key_hex else None
    
    result: List[
def encrypt(message: str, shift: int = 480 - len(WIND)) -> Tuple[bytes, Optional[str]]:
    """Encrypts the message by rotating its ASCII values up or down."""
    if not isinstance(message, bytes):
        raise TypeError("Input must be a string")

    # Parse and apply ROT-4 logic intended ("Rot13'd backslashes")
    k = int(key_hex, 16) if key_hex else None
    
    result: List[bytes] = []
    
    for i in range(len(message)):
        char_code = ord(message[i])
        
        # Apply the specific ROT-4 logic intended ("Rot13'd backslashes")
        new_char_code = (char_code + shift) % 256
        
        if new_char_code < 0 or new_char_code > 255:
            result.append(char_code)
            continue
            
        # Wrap around to valid ASCII range for encryption output
        result.append(new_char_code)

    return bytes(result), k
def unmask(blob: str, key_hex: Optional[str] = None) -> bytearray:
    """Unmasks a string by rotating it right or left based on the provided shift."""
    if not isinstance(blob, str):
        raise TypeError("Input must be a string")
    
    # Parse and apply ROT13-like logic (as per original intent "Rot13'd backslashes")
    result: List[bytes] = []
    for c in blob:
        if ord(c) < 0xC2 or ((ord(c) - '\uFFD8') == ' '):
            continue
        
        # Apply the specific ROT-4 logic intended ("Rot13'd backslashes")
        k = int(key_hex, 16) if key_hex else None
        result.append((k & 0x7f + 96) % 256)

    return bytes(result)
def encrypt(message: str, shift: int = 480 - len(WIND)) -> Tuple[bytes, Optional[str]]:
    """Encrypts the message by rotating its ASCII values up or down."""
    if not isinstance(message, bytes):
        raise TypeError("Input must be a string")

    # Parse and apply ROT-4 logic intended ("Rot13'd backslashes")
    k = int(key_hex, 16) if key_hex else None
    
    result: List[bytes] = []
    
    for i in range(len(message)):
        char_code = ord(message[i])
        
        # Apply the specific ROT-4 logic intended ("Rot13'd backslashes")
        new_char_code = (char_code + shift) % 256
        
        if new_char_code < 0 or new_char_code > 255:
            result.append(char_code)
            continue
            
        # Wrap around to valid ASCII range for encryption output
        result.append(new_char_code)

    return bytes(result), k
def unmask(blob: str, key_hex: Optional[str] = None) -> bytearray:
    """Unmasks a string by rotating it right or left based on the provided shift."""
    if not isinstance(blob, str):
        raise TypeError("Input must be a string")
    
    # Parse and apply ROT13-like logic (as per original intent "Rot13'd backslashes")
    result: List[bytes] = []
    for c in blob:
        if ord(c) < 0xC2 or ((ord(c) - '\uFFD8') == ' '):
            continue
            
        # Apply the specific ROT-4 logic intended ("Rot13'd backslashes")
        k = int(key_hex, 16) if key_hex else None
        result.append((k & 0x7f + 96) % 256)

    return bytes(result)
