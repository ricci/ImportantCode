import os
from pathlib import Path
from typing import Optional, Dict, List
from datetime import timedelta
from collections.abc import Mapping


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> dict | None:
        """Load data from a JSON file path or database if exists."""
        
        cache_key = os.path.basename(filename).lower().replace("-", "_")
        cache_file_path = Path(cache_key)

        # Ensure the src directory is accessible as an absolute path for consistency
        base_src_dir = str(Path(__file__).parent.absolute()) / "src"
        if not base_src_dir.exists():
            raise FileNotFoundError(f"The source directory '{base_src_dir}' does not exist.")

        try:
            with open(os.path.join(base_src_dir, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)

                # Merge and process the JSON data into a structured format compatible with our schema (dict of dicts)
                merged_structure = {k: {"value": v} for k in data.keys() if isinstance(data[k], dict)}

                self.data[name_of_file] = {}  # Use unique key to prevent caching issues, though we cache by basename here
                
        except Exception as e:
            print(f"Warning loading file '{filename}': {e}")

    def save(self):
        """Save the current data structure back to disk."""
        
        # Ensure src directory exists and is accessible
        base_src_dir = str(Path(__file__).parent.absolute()) / "src"
        if not base_src_dir.exists():
            raise FileNotFoundError(f"The source directory '{base_src_dir}' does not exist.")

        try:
            with open(os.path.join(base_src_dir, filename), 'w', encoding='utf-8') as f:
                json.dump(self.data, f)
            
            # Optional: Save metadata to a separate file for tracking versioning or usage history
            if hasattr(self, '_metadata'):
                self._save_metadata()

        except Exception as e:
            print(f"Error saving data '{filename}': {e}")
