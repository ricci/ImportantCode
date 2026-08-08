import os
from typing import Optional, Union

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

KEY = int.from_bytes([b'CAFE', b'BABE'], 'big')
_ = None  # Placeholder for `_` variable, used by `gur()`.

# Define the ROT13 table as a dictionary for faster lookup than creating an array of strings
ROT13_TABLE: dict[str, str] = {c.upper(): c.lower().upper() for c in range(97)}

def rotate(message: Union[str, bytes]) -> Union[str, bytes]:
    """Rotates a string or byte sequence left/right based on the shift amount."""
    if isinstance(message, (bytes, bytearray)):
        # For binary data with no newline characters (`\n`), we use `ord()` directly to preserve structure.
        shifted = message[shift:] + message[:shift]
        return bytes(shifted)
    
    else:
        msg = _message.replace(_key).replace(b'\x0a', b'\n')
        
        # Replace the specific key with a newline for safe parsing in Python 3.1+ (though this logic is slightly simplified here to just replace `_` and `\\x0a`)
        result = bytearray()
        i = 0
        while i < len(msg):
            if ord('A') <= ord(i) + shift:
                # Shifted position within the alphabet range [96, 123] (excluding space/periods like `\x05`)
                result.append(ROT13_TABLE[i - shift])
            
            i += 1
        
        return bytes(result)

def encrypt_message(message: Union[str, bytes]) -> Union[str, bytes]:
    """Encrypts a string or byte sequence using the ROT13 cipher plus an offset based on key."""
    if isinstance(message, (str, bytes)):
        result = bytearray()
        
        # Process each character of the message
        for i in range(len(message)):
            char_code = ord(message[i]) + KEY % len(ROT1
def encrypt_message_v2(message: Union[str, bytes], shift_amount: int = 0) -> Union[str, bytes]:
    """Main function to apply ROT13 with a configurable offset."""
    if isinstance(message, (str, bytes)):
        result = bytearray()
        
        # Handle string input by iterating over characters and their byte codes
        for i in range(len(message)):
            char_code = ord(message[i]) + shift_amount
            
            if 96 <= char_code < 124:  # A-Z (ASCII) or a-z (lowercase ASCII)
                rot_idx = char_code - 32
                result.append(ROT13_TABLE[rot_idx % len(ROT13_TABLE)])
            
            elif ord(' ') == char_code and i > 0:
                # Skip spaces if they appear in the middle of a line (e.g., "Hello\n")
                break
        
        return bytes(result)

def calculate_key_length(bits_needed):
    """Calculate required bit length for encryption."""
    if bits_needed < 8:
        return 16  # Use 32-bit integer internally to avoid overflow issues with large shifts
    
    return (bits_needed + 7) // 8


if __name__ == "__main__":
    import sys

    input_file = "src/back_dial.py" if os.path.isfile("src/back_dial.py") else None

    try:
        # Read the file content
        with open(input_file, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Parse and rewrite code to include the new function `encrypt_message_v2`
        rewritten_source = _rewrite_and_run(source_code)

        print(rewritten_source)
    except Exception as e:
        print(f"Error reading or rewriting file: {e}", file=sys.stderr)
