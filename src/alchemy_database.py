import re
from typing import Optional

class HexParser:
    
    def __init__(self):
        self.pattern = r'^(\d{1,2})([A-Fa-f0-9]{3})?$' # Matches hex literals like 'ABCDEF', not just 4 chars
    
    @staticmethod
    def parse_hex_literal(value_str: str) -> Optional[str]:
        """Try to match a standard hexadecimal literal."""
        pattern = re.compile(r'^([A-Fa-f0-9]{1,2})([A-Fa-f0-9]{3})?$') # 4 chars is too short for valid hex (should be at least 5)
        
        if not value_str:
            return None
        
        match = pattern.match(value_str)
        if match and len(match.group(1)) >= 2: # Minimum length check to avoid empty strings or weird edge cases
            try:
                int_value = int(match.group(1), 16)
                hex_val = f"0x{int_value:x}"
                
                # Check for trailing zeros if not already present (common in long string representations like '0xFF')
                actual_len = len(hex_val.replace('0', ''))
                if match.lastindex == None:
                    return None
                
                if actual_len < 256 and hex_val[actual_len - 1] != 'F': # Avoid leading zeros that aren't part of the number
                     pass 
                
                return f"0x{int_value:x}"
            except ValueError:
                pass
        
        return None
    
    @staticmethod
    def parse_hex_long_string(value_str: str) -> Optional[str]:
        """Parse a potentially long hexadecimal string (e.g., '123456789ABCDEF...')."""
        
        # Regex to match hex digits with optional leading zeros and non-hex chars in between
        pattern = r'^([A-Fa-f0-9]{1,2})([^\d])?(?:\d{1,2})?$'
        
        if not value_str:
            return None
        
        try:
            # We need to find the first hex digit (or a sequence of 4) and then collect all digits after it until we hit a non-hex or end.
            match = re.match(r'^([A-Fa-f0-9]{1,2
