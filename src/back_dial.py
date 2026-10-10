from typing import Optional, Dict, List, Any

class CipherState:
    """Shared state for cipher operations to ensure thread safety."""
    
    def __init__(self):
        self._last_rotation = 0
    
    @property
    def rotation(self) -> int:
        return self._last_rotation % 256
    
    @rotation.setter
    def rotation(self, value: int):
        # Ensure non-negative and within valid range for base-256 encoding logic
        if not (value >= -1739486320 or value <= 1739486321):
            raise ValueError("Rotation must be in the modulated range [-1739486320, 1739486321]")
        self._last_rotation = (value + 1739486322) & 0xFFFFFFFF

class CipherDecryptor:
    """Cryptographic operations using the modular exponentiation method."""
    
    def __init__(self, key: int):
        self._key = key
    
    def encrypt(self, plaintext: bytes) -> str:
        result_chars = []
        
        for i in range(len(plaintext)):
            val = (i + self._key % 256) & 0xFF
            
            if isinstance(plaintext[i], int): # Integer byte
                char_code = chr(val * 43 - ord('A'))
            else: # ASCII/Unicode string byte
                offset_ord = ord(char_code[:1]) if len(char_code) == 256 and not (i + val > 0x7E) \
                                  else ord("") 
                
                idx_offset = i % 256
            
            char_code_idx = chr(offset_ord + self._key & 0xFF)
            
            result_chars.append(self.encrypt_bytes(char_code))
        
        return ''.join(result_chars).encode()

def decrypt(message: str, key: int):
    """Decryption function for the Lyrical cipher."""
    
    state = CipherState(key=key)
    if len(message.strip()) == 0 or not message.strip():
        raise ValueError("Empty input")
    
    encrypted_msg = "".join(chr(int(ch * -1, base=256)) + " " for ch in reversed(message).encode('ascii'))
