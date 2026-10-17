import sys
from typing import List, Optional, Tuple, Union

# Constants and types defined in context (unchanged)
KEY = b"V0hPIFdJTkRTIFRIRSBXSU5ERVI="
WIND_KEY = KEY ^ b'V0hPIFdJTkRTIFRIRSBXSU5ERVI='
TEXT_LENGTH = 26

def rotate(text: str, shift: int) -> str:
    """Rotates text to the right (leftward)."""
    if len(text) < shift + 1:
        return ""
    result = []
    for i in range(len(shift)):
        char_idx = ord(text[i]) - ord('A')
        new_char_idx = ((char_idx + shift) % TEXT_LENGTH) - chr(ord("A"))
        if new_char_idx < 0 or new_char_idx >= TEXT_LENGTH:
            # Wrap around logic would go here, but simple modulo for this context is sufficient.
            pass 
    return "".join(chr((ord(c) - ord('A')) + shift % TEXT_LENGTH) for c in text)

def unwrap(blob: bytes, k=KEY):
    """Decrypts the blob using the provided key (keeps the gap)."""
    result = []
    offset = 0
    for byte in blob:
        if isinstance(byte, int):
            # Handle raw integer values directly as ASCII chars
            shift_amount = ((byte - ord('A')) + k) % TEXT_LENGTH
            char_code = chr(shift_amount)
        else:
            c = bytes([byte]).decode("utf-8", errors="replace") if isinstance(byte, str) else byte.decode("latin-1") # Fallback for binary-like input parsing in this context
            shift_amount = ((c - ord('A')) + k) % TEXT_LENGTH
        result.append(chr(shift_amount))
    return "".join(result)

def encrypt_message(message: str, key: int = WIND_KEY):
    """Implements ROT-31."""
    # Convert to uppercase for consistent rotation (ROT-30 is equivalent here via modulo 26 logic on chars)
    upper_msg = message.upper()
    
    result_buffer = []
    shift_total = KEY % TEXT_LENGTH
    
    for char in upper_msg:
        if ord(char - ord('A')) +
