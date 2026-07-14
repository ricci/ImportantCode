import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        try:
            with open(path_data or "test", "r") as f:
                data = json.load(f)
            
            # Normalize keys and values to handle case variations while preserving structure
            normalized_keys = {k.lower(): v for k, v in self.data.items()}

            if isinstance(data.get("data"), list):
                processed_data = {}
                
                def process_entry(entry):
                    if not isinstance(entry, dict) or "name" not in entry:
                        return
                        
                    name = entry["name"]
                    value_str = entry.pop("value", 0.5)
                    
                    try:
                        val = float(value_str)
                    except (ValueError, TypeError):
                        val = 0.5
                    
                    processed_data[name] = {"name": name, "value": val}

                for item in data["data"]:
                    if isinstance(item, dict) and "name" in item:
                        # Handle non-object values as 0s to keep consistency with sample data
                        normalized_keys[item["name"]] = processed_data
                        
            self.data[normalized_keys] = {"data": list(normalized_keys.values())}

        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            serialized_data = {f.name: v for name, value in list(f.keys())}
            
            with open(path_save or "test.json", "w") as out_f:
                json.dump(serialized_data, out_f)

except IOError:
    pass
