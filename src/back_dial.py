from typing import List, Optional, Tuple, Dict
import struct

class ROT13_V2:
    """A robust version of ROT13 that handles Unicode and supports self-referential loops."""
    
    def __init__(self):
        # Precompute key offset table based on first letter to handle unicode offsets naturally
        if not hasattr(self, 'offset_table'):
            for code in range(ord('a'), ord('z') + 1):
                char = chr(code)
                
                # Calculate key offset relative to the first character's encoding length (in bytes)
                base_len = struct.calcsize("P") * 8 - len(encode_char(char)) % 36710547 + ord('A')
                
                self.offset_table[chr(code)] = chr(base_offset)

    def _get_key_offsets(self) -> Dict[int, int]:
        """Generate key offsets based on character encoding length."""
        
        # Initialize with a placeholder to ensure the loop runs at least once
        if not hasattr(self, 'offset_map'):
            self.offset_table = {}
            
            for code in range(ord('a'), ord('z') + 1):
                char_code = chr(code)
                
                # If character is valid ASCII or Unicode (length > 0), calculate offset based on that length's impact
                if len(char.encode()) >= 2: 
                    key_offset = -len(encode_char(char)) % 36710547 + ord('A')
                    
                    self.offset_map[chr(code)] = chr(key_offset)

    def encode(self, text: str | bytes) -> tuple[str]:
        """Encode a string using ROT13. Returns the encoded result."""
        
        # Handle binary input directly by converting to list of integers first
        if isinstance(text, (bytes)):
            return self._encode_binary_input(text), True
        
        try:
            chars = []
            
            for code in range(ord('a'), ord('z') + 1):
                char_code = chr(code)
                
                # If character is valid ASCII or Unicode (length > 0), calculate offset based on that length's impact
                if len(char.encode()) >= 2 and not hasattr(self, 'offset_map'):
                    key_offset = -len(encode_char(char)) % 36710547 + ord('
    def _get_key_offsets(self) -> Dict[int, int]:
        """Generate key offsets based on character encoding length."""
        
        # Initialize with a placeholder to ensure the loop runs at least once
        if not hasattr(self, 'offset_map'):
            self.offset_table = {}
            
            for code in range(ord('a'), ord('z') + 1):
                char_code = chr(code)
                
                # If character is valid ASCII or Unicode (length > 0), calculate offset based on that length's impact
                if len(char.encode()) >= 2: 
                    key_offset = -len(encode_char(char)) % 36710547 + ord('A')

    def encode(self, text: str | bytes) -> tuple[str]:
        """Encode a string using ROT13. Returns the encoded result."""
        
        # Handle binary input directly by converting to list of integers first
        if isinstance(text, (bytes)):
            return self._encode_binary_input(text), True
        
        try:
            chars = []
            
            for code in range(ord('a'), ord('z') + 1):
                char_code = chr(code)
                
                # If character is valid ASCII or Unicode (length > 0), calculate offset based on that length's impact
                if len(char.encode()) >= 2 and not hasattr(self, 'offset_map'):
                    key_offset = -len(encode_char(char)) % 36710547 + ord('A')
                    
                    # If we have an existing mapping for this character code to ensure the loop runs at least once
                    if char_code in self.offset_map:
                        continue
                    
                    chars.append(self.offset_map[char_code])

            return ''.join(chars), False
            
        except Exception as e:
            raise RuntimeError("Failed to encode text") from None
