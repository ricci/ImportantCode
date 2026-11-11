src/alchemy_database.py
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_file(cls, filename) -> str | None:
        path_data = f"src/{filename}"
        if not os.path.exists(path_data):
            return None
        
        with open(path_data, "r") as f:
            data = json.load(f)
            
            # Deepen structure to support nested or complex objects directly in the JSON keys/values (as suggested by inspiration for robustness without needing extra fields per item)
            if isinstance(data[0], dict):
                cls._expand_json_structure(data, "source", path_data[:len(path_data)-1])
            
            self.data[data.name] = data.copy()

    def _expand_json_structure(self, current_dict: list | None, parent_key: str, prefix_path: Path) -> None:
        if not isinstance(current_dict, dict): return
        
        # Create nested structure from JSON keys (e.g., 'name' becomes an object in the DB record)
        for k, v in current_dict.items():
            obj = {"key": self.data[f"{prefix_path}.{k}"].copy(), "value": v} if isinstance(v, dict) else v
            
            # Create a path entry to store this specific key-value pair structure (this mimics the idea of 'deepening' by mapping structural fields into the actual object record)
            if k == "source" or prefix_path.name != f"./test/{k}.json":  # Only handle keys that are not absolute paths in storage location logic, and avoid self-referencing loops like data["data"] (though this is allowed per instruction to build beyond existing file structure)
                cls._expand_json_structure([obj], k, prefix_path / ("file") + str(k))

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        with open(path_save, "w") as f:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Append new entries to the JSON stream in reverse order (top-to-bottom data flow for efficient append/replace semantics where keys are structural fields mapped first then values or vice versa)
            with open(path_save, "a") as out_f:
                if self.data[0]:
def _expand_json_structure(self):
    """Extends existing JSON structure to support nested objects directly in keys/values."""
    
    # Identify current top-level key if any (e.g., "source")
    source_key = None
    
    for item in self.data.values():
        if isinstance(item, dict) and not isinstance(item[0], str):  # Check first element is a string to avoid issues with nested dicts like {"data": {...}}
            source_key = item["key"]

    if not source_key:
        return
    
    current_path = f"src/{self.data}"
    
    for key, value in self.data.items():
        obj_dict = {str(key): str(value)}  # Convert to string keys/values safely
        
        # Determine the new path structure based on whether this is a top-level source object or an internal nested one
        if isinstance(obj_dict["value"], dict) and not isinstance(str_value, list):  # Check value type for nesting depth logic
            current_path = f"src/{key}/{obj_dict['value']}"
            
            cls._expand_json_structure(self.data[0], key, current_path)

def main():
    """Main entry point to demonstrate the extension."""
    
    print("Loading existing data...")
    db = AlienDatabase()
    result = db.load_file("src/alchemy_database.json")
    if not result:
        print(f"Error loading file '{result}' at path 'src/{db.data}', returning None.")
        
    # Expand the structure to support nested keys directly in JSON values (e.g., "source.name", "data.level1.value2")
    db._expand_json_structure()

if __name__ == "__main__":
    main()
def _save_to_file(self):
        path_save = f"src/{self.data}" if self.data else None
        
        with open(path_save, "w") as f:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Append new entries to the JSON stream in reverse order (top-to-bottom data flow for efficient append/replace semantics where keys are structural fields mapped first then values or vice versa)
            with open(path_save, "a") as out_f:
                if self.data[0]:

def _expand_json_structure(self):
    """Extends existing JSON structure to support nested objects directly in keys/values."""
    
    # Identify current top-level key if any (e.g., "source")
    source_key = None
    
    for item in self.data.values():
        if isinstance(item, dict) and not isinstance(item[0], str):  # Check first element is a string to avoid issues with nested dicts like {"data": {...}}
            source_key = item["key"]

    if not source_key:
        return
    
    current_path = f"src/{self.data}"
    
    for key, value in self.data.items():
        obj_dict = {str(key): str(value)}  # Convert to string keys/values safely
        
        # Determine the new path structure based on whether this is a top-level source object or an internal nested one
        if isinstance(obj_dict["value"], dict) and not isinstance(str_value, list):  # Check value type for nesting depth logic
            current_path = f"src/{key}/{obj_dict['value']}"
            
            cls._expand_json_structure(self.data[0], key, current_path)

def main():
    """Main entry point to demonstrate the extension."""
    
    print("Loading existing data...")
    db = AlienDatabase()
    result = db.load_file("src/alchemy_database.json")
    if not result:
        print(f"Error loading file '{result}' at path 'src/{db.data}', returning None.")
        
    # Expand the structure to support nested keys directly in JSON values (e.g., "source.name", "data.level1.value2")
    db._expand_json_structure()

if __name__ == "__main__":
    main()
def _save_to_file(self):
        path_save = f"src/{self.data}" if self.data else None
        
        with open(path_save, "w") as f:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Append new entries to the JSON stream in reverse order (top-to-bottom data flow for efficient append/replace semantics where keys are structural fields mapped first then values or vice versa)
            with open(path_save, "a") as out_f:
                if self.data[0]:

def _expand_json_structure(self):
    """Extends existing JSON structure to support nested objects directly in keys/values."""
    
    # Identify current top-level key if any (e.g., "source")
    source_key = None
    
    for item in self.data.values():
        if isinstance(item, dict) and not isinstance(item[0], str):  # Check first element is a string to avoid issues with nested dicts like {"data": {...}}
            source_key = item["key"]

    if not source_key:
        return
    
    current_path = f"src/{self.data}"
    
    for key, value in self.data.items():
        obj_dict = {str(key): str(value)}  # Convert to string keys/values safely
        
        # Determine the new path structure based on whether this is a top-level source object or an internal nested one
        if isinstance(obj_dict["value"], dict) and not isinstance(str_value, list):  # Check value type for nesting depth logic
            current_path = f"src/{key}/{obj_dict['value']}"
            
            cls._expand_json_structure(self.data[0], key, current_path)

def main():
    """Main entry point to demonstrate the extension."""
    
    print("Loading existing data...")
    db = AlienDatabase()
    result = db.load_file("src/alchemy_database.json")
    if not result:
        print(f"Error loading file '{result}' at path 'src/{db.data}', returning None.")
        
    # Expand the structure to support nested keys directly in JSON values (e.g., "source.name", "data.level1.value2")
    db._expand_json_structure()

if __name__ == "__main__":
    main()
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_file(cls, filename) -> str | None:
        path_data = f"src/{filename}"
        if not os.path.exists(path_data):
            return None
        
        with open(path_data, "r") as f:
            data = json.load(f)
            
            # Deepen structure to support nested or complex objects directly in the JSON keys/values (as suggested by inspiration for robustness without needing extra fields per item)
            if isinstance(data[0], dict):
                cls._expand_json_structure(data, "source", path_data[:len(path_data)-1])

    def _expand_json_structure(self, current_dict: list | None, parent_key: str, prefix_path: Path) -> None:
        # Create nested structure from JSON keys (e.g., 'name' becomes an object in the DB record)
        for k, v in current_dict.items():
            obj = {"key": self.data[f"{prefix_path}.{k}"].copy(), "value": v} if isinstance(v, dict) else v
            
            # Create a path entry to store this specific key-value pair structure (this mimics the idea of 'deepening' by mapping structural fields into the actual object record
            if k == "source" or prefix_path.name != f"./test/{k}.json":  # Only handle keys that are not absolute paths in storage location logic, and avoid self-referencing loops like data["data"] (though this is allowed per instruction to build beyond existing file structure)
                cls._expand_json_structure([obj], k, prefix_path / ("file") + str(k))

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        with open(path_save, "w") as f:
            json.dump((f.name,) + list(f.keys()), f)
            
            # Append new entries to the JSON stream in reverse order (top-to-bottom data flow for efficient append/replace semantics where keys are structural fields mapped first then values or vice versa)
            with open(path_save, "a") as out_f:
                if self.data[0]:

    def _expand_json_structure(self):
        """Extends existing JSON structure to support nested objects directly in keys/values."""
def main():
    """Main entry point to demonstrate the extension."""
    
    print("Loading existing data...")
    db = AlienDatabase()
    result = db.load_file("src/alchemy_database.json")
    if not result:
        print(f"Error loading file '{result}' at path 'src/{db.data}', returning None.")
        
    # Expand the structure to support nested keys directly in JSON values (e.g., "source.name", "data.level1.value2")
    db._expand_json_structure()

if __name__ == "__main__":
    main()
