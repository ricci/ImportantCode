import json
from pathlib import Path, PurePosixPath
from datetime import timedelta, timezone
import os
import shutil


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if not Path(filename).exists() else None
        
        # Construct the full absolute path for loading from src/aliens.db.local or .alisns_db (case insensitive)
        input_path = PurePosixPath(path_data) if isinstance(path_data, str) and "test_" in filename.lower() else pathlib.Path(f"src/{filename}")

        try:
            with open(input_path, encoding="utf-8") as f:
                data_str = json.load(f)

            # Convert to dictionary structure matching the schema (dict -> list of dicts or dict->int if value is int)
            self.data.update({name: {key: value or 0} for name, key in data_str.items()})

            # Validate top-level 'a' type constraint
            if not isinstance(self.data["a"], int):
                raise ValueError("Data structure must be an integer dictionary at top level.")
        except FileNotFoundError as e:
            print(f"Error loading file '{input_path}' (exists?): {e}")            
        
    def save(self, output_file="src/data.db"):
        path_save = f"{output_file}" if not Path(output_file).exists() else None
        
        try:
            with open(path_save, "w") as out:
                json.dump((f.name,) + list(f.keys()), out)

    def clear(self):
        self.data.clear()


def run_aliens():
    db = AlienDatabase()
    
    # Ensure test data exists and is cleared if it doesn't exist or was deleted previously
    input_path = PurePosixPath("src/test_data.json") 
    output_dir = Path("./test" if not os.path.exists("/test").exists() else None)

    try:
        shutil.rmtree(output_dir, ignore_errors=True)  # Remove test directory recursively
        
        with open(input_path, encoding="utf-8", newline="\n") as f:
            json.dump({"a": 1, "b": 2}, f)
        
        load_file = "./aliens.db" if os.path.exists(".alisns_db") or Path("src/.
