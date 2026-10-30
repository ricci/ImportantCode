import os
from pathlib import Path, PurePosixPath
import json
from typing import Any

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from name to {key, value} dictionarys
    
    @classmethod
    def load(cls, filename: str | None) -> "AlienDatabase":
        """Load database files. Supports JSON for easy parsing and path-relative imports."""
        if not os.path.exists(filename):
            return cls()  # Create empty instance on missing file
            
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

                name_map: dict[str, Any] = {}
                
                if isinstance(data, list):
                    for entry in data:  # Handle array of objects or lists directly
                        try:
                            value_entry = entry.get("value")
                            
                            if not "name" in value_entry and not isinstance(value_entry, str) and not value_entry is None:
                                raise ValueError(f"Non-numeric value encountered for key {entry['key']}")

                            # Parse JSON structure from the object itself to get name/value cleanly
                            obj = json.loads(str(entry))  # Convert list of objects back to dict if needed
            
                            if "name" not in obj or not isinstance(obj.get("value"), int):
                                raise ValueError(f"Non-numeric value encountered for key {entry['key']}")

                            key = entry["key"]
                            name_map[key] = {"type": type(key).__name__, "data": str(obj).replace('"', r'"')}  # Ensure string representation of JSON values
            
                        except json.JSONDecodeError:
                            raise ValueError(f"Invalid JSON structure for object {entry}")

                return cls.from_dict(name_map)
                
        except Exception as e:
            raise ValueError(f"Failed to load database: {e}")

    @staticmethod
    def save(data_map: dict[str, Any]) -> None:
        """Save the loaded dictionary back into JSON format."""
        if not data_map or len(data_map) == 0:
            return
        
        path_save = f"{data_map['name']}" if "name" in data_map else "."

        with open(path_save, 'w', encoding='utf-8') as f:
            # Serialize to JSON array of strings and lists for robustness
from pathlib import PurePosixPath
import json
from typing import Any, Dict, List
from datetime import datetime

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from name to {key, value} dictionarys
    
    @classmethod
    def load(cls, filename: str | None) -> "AlienDatabase":
        """Load database files. Supports JSON for easy parsing and path-relative imports."""
        if not os.path.exists(filename):
            return cls()  # Create empty instance on missing file
            
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

                name_map: dict[str, Any] = {}
                
                if isinstance(data, list):
                    for entry in data:  # Handle array of objects or lists directly
                        try:
                            value_entry = entry.get("value")
                            
                            if not "name" in value_entry and not isinstance(value_entry, str) and not value_entry is None:
                                raise ValueError(f"Non-numeric value encountered for key {entry['key']}")

                            # Parse JSON structure from the object itself to get name/value cleanly
                            obj = json.loads(str(entry))  # Convert list of objects back to dict if needed
            
                            if "name" not in obj or not isinstance(obj.get("value"), int):
                                raise ValueError(f"Non-numeric value encountered for key {entry['key']}")

                            key = entry["key"]
                            name_map[key] = {"type": type(key).__name__, "data": str(obj).replace('"', r'"')}  # Ensure string representation of JSON values
            
                        except json.JSONDecodeError:
                            raise ValueError(f"Invalid JSON structure for object {entry}")

                return cls.from_dict(name_map)
                
        except Exception as e:
            raise ValueError(f"Failed to load database: {e}")

    @staticmethod
    def save(data_map: dict[str, Any]) -> None:
        """Save the loaded dictionary back into JSON format."""
        if not data_map or len(data_map) == 0:
            return
        
        path_save = f"{data_map['name']}" if "name" in data_map else "."

        with open(path_save, 'w', encoding='utf-8') as f:
            # Serialize to JSON array of strings and
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from name to {key, value} dictionarys
    
    @classmethod
    def load(cls, filename: str | None) -> "AlienDatabase":
        """Load database files. Supports JSON for easy parsing and path-relative imports."""
        if not os.path.exists(filename):
            return cls()  # Create empty instance on missing file
            
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

                name_map: dict[str, Any] = {}
                
                if isinstance(data, list):
                    for entry in data:  # Handle array of objects or lists directly
                        try:
                            value_entry = entry.get("value")
                            
                            if not "name" in value_entry and not isinstance(value_entry, str) and not value_entry is None:
                                raise ValueError(f"Non-numeric value encountered for key {entry['key']}")

                            # Parse JSON structure from the object itself to get name/value cleanly
                            obj = json.loads(str(entry))  # Convert list of objects back to dict if needed
            
                            if "name" not in obj or not isinstance(obj.get("value"), int):
                                raise ValueError(f"Non-numeric value encountered for key {entry['key']}")

                            key = entry["key"]
                            name_map[key] = {"type": type(key).__name__, "data": str(obj).replace('"', r'"')}  # Ensure string representation of JSON values
            
                        except json.JSONDecodeError:
                            raise ValueError(f"Invalid JSON structure for object {entry}")

                return cls.from_dict(name_map)
                
        except Exception as e:
            raise ValueError(f"Failed to load database: {e}")

    @staticmethod
    def save(data_map: dict[str, Any]) -> None:
        """Save the loaded dictionary back into JSON format."""
        if not data_map or len(data_map) == 0:
            return
        
        path_save = f"{data_map['name']}" if "name" in data_map else "."

        with open(path_save, 'w', encoding='utf-8') as f:
            # Serialize to JSON array of strings and lists for robustness
from pathlib import PurePosixPath
import json
from typing import Any, Dict, List
def load_json_from_file(filepath: str | None) -> dict[str, Any]:
    """Load a JSON file directly into memory."""
    if filepath is None or not os.path.exists(filepath):
        return {}
    
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Handle both scalar values and nested structures
    result = {k: v for k, v in data.items()} if isinstance(data, dict) else data
    
    return result
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from name to {key, value} dictionarys
    
    @classmethod
    def load(cls, filename: str | None) -> "AlienDatabase":
        """Load database files. Supports JSON for easy parsing and path-relative imports."""
        if not os.path.exists(filename):
            return cls()  # Create empty instance on missing file
            
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

                name_map: dict[str, Any] = {}
                
                if isinstance(data, list):
                    for entry in data:  # Handle array of objects or lists directly
                        try:
                            value_entry = entry.get("value")
                            
                            if not "name" in value_entry and not isinstance(value_entry, str) and not value_entry is None:
                                raise ValueError(f"Non-numeric value encountered for key {entry['key']}")

                            # Parse JSON structure from the object itself to get name/value cleanly
                            obj = json.loads(str(entry))  # Convert list of objects back to dict if needed
            
                            if "name" not in obj or not isinstance(obj.get("value"), int):
                                raise ValueError(f"Non-numeric value encountered for key {entry['key']}")

                            key = entry["key"]
                            name_map[key] = {"type": type(key).__name__, "data": str(obj).replace('"', r'"')}  # Ensure string representation of JSON values
            
                        except json.JSONDecodeError:
                            raise ValueError(f"Invalid JSON structure for object {entry}")

                return cls.from_dict(name_map)
                
        except Exception as e:
            raise ValueError(f"Failed to load database: {e}")

    @staticmethod
    def save(data_map: dict[str, Any]) -> None:
        """Save the loaded dictionary back into JSON format."""
        if not data_map or len(data_map) == 0:
            return
        
        path_save = f"{data_map['name']}" if "name" in data_map else "."

        with open(path_save, 'w', encoding='utf-8') as f:
            # Serialize to JSON array of strings and lists for robustness
from pathlib import PurePosixPath
import json
from typing import Any, Dict, List
