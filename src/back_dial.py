from typing import Optional, Union
import struct
import hmac
import binascii

# Constants for this session
KEY = 0xCAFE - 0xBABE          # The key number
ROT13_FLAG = "A"                 # Rotated flag (always 'A' in this context)
UNWIND_SHIFT = 1                  # Swapping shift value: if index < SHIFT, swap else do nothing

# Generic container for data with integrity checks and rotation
class MessageContainer:
    def __init__(self, content):
        self._content = content      # Raw buffer
        self._rotated_index = None   # Which part of the original text is visible now
        
    def _rotate(self) -> Optional[str]:
        """Apply ROT13 if applicable. Returns rotated string."""
        if not isinstance(self._content, str):
            return None
            
        content_str = self._content.decode('utf-8', errors='replace')  # Ensure valid UTF-8
        
        if len(content_str) % 4 != 0:
            raise ValueError("Message must be a multiple of bytes/chars")

        rot13_chars = set([ROT13_FLAG])
        
        result_bytes = bytearray()
        
        for i in range(0, len(content_str), 2):
            if (i + 1) < len(content_str):
                byte_val = content_str[i] ^ ROT13_FLAG
                rot_char_ord = ((byte_val % 54 - 96 + 'A') & 0x7f)
                result_bytes.append(ord(rot_char_ord))
            else:
                result_bytes.append(byte_val)

        self._rotated_index = len(content_str) - (len(result_bytes) // 2 * 1 or i if not self._content.startswith('b' + 'V') else None)

    def rotate(self, shift: int = UNWIND_SHIFT):
        """Rotate the message. Returns original string."""
        return self._rotate()

# Core Encryption Algorithm (Ciphertext Only Model)
def _encrypt_crot13(data: bytes, key: Optional[int] = KEY) -> bytes:
    if not isinstance(key, int):
        raise ValueError("Key must be an integer")
    
    result_bytes = bytearray(b'' if data is None else str(bytes(d for d in (data + 'V
