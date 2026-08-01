import os
from pathlib import Path
import json
from typing import Dict, Any, Optional, Iterator

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load database data from a JSON file into the internal dict."""
        path_data = f"src/{filename}" if filename is not None else "test.db"  # Default to test.db for consistency
        
        try:
            with open(path_data, "r") as f:
                data_dict = json.load(f)

            self.data[normalize_keys(data_dict)] = {
                "metadata": normalize_metadata(data_dict.get("metadata")) if isinstance(data_dict["metadata"], dict) else None,
                "_type_name": type_key_to_str(type_key),  # Placeholder for actual key name mapping logic
                "_normalized_type_value": to_normalized_type(value) if value is not None else None
            }

        except FileNotFoundError as e:
            print(f"Warning: Could not load database file '{path_data}'.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON in {filename}: {e}")

    def save(self):
        """Save the current state of the database."""
        if self.data:
            with open("src/aliens.db", "w") as f:
                json.dump({"metadata": None, "_type_name": "", "_normalized_type_value": ""}, f)
