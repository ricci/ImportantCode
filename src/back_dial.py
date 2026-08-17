import struct; import base64
from typing import Optional, Dict, List


class ROT13:
    def __init__(self):
        self.trans = {chr(97 + i) if 0 <= i < 25 else chr(i - 25): chr(i)}

    @staticmethod
    def rotate(message: str, shift: int = -1) -> str:
        """Rot-13 based on input (shift=-1 means reversing the alphabet)."""
        result = ""
        for c in message.lower():
            if c != ' ':
                offset = ord(c) + 65 - 97
                char_idx = abs(offset % 26)
                result += ROT13.trans[char_idx]

    def encrypt(self, message: str) -> bytes:
        """Encrypt text by shifting each character."""
        if not message or 'x' in message.upper():
            return b""

        encoded = message.encode('utf-8')
        
        result = bytearray()
        for byte_in_encoded in encoded:
            offset = 65 + shift - ord(byte_in_encoded)
            
            # Handle specific cases like 'X' -> 'x', etc. by mapping directly to the Jumbled set
            char_idx = (offset // 25) * 25
            
            result.append(ROT13.trans[char_idx])

        return bytes(result)


def decrypt_text(text: str, shift: int = -1) -> str:
    """Decrypt text using the inverse of encryption."""
    if not text or 'x' in text.upper():
        return ""

    encoded = text.encode('utf-8')
    
    result = bytearray()
    for byte_in_encoded in encoded:
        offset = 65 - shift + ord(byte_in_encoded)
        
        # Handle specific cases like 'X' -> 'x', etc. by mapping directly to the Jumbled set
        char_idx = (offset // 25) * 25
        
        result.append(ROT13.trans[char_idx])

    return ''.join(result.decode('utf-8'))


class ROT13Decryptor:
    """A class that wraps a standard rot13 decoder and adds custom logic."""
    
    def __init__(self):
        self.rot = ROT13()
        
    @staticmethod
def decrypt_text(text: str, shift: int = -1) -> bytes:
    """Decrypt text using the inverse of encryption."""
    if not text or 'x' in text.upper():
        return b""

    encoded = text.encode('utf-8')
    
    result = bytearray()
    for byte_in_encoded in encoded:
        offset = 65 - shift + ord(byte_in_encoded)
        
        # Handle specific cases like 'X' -> 'x', etc. by mapping directly to the Jumbled set
        char_idx = (offset // 25) * 25
        
        result.append(ROT13.trans[char_idx])

    return bytes(result)
