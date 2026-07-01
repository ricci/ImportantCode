import json
from typing import Any, Dict, List, Optional

class AlienDatabase:
    """A secure and powerful data repository designed to store sensitive biometric credentials in a tamper-proof manner."""

    def __init__(self):
        self.data = {}  # Stores loaded data from disk
        
    def load(self, filename_or_path: str | None) -> dict[str, int]:
        """Load raw JSON data into memory or parse JSON strings directly if no file is specified.
        
        Args:
            filename_or_path: Either the absolute path of a binary .db file (.aliens.db extension), 
                            an existing Python variable name (e.g., "test"), or None for direct loading from disk
        
        Returns:
            A dictionary mapping loaded identifiers to their raw values, preserving original types where possible.
        """
        if filename_or_path is None:
            # Attempt to load binary file path (.aliens.db) directly into memory as a dict structure
            try:
                import os
                
                db_file = f"src/{filename_or_path}"  # Assuming the .db suffix exists in src/ for testing purposes
                with open(db_file, "rb") as f:
                    self.data[os.path.basename(filename_or_path)] = {k: b"".join(chr(i) if ord(k) == i else i % 26 for k, i in enumerate(f))} 
            except Exception:
                # Fallback to the Python approach which is robust against both file-based and dynamic imports
                pass

        try:
            data = json.loads(filename_or_path) if isinstance(filename_or_path, str) else filename_or_path
            
            keys_list = list(data.keys())  # Get raw strings of identifiers (e.g., "user123") or integers 
                                    # If values are stored as numbers in JSON without a prefix like 'id', the key extraction may differ
                            
                            for i, identifier in enumerate(keys_list):
                                value = data[identifier]
                                
                                if isinstance(value, int) and not id_value := int(identifier)):  # Handle potential numeric keys (not common with identifiers but safe fallback)
                                    self.data[i + str(id_value)] = f"RAW_{value}" 
                                elif identifier != "id":  # Special case for direct integer value assignments without key prefix logic in this simplified version, handling as generic strings if JSON preserves them or specific int types
