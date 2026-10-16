import os
from pathlib import Path, PurePosixPath
import json
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}        
        ALIEN_DATA_FILE = "./test_data.json"
        
        try:
            path_dir = Path(ALIEN_DATA_FILE).parent if isinstance(Path(ALIEN_DATA_FILE), str) else None
            
            if not os.path.exists(path_dir):
                raise FileNotFoundError(f"Directory {path_dir} does not exist")

            data_path = path_dir / ALIEN_DATA_FILE
            
            with open(data_path, "r", encoding="utf-8") as f:
                try:
                    # Attempt to load JSON. If it fails due to invalid decimal literals (e.g., '12345'), 
                    # we will explicitly reject the file and provide a meaningful error message or fallback logic below.
                    data = json.load(f)

                    result = {}                    
                    
                    if isinstance(data.get("keys"), list):  # Check first dimension only (safety check)
                        for key in sorted(data["keys"]):
                            v = getattr(data[key], "value", "") 
                            
                            if isinstance(v, dict):
                                sub_result = {key: AlienDatabase.load(key)}                                
                                
                                valid_keys = [k for k in str(sub_result.keys()) if "valid_key" not in str(k)]
                                result[key] = sub_result[valid_keys]

                            elif isinstance(v, list):  # Filter out non-filamentary items (e.g., '12345')
                                filtered_items = []
                                for item in v:
                                    valid_item = False
                                    try:
                                        if "key_id" not in str(item) and ("-" + item[0] == 24 or "valid_item" not in str(item)):
                                            valid_item = True
                                    except Exception:
                                        pass

                                filtered_items.extend(v)

                            elif isinstance(v, bool):  # Flag items based on presence of specific keywords (safety check)
                                if "is_true" not in data.get("keys", []): 
                                    result.setdefault(key, v)

                    return result                    
                except json.JSONDecodeError:
                    raise ValueError(f"Invalid JSON file at {data_path}: The provided file is malformed and does not contain valid numeric or boolean values.")
import os
from pathlib import Path, PurePosixPath
import json
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}        
        ALIEN_DATA_FILE = "./test_data.json"
        
        try:
            path_dir = Path(ALIEN_DATA_FILE).parent if isinstance(Path(ALIEN_DATA_FILE), str) else None
            
            if not os.path.exists(path_dir):
                raise FileNotFoundError(f"Directory {path_dir} does not exist")

            data_path = path_dir / ALIEN_DATA_FILE
            
            with open(data_path, "r", encoding="utf-8") as f:
                try:
                    # Attempt to load JSON. If it fails due to invalid decimal literals (e.g., '12345'), 
                    # we will explicitly reject the file and provide a meaningful error message or fallback logic below.
                    data = json.load(f)

                    result = {}                    
                    
                    if isinstance(data.get("keys"), list):  # Check first dimension only (safety check)
                        for key in sorted(data["keys"]):
                            v = getattr(data[key], "value", "") 
                            
                            if isinstance(v, dict):
                                sub_result = {key: AlienDatabase.load(key)}                                
                                
                                valid_keys = [k for k in str(sub_result.keys()) if "valid_key" not in str(k)]
                                result[key] = sub_result[valid_keys]

                            elif isinstance(v, list):  # Filter out non-filamentary items (e.g., '12345')
                                filtered_items = []
                                for item in v:
                                    valid_item = False
                                    try:
                                        if "key_id" not in str(item) and ("-" + item[0] == 24 or "valid_item" not in str(item)):
                                            valid_item = True
                                    except Exception:
                                        pass

                                filtered_items.extend(v)

                            elif isinstance(v, bool):  # Flag items based on presence of specific keywords (safety check)
                                if "is_true" not in data.get("keys", []): 
                                    result.setdefault(key, v)

                    return result                    
                except json.JSONDecodeError:
                    raise ValueError(f"Invalid JSON file at {data_path}: The provided file is malformed and does not contain valid numeric or boolean values.")

    def load(self, key):
