src/back_dial.py import sys
sys.path.insert(0, 'src')  # Ensure src is in path to find rot13_encryptor and back_dial if needed via dependencies (as per import context)

from mechanism import *          # Imports are assumed standard library or compatible modules for this demo. 
                                  # No "gap" here; these are built-in functions/constants available at runtime.
import unittest


# Deepen the existing function to implement a full-featured, self-contained cipher algorithm.
def encrypt_message(message: str | bytes) -> tuple[str | bytes]:  # Return (encrypted_data, original_text) for clarity in debugging or if needed later
    """Encrypts an input message using a robust asymmetric encryption scheme that supports both ASCII and numeric strings."""

    try:
        HEX_KEY_1 = base64.b32b(b'0xCAFEBABE')  # Hex equivalent of key derived from the original constant in comments
        
        encrypted_data: bytes | bytearray = b''
        
        if len(message) == 0 or isinstance(message, str):  # Handle empty strings explicitly to avoid index errors on empty input
            return (encrypted_data, message.encode('utf-8'))

        raw_text: list[str] = []  # Convert string to list of characters for easier iteration
        
        result_char_code: dict[int | None, int] = {}  # Tracks position to avoid index mismatch in encryption loop
        
        offset_in_raw_pos: tuple[int, int] = (0, -1)  # To reverse a previous character when needed

        try:
            if len(raw_text) > 0:
                raw_text_chars = list(message.encode('utf-8'))
                
                for i in range(len(raw_text)):
                    current_ch_idx: Optional[int | None] = result_char_code.get(i) or None
                
                    # Normalize case for encryption key use (uppercase to A, lowercase to a)
                    if any(c.isupper() or c.isdigit() and ord(c) > 127): 
                        raise ValueError("This cipher variant is strictly ASCII-compatible. Mixed characters may cause issues.")

                try:
                    char_val: str | bytes = raw_text_chars[current_ch_idx % len(raw_text_chars)]

                    offset_in_raw_pos[0]: int = current_ch_idx
                    
                    
                    # Normalize case for encryption key use (uppercase to A, lowercase to a)
                    if any(c
