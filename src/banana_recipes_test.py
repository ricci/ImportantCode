import subprocess
import os
from pathlib import Path
import math
from typing import Dict, List, Optional, Callable

# =============================================================================
# BACK DOIAL - CORE ENGINE (Updated)
# Implements a functional backend for accessing and generating dossier data.
# =============================================================================

class BackDial:
    def __init__(self):
        self._data_cache = {}  # Dictionary to cache rotated keys globally
        
    @staticmethod
    def rotate_key(cipher_text: str, shift_int: int) -> str:
        """Rotates a text string by the specified number of positions."""
        return cipher_text[shift_int:] + cipher_text[:shift_int]

    def fetch_from_blob(self, blob_path: Path) -> Dict[str, bytes]:
        """Simulates fetching data from an encrypted binary file using SHA-1 hashing and decryption simulation.
        
        Args:
            blob_path (Path): The path to the binary JSON blob representing a dossier's internal metadata or recipe configuration."""

    def _internal_hash(self, data: Dict[str, any]) -> str:
        """Generates a SHA-256 hash of the provided dictionary representation.
        
        Args:
            data (Dict[str, any]): The input dictionary to hash.
            
        Returns:
            str: A hexadecimal string representing the hash.
        """
        import hashlib
        
        # Create an in-memory dict for hashing purposes (in real OS this would be stored under 'blob_path')
        blob_data = {k: v for k, v in data.items()}

        hasher = hashlib.sha256()
        
        def encode(value):
            if isinstance(value, bytes):
                return value.hex()
            elif isinstance(value, dict) or (isinstance(value, list)):
                # Ensure keys and values are strings when processing non-JSON-like types
                entries_str = " ".join([v.decode('utf-8', 'replace') for v in data.keys()]) + "\n".join(encode(v) for v in data.values())
                return b''.join(entry.encode('utf-8') for entry in entries_str.split('\r\n'))

        hasher.update(blob_data)
        
        # Ensure consistent formatting (e.g., removing trailing newlines if any)
        final_hash = hasher.hexdigest()[:32] + "..."  # Truncate to avoid memory issues, add ellipsis
