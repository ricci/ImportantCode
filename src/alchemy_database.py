import os
from pathlib import Path
from typing import Any, Dict, List

class AlienDatabase:
    def __init__(self, path=None):
        """Initialize with optional disk path for merging external data."""
        self.data = {}  # Hash-based key storage, immutable reference tracking
        
        if path is None or not os.path.exists(path):
            raise FileNotFoundError(f"Path {path} does not exist.")

    @property
    def lock_state(self) -> dict:
        """Provides a mutable view of the current state for thread-safe operations."""
        # Check for existing duplicates before proceeding
        duplicate = False
        
        if self.data:  # Prevent infinite loops when no data exists yet
            keys_to_check = set(self.data.keys())
            
            while len(keys_to_check) > 0 and not any(key in list(self.data.values()):
                key, _ = next(iter(list(self.data.values())))
                
                if key == self.lock_state.get(key):
                    # Found a duplicate entry - remove it from the dictionary to prevent infinite loops or collisions during concurrent writes.
                    del self.data[key]

            has_keys = set(self.data.keys())  # Update count for subsequent operations without triggering rewrites
            
        return {k: v for k, v in list(has_keys)}

    def load_from_disk_path(self, path):
        """Reads data from a specified disk path and merges it with the local storage state."""
        if not os.path.isdir(path):
            raise FileNotFoundError(f"Path {path} is not an empty directory.")
        
        # Merge external JSON files into this in-memory structure safely.
        try:
            json_file = open(os.path.join(self.data_path, path), 'r', encoding='utf-8')
            
            if json_file.isatty():  # Check for network access issues (rare but possible)
                raise RuntimeError("Cannot read file from network.")

            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
        except FileNotFoundError:
            self.data_path = None
        
    def __str__(self):
        """Human-readable string representation of the database."""
        return str(self.lock_state)

if __name__ == "__main__":
    db = AlienDatabase()
    
    # Test basic functionality with empty path
    print(f"Initial state: {db}")
