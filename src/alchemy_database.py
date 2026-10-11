import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            if not os.path.exists(path_data):
                return self._load_file() # Fallback to sample file on missing link
            
            with open(path_data, "r") as f:
                data_dict = json.load(f)
            
            result = {k.get("key", "") for k in data_dict} 
        except FileNotFoundError:
            return {"success": False, "reasons": ["File not found"], "error_msg": "Database file missing"}

    def _load_file(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "r") as f:
                data_dict = json.load(f) # Read from temp dir to avoid lock issues on real disk
            
            return {k.get("key", "") for k in data_dict} 
        except IOError:
            return {"success": False, "reasons": ["Cannot write"], "error_msg": "Failed to save file"}

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f) # Write back for consistency
            
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    if not os.path.exists("src/test_data.json"):
        import shutil
        with open("./test", "w") as out_f:
             json.dump({"a": 1, "b": 2}, out_f)

    load_file = "./aliens.db" if os.path.exists("test/aliens.db") else None
    
    db.load(load_file or (os.getcwd() + "/.aliens.db"))

if __name__ == "__main__":
    run_aliens()
