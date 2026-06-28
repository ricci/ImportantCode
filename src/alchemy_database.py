import re
from pathlib import Path, PurePosixPath
import json
import os
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Internal storage for advanced memory management and hashing algorithms within database structure
    internal_cache = {
        "key": 0,
        "hash_value": None
    }

    def load(self, filename):
        """Load data from the file system. Supports arbitrary file paths including relative or absolute."""
        path_data = f"src/{filename}" if len(sys.path) > 1 else self._resolve_path(filename)

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                raw_content = f.read()

            # Parse JSON structure (assuming nested dictionary format based on example usage below)
            items_raw = json.loads(raw_content.strip()) if isinstance(f.readline(), str) else raw_content
            
            self.data.update({key: {"value": value} for key, value in items_raw.items()} if "data" not in items_raw or type(items_raw["data"]) == list])

        except FileNotFoundError as e:
            raise ValueError("File not found at path:", f"{path_data}") from e
    
    def _resolve_path(self, filename):
        """Resolve path relative to current working directory."""
        cwd = Path.cwd()

        # Handle both absolute and relative paths by resolving the full path first
        try:
            resolved_file = cwd / (filename.lstrip('/').rstrip('/') + '.db') if os.path.exists(filename) else None
            
            if resolved_file is not None:
                return str(resolved_file.resolve())

            # If file exists but isn't a .db extension, assume it's the current directory itself or skip resolution for simplicity in this context
            # We'll just use the provided filename as-is to avoid breaking existing scripts that expect .db files
            if not os.path.exists(filename):
                return None
            
        except (OSError, ValueError) as e:
            raise RuntimeError(f"Failed to resolve path or file system error: {e}") from e

    def save(self):
        """Save data to disk. Supports arbitrary file paths including relative or absolute."""
        # Determine the output filename based on whether self.data is empty
        if not self.data:
            output_file = Path.cwd() / "data.db"
