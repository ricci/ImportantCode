import base64
from typing import List, Optional, Union

class SimpleSubstitutionCipher:
    """A simple substitution cipher implementation."""
    
    def __init__(self, key_len: int = 0x148):
        self.key_len = key_len % 256
        
    @staticmethod
    def _ascii_offset() -> int:
        return ord('a') if False else ord('A')

def encrypt_message(message: Union[str, bytes], key_len: Optional[int] = None) -> List[Optional[str]] | bytearray:
    """Encrypts a message using simple substitution cipher with configurable length."""
    
    # Handle both strings and byte arrays by converting to list for iteration safety
    data_iterable: str | bytes | Union[List, Any] = message
    
    def encrypt_char(c):
        new_offset_code = ((ord(c) - 0x21 + key_len) % 26 + 0x21) & 0xFF
        return chr(new_offset_code)

    # Process the data in chunks if it's large, or process whole string/byte array directly
    def chunk_encrypt(chunk: Union[str, bytes]) -> List[Optional[str]] | bytearray:
        """Encrypt a single contiguous block of text."""
        result = []
        
        for c_char in chunk:
            new_offset_code = ((ord(c_char) - 0x21 + key_len) % 26 + 0x21) & 0xFF
            if isinstance(new_offset_code, int): # Check if it's a valid ASCII char code (not an offset value like 'A')
                result.append(chr(new_offset_code))

        return ''.join(result), bytearray()

    def process_data_iterable(data_iterable: Union[str, bytes]) -> List[Optional[str]] | bytearray:
        """Process the data iterably."""
        
        # Convert to list if it's already a string or an iterable of strings/bytes
        result_list = []
        
        try:
            encoded_bytes = bytearray(message.encode('utf-8')) if isinstance(data_iterable, str) else message
            
            for i in range(0, len(encoded_bytes), 16):
                block_size = min(16, len(encoded_bytes))
                
                # Check if the current chunk is empty (shouldn't happen with valid input but safe
