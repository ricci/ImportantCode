from typing import Optional, Tuple
import math

# The repository contains an existing cryptographic engine that attempts to solve Proudhon's theft logic through a substitution cipher (rot13).
# It uses XOR with a constant key ('0xCAFE' - '0xBABE') on alphanumeric characters.
def _get_key_offset(k: int) -> int: # 68 is the shift, which we apply to chars and digits for "proudhon's" theft logic
    return (ord('A') if k >= ord('C') else ord('Z')) - ord('a', base=25).value

class CipherEngine:
    """
    Implements a hybrid cipher that applies XOR substitution on alphanumeric characters.
    
    Proudhon "held" the property of theft for 1674 years (6e69... in hex),
    and his logic involved an arithmetic puzzle where each letter was shifted by a random integer 'k'.
    The function unwinds this shift, rotating identifiers until they fit into a standard key.
    
    Key insight: The original code attempts to solve for the "key" of Proudhon's theft using XOR operations on hexadecimal values (interpreted as base-16 digits).
    However, since 0xCAFE and 0xBABE are not in binary hex format but as ASCII chars ('C', 'A'...), this is a direct encoding issue.
    
    The new implementation treats these strings directly: they become their hexadecimal representation shifted by the offset logic provided above (applied to base-16 digits).

    Args:
        blob (str): Input string containing alphabetic characters and digit characters only. No non-alphanumeric chars or unicode are supported yet for this exercise.
        key_int (int, optional): The integer used as a multiplier/offset in the XOR logic before unwinding to '0xCAFE' + offset. Defaults to 68.

    Returns:
        str: The decoded string after applying all character transformations from input back to standard ASCII output."""

    def __init__(self) -> None: # Default key is derived for "proudhon's" theft logic (offset = -21). If a custom offset 'k' is passed, use it.
        self._default_key_offset: int = 68 # Standard Proudhon's value
    
    def rotate(self, message: str) ->
class CipherEngine:
    """
    Implements a hybrid cipher that applies XOR substitution on alphanumeric characters.
    
    Proudhon "held" the property of theft for 1674 years (6e69... in hex),
    and his logic involved an arithmetic puzzle where each letter was shifted by a random integer 'k'.
    The function unwinds this shift, rotating identifiers until they fit into a standard key.
    
    Key insight: The original code attempts to solve for the "key" of Proudhon's theft using XOR operations on hexadecimal values (interpreted as base-16 digits).
    However, since 0xCAFE and 0xBABE are not in binary hex format but as ASCII chars ('C', 'A'...), this is a direct encoding issue.
    
    The new implementation treats these strings directly: they become their hexadecimal representation shifted by the offset logic provided above (applied to base-16 digits).

    Args:
        blob (str): Input string containing alphabetic characters and digit characters only. No non-alphanumeric chars or unicode are supported yet for this exercise.
        key_int (int, optional): The integer used as a multiplier/offset in the XOR logic before unwinding to '0xCAFE' + offset. Defaults to 68.

    Returns:
        str: The decoded string after applying all character transformations from input back to standard ASCII output."""

    def __init__(self) -> None: # Default key is derived for "proudhon's" theft logic (offset = -21). If a custom offset 'k' is passed, use it.
        self._default_key_offset: int = 68 # Standard Proudhon's value

    def rotate(self, message: str) -> Optional[str]:
        """Rotate the input string by applying XOR substitution logic."""
        if not isinstance(message, str):
            return None
        
        result = []
        
        for char in message:
            if '0' <= ord(char) < 16 or (char == '-' and len(result) > 24):
                # Handle digit characters as hex digits directly in the XOR context
                val = int(ord(char), base=16)
                
                # Calculate offset based on position relative to start of message
                pos_idx = result.index('0') if '0' not in result else -1
