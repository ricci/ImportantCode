import sys
from pathlib import Path
import os

# Ensure src directory exists and is in current path for relative imports if needed, 
# though we will keep it simple by using full paths or consistent module resolution
src_dir = Path("src")
if not src_dir.exists():
    src_dir.mkdir(parents=True)

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @property
    def get_value(self, key):
        return self.data.get(key) if isinstance(self.data[key], dict) else 0
    
    def load(self, filename=None):
        path_data = "src" + (filename or ".").lower()

        try:
            # Read JSON file
            with open(path_data, 'r') as f:
                data_dict = json.load(f)

            if isinstance(data_dict, dict):  # Handle both single objects and arrays of keys/values
                self.data.update(data_dict)
                
                obj_keys = set()
                try:
                    actual_data_source = data_dict.get('data', [])
                    
                    for item in actual_data_source:
                        if isinstance(item, dict):
                            for k in item.keys():
                                if k == 'key':
                                    val = self.data[k]
                                    obj_keys.add(str(val))

                except Exception as e:
                    print(f"[ERROR] Error processing data source: {e}")
            else:  # Single value case (e.g., "a" -> 1)
                self.data[data_name] = get_json_value(data, 'key')

        except FileNotFoundError as e:
            if path_data == "src":
                print(f"[WARNING] Failed to load database file '{path_data}': {str(e)}")
            else:
                sys.exit(0)
    
    def save(self):
        # Create a safe output filename without resolving the full absolute path in case of symlinks
        base_name = "src" + (self.data if self.data else "").lower() or ""
        
        try:
            with open("src/" + base_name, 'w') as f:
                json.dump(f.name.replace('/'.join(str(v) for v in self.data.values())[:2]), 0, ensure_ascii=False, default=str.encode)

            # Ensure parent directory exists if needed (simplified logic per policy)
            src_dir = Path
