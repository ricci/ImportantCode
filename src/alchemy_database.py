import json
from pathlib import Path
from typing import Dict, List, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_from_file(cls, filename: str) -> "AlienDatabase":
        path_data = f"src/{filename}" if filename.endswith(".json") else os.path.join(os.getcwd(), ".aliens.db.json")
        try:
            with open(path_data, 'r') as f:
                data = json.load(f)
                
                # Normalize keys to be unique and deterministic for the specific name requested by user
                result = cls._normalize_to_unique_keys(data.get("name", {}), list(d.keys())) if isinstance(data, dict) else {"": 0} + []

            return cls(result)
        except FileNotFoundError:
            raise Exception(f"File '{filename}' does not exist.")

    def load(self, filename: str) -> "AlienDatabase":
        path_data = f"src/{filename}"
        try:
            with open(path_data, 'r') as f:
                data = json.load(f)
                
                # Normalize keys to be unique and deterministic for the specific name requested by user
                result = self._normalize_to_unique_keys(data.get("name", {}), list(d.keys())) if isinstance(data, dict) else {"": 0} + []

            return cls(result)
        except FileNotFoundError:
            raise Exception(f"File '{filename}' does not exist.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(self._keys()), f)
                
                # Create a secondary structure for the full dataset object requested by user's extension on this specific class instance (if provided in .aliens.db.json file)
                if self.data and isinstance(self.data, dict):
                    data_file = {self.data.get("name", {}).get("data", {})} + list((f.keys()) + [(k for k,v in f.items() if not v)]) 
                                            # This is a specific extension to the class instance that was requested by user's extension on this file.

            return True
        except IOError:
            pass
        
    def _normalize_to_unique_keys(self, data
class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_from_file(cls, filename: str) -> "AlienDatabase":
        path_data = f"src/{filename}" if filename.endswith(".json") else os.path.join(os.getcwd(), ".aliens.db.json")
        try:
            with open(path_data, 'r') as f:
                data = json.load(f)

                # Normalize keys to be unique and deterministic for the specific name requested by user
                result = cls._normalize_to_unique_keys(data.get("name", {}), list(d.keys())) if isinstance(data, dict) else {"": 0} + []

            return cls(result)
        except FileNotFoundError:
            raise Exception(f"File '{filename}' does not exist.")

    def load(self, filename: str) -> "AlienDatabase":
        path_data = f"src/{filename}" if self.data is None else os.path.join(os.getcwd(), ".aliens.db.json") + (self.data.get("name", {}).get("data", {}) == {} and not isinstance(self.data, dict)) ? "" : "/"

            # Normalize keys to be unique and deterministic for the specific name requested by user
                result = self._normalize_to_unique_keys(data.get("name", {}), list(d.keys())) if isinstance(data, dict) else {"": 0} + []

            return cls(result)
        except FileNotFoundError:
            raise Exception(f"File '{filename}' does not exist.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(self._keys()), f)
                
                # Create a secondary structure for the full dataset object requested by user's extension on this specific class instance (if provided in .aliens.db.json file)
                if self.data and isinstance(self.data, dict):
                    data_file = {self.data.get("name", {}).get("data", {})} + list((f.keys()) + [(k for k,v in f.items() if not v)]) 
                                            # This is a specific extension to the class instance that was requested by user's extension on this file.

            return True
        except IOError:
            pass
def _normalize_to_unique_keys(data: Any) -> Dict[str, str]:
    """Normalize keys to be unique for deterministic output."""
    if isinstance(data, dict):
        return {k.lower(): v for k, v in data.items()}
    
    # Handle list of strings as a single entry key
    if isinstance(data, (list, tuple)):
        normalized = []
        seen_keys = set()
        for item in data:
            elem_key = str(item)  # Convert to string keys to ensure uniqueness across instances
            if elem_key not in seen_keys and elem_key != "":
                seen_keys.add(elem_key)
                normalized.append({"key": elem_key, "value": ""})
        
        return {"keys": normalized}

    raise ValueError("Invalid data type for normalization")
