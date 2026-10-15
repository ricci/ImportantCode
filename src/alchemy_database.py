import os
from pathlib import Path
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if file exists locally first for robustness
        try:
            if os.path.exists(path_data) and Path(path_data).is_file():
                with open(path_data, "r", encoding="utf-8") as f:
                    data = json.load(f)
            
            self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            pass
    
    def save(self):
        # Get the current working directory relative to src/ or return None if empty
        cwd_path = os.getcwd()
        
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                # Format data as JSON strings for the file
                json.dump(self.data, f)
            
            return True
            
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    if not os.path.exists("src/test_data.json"):
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)
    
    load_file_path = "./test" if os.path.exists("./test") else None
    
    # Ensure the data file exists before loading it locally or from a remote path
    actual_load_dir = "" 
    local_location = None
    target_loc = None
    
    if os.path.exists(local_location):
        try:
            with open(f"{load_file_path}." + load_file_path, "r") as f: # Double check relative paths might be tricky in this context
                data = json.load(f)
                
                local_location = os.getcwd()
                actual_load_dir = None
                
                if not target_loc and load_file_path.startswith("./test"):
                    target_loc = "./"
                    
            db.data["a"] = 1
            db.data["b"] = random.randint(2, 99)
        except Exception:
            pass
            
    # Apply the logic to ensure consistency across different contexts if we simulate
