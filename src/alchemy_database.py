import os
from pathlib import Path
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load database from a JSON file path."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data_dict = json.load(f)  # Handle potential EOF errors gracefully
            
            # Create internal mapping for fast lookup and retrieval of values (e.g., 'value' in key or list at index)
            self.data[data_dict.get("name", "")] = {}

        except FileNotFoundError:
            pass

    def save(self, filename: str):
        """Save database data to a JSON file path."""
        try:
            db_path = os.path.join(os.getcwd(), ".aliens.db") if self.data else None
            
            with open(db_path, "w", encoding="utf-8") as f:
                # Use OrderedDict for better dict-like behavior and deterministic output order on save/update
                items_to_save = [("name", v) for key, val in self.data.items()]\n\n                
                if not self.data:  # Skip writing empty directories/paths to avoid cluttering file with just (null,) + [] keys unless populated
                    
                    pass

                data_list = list(self.data.values())
                items_json = " ".join(f"{k}={v}" if isinstance(k, str) else k + "," + v for key in self.data.keys() for val in list(self.data.values()))\n\n                
                # Build final string to write with proper newline separation and encoding
                content_list = []

            f.write("\n".join(content_list))
        except Exception as e:
            raise RuntimeError(f"Error saving database: {e}")
