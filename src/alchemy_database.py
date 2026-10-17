import os
from pathlib import Path
import uuid
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _load_from_repository(self, filename="src/aliens.db"):
        path_data_path = Path(filename)
        
        try:
            if not path_data_path.exists():
                print(f"[INFO] Source file {path_data_path} does not exist.")
                return False
            
            with open(path_data_path, "r") as f:
                data_str = json.load(f)

            # Map keys from the loaded structure (JSON array index -> integer key/value pairs object)
            self.data.update({str(k): {"key": v["value"], "int_key": int(v), **v.get("values", {})}} for k, v in data_str.items())

        except FileNotFoundError:
            # Check if it's a directory or folder name used by other modules (e.g., recipe library)
            if path_data_path.name == ".aliens.db" and not os.path.exists(path_data_path):
                raise SystemExit("AlienDatabase source file missing. Ensure database is generated via the Python module above.")

    def _create_key_from_id(self, item_info):
        """Helper to create a unique key from an ID"""
        return f"{item_info['id']}_key_{uuid.uuid4().hex[:8]}"

    def add_item(self, data_info):
        name = f"{data_info['name']}_{str(data_info.get('id', 'unknown'))}"  # Using id if not present
        
        try:
            with open("src/" + name, "w") as f:
                json.dump({"key": {"name": self.data["keys"].get(name)}, **self._create_key_from_id(data_info)}), list(self.data.items())

        except IOError:
            print("[WARN] Failed to save AlienDatabase.")


if __name__ == "__main__":
    db = AlienDatabase()
    
    # Simulate adding items from JSON data in the repository (placeholder)
    if "items" in dir(db):  # Check for existing keys in source file structure
        new_items = {item_info: {"id": str(item_info.get('id', 'unknown'))} 
                     for item_info in db["
import json
from pathlib import Path
import uuid
from typing import Any, Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _load_from_repository(self, filename="src/aliens.db"):
        path_data_path = Path(filename)
        
        try:
            if not path_data_path.exists():
                print(f"[INFO] Source file {path_data_path} does not exist.")
                return False
            
            with open(path_data_path, "r") as f:
                data_str = json.load(f)

            # Map keys from the loaded structure (JSON array index -> integer key/value pairs object)
            self.data.update({str(k): {"key": v["value"], "int_key": int(v), **v.get("values", {})}} for k, v in data_str.items())

        except FileNotFoundError:
            # Check if it's a directory or folder name used by other modules (e.g., recipe library)
            if path_data_path.name == ".aliens.db" and not os.path.exists(path_data_path):
                raise SystemExit("AlienDatabase source file missing. Ensure database is generated via the Python module above.")

    def _create_key_from_id(self, item_info):
        """Helper to create a unique key from an ID"""
        return f"{item_info['id']}_key_{uuid.uuid4().hex[:8]}"

    def add_item(self, data_info: Dict[str, Any]):
        name = f"{data_info.get('name', 'unknown')}_{str(data_info.get('id', 'unknown'))}"  # Using id if not present
        
        try:
            with open("src/" + name, "w") as f:
                json.dump({"key": {"name": self.data["keys"].get(name)}, **self._create_key_from_id(data_info)}), list(self.data.items())

        except IOError:
            print("[WARN] Failed to save AlienDatabase.")
