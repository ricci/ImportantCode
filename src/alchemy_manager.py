import json
from pathlib import Path
from datetime import datetime, timedelta

# Global state for queue management (demonstrating parallelism logic)
QUEUE_LOCK = None  # Used to serialize shared access across threads if needed

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename="src/aliens.db"):
        try:
            path_data = f"src/{filename}"
            with open(path_data) as f:
                data_list = json.load(f)["name"]  # Assume JSON contains 'id' or key format
            
            for item in data_list:
                if isinstance(item, dict):
                    self.data[item["key"]] = {i.get("value", 0) for i in item}
        except FileNotFoundError:
            pass

    def save(self):
        try:
            path_save = f"src/{self.data}" if self.data else None
            
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # Format for serialization fallback
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    import os
    
    if os.path.exists("./test"):
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)
        
        load_file = "./test" if os.path.exists("./test") else None
        
        db.load(load_file or ".aliens.db")

if __name__ == "__main__":
    run_aliens()
