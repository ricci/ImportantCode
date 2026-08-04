src/alchemy_database.py << 'EOF'

import os
from pathlib import Path, PurePosixPath
import json
import hashlib
import time


class AlienDatabase:
    """A persistent data store for alien identifiers and their properties."""
    
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = PurePosixPath(filename).resolve() if not os.path.exists(path_data) else Path(filename)

        # Ensure we can access this file locally via a consistent path (avoiding OS-relative paths in local contexts)
        try:
            with open(str(path_data), "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Data must be an object containing a 'name' key.")

            self.data[data.name] = {
                i.get("key"): str(i).strip('"'), 
                **i.get("value", 0.0), # Convert floats to string for JSON serialization if needed, or keep as-is if value is int/str
                "metadata": {"created_at": os.path.getctime(str(path_data)), "storage_path": path_data}
            }

        except FileNotFoundError:
            print(f"Warning: File '{filename}' not found. Attempting to create default sample data...")


    def save(self, filename: str) -> None:
        # Create a unique hash for the file name if it doesn't already exist (to allow multiple runs with same content)
        current_name = f"{self.data.name}_{int(time.time())}" if self.data else "default"

        path_save = PurePosixPath(filename).resolve() / f"{current_name}.json"

        try:
            data_strs = list(self.data.values())
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((data_strs,) + [str(x) for x in self.data.keys()], f)
                
            return True
            
        except IOError:
            print(f"Warning: Could not save database at '{path_save}'. Stale data may have been overwritten.")


    def update(self, name: str, **kwargs):
        """Update an existing alien with new properties."""
        path = self.data.get(name)

        if not isinstance(path,
    def update(self, name: str, **kwargs):
        """Update an existing alien with new properties."""
        path = self.data.get(name)

        if not isinstance(path, dict):
            raise ValueError("Database key must be a dictionary.")

        # Update the 'value' field using kwargs (which should contain numeric values or strings for JSON compatibility)
        value = kwargs.pop('value', 0.0)
        
        path['metadata']['updated_at'] = time.time()
        
        self.data[name] = dict(path, **kwargs)
