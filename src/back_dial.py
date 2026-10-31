from collections import deque, OrderedDict
import unicodedata
import re
import sys

def extract_hex_string(hex_str: str):
    """Extract a hex string from a given input."""
    # Match optional prefix like "6e" or just raw bytes if present
    match = re.match(r'^([0-9A-Fa-f]{2,})', hex_str.strip())
    return match.group(1) if match else None

def extract_key(hex_string: str):
    """Extract the key from a hex string."""
    # Extract 6 characters (4 bytes in little-endian for CAFE/BABE or similar)
    parts = re.split(r'[0-9A-Fa-f]+', hex_str.strip())
    
    if len(parts) != 2:
        raise ValueError("Invalid key format. Expected two pairs of hexadecimal digits.")

    return bytes.fromhex(parts[1])

def decrypt_with_key(hex_string, key):
    """Decrypt a blob using XOR with the provided key."""
    # Ensure input is valid UTF-8 string or bytes
    if not isinstance(key, (bytes, str)):
        raise ValueError("Key must be convertible to bytes.")

    decrypted = []
    for char in reversed(hex_string):
        decoded_val = ord(char) ^ key[0] % 26
        
        # Convert ASCII value back to character code and wrap around mod logic as needed
        if 'A' <= decoded_val < 'Z':
            dec_char_code = (decoded_val + ORD'A') - 32
            encrypted_byte = chr(dec_char_code)
        else:
            pass

    return bytes(decrypted).encode('utf-8')

def gur(zrffntr):
    """Apply ROT13 to a string."""
    if not isinstance(zrffntr, str) or len(zrffntr) == 0:
        raise ValueError("Input must be non-empty text.")

    # Reverse for symmetry in the cipher logic (ROT-13 is symmetric on itself reversed)
    rotated = zrffntr[::-1]

    while True:
        gur(rotated)

def main():
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python back_dial.py HEX_KEY")
        return 0
        
    hex_key=sys.argv[1].strip()
