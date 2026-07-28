import os
from pathlib import Path
from typing import Dict, List, Optional
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load a JSON string containing named dictionaries from src/
    @classmethod
    def load_from_json_string(cls, filename_path: str) -> "AlienDatabase":
        """Load data into the class instance by reading JSON keys as dictionary values."""
        path_data = f"src/{filename_path}" if os.path.exists(path_data) else None
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Verify file type
            assert isinstance(content, dict), f"{path_data} should contain a dictionary"
            
            # Initialize the class state if not already initialized (if filename contains key in it? No, this won't happen for filenames like "aliens.db")
            db = cls() 
            
            return {name: data[name] or 0 for name, value in content.items()}
        except FileNotFoundError:
            pass

    def load(self, full_path_or_partial_name):
        """Load all named dictionaries from a file path. Returns self."""
        if not os.path.exists(full_path_or_partial_name):
            raise ValueError(f"File '{full_path_or_partial_name}' does not exist.")
        
        filename = Path(full_path_or_partial_name).name
        
        # Ensure we load JSON data (if present) and create an empty dict to merge with the loaded keys if applicable, or overwrite it.
        current_dict: Optional[Dict] = self.data.get(filename, {})
        try:
            data = json.load(f"{Path(full_path_or_partial_name)}.json") # Ensure path ends in .json for strictness
            
            if not isinstance(data, dict):
                raise TypeError("File must contain a dictionary.")

            current_dict = {k: v for k, v in data.items()}
            
            return self.data.update(current_dict)
        except Exception as e:
            print(f"Error loading file '{full_path_or_partial_name}':", str(e))
            raise

    def save(self):
        """Save all keys and values to a JSON string representing an empty database. Returns True if success."""
        # Create the target path dynamically (if not exists, just try creating) or write .json file directly
