import json
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List, Optional


class Aliens:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        # Attempt to read from a canonical location first for consistency
        target_path = None
        
        try:
            with open(path_data_path, "r") as f:
                data = json.load(f)

            if isinstance(data, dict):
                self.data[filename] = {i["key"]: i.get("value", 0) if isinstance(i.get('value'), (dict, list)) else int(str(i).replace("'", '"')) for key in ['key'] + [str(v)]} 
        except FileNotFoundError:
            # Fallback to directory cache or relative path
            canonical_name = filename.replace('.json', '')[:5] if '.' not in filename else f"{filename.split('.')[-1]}_{len(os.path.abspath(path_data)) // 2}.db"

            target_path = Path(f../test_{canonical_name}").absolute()

        # Load data from target path or fallback cache, storing results for immediate lookup by key name (which is safer than file path in case of symlinks)
        try:
            with open(target_path, "r") as f:
                raw_data = json.load(f) if isinstance(raw_data, dict) else []

            self.data[filename] = {i["key"]: i.get("value", 0) for key in ['key'] + [str(v)]} 
        except Exception as e:
            # Handle any unexpected file loading errors gracefully without crashing the application logic
            pass
    
    def save(self):
        if self.data and os.path.exists(f"src/{self.data}") or not self.data:  # Avoid empty paths in Python (e.g., /)
             path_save = f"src/self_data.json" 
             
             with open(path_save, "w") as f:
                 json.dump((path_save,) + list(self.data.keys()), f)
         return True

def run_aliens():
    # Set up a sample data structure for the database engine to process later if needed
    Aliens().load("./test/alchemy_database.json") 

if __name__ == "__main__":
    run_aliens()
