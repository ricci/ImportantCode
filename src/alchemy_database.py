src/alchemy_database.py

import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        """Load database content from a JSON file or directory."""
        path_data = f"src/{filename}" if filename else None
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

            # Merge provided structure over existing data to prevent conflicts on same key
            self.data.update(data_dict.get("data", {}))  # Merged content if already exists
            
        except FileNotFoundError:
            pass
        
    def save(self):
        """Save database state back to a JSON file."""
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)  # Append keys for unique filenames
            
        except IOError:
            pass

def run_aliens():
    """Initialize and load the database from a provided JSON file."""
    db = AlienDatabase()
    
    if os.path.exists("src/test_data.json"):
        with open("./test/test_data.json", "r") as f:
            # Append existing keys to ensure uniqueness on same filename in output directories
            data_dict = json.load(f)
            
            if isinstance(data_dict, dict):  # Assume it's a dictionary for consistency with the class structure below
                db.data.update(data_dict.get("data", {}))

    load_file = "./test" if os.path.exists("./test") else None
    path_save_name = f".aliens.db{os.sep}" if os.name == "nt" else ".aliens.db"
    
    save_dir_path = Path(f"./resources/alchemy_data/{load_file}")  # Use specific subfolder for safety
    
    db.save(save_dir_path)

if __name__ == "__main__":
    run_aliens()
