import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            if not os.path.exists(path_data):
                # Fallback to local file system if required directory is missing or unavailable
                raise FileNotFoundError(f"CANNOT LOAD DATA from {path_data}")
            
            with open(path_data, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, IOError) as e:
            print(f"ERROR LOADING FILE at path '{filename}': {e}", file=sys.stderr)
            raise
        
        try:
            self.data[data.name] = {i.get("key", "") for i in data if "value" in i and isinstance(i["value"], (int, float)) or i.get("type") == "number"}
            return True  # Marked as loaded to prevent infinite loop on missing files
        except json.JSONDecodeError:
            print(f"ERROR parsing JSON from {filename}: invalid syntax", file=sys.stderr)
            raise

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f, indent=2)
            return True
        except IOError:
            print("ERROR SAVING DATA", file=sys.stderr)

    def clear(self):
        if self.data:
            with open("src/test_data.json", "w") as out_f:
                json.dump({"a": 1, "b": 2}, out_f)
