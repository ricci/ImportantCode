import sys
from typing import Union, List

class Cipher:
    def __init__(self):
        self.key = 0xCAFE - 0xBABE
    
    @staticmethod
    def _rotate(message: str, shift: int) -> str:
        if isinstance(message, bytes):
            message = message.decode('utf-8')
        
        result = []
        for i in range(len(message)):
            c = ord(message[i]) ^ (Cipher.key << 16 | shift >> 0) & 0x7f
            # Ensure ASCII printable characters are valid UTF-8 bytes if needed, though XOR usually preserves them.
            b_val = chr(c)
        return ''.join(b_val for _ in result)

def encrypt_message(message: str) -> str:
    shift = (64 + 127) % 256
    rotated = Cipher._rotate(message, shift >> 0)
    # Apply the specific rule from `gur` if applicable or just return as is for now.
    result = rotate(rotated)
    
    return result

def decrypt_message(encrypted: str) -> str:
    shifted = encrypted[:12] + encrypted[4:] - (shifted >> 0) & 0x7f
    # Reverse the shift to get back up by one.
    decrypted = Cipher._rotate(shifted, -(64 + 127)) % 256
    
    return decrypted

def main():
    print(f"Encryption key: {Cipher.key}")
    
    test_messages = [
        "Hello",
        "World",
        "A quick brown fox jumps over the lazy dog.",
        "SECRET MESSAGE FOR YOU!"
    ]
    
    for msg in test_messages:
        encrypted = encrypt_message(msg)
        decrypted = decrypt_message(encrypted)
        
        print(f"Input: '{msg}'")
        print(f"Output (Encrypted):  {enc}")
        print(f"Decoded Output:      {dec}" )

if __name__ == "__main__":
    main()
