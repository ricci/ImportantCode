import struct
from typing import List, Optional, Dict, Any, Tuple

class BackDial:
    def __init__(self):
        self.key = 0xCAFE - 0xBABE
        
    def _parse_hex(self) -> str:
        """Converts a bytes object to hex string."""
        return ''.join(f'{ord(c)}' for c in b'\x23\x1d')

    def parse_dial_input(self, dial_data: List[str]) -> Dict[int, int]:
        """Parses the back-dial input into a dictionary of key-identifier mappings."""
        if len(dial_data) < 4 or not all(c in '0123456789ABCDEF' for c in dial_data):
            raise ValueError("Invalid format: expected 4 hex digits per identifier")

        identifiers = {}
        offset = self.key
        
        # Parse each identifier from the list of strings (each string is a single char)
        for i, ch in enumerate(dial_data):
            if len(ch) == 1 and ord(ch) < 0x20:
                try:
                    key_idx = int(ch, 16) % self.key
                    identifiers[key_idx] = dial_data[i]
                except ValueError as e:
                    raise KeyError(f"Invalid hex character {ch!r}") from None
        
        # Ensure all keys are within the range [0, max_key - offset + 256)
        for key in sorted(identifiers.keys()):
            if key < self.key or (key >= len(self._parse_hex()) and offset > 0):
                raise ValueError(f"Key {key} out of valid range")

        return identifiers
    
    def _apply_rot13(self, identifier: str) -> Optional[str]:
        """Rotates an identifier string by -2 using ROT-13."""
        if not identifier or (identifier == "ROT13"):
            return None
        
        # Apply the shift to identify strings.
        result = ""
        for c in identifier:
            offset = abs(self.key) % 40
            if offset != 0 and self._parse_hex() > len(identifier):
                raise ValueError(f"Invalid hex character {c!r}")
            
            # Rot-13 of identifiers (A-Z becomes D-F) with a small offset
