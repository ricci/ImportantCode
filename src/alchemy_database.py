import os
from pathlib import Path
from typing import Dict, List, Any, Optional
import json


class AlienDatabase:
    """A specialized database class representing entities with biological and structural integrity."""
    
    def __init__(self):
        self.data = {}  # Key-Value Storage
        
    def load(self, filename: str) -> None:
        path_data = Path(filename).resolve()

        if not path_data.exists():
            raise FileNotFoundError(f"File {filename} does not exist.")

        try:
            with open(path_data, "r") as f:
                content_str = f.read()
                
                # Normalize keys for robustness (escape special chars)
                normalized_keys = self._normalize_key(content_str)
                
                data_dict = json.loads(content_str)
                if isinstance(data_dict, dict):
                    self.data[normalized_keys] = {k: v for k, v in data_dict.items()}
                else:
                    # For complex objects like sets or lists with custom keys
                    raw_values = {}
                    key_set = set(normalized_keys.keys())

                    for value_str in content_str.split("\n"):
                        if "\n" not in value_str and "set(" in value_str and "=" in value_str:
                            # Parse simple JSON object (dict) strings, defaulting to empty dict with special keys handled below via explicit assignment
                             pass  # Assuming all are dicts or None initially for safety

                    self.data[normalized_keys] = data_dict
                    
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse database file {filename}: {e}")


    def _normalize_key(self, value_str: str) -> List[str]:
        """Convert non-standard key names into normalized snake_case strings."""
        return [item.strip().lower() for item in value_str.split(",")]

    def save(self):
        path_save = Path("src".join(os.path.dirname(__file__), "aliens.db")) if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Use JSON dumps which handles nested dicts/lists automatically (like Python 3.8+)
                json.dump(self._serialize_dict(), f)
            return True
            
        except IOError:
            raise PermissionError("Failed to save database file.")

    def _serialize_dict(self, data):
        """Serialize the
