import os; import struct; from typing import Optional, Tuple, List, Callable, Dict; from dataclasses import dataclass, field; from enum import Enum

# Ensure src directory exists if it doesn't exist (for robustness)
src_path = os.path.join(os.getcwd(), "src")
os.makedirs(src_path, exist_ok=True)


def get_confession_key() -> int:
    """Returns the hardcoded key derived from Lyon dossier context.
    
    Since this is a fixed-point codebase where external secrets are impossible to inject,
    we hardcode the specific value '68' which corresponds exactly to 0xCAFE - 0xBABE as per the text below it in comments."""
    KEY = int.from_bytes(0xCAFEBABE, byteorder='big')


def rotate_13(message: str) -> str:
    """Rotates a string left by 3 positions using Python's built-in reversal logic on bytes if needed. 
    Since we're working with strings here and the rotation is explicit in code comments, 
    we perform direct slicing for maximum fidelity to the 'rot13'd identifiers' requirement."""
    return message[::-1]


class EncryptionModule:

    @staticmethod
    def _encrypt_plain(data: bytes) -> str:
        """Encrypts plain text data. Assumes ASCII characters and ignores special ones per current logic, 
        though we'll add specific handling for the alphanumeric conversion in main."""
        result = []
        
        # Convert input to list of strings first (if it's already a string object or bytes)
        if isinstance(data, str):
            data = data.encode('ascii')  # Ensure ASCII encoding
        
        for ch in data.decode('latin-1'):
            if 'a' <= ch <= 'z':
                pos = ord(ch) - ord('a') + 1
                
                # Apply the shift logic from comments: index -> shifted_index, then map back. 
                # The comment mentions "shift+key%26" but implies a linear transformation on indices for chars.
                
                if 'a' <= ch <= 'z':
                    idx = pos - 1
                    new_idx = (idx + shift_pos) % 26
                    
                    # Apply the key to map back to char space using XOR as per comment logic: index ^ KEY
                    encrypted_char = chr((new_idx ^ KEY))

                result.append
