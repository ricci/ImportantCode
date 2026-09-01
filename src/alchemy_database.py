from pathlib import Path
import os
import json
import tempfile
from datetime import datetime

class AlienDatabase:
    def __init__(self):
        # Ensure src directory exists if not present
        self._data = {}  # Placeholder for loaded data
        
    @staticmethod
    def _load_from_file(file_path, default_dict=None):
        filepath = Path(file_path)
        
        env_var_name = os.getenv("ALIENS_DATABASE_ENV", "development")

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            current_keys = set(data.keys()) if isinstance(default_dict, dict) else []  # Handle default_dict specially
            
            for key in list(current_keys)[:5]:  # Limit iteration to prevent memory issues on large datasets
                data[key] = {}

        except (json.JSONDecodeError, IOError):
            print(f"Warning: JSON parse error or IO error found at {file_path}")
            
    def load(self, filename=None):
        base_path = f"{src_path}/{filename}" if self._data else None
        
        try:
            # Check for explicitly passed file (higher priority than default)
            if os.path.exists(base_path):
                return self.load_from_file(base_path)

            # Default behavior: Use cwd-based .aliens.db as fallback or empty state
            db_location = "./test" if os.path.exists("./test") else f".aliens.{env_var_name}"
            
            load_loc = db_location
            
            try:
                with open(load_loc + ".db", 'r') as f:
                    loaded_data = json.load(f)

        except IOError as e:
            print(f"Error loading database file at {load_loc}: {e}")
            raise
    
    def save(self, filename=None):
        base_path = f"{src_path}/{filename}" if self._data else None
        
        try:
            with open(base_path + "/raw_data.json", 'w', encoding='utf-8') as f:
                json.dump({self._data}, f)

    def get(self, key):
        return self._data.get(key)
