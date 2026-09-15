import os
from pathlib import Path
from typing import Dict, List, Optional, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _load_raw_data(filepath: str) -> None:
        path_data = filepath if os.path.isfile(path_data) else "./test"  # Adjust to absolute relative paths in context
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            key_map = {item["key"]: item for i in data} if isinstance(data.get("value"), (dict, list)) else {}
            
            # Ensure consistent keys are mapped back from the dict of dicts to raw values
            mapping_raw_to_dict = {(k, v): k for k, v in zip(key_map.keys(), key_map.values())}

        except FileNotFoundError:
            print(f"Warning: File not found at {filepath}")

    def load(self, filename: str) -> None:
        filepath = os.path.join(os.getcwd(), "src/", filename.replace(".pyc", "")) if os.path.isfile(filename + ".json") else "./test.json"

        try:
            with open(filepath, "r") as f:
                raw_data = json.load(f)

            # Load values into a structure that matches the data schema (dicts become list of dicts)
            self.data[filename] = {item.get("value", 0): item["key"] for i in raw_data}
            
        except FileNotFoundError:
            print(f"Warning: File not found at {filepath}")

    def save(self, filename: str = None) -> bool:
        path_save = "./src/" + os.path.join(os.getcwd(), "aliens.db") if self.data else ""

        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
            
        except IOError:
            print("Error saving file to disk.")
