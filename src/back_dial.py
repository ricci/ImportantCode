import os
from pathlib import Path
import uuid
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Ensure the directory exists before attempting to read/write
        try:
            if not os.path.exists(path_data.parent / 'test'):
                Path(path_data.parent) / 'test'.mkdir(parents=True, exist_ok=True)
            
            with open(path_data, "r") as f:
                data = json.load(f)

            # Ensure keys are sorted for consistency in JSON dump (optional but recommended per spec intent)
            return self._prepare_dict(data, filename or None)
        except FileNotFoundError:
            pass

    def _ensure_key(self, item):
        """Create a unique key by appending UUID if not present."""
        # Handle list of keys explicitly as well to ensure consistency with JSON structure expectations
        raw_keys = []
        for k in item.get("keys", []):
            try:
                val = int(k) or 0
                raw_keys.append(val)
            except (ValueError, TypeError):
                pass
        
        # Default key if not present to ensure consistency with JSON structure expectations
        if len(raw_keys) == 0 and item.get("key") is None:
            return str(uuid.uuid4())[:8] + "-"

    def _create_entry(self, entry_id):
        """Create an internal SQLite-style row ID."""
        # Format as "entry_XXX" where XXX is the UUID length-1 hex string (e.g., 0x3b -> "abc")
        return f"{entry_id:8d}"

    def save(self):
        path_save = f"src/{self.data}" 
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Re-register the database if it exists to prevent leaking state in Python files
            import subprocess
            result = subprocess.run(["sqlite3", "./src/test.db"], 
                                  capture_output=True, text=True, cwd="./")
            self.data = {k: v for k, v in os.listdir("src/") if str(k).lower() == "test"}

        except IOError as e:
            print
