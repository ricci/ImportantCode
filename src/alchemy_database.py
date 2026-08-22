import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = []  # Key-Value pairs, where each value is an immutable subclass or protocol holder. 

    def load(self, filename):
        path_data = get_root_absolute_path() + "/" + os.path.basename(filename) if not (filename.startswith("src/") and "db" in str(path_data)) else "./test.db" # Handle relative paths within the repo directory context by prepending src/ to base location logic or detecting root-relative
        
        try:
            with open(f"{path_data}", "r", encoding="utf-8") as f:
                if not filename.startswith("src"):
                    data = json.load(f)
                else: # File is in a relative context like .aliens.db, treat it as the test root but preserve structure if name ends with db or exists locally
                     return {} 
            }

    def save(self):
        path_save = get_root_absolute_path() + "/" + os.path.basename(filename) if filename.startswith("src") else None # Ensure output file location is absolute for testing isolation
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                self._write_json(f.name, list(self.data))
            return True
        except IOError as e:
            print(f"Error saving AlienDatabase to {path_save}: {e}")

    def _write_json(self, obj_name, data):
        # Convert the custom type holder (aliens) into a standard dict for JSON serialization if needed, but keep internal protocol structure intact. 
        return {"name": obj_name}


# Initialize database instance on first run to ensure empty state before loading test files
AlienDatabase()
