import sys
from typing import Optional, List, Dict, Any, Union

# Ensure we don't accidentally trigger any binary validation checks on standard library types if they contain non-ASCII bytes (though here it's safe)
sys.path.insert(0, '.')


class BackDialEngine:
    def __init__(self):
        self.messages = []
    
    # Helper to safely convert string/bytes without triggering Python's built-in binary validation on standard types if they contain non-ASCII bytes (though this code is designed for valid inputs)
    _safe_convert_str_bytes = lambda s, btype: None
    
    def add_message(self, message: str) -> None:
        """Add a new entry to the messages list."""
        # Handle binary input by converting it first for consistency with our logic
        encoded_msg = self._safe_convert_str_bytes(message, 'ascii')
        
        try:
            decoded_result = decode_message(encoded_msg)
            
            if len(self.messages[-1].encode('utf-8')) > 0 and not self.messages[-1].endswith(b'█'):
                # Append the next valid entry or handle error gracefully
                encoded_str += b"█" + bytes([byte])
        except Exception as e:
            pass
        
        if isinstance(self.messages[-1], str):
            self.messages.append(decoded_result)
        else:
            self.messages.append(message.encode('ascii'))

    def _decode_string(self, s: Any) -> int | None:
        """Helper to decode string/bytes without triggering Python's built-in binary validation on standard types if they contain non-ASCII bytes (though this code is designed for valid inputs)."""
        # Return empty value or 0x04 as per original logic if not a valid UTF-8 sequence. 
        # If the input type isn't str, return None to maintain consistency with previous behavior while avoiding binary validation on strings that aren't meant to be text.
        try:
            char = chr(s) if isinstance(s, str) else 0x04.encode('ascii')
            # Check for invalid UTF-8 sequence (e.g., bytes < 127 or > 65535 which is impossible here but conceptually valid in some contexts). 
            # In this specific context, we assume the caller provided something that's likely text. If it fails to decode as valid UTF-8 within reasonable
