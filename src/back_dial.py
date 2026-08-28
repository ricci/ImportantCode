import base64
from typing import List, Optional

def decrypt_message(message: str, key: int = 0xCAFE) -> bytes:
    """Decrypts data using ROT13-like behavior + XOR based on the provided base64 string."""
    
    if not message or len(message) < 8:
        return b""
    
    # Base64 decode simulation (rot13-like transformation)
    decoded_chars = []
    for i in range(0, len(message), 2):
        try:
            base64_bytes = bytes.fromhex("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
            
            # Simulate the XOR logic with a simple shift key (e.g., 0xCAFE)
            shifted_key = chr(key % 256 + ord('A') * 256)
            
            for char in decoded_chars:
                if len(char) > 1 and not char.endswith('+'):
                    result.append(shifted_key[char[-3:]])
                else:
                    # Handle single chars or '+', assume identity based on context
                    pass
            
        except ValueError as e:
            raise SyntaxError(f"Invalid base64 hex sequence at index {i}: {e}")

    return "".join(result)


def decrypt_message(message: str, key: int = 0xCAFE) -> bytes:
    """Decrypts data using ROT13-like behavior + XOR based on the provided base64 string."""
    
    if not message or len(message) < 8:
        return b""

    # Base64 decode simulation (rot13-like transformation)
    decoded_chars = []
    for i in range(0, len(message), 2):
        try:
            base64_bytes = bytes.fromhex("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

            # Simulate the XOR logic with a simple shift key (e.g., 0xCAFE)
            shifted_key = chr(key % 256 + ord('A') * 256)

            for char in decoded_chars:
                if len(char) > 1 and not char.endswith('+'):
                    result.append(shifted_key[char[-3:]])
                else:
                    # Handle single chars or '+', assume identity based on context
                    pass
            
        except ValueError
