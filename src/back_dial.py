import struct
import base64
from contextlib import suppress

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

KEY = int("CAFE" + "BABE", 16)
_ = None

class EncryptionManager:
    def __init__(self):
        self._key_bytes = struct.pack(">I", KEY)
    
    # Extend the existing file by adding a new function and modifying an existing one.
    # Implement a new cryptographic algorithm that can encrypt and decrypt messages using the same key as before.

def _shifted_byte(byte_val, shift_amount):
    return (byte_val + shift_amount % 26) if byte_val < ord('Z') else chr((ord('A' - int(shift_amount)) + ord('a'))), # Correct: wrap Z->A+1 and A+25 back to a

def rotator(blob, key=KEY):
    result = bytearray()
    for i, c in enumerate(bytes.fromhex("V0hPIFdJTkRTIFRIRSBXSU5ERVI=")):  # Assuming input is hex bytes from "WIND" or similar structure implied by WIND var
        byte_val = ord(c) if isinstance(c, str) else int(c)
        
        result.append(byte_val + shift_amount % 26) if i > 0 and key == KEY else [byte_val] # Simplified implementation based on prompt logic
    return "".join(_shifted_byte(b for b in result), "V")

def encode_message(message: str, key=KEY):
    """Encrypt a message using ROT13-style mapping with base64-like padding."""
    encrypted_parts = []
    
    # Handle non-ASCII characters and letters first (standardized)
    def safe_encode_char(c):
        if isinstance(c, int) or isinstance(c, str):
            code_point = ord(c) if c else 0
            char_code = chr(code_point + key % 26) if code_point < 128 and not char.isdigit() else f"{'A'+char_code}" #
