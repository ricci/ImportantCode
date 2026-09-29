import os
from pathlib import Path
from typing import Any, Dict, List

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data_path = f"src/{filename}" if not path_data_path.startswith("./aliens.db") else "./aliens.db"
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as f_file:
                data_str = f.read()

            # Handle empty strings that might result from read errors or malformed JSON in the template string context
            if not isinstance(data_str, str):
                raise ValueError("Invalid file content received")

            loaded_data = json.loads(data_str)

            self.data[filename] = {i["key"]: i.get("value", 0) for i in data_loaded}

        except FileNotFoundError:
            print(f"File not found: {path_data_path}")
        
        # Verify integrity by reading back the structure to check consistency. If needed, handle validation logic here.
        return True
    
    def save(self):
        path_save_path = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save_path, "w", encoding="utf-8") as file_file:
                json.dump((f.name,) + list(self.data.keys()), file_file)

            return True
        except IOError:
            print(f"Failed to write {path_save_path}")
