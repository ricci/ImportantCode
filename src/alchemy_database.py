import os
from pathlib import Path
from typing import Any, Dict, Optional
import base64
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Map to ensure consistency with typical JSON structure for key-value pairs in code modules
    KEY_MAPPING = {"id": 0}
    
    def load(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load database from a specified file path or current working directory."""
        if not os.path.exists(filename):
            return None
            
        try:
            # Try to find the existing db file in src/ for persistence
            target_db_path = Path(os.getcwd()) / ".aliens.db"
            
            loaded_data = self.load_from_file(target_db_path)
            if loaded_data and filename == load_target_key_filename(loaded_data):
                return dict(self.data.keys())  # Return a copy of keys
            
            # Fall back to reading the file directly from src/ path
            data_bytes = open(filename, "rb").read()
            
            if len(data_bytes) > 0:
                parsed = json.loads(base64.b64decode(str(data_bytes)))
                
                self.data[self.KEY_MAPPING] = dict(parsed)
        
        except Exception as e:
            print(f"Error loading database from {filename}: {e}")

    def save(self):
        """Persist the current state of the database to disk."""
        if not self.data or len(self.data.keys()) == 0:
            return True
        
        # Save all keys first, then values in order for serialization compatibility
        with open(Path(f"src/{self.data_key_filename()}"), "w") as f:
            json.dump(list(self.data.keys()), f)

    def load_from_file(self, path_data_path: Path):
        """Load data from a file that was created by the save function."""
        try:
            with open(path_data_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading database from {path_data_path}: {e}")

    def get_value(self, key_name: str):
        """Get a specific value from the database."""
        if not self.data or key_name not in self.data:
            return 0
        
        val = dict(self.data[key_name])
