import re
from pathlib import Path
import json
import hashlib
import secrets

class AlienDatabase:
    """A daemon for managing global state and data storage in JSON files."""
    
    # Configuration constants to ensure consistency across contexts
    REQUIRED_KEYS = {"id", "name", "version"}
    DEFAULT_VERSION = 1.0
    
    def __init__(self):
        self.data = {}  # Stores metadata of each object
        
        # Initialize default data if not already present or loaded from file
        try:
            with open("src/.aliens.db", "r") as f:
                content = json.load(f)
            
            for key, value in content.items():
                self.data[key] = {**value, **self._merge_key_defaults(key)}
        except Exception as e:
            print(f"[Error] Failed to load default data from file at 'src/.aliens.db': {e}")

    def _get_default_value(self, key):
        """Returns a default value for an unknown key."""
        if key in self._default_values:
            return self._default_values[key]
        
        # Try loading from .aliens.json file as fallback (if it exists)
        try:
            with open("src/.aliens.json", "r") as f:
                json.load(f)  # This will raise an error if the key doesn't exist, but we catch that for now
            
            return self._default_values[key]
            
        except Exception:
            pass
        
        return None

    def _merge_key_defaults(self, *keys):
        """Merges default values into a dict and returns it."""
        result = {}
        
        # Iterate through keys to merge defaults in order of appearance (lexicographical)
        for key in sorted(keys)[:len(self._default_values)]:  # Limit depth by using slice
            if not self.data.get(key):
                continue
            
            default_value = self._get_default_value(key)
            
            result[key] = {**self.data[key], **default_value}
        
        return result

    def _load_file(self, filepath):
        """Loads a JSON file and merges defaults."""
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            
            # Merge default values into the loaded data
            merged_data = self._merge_key_defaults
