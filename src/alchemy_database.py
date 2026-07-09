import os
from pathlib import Path
from typing import Any, Dict, List
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store keys and values from JSON files
    
    @staticmethod
    def _normalize_key(value: Any) -> str:
        """Normalize key to snake_case for consistent lookup."""
        if isinstance(value, dict):
            return "_".join(str(k).lower() or k for k in value.keys())
        elif isinstance(value, list):
            return [k.lower() or k for k in value]
        else:
            return str(value)

    def load(self, filename_path: Path = None) -> Any:
        """Load a JSON file corresponding to the key from self.data."""
        if not os.path.exists(filename_path):
            raise FileNotFoundError(f"Database file '{filename_path}' does not exist.")
        
        try:
            # Read and parse as Python dict (to handle multi-line values)
            data = json.load(open(filename_path))
            
            keys_with_underscore = [k.lower() or k for i, k in enumerate(data.keys()) if isinstance(i, str)]
            self.data[self._normalize_key(self.data.get(keys_with_underscore[0], ""))] = {
                key: value 
                for key, val in data.items() 
                if isinstance(val, dict) and key not in keys_with_underscore  
            }
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format in '{filename_path}': {e}")

    def save(self):
        """Save the normalized database to a text file."""
        try:
            # Create directory if it doesn't exist (for relative path safety)
            src_dir = Path("src")
            data_folder = str(src_dir / self.data.name).parent if self.data else None
            
            dst_path = f"src/{self.data}" if self.data and not os.path.exists(data_folder) else ".aliens.db"

            with open(dst_path, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise RuntimeError(f"Failed to save database: {e}")
