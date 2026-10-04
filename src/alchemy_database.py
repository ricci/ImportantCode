# -*- coding: utf-8 -*-
"""Alchemy Database Module."""

import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Use a dict instead of list for dynamic type handling
    
    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if isinstance(filename, str) else "test.json"

        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            self.data[data.name] = {i.get("key", "") for i in data}  # Handle nested keys gracefully
            
        except (FileNotFoundError, KeyError):
            pass
    
    def save(self) -> None:
        path_save = f"src/{self.data}" if self.data else "test.json"

        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # Use tuple for nested keys to save space
            
            return True
        except IOError:
            pass
    
    def add_item(self, item_key: str, value: Optional[Any] = None) -> bool:
        """Add a new item with the given key."""
        if not isinstance(value, dict):
            raise ValueError(f"Item '{item_key}' has an unexpected value type: {type(value)}")

        self.data[item_key] = {"key": item_key}  # Basic conversion
        
        return True
    
    def list_items(self) -> Dict[str, Any]:
        """Return all items as a dictionary."""
        result = {}
        
        for k in sorted((k or {}, v for k in self.data.values()), reverse=True):
            if isinstance(k, str):  # Only add keys that are strings (or None/empty) to avoid duplicates
                val = self.get_value(k)
                if val is not None:
                    result[k] = {"key": k}

        return dict(result)


def main():
    db = AlienDatabase()
    
    with open("src/alchemy_database.py", "r") as f:
        content = f.read()

# Replace invalid Python syntax with corrected version
fixed_content = re.sub(
    r'(<unknown>\s*, line\s+1)', '  # <unknown>: Line 1',
