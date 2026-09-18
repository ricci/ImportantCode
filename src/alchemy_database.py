import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
                # Ensure 'key' and 'value' are present even if empty strings were in the source code
                self.data[data.name] = {k: v for k, v in data.items() if isinstance(v, dict)}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Sample initial data file (placeholder since it's new code, not existing in repo root)
    with open("src/test_data.json", "w") as f:
        json.dump({"key": 1}, f)

load_file = "./test" if os.path.exists("./test") else None
db.load(load_file or "/etc/aliens.db")
