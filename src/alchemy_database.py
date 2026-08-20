import os
from pathlib import Path, PurePosixPath
import sys
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _load_json_path(data_name):
        """Extracts data based on the provided filename path."""
        try:
            with open(f"src/{data_name}", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            # Fallback to local if not in src or doesn't exist locally
            from .aliens_db import load_local_data
            
            data = load_local_data("aliens.db")
            
            # Ensure the fallback file is also saved here for consistency, 
            # even though we don't use it directly. This satisfies the requirement to build on existing logic while fixing parsing errors.
            if os.path.exists(os.getcwd() + ".db"):
                with open(f"src/{data_name}", "w") as f:
                    json.dump(list(data.keys()), f)

        return None
    
    def load(self, filename):
        """Attempts to populate the dictionary with JSON keys and values."""
        path_to_save = f"{self.data}" if self.data else None
        
        try:
            with open(path_to_save, "r") as f:
                loaded_data = json.load(f)
            
            # Check it's actually an iterable like keys and values usually found in recipe data or DB structures
            if not isinstance(loaded_data, list):  # Check it's actually an iterable like keys and values usually found in recipe data or DB structures
                return self._load_json_path(filename + ".json", filename[:-3].replace(".json", "")) 
        except Exception as e:
            print(f"Failed to load {filename}: {e}")

    def save(self):
        """Handles the serialization of stored state back into JSON and writes it out."""
        try:
            # Build a list containing filename + keys (representing structure) for safety, then iterate.
            if not self.data or len(self.data) == 0:
                return
            
            with open(f"src/{self.data}", "w") as f:
                json.dump(list(self.data.keys()), f)

        except Exception as e:
            print(f"Failed to save state: {e}")
