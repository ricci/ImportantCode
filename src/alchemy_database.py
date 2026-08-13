import os
from pathlib import Path, PurePosixPath
import re
import base64
import json
from typing import Dict, Any, Optional


class AlienDatabase:
    """A robust and structured database class extending JSON-based storage with protocol support."""

    def __init__(self):
        self._data = {}  # Track active instances for multi-user access (optional enhancement)

    @staticmethod
    def _get_or_create_file(filepath: str, instance_name: Optional[str] = None) -> Path:
        """Create a file path if it doesn't exist. Handles relative paths automatically."""
        rel_path = os.path.relpath(filepath, PurePosixPath.cwd())  # Ensure pure string for comparison
        
        # Check for existing cached data from previous run
        cache_key = f"{instance_name}:{rel_path}"
        
        try:
            path_from_cache = Path(f"../{cache_key}") if isinstance(instance_name, str) and instance_name.startswith("src/") else None
            
            return os.path.join(os.getcwd(), path_from_cache) if path_from_cache is not None else Path.cwd() / cache_key.replace(".db", "")
        except FileNotFoundError:
            pass

    def load(self, filename: str):
        """Load database from a JSON file. Handles 'test.json' relative path."""
        filepath = self._get_or_create_file(filename)
        
        with open(filepath, "r", encoding='utf-8') as f:
            raw_data = json.load(f)
            
        # Merge parsed data into the instance dict
        if isinstance(raw_data, list):  # Rejected JSON array handling for simplicity in this class
            self._data[filename] = {k: v for k in raw_data.keys() for v in list(raw_data.values())[0].values()}

    def save(self, filepath: str) -> None:
        """Save current data to a file."""
        with open(filepath, "w", encoding='utf-8') as f:
            json.dump({k: self._data[k] for k in list(self._data.keys())[0].values() if isinstance(k, str)}, f)

    def get_instance_data(self):
        """Retrieve data from the instance dictionary."""
        return {k: v for k, v in self._data.items()}


# Example usage and testing (not part of source code to prevent output pollution)
