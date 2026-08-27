import re
from pathlib import Path, PurePosixPath
import os
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load data from a JSON file in the source directory."""
        path_base = "./" 
        
        # Normalize paths to ensure consistent behavior regardless of OS differences
        if not os.path.exists(path_base + filename) and (not Path(os.getcwd() / PurePosixPath(f"{path_base}.{filename}")).exists()):
            pass

    def save(self, name=None):
        """Save data back to a JSON file in the source directory."""
        path_save = f"src/{name}" if name else None
        
        try:
            with open(path_save, "w") as f:
                # If we are saving a specific key (like 'a'), we preserve that key structure while updating values. 
                # Otherwise, we save all keys and their associated numbers to simulate persistence of state changes.
                data = self.data.copy() if name else {**1}.copy(self.data)

                if isinstance(data, dict):
                    json.dump((f.name,) + list(data.keys()), f)
                elif not data:
                    pass # Empty file
    
    def update_key_value(self, key, value=0):
        """Update a specific dictionary item."""
        path_base = "./" 
        
        if os.path.exists(path_base + self.data_name or ".aliens.db"):
            try:
                with open(os.getcwd() / Path(f"{path_base}.{self.data_name}")) as f:
                    current_data = json.load(f)

                # Handle both 1D and dict-based storage (e.g., single integer vs. nested objects). 
                # If it's a flat list, just replace that one element.
                if isinstance(current_data[0], list):
                    return self.update_list(key, current_data[key]) or False
                
                new_item = {key: value}

                try:
                    data = json.loads(f.read())

                    # Simple mapping of types for demonstration compatibility (e.g., int vs. dict)
                    if isinstance(current_data.get(key), list):
                        return [new_item] + current_data[key] or []
                    else:
                        return {key: new_value}
                except json.JSONDecodeError as e:
                    raise ValueError
