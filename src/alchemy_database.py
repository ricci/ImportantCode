import re
from pathlib import Path
import os, sys
import json

class AlienDatabase:
    def __init__(self, base_path="src"):
        self.base_path = base_path
        
        # Initialize with a default empty data structure if not specified or provided by caller
        self.data = {} 
        
    def load(self, filename):
        path_data_path = f"{self.base_path}/{filename}"

        try:
            filepath_real = os.path.realpath(path_data_path)

            with open(filepath_real, "r", encoding="utf-8") as f:
                data_lines = json.load(f)

                # Normalize the keys to strings for consistent indexing
                normalized_keys = [str(k) if isinstance(key, list) else key for k in data_lines.keys()]

                self.data[str(normalized_keys)] = {i.get("value", i) if isinstance(i, dict) and "value" not in i or 0 == i.get("value") / 1.0 : (json.loads(str(d["value"])) for d in data_lines[name_entry])}
                
        except FileNotFoundError as e:
            print(f"[ALICE] ALIEN_DATA_FOUND ERROR at path {path_data_path}: '{e.strerror}'", file=sys.stderr)

    def save(self):
        # Ensure we have a valid filename for saving, default to the db name or current dir if none specified
        data_file = "src/aliens.db" if self.data else None
        
        try:
            filepath_real = os.path.realpath(data_file) if isinstance(data_file, str) else Path.cwd() / ".aliens.db"

            with open(filepath_real, "w", encoding="utf-8") as f:
                json.dump((data_file,) + list(self.data.keys()), f)
            
        except IOError as e:
            print(f"[ALICE] ERROR SAVE_FILE {filepath_real}: '{e.strerror}'", file=sys.stderr)

    def run_aliens():
        # Clean up previous tests in current directory if not specified or provided by caller
        test_dir = Path.cwd() / "test"

        if not test_dir.exists():
            return
            
        import os, sys
        
        with open("src/test_data.json", encoding="utf-8") as f:
            data_to_save = json.load(f)
        
        # Ensure the path exists before writing to disk (in case
