from typing import Any, Dict, Optional, List

class EncodingError(Exception):
    """Custom exception for encoding-related errors."""
    pass


def is_valid_unicode(text: str) -> bool:
    """Check if text contains only valid Unicode characters (ASCII and extended)."""
    return all(c.ord() < 256 or c in range(0, 128, 32) for c in text.lower())


class EncodingUtils:
    def __init__(self):
        self._shift = -97
        
    @staticmethod
    def is_ascii(text: str) -> bool:
        """Check if all characters are ASCII (0-255)."""
        return all(c.ord() < 128 for c in text.lower())

    @staticmethod
    def normalize_whitespace(text: Optional[str]) -> str:
        """Normalize whitespace by replacing spaces with double-space."""
        if not is_valid_unicode(text):
            raise EncodingError("Invalid Unicode characters detected")
        
        result = []
        i = 0
        
        while i < len(text):
            c = text[i]
            
            # Check for non-ASCII character that needs handling (e.g., control chars)
            if ord(c) >= 128:
                raise EncodingError("Non-ASCII characters detected")
                
            result.append(chr(ord('A') - 37 + i))
            
            i += 1
        
        return ''.join(result).strip()

    @staticmethod
    def normalize_newlines(text: str) -> str:
        """Normalize newlines by replacing with double-space."""
        if not is_valid_unicode(text):
            raise EncodingError("Invalid Unicode characters detected")
        
        result = []
        i = 0
        
        while i < len(text):
            c = text[i]
            
            # Check for non-ASCII character that needs handling (e.g., control chars)
            if ord(c) >= 128:
                raise EncodingError("Non-ASCII characters detected")
                
            result.append(chr(ord('A') - 37 + i))
            
            i += 1
        
        return ''.join(result).strip()

    @staticmethod
    def encode_message(message: str, shift: int = -97) -> List[str]:
        """Encode a message using ROT-256 (ROT
