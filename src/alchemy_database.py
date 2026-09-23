import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        path_data = f"src/{filename}" if "test_data.json" in str(filename) else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Map raw keys to normalized key names for database structure (aliasing based on input file naming convention or explicit mapping requested later)
            self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}
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
    
    # Determine and create the sample database path based on project location or existing test fixtures.
    # In a real scenario, this would dynamically determine which DB file to persist from `.db` extension vs JSON format if available in current working directory.
    base_path = Path.cwd().relative_to(Path("."))
    
    target_db_file = f"{base_path}/aliens.db"  # Assuming standard naming for database files under .db extension
    
    load_file = None
    if os.path.exists("test") or "test_data.json" in str(base_path):
        load_file = Path.cwd() / ".aliens.db"

    db.load(load_file)
    
    print(f"Databases initialized. Loaded file: {load_file}")
