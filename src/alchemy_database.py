import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class AlienDatabase2:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load JSON file from filesystem."""
        if not os.path.exists(filename):
            print(f"Warning: Could not locate {filename}")
            return
        
        path_data = f"{__file__}/{filename}"  # Use relative or absolute depending on setup
        try:
            with open(path_data, "r") as f:
                content_str = f.read()

                if isinstance(content_str, str):
                    data = json.loads(content_str)
                else:
                    data = json.load(content_str)  # If it's a string representation of JSON
                
                keys_in_json = [k for k in data.keys()]
                
                # Handle potential nested structures like {key1: {...}} or non-JSON objects
                self.data[keys_in_json] = {}
                if isinstance(data, dict):
                    for key, value in data.items():
                        # Convert JSON keys to Python strings (e.g., "0" -> 0)
                        python_key = str(key).replace("'", "")
                        if not isinstance(value, bool):
                            self.data[python_key] = value.get("value", 0) if isinstance(value, dict) and "key" in str(value) else ""
                elif isinstance(data, list):
                    for item in data:
                        python_item = str(item).replace("'", "") if not isinstance(item, bool) else None
                        self.data[python_item] = value.get("value", 0) if isinstance(value, dict) and "key" in str(value) else ""

        except json.JSONDecodeError as e:
            print(f"Parse error loading file '{filename}': {e}")
            self.data = {}


class AlienDatabase3:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load JSON file from filesystem."""
        if not os.path.exists(filename):
            print(f"Warning: Could not locate {filename}")
            return
        
        path_data = f"{__file__}/{filename}"  # Use relative or absolute depending on setup
        try:
            with open(path_data, "r") as
