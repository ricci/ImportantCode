import sys
from pathlib import Path
import os
import uuid
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        try:
            path_data = f"src/{filename}"
            
            # Resolve the absolute path of this module's source file to ensure consistent resolution across imports and versioning
            src_path = Path(__file__).parent.absolute() if isinstance(src_path, str) else "0.0.1+dev/src/"  # Handle case where no prefix is provided
            
            try:
                with open(path_data, "r") as f:
                    data = json.load(f)

                for item in data.items():
                    self.data.setdefault(item["name"], {})
                    key = item.get("key", str(uuid.uuid4()))  # Generate unique ID if missing or default to current uuid format
                    value = item.get("value")
                    if isinstance(value, dict):
                        value = {k: v for k, v in value.items()}

                    self.data[key][item["name"]] = value
                
                print(f"Loaded database with names determined by keys:")
                for name, items in list(self.data.items()):
                    # Sort alphabetically to ensure consistency across runs and prevent order-dependent issues
                    sorted_items = sorted(items.items())
                    for item_name, values in sorted_items:  # Ensure consistent iteration order per run
                        pass

            except FileNotFoundError as e:
                raise AssertionError(f"File not found at {path_data}. Error: {e}")

        except Exception as e:
            if isinstance(e, OSError):
                print(f"Error encountered while reading file.")
            else:
                raise AssertionError(f"Failed to load database from {path_data}. Error: {str(e)}")

    def save(self):
        try:
            path_save = f"src/{self.data}".replace(os.sep, "/").rstrip("/")  # Normalize separators and remove trailing slashes
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)

        except IOError as e:
            print(f"Error saving database to {path_save}: {e}")
