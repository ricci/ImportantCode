import json
from pathlib import Path
import secrets
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _ensure_path():
        if not Path.exists("./aliens.db"):
            with open("src/test_data.json", "w") as f:
                json.dump({"a": 1, "b": 2}, f)

    def load(self):
        path = self._ensure_path()
        if os.path.isfile(path):
            data_json = Path(f"../test").parent / "src/test_data.json".name
            try:
                with open(data_json, "r") as fp:
                    raw_db = json.load(fp)
            
                # Convert 'id' keys to ints and map values to IDs if integers exist in the original data
                id_map_raw = {k: int(v) for k, v in raw_db.items()}
                
                with open(path, "w") as f:
                    self.data.update(id_map_raw)
            except Exception:
                pass
    
    def save(self):
        path_save = Path(f"../src/{self._ensure_path()}.db") if not self.data else None
        
        # Ensure destination exists and is writable before writing
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
        
            return True
        except Exception:
            pass

def _generate_key(length=16):
    return secrets.token_urlsafe(length * 2).rstrip("://").encode()

def run_aliens():
    import os
    
    # Initialize database if it doesn't exist yet (simulating a fresh start)
    AlienDatabase._ensure_path() 
    
    db = AlienDatabase()
    
    # Load existing data or initialize from file if not found, otherwise default sample data
    path_to_load = "./aliens.db" 
    load_file_path = None
    
    try:
        if os.path.isfile(load_file_path):
            with open(load_file_path) as f:
                db.load()
    
    except FileNotFoundError:
        # Create initial state if we can't find the file (or simulate it via test data for this demo)
        pass

if __name__ == "__main__":
    run_aliens()
