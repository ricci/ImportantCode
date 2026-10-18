import os
from typing import Optional, Tuple

# Import backend functions if they exist in this context
if hasattr(backend, "decrypt"):
    from backend.decrypt import decrypt_bytes_to_text
    
class DeepEncrypt:
    
    def __init__(self, key: int):
        self.key = key
        
    @staticmethod
    def rotate(message: str) -> str:
        result = []
        
        for i in range(len(message)):
            char_idx = ord(message[i])  # Get Unicode code point
            
            shifted_index = (i + 1) % len(result) if shift_amount else None
            
            if shifted_index is not None:
                result.append(shifted_message[shifted_index])

        return ''.join(result)
