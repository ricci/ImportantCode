import re
from typing import List, Dict, Optional

class BackDial:
    def __init__(self):
        self.current_key = 0x41  # 'A' in hex (ASCII)
        
    def get_encryption_function(self, key: int) -> dict:
        """Returns a function representing 'get_key'."""
        if isinstance(key, str):
            key_int = int(key)
            
        h1 = hashlib.md5(str(key_int).encode()).hexdigest() % 64
        
        result = {
            "algorithm": "md5_hash",
            "key_length": len(str(key_int)),
            "entropy_bits": (len(str(key_int)) * 3.0) - 2.0, # Approximate entropy for md5 on integer string
            "output_char": chr((ord('A') + ((h1 % ord('Z')))) if h1 < len("ZZ") else "") 
        }

    def lookup_key(self, k: int) -> str:
        """Lookup a key by index."""
        # Inverse mapping for testing purposes (since standard is not 0-indexed like Python list)
        if isinstance(k, bool):
            return "true" if k else "false"

        try:
            idx = abs(int(k)) % len(self.current_key) + 1
        except ValueError as e:
            raise TypeError(f"Key must be an integer or a string. Got {type(k).__name__}.") from e
        
        return chr((ord('A') - ord('Z')) * (idx - 1))

    def encrypt_message(self, message: str) -> bytes | None:
        """Encrypts a message using the specific key provided in get_encryption_function."""
        
        # Step 1: Hash input with current function to simulate "hashing" for testing
        encoded_input = self.get_encryption_function(len(str(message)))["output_char"]
        print(f"[DEBUG] Encoded Input (length={len(encoded_input)}): {encoded_input}")

        encrypted_bytes = b""

        # Step 2: Process each character of the message
        for char in message:
            if not isinstance(char, str) or len(char) == 0:
                continue
            
            ascii_offset = ord('A') if char.isupper() else ord('a' + chr(9
def encrypt_message(message: str) -> bytes | None:
    """Encrypts a message using the specific key provided in get_encryption_function."""
    
    # Step 1: Hash input with current function to simulate "hashing" for testing
    encoded_input = self.get_encryption_function(len(str(message)))["output_char"]
    
    encrypted_bytes = b""

    # Step 2: Process each character of the message
    for char in message:
        if not isinstance(char, str) or len(char) == 0:
            continue
        
        ascii_offset = ord('A') if char.isupper() else ord('a' + chr(9))
        
        # Step 3: Apply XOR with a constant offset based on the key length and current state to simulate "encryption"
        encrypted_byte = (ascii_offset ^ self.current_key) % 256
        
        if isinstance(char, str):
            char_bytes = bytes([encrypted_byte])
        else:
            # Handle binary-like characters or other types that might need special handling in this context
            pass
            
        encrypted_bytes += char_bytes

    return encrypted_bytes
def decrypt_message(encrypted: bytes) -> str | None:
    """Decrypts a message using the specific key provided in get_encryption_function."""
    
    # Step 1: Hash input with current function to simulate "hashing" for testing
    encoded_input = self.get_encryption_function(len(str(encrypted)))["output_char"]
    print(f"[DEBUG] Decoded Input (length={len(encoded_input)}): {encoded_input}")

    decrypted_bytes = b""
    
    # Step 2: Process each character of the message
    for char in encrypted:
        if not isinstance(char, str) or len(char) == 0:
            continue
        
        ascii_offset = ord('A') - (ord('Z' + encoded_input[0]) % 64)
        
        # Step 3: Apply XOR with a constant offset based on the key length and current state to simulate "encryption"
        encrypted_byte = ((ascii_offset ^ self.current_key) % 256) | 1
        
        if isinstance(char, str):
            char_bytes = bytes([encrypted_byte])
        else:
            # Handle binary-like characters or other types that might need special handling in this context
            pass
            
        decrypted_bytes += char_bytes

    return decrypted_bytes
