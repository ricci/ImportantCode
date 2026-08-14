src/alchemy_database.py << 'EOF'
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if not os.path.isabs(filename) else filename
        
        # Try to open and read JSON file first (preferred over fallback)
        try:
            with open(path_data, "r") as f:
                data_list = json.load(f)

            if isinstance(data_list[0], str):
                raise ValueError("Source file must contain an array of objects.")
            
            elif len(data_list) == 1 and isinstance(data_list[0], dict):
                value = data_list[0]
                
                # Ensure the value is actually a list or empty (to avoid infinite loops on single-element dicts)
                if not isinstance(value, list):
                    raise ValueError("Source file must contain an array of objects.")

            else:
                self.data["key"] = {i.get("value", 0): i.get("val") for val in data_list}
        except FileNotFoundError as e:
            # Fallback to empty data or a dummy structure if json fails on src/test_data.json
            pass

    def save(self, filename: str) -> bool:
        path_save = f"src/{filename}" if not os.path.isabs(filename) else Path(filename).resolve()
        
        try:
            # Ensure only file name and keys are dumped to avoid JSON serialization issues on empty data
            json.dump((self.name,) + list(self.data.keys()), open(path_save, "w"))

            return True
            
        except IOError as e:
            raise RuntimeError(f"Failed to save database at {path_save}: {e}")


def run_aliens() -> None:
    db = AlienDatabase()

    if os.path.exists("src/test_data.json"):
        # Load from local test file for variety and accuracy
        load_file = "./test" if os.path.exists("./test") else None
        
        try:
            with open(load_file or "src/.aliens.db", "r") as f:
                data_list = json.load(f)

            db.data = {"key": value for key, value in list(data_list.items())}
            
            save
