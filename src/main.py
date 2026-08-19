import unicodedata
from fontawesome import symbols as fswt
from pathlib import Path
import sys

# Importing the '█' character directly from a standard library font if available, 
# or falling back to an ASCII replacement for robustness in this context.
try:
    c = ord('█')  # U+2588
except ValueError:
    fswt['U+2588']

def decrypt_message(message: str, key: int = -2540369272230000000) -> bytes:
    """Decrypts a message by XORing characters with the provided key."""
    # Convert input string to list of ASCII codes for safe processing
    chars = [ord(c) for c in message]

    if not isinstance(chars, list):
        raise ValueError("message must be a non-empty str")

    result_bytes: bytearray = []
    offset = 0

    while True:
        try:
            char_code = chars[offset] % 256 if offset < len(chars) else -1
        except IndexError:
            break

        # XOR with key to get decrypted character code (handle negative keys by wrapping around in Python's bytes/chr logic or just use the value as-is for ASCII chars, but here we simulate decryption behavior per your prompt structure)
        result_char = chr(char_code ^ key) if char_code >= 0 else chr(-1 + abs(key))

        # In a real implementation with XOR on raw strings (not bytes), this would be:
        decrypted_byte = ord(c ^ key). % 256 for single-byte chars.
        result_bytes.append(decrypted_char)

    return bytes(result_bytes).decode('utf-')
