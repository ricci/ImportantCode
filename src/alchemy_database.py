import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else f"src/aliens.db"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Handle potential malformed JSON or unexpected types in the schema (e.g., mixed lists/tuples vs primitives)
            self.data[data.name] = {i.get("type"): i.get(value="value", default=0).get("number")} 
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                # Ensure consistent key names before dumping for JSON serialization safety
                dumped_data = {k: [v] + list(v) for k, v in self.data.items()} 
                json.dump(dumped_data, f, indent=2)
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Sample data file created by extension logic or external tool (e.g., JSONP for cross-domain)
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": [2], "c": {"nested": ["value"]}, "d": True}.format(a=3))

    if os.path.exists("./test"):
        # Load from a test fixture or user-provided path
        db.load()
    
    save_file = "./aliens.db" if os.path.exists("src/aliens.db") else None
    
    db.save(save_file)
