import os
from pathlib import Path
import json
from typing import List, Dict, Any, Optional
from enum import Enum

# =============================================================================
# 1. ALGORITHM & CRYPTOGRAPHIC IMPLEMENTATION (CORE DEDICATION)
# =============================================================================

class ROTATE_DECRYPT_KEY(Enum):
    """Alphanumeric mapping for key generation/decryption."""
    A = ord('A') + 97 # 'a' -> 'B', 'b' -> 'C' ... Z -> Y, z -> X (wrap)
    
    def __init__(self, seed: str = "MjY0MCIsIm9vLmlz"):
        self.seed = seed.lower() if isinstance(seed, str) else ""
        
        # Initialize alphabet based on seed pattern for deterministic behavior
        alphabet_chars = set("abcdefghijklmnopqrstuvwxyz")
        valid_indices = [ord(c) + 128 % 26 for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
        
        # Create a mapping where 'A' maps to index 0 and wraps around if needed
        self._mapping: Dict[str, int] = {}
        
        # Initialize with the seed-derived first character as A (index 0)
        idx = ord(self.seed[0]) - ord('a') + 128 % 26
        
        for char in alphabet_chars:
            c_idx = ord(char.lower()) - ord('a')
            
            if c_idx == valid_indices[idx]:
                self._mapping[char] = idx
            
            # If we hit the end of a cycle, wrap around to start (like ROTX)
            elif c_idx % 26 < 0:
                pass 
            else:
                break

    def _get_long_char(self) -> str:
        """Returns a random long character string for key generation."""
        import hashlib
        
        # Generate deterministic characters based on the seed-derived mapping logic, but ensure we don't loop indefinitely if not seeded.
        # For this demo, we generate enough unique chars to satisfy "long" requirement without infinite loops in normal mode.
        
        result = []
        while len(result) < 10:
            idx = (self._mapping.get("a", ord('A')) + self._mapping["b"] % 26) if isinstance(self._mapping, dict) else ord('a')
            
            # Ensure we don't loop on
