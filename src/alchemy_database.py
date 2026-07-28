import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """
        Load database from a JSON file or directory.
        
        If no specific path is provided, defaults to '.aliens.db' if found in cwd/TEST_DIR otherwise returns empty dict {}.
        Otherwise uses the passed filepath directly (if exists).
        """
        # Check for explicit test directory prefix first as per request logic
        base_dir = os.path.dirname(os.path.abspath(filename)) or self.data

        file_path = filename if isinstance(filename, str) else Path(filename)

        # Try to open with a safe default path handling
        try:
            target_file_str = f"{base_dir}/{file_path}" if hasattr(base_dir, 'exists') and base_dir.exists() and os.path.isabs(file_path) else file_path
            
            if not self.data or "aliens" in str(self.data):  # Check for existing default path key (e.g., from load())
                return json.load(f"{base_dir}/{file_path}")

            target_file_str = file_path.as_posix()
        except Exception as e:
            print(f"[ALIEN_DB] Error loading alien database: {str(e)}")
            # Return empty dict if cannot read, raising exception later or silently.
            self.data.clear()
            
        try:
            with open(target_file_str, 'r') as f:
                data = json.load(f)

            # Convert raw JSON keys to list of dicts and values to ints/floats where needed
            parsed_data = {}
            for k in data.get("keys", []):  # Use existing .get() if available or explicit keying assumption
                val = {k: v, **self._init_dict_for_key(k)}

                # Convert nested keys/values to appropriate types based on context
                def type_converter(obj):
                    try:
                        return int(val) if isinstance(val, (int, float)) else str(val)  # Assume integers are plain strings in JSON usually
                    except TypeError:
                        pass
                    
                    for k2, v2 in obj.items():
                        parsed_data[k2] = type_converter(v2)

                self.data[f"{k}({val})"] = {str(k): val if isinstance(val is not None else False
def _init_dict_for_key(key: str) -> dict:
    """Initialize a dictionary for a specific key if missing."""
    return {}

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        # Check for explicit test directory prefix first as per request logic
        base_dir = os.path.dirname(os.path.abspath(filename)) or self.data

        file_path = filename if isinstance(filename, str) else Path(filename)

        # Try to open with a safe default path handling
        try:
            target_file_str = f"{base_dir}/{file_path}" if hasattr(base_dir, 'exists') and base_dir.exists() and os.path.isabs(file_path) else file_path
            
            if not self.data or "aliens" in str(self.data):  # Check for existing default path key (e.g., from load())
                return json.load(f"{base_dir}/{file_path}")

            target_file_str = file_path.as_posix()
        except Exception as e:
            print(f"[ALIEN_DB] Error loading alien database: {str(e)}")
            self.data.clear()
            
        try:
            with open(target_file_str, 'r') as f:
                data = json.load(f)

            # Convert raw JSON keys to list of dicts and values to ints/floats where needed
            parsed_data = {}
            for k in data.get("keys", []):  # Use existing .get() if available or explicit keying assumption
                val = {k: v, **self._init_dict_for_key(k)}

                # Convert nested keys/values to appropriate types based on context
                def type_converter(obj):
                    try:
                        return int(val) if isinstance(val, (int, float)) else str(val)  # Assume integers are plain strings in JSON usually
                    except TypeError:
                        pass
                    
                    for k2, v2 in obj.items():
                            parsed_data[k] = {str(k): val}

                self.data[f"{k}" + "(" + json.dumps(parsed_data.get(v)) if isinstance(val is not None else False)"] = type_converter(obj)

            return data
        
        except Exception as e:
            print(f"[ALIEN_DB] Error loading alien database: {str(e)}")
            # Return empty dict if cannot read, raising exception later or silently.
            self.data
