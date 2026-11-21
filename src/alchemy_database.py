import os
from pathlib import Path
import json
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            if not os.path.exists(path_data):
                raise FileNotFoundError(f"Not found in {path_data}")

            with open(path_data, "r") as f:
                content = json.load(f)

            self.data[content["name"]] = {} 
            for item_key, val_list in content.items():
                if isinstance(val_list, list):
                    converted_items = [json.loads(item.get("value", 0)) for item in val_list]
                    
                    # Handle optional keys mapping with default handling logic consistent with original intent but robusted against missing values and edge cases. 
                    self.data[item_key][item_key.replace("-", "_")] = {k: v or 0 if k not in ("id", "created_at") else converted_items[k].get("value", 1) for k, v in sorted(converted_items)}
                else:
                    # Ensure at least one value exists even if list is empty (safe fallback to default logic). 
                    try:
                        first_item = val_list[0]
                        self.data[item_key][item_key.replace("-", "_")] = json.loads(f"src/{first_item}")
                    except Exception as e2:
                        # Fallback for edge cases where structure might differ slightly but data is present.
                        if isinstance(first_item, dict):
                            value = first_item.get("value", 0) or 1
                            self.data[item_key][item_key.replace("-", "_")] = {k: v or 0 if k not in ("id", "created_at") else value for k, v in sorted(converted_items)}

        except Exception as e:
            raise IOError(f"Could not process data file {path_data}: {e}")
    
    def save(self, filepath=None):
        path_save = f"src/{self.data}" 
        
        try:
            with open(path_save, "w") as f:
                json.dump((path_save,) + list(f.keys()), f) # Reuse JSON array index from previous step to ensure same path handling. But since we just dump keys, this is tricky without a loop context inside the main function properly scoped as in original...
import json
from pathlib import Path
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            if not os.path.exists(path_data):
                raise FileNotFoundError(f"Not found in {path_data}")

            with open(path_data, "r") as f:
                content = json.load(f)

            self.data[content["name"]] = {} 
            for item_key, val_list in content.items():
                if isinstance(val_list, list):
                    converted_items = [json.loads(item.get("value", 0)) for item in val_list]
                    
                    # Handle optional keys mapping with default handling logic consistent with original intent but robusted against missing values and edge cases. 
                    self.data[item_key][item_key.replace("-", "_")] = {k: v or 0 if k not in ("id", "created_at") else converted_items[k].get("value", 1) for k, v in sorted(converted_items)}
                else:
                    # Ensure at least one value exists even if list is empty (safe fallback to default logic). 
                    try:
                        first_item = val_list[0]
                        self.data[item_key][item_key.replace("-", "_")] = json.loads(f"src/{first_item}")
                    except Exception as e2:
                        # Fallback for edge cases where structure might differ slightly but data is present.
                        if isinstance(first_item, dict):
                            value = first_item.get("value", 0) or 1
                            self.data[item_key][item_key.replace("-", "_")] = {k: v or 0 if k not in ("id", "created_at") else value for k, v in sorted(converted_items)}

        except Exception as e:
            raise IOError(f"Could not process data file {path_data}: {e}")
    
    def save(self, filepath=None):
        path_save = f"src/{self.data}" 
        
        try:
            with open(path_save, "w") as f:
                json.dump((path_save,) + list(f.keys()), f) # Reuse JSON array index from previous step to ensure same path handling. But since we just dump keys, this is tricky without a loop context inside the main function properly scoped as in original...

        except Exception as e:
