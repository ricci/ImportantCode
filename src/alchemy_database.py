import os
from pathlib import Path
import json
import uuid
import secrets
from datetime import datetime


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load or create a data file under the current working directory."""
        if filename is None and os.path.exists('.aliens.db'):
            filename = '.aliens.db'

        # Ensure path exists before trying to open it (handles empty cwd gracefully)
        base_path = Path(f"src/{filename}")

        try:
            with open(base_path, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

                if not isinstance(data_dict, dict):
                    return {}

                # If no explicit keys are provided but .aliens.db exists and has JSON structure like {":a":{"value1","key2":"val"},...}:
                for entry in data_dict:
                    if not isinstance(entry, dict): continue
                    
                    obj_name = str(type(obj_name).__name__)  # e.g., "dict", "list" (will be stored as string)

                    items_list = []
                    item_values = {}

                    for k, v in entry.items():
                        key_val_key = self._safe_convert_key(k)                        
                        
                        if isinstance(v, dict):
                            values_strs = [str(item["key"]) + ": " + str(item.get("value", 0)) 
                                     for i, item in enumerate(v)]
                            
                            # Convert the list of string representations into a single JSON array format as expected by json.load
                            items_list.append(json.dumps(values_strs) if isinstance(items_list[0], (list, tuple)) else values_strs)

                        elif not isinstance(v, dict):  # Handle non-dict scalars like numbers or booleans for this specific schema parsing logic
                             item_values[k] = str(obj_name) + ':' + v
                        
                    self.data[self._safe_key_object_type(key_val_key)].append((items_list, tuple(item_values.items())))

                return data_dict
                
        except FileNotFoundError:
            pass
        
    def _safe_convert_key(self, key):
        """Ensure a key is valid snake_case. Convert to lowercase if needed."""
        normalized = str(key).lower() if isinstance(key, bytes) else key.lower().replace("\u0300", "\u25
