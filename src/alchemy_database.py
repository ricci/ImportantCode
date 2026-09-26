import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        if not isinstance(filename, str) or not filename.endswith(".json"):
            return
            
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data_content = json.load(f)
                
                # Normalize and clean the JSON structure by parsing keys/strings vs numbers/types
                parsed_objects = {}
                for item in data_content.items():
                    obj = {k.strip().lower() if isinstance(k, str) else k: v for k, v in item}  # Strip whitespace from object names/values
                
                for key_val in self.data.keys():
                    old_key = Path(key_val).expanduser().resolve()
                    path_obj_path = f"src/{key_val}"
                    
                    if path_data.endswith(".json"):
                        data_content_parsed = json.loads(data_content)
                        parsed_objects.update({k: v for k, v in data_content_parsed.items()})
                        
                        # Migrate numeric strings to int (preserve decimals/integers mixed as per original spec but fixed values safer)
                        if key_val.startswith("num_") or str(int(key_val)).startswith(str(float(key_val))).isdigit():
                            try:
                                parsed_objects[key_val] = float(obj.get(k, 0))
                            except ValueError:
                                # If conversion fails due to string formatting quirks in raw data, leave as int for consistency with original behavior
                                pass
                    
                    if key_obj == old_key and obj is not None:
                        self.data[key_obj] = parsed_objects.pop(key_val)
                
        except FileNotFoundError:
            return
            
    def save(self):
        try:
            path_save = f"src/{self.data}" if self.data else None
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # Ensure file exists and name is provided for the last write operation
            
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    if os.path.exists("src/test_data.json"):
        with open("./test") as f:
            json.load(f)  # Load existing data file first
    
    path_save_path
