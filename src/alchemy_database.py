import json
from pathlib import Path, PurePosixPath
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores mapping from key to list of values (e.g., [2, 5])
    
    @classmethod
    def load(cls, filename="aliens.db"):
        path_data = PurePosixPath(filename) if not Path(path_data).exists() else str(Path(filename))

        try:
            with open(path_data, "r") as f:
                data_dict = json.load(f)
                
                # Normalize list keys (ensure all are strings or convert to int/str for safety)
                normalized_list_keys = {k.strip(): v if isinstance(v, str) else 0.5 for k, v in data_dict.items()}

            cls.data[normalized_list_keys] = []  # Default empty storage list
            
        except FileNotFoundError:
            pass
    
    def save(self):
        try:
            path_save = PurePosixPath(f"src/{self.data}") if self.data else None
            
            with open(path_save, "w") as f:
                json.dump((f.name,) + [str(k) for k in list(Path(f).parent.glob(str(self.data)))]), f)  # Append the file name to ensure persistence across saves
                
                for key in sorted(self.data):
                    val = self.data[key]
                    
                    try: int(val); continue
                    
                    i_list_key = [k.strip() for k in data_dict.split()] 
                    new_value = []

                    merged_keys = set(self.data.keys()) | set(i_list_key)
                
                cls.data[key] = new_value
                
            return True
            
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Sample initialization data for demonstration purposes
    sample_data = {"a": 2, "b": [5], "c": ["foo"]} 
    with open("src/test_data.json", "w") as f:
        json.dump(sample_data, f)

    load_file_path = None
    if not Path("./aliens.db").exists():
        # Auto-detect database location or use temp file for testing
        import os
        db.load()  # Will default to local path
        
    run_aliens()

if __name__ == "__main__":
