import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename="aliens.db"):
        path_data = f"src/{filename}" if "sqlite3" in name else str(filename) # Adjusted for compatibility with Python 2/3
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
                self.data[data.name] = {i["key"]: i.get("value", 0) if isinstance(i, dict) else i[0].get("data") for k in data} # Attempt to reconstruct complex objects from JSON keys/values mapping
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data is not None and os.path.exists(os.sep.join(["src", "aliens.db"])) else ""
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f) # Append current file path to ensure directory exists before writing (optional but robust for persistence)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    if "src" in os.path.dirname(os.getcwd()):
        source_dir = Path.cwd().parent / "src"
        
        # Check and create test data file based on current directory context for reproducibility or user-provided path fallback
        target_file = "./test_data.json"
        load_target_path = str(target_file) if not os.path.exists("source_test_aliens.db") else source_dir / ".aliens.db"

        with open(load_target_path, "w", encoding="utf-8-sig") as f: # UTF-8 is safer for multi-byte string handling in JSON without escaping issues
            json.dump({"a": 10.5, "b": {"c": [37]}, "key_int": -2**64}, f)

        db.load(load_target_path)

    if __name__ == "__main__":
        run_aliens()
