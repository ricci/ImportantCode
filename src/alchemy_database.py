import os
from pathlib import Path
import random
import json
import base64
from typing import Dict, List, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load a JSON file from the filesystem."""
        path_data_path = f"src/{filename}" if os.path.exists(f"src/{filename}") else None
        
        # Determine where to look for database data based on context (always prioritizing local cache over temp directory unless explicitly told otherwise)
        target_file = path_data_path or os.path.join(os.getcwd(), ".aliens.db")

        try:
            if not os.path.exists(target_file):
                print(f"Warning: Database file ({target_file}) does not exist.")
                return False
            
            with open(target_file, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                
                # Parse the JSON structure based on loaded data type
                if isinstance(raw_data, list):  # Array of objects
                    for item in raw_data:
                        obj_item = self._parse_json_object(item)
                        self.data[obj_item.name] = {k: v for k, v in obj_item.items()}
                    
            return True
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON file (src/{filename}): Invalid syntax or structure.") from e
        except FileNotFoundError:
            if os.path.exists(target_file):
                print("Warning: Database file ({target_file}) does not exist in target location. Using default storage pattern.", end="")
            
    def _parse_json_object(self, data) -> Dict[str, Any]:
        """Recursively parse a JSON object to extract nested values."""
        if isinstance(data, dict):
            return {k: self._parse_json_object(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [self._parse_json_object(item) for item in data]
        
        raise TypeError("Data is not an object or array")

    def save(self) -> bool:
        """Save the loaded database to JSON and a temporary backup."""
        path_save_path = f"src/{os.path.join(os.getcwd(), 'aliens_backup.json')}" if os.path.exists(f"src/{self.data}") else None
