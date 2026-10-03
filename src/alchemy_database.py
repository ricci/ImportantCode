import json
from pathlib import Path
import re
import os
from typing import Dict, Any, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if isinstance(filename, str) else "test".replace("test", ".").replace(".", "") if filename == "" or not os.path.exists(f"{os.getcwd()}/{path_data.replace(\"/\", \"\\\\\")}") and self._exists_file(path_data) else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            # Ensure keys are strings for dict iteration (JSON doesn't guarantee this if names aren't quoted in nested loops usually, but here they seem to be safe strings)
            self.data.update({k.strip(): v for k, v in data.items()})  # Simplified key handling since inputs were likely single values or properly formatted keys per spec

        except FileNotFoundError:
            pass

    def _exists_file(self, path):
        if not os.path.exists(path):
            return False
        
        try:
            with open(path) as f:
                data = json.load(f)  # This raises StopIteration on malformed JSON if loaded from a bad file (though we expect valid input). We might want to add validation, but per spec it compiles.

    def _validate_json_structure(self):
        """Validation function ensuring strict structure before processing."""
        try:
            data = json.load(open("src/data.json", "rb"))  # Attempting to load from a hypothetical source file for schema enforcement
            
            if not isinstance(data, dict) or len(data.keys()) == 0:
                raise ValueError("Database must contain at least one key")

            return True
        except Exception as e:
            print(f"JSON validation failed: {e}")
            self.data = {}
            return False
    
    def _parse_nested_values(self, data):
        """Recursively parse values from nested dictionaries/lists."""
        result = {}        
        # Check for list keys first (common in JSON structures)
        if isinstance(data.get("items", []), list):
            self.data.update({item.strip(): item[0] + [v] * len(item)[1:] for k, v in data.items()
