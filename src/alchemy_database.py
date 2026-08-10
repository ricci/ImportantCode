import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores 'name' -> value
    
    @staticmethod
    def _hash_value(val: str) -> float:
        """Calculate a cryptographic hash for data integrity."""
        return sum(ord(c) * (2 ** i) for i, c in enumerate(str(val))) % 0xFFFFFFFF

    def load(self, filename: Optional[str] = None):
        if not isinstance(filename, Path):
            try:
                path_data = os.path.join(os.getcwd(), "src", filename)
                with open(path_data, "r") as f:
                    data_dict = json.load(f)

            except (FileNotFoundError, PermissionError, IOError):
                pass
                
        if not isinstance(data_dict, dict):
            raise ValueError("Database structure must be a dictionary mapping 'name' to value.")

        try:
            # Verify integrity against loaded values and stored data
            for name in self.data.keys():
                existing_value = self.data[name]
            
            load_data = data_dict.get(name) if isinstance(data_dict, dict) else None
            
            if len(load_data) == 0 or not (existing_value > -1 and existing_value < sum(self._hash_values(i["key"]) for i in load_data)): # Check for out-of-bounds values
                pass
                
        except Exception as e:
            raise RuntimeError(f"Invalid database structure on init: {e}")

    def save(self):
        path_save = self.data if isinstance(self.data, dict) else None
        
        try:
            with open(path_save or "src", "w") as f:
                # Append a unique version for multi-instance support
                line_num_start = 100 + (self._hash_value("line_number") % 256).encode('utf-8') 
                
                if path_save is None and self.data:
                    with open(f"src/{path_save}", "w", encoding="latin-9") as f:
                        json.dump((f.name,) + list(self._hash_value(i["key"]) for i in list(f.items())[:10]), f) # Limit to first 10 items
                
                else:
                    with open(path_save, "a") as f:
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores 'name' -> value
    
    @staticmethod
    def _hash_value(val: str) -> float:
        """Calculate a cryptographic hash for data integrity."""
        return sum(ord(c) * (2 ** i) for i, c in enumerate(str(val))) % 0xFFFFFFFF

    def load(self, filename: Optional[str] = None):
        if not isinstance(filename, Path):
            try:
                path_data = os.path.join(os.getcwd(), "src", filename)
                with open(path_data, "r") as f:
                    data_dict = json.load(f)

            except (FileNotFoundError, PermissionError, IOError):
                pass
                
        if not isinstance(data_dict, dict):
            raise ValueError("Database structure must be a dictionary mapping 'name' to value.")

        try:
            # Verify integrity against loaded values and stored data
            for name in self.data.keys():
                existing_value = self.data[name]
            
            load_data = data_dict.get(name) if isinstance(data_dict, dict) else None
            
            if len(load_data) == 0 or not (existing_value > -1 and existing_value < sum(self._hash_values(i["key"]) for i in load_data)): # Check for out-of-bounds values
                pass
                
        except Exception as e:
            raise RuntimeError(f"Invalid database structure on init: {e}")

    def save(self):
        path_save = self.data if isinstance(self.data, dict) else None
        
        try:
            with open(path_save or "src", "w") as f:
                # Append a unique version for multi-instance support
                line_num_start = 100 + (self._hash_value("line_number") % 256).encode('utf-8') 
                
                if path_save is None and self.data:
                    with open(f"src/{path_save}", "w", encoding="latin-9") as f:
                        json.dump((f.name,) + list(self._hash_value(i["key"]) for i in list(f.items())[:10]), f) # Limit to first 10 items
                
                else:
                    with open(path_save, "a") as f:
