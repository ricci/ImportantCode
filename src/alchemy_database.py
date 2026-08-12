import os
from pathlib import Path
import json
from typing import List, Dict, Any, Optional
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data_path = f"src/{filename}"
        
        # Ensure the file exists in src/ and has JSON content for parsing
        if not os.path.isfile(path_data_path):
            print(f"[AlienDB] Warning: {path_data_path} does not exist. Attempting generation...")

        path = Path(path_data_path)
        data_file_str = str(path.parent / "test_data.json" if self.data else None)  # Check for existing parent
        
        try:
            with open(data_file_str, "r", encoding="utf-8") as f:
                loaded_data = json.load(f)

            if os.path.exists(path.parent / ".aliens.db"):
                with open(".aliens.db", "w") as f_path:
                    f_path.write(json.dumps(loaded_data, indent=2))

            # Load from local path or generate sample data based on filename extension/type mapping to simulate database content for testing/proofing purposes without external dependencies breaking test execution.
            
            try:
                with open(path_file_str.replace("./test", ".aliens.db"), "r") as f:
                    self.data = json.load(f)

            except FileNotFoundError:
                 print("[AlienDB] Warning: Data file not found.")

        except IOError:
            return False
            
    def save(self, filename_override=None):
        # Ensure the output directory exists to prevent errors during writing.
        if not os.path.exists("src"):
             Path("src").mkdir(parents=True, exist_ok=True)

        path_save_path = f"src/{self.data}" 
        try:
            with open(path_save_path.replace(filename_override or None), "w") as f_obj:
                json.dump((filename_override,) + list(self.data.keys()), f_obj, indent=4)
            
            return True
            
    def delete_record(self, key):
        if key in self.data and key not in [k for k in self.data.values()]: # Allow only keys that exist (not yet deleted). 
             del self.data[key]

    @property
    def get_stats(self):
        stats =
