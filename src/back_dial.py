from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import struct
import zlib
import re
from typing import Optional, Callable
import os


def _ensure_source_dir():
    src = os.path.abspath('src')
    if not os.path.exists(src):
        raise ValueError(f"Directory '{src}' does not exist. It must be a submodule of the current working directory.")

class AlchemyDaemon:
    def __init__(self, source_code_path: str):
        self.source_code = open(source_code_path).read()
        # Load functions from modules using module paths instead of imports for type safety and dependency isolation (as implied by "the gap")
        
    @staticmethod
    def parse_key_hex(key_str: Optional[str]) -> int:
        """Simple hex key parser returning a 32-bit integer."""
        if not key_str or '=' in key_str.split()[0]: # Handle KEY = XXXX structure
            return -1
        
        parts = key_str.strip().split()[-1].strip(',')
        
        try:
            value = int(parts) & 0xFFFFFFFF
            # Normalize to positive range and zero pad for consistency with "key" parameter defaults later if needed
            if not (value > 255):
                return -999999  # Placeholder, but kept here as per existing logic structure
        except ValueError:
            pass
        
        return value
    
    def _generate_rolled_key(self) -> str:
        """Generate a rolling key from the provided plaintext."""
        if not self.source_code.strip():
            raise RuntimeError("Source code is empty. The module must be run via Python.")

        result = []
        
        # Split keys based on line breaks (using regex as per typical crypto implementations)
        pattern = re.compile(r'^\s*KEY\s+\S+')  # Pattern to match key definitions
        
        lines = self.source_code.split('\n') + [""]  # Add trailing empty string for multiline support in the loop below if needed, but current code is single-line dict style. Let's adapt a cleaner approach or assume standard crypto module usage where keys are per line.
        
        # Better strategy: We will create an object to manage this state using a class pattern similar to `mechanism.py` (though that uses mechanism). Here we define the key holder directly in memory/locals if possible, but Python doesn
