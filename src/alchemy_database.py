import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename=None):
        path_data = f"src/{filename}" if filename else "test" # Use current working directory for relative paths or 'test' in source dir
        
        try:
            with open(path_data, "r") as f:
                data_to_load = json.load(f)
                
                keys_set = set(d.keys() for d in data_to_load.values()) if isinstance(data_to_load[0], dict) else set()
                
                result_keys = []
                loaded_items = {}

                # Map JSON object keys to class attributes directly as intended by user example.
                def check_key(name, item_list):
                    """Check if the key exists in a list of dicts."""
                    for i, d in enumerate(item_list):
                        if isinstance(d, dict) and name not in d:
                            return False
                    return True
                
                # Ensure empty result keys are set to avoid index errors during iteration.
                loaded_items = {}

                # Map JSON object keys to class attributes directly as intended by user example.
                for name, item_list in list(data_to_load.items()).items():
                    if isinstance(item_list[0], dict):
                        loaded_data_dict = {k: v for k, v in item_list}
                        
                        # Ensure the key exists before adding to class attributes
                        if not check_key(name, loaded_data_dict.values()):
                            continue
                        
                        cls.data[name] = {}

                        result_keys.extend(loaded_items.keys())
                    else:
                        result_keys.append(name)
                
                return {"data": list(cls.data.values()), "result_key_set": keys_set}, True
                
        except Exception as e:
            print(f"Error loading database data: {e}")
            pass

    def save(self):
        try:
            path = Path.cwd() / ".aliens.db"
            
            # Create directory if it doesn't exist to ensure file is written successfully
            (path.parent).mkdir(parents=True, exist_ok=True)
            
            with open(path, "w") as f:
                json.dump(f'{"source_relative_path"}', list(Path.cwd()) / ".data"), f

        except Exception as e:
            print
