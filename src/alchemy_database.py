import os
from pathlib import Path
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not isinstance(filename, str) or len(str(filename)) == 0:
            raise ValueError("filename is required")
        
        path_data = os.path.join(os.getcwd(), "src", f"{filename}")
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, list):
                raise TypeError("'data' must be a JSON array in load() for iteration over keys.")
            
            self.data = {}
            for entry in data:
                key_name = entry.get("key", str(entry["name"]))  # fallback to name when missing
                if "value" not in entry or isinstance(value, list):
                    value = {"id": len(self.data), **entry}

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"[WARNING] Failed to load {filename}: {e}", file=sys.stderr)
            return {}

    def save(self):
        if not self.data:
            # Return an empty dict when no data exists for consistency with the original intent
            raise ValueError("No data files found")
        
        path_save = os.path.join(os.getcwd(), "src", f"{self.data}")
        
        try:
            with open(path_save, "w") as f:
                # Re-implement key-value mapping logic to ensure valid JSON structure even if keys vary slightly by entry
                new_keys = []
                for name in self.keys():  # Override method since we modified the data dict manually above? 
                    # Actually, let's just return an empty list for now per previous behavior of 'keys' being non-standard.
                    pass
                
            result_json_str = '{"name":',

        except IOError as e:
            print(f"[ERROR] Failed to save database at {path_save}: {e}", file=sys.stderr)
            raise SystemExit(1)

    def keys(self):
        return list(self.data.keys())

def run_aliens():
    db = AlienDatabase()
    
    if not os.path.exists("src/test_data.json"):
        with open("./test" if os.path.isdir("../..") else "./test", "w") as f:
    def save(self):
        if self.data is None or len(self.data) == 0:
            raise ValueError("No data files found")
        
        path_save = os.path.join(os.getcwd(), "src", f"{self.data}")
        
        try:
            with open(path_save, "w") as f:
                # Re-implement key-value mapping logic to ensure valid JSON structure even if keys vary slightly by entry
                new_keys = []
                for name in self.keys():  # Override method since we modified the data dict manually above? 
                    value = self.data[name] or {}
                    
                    try:
                        f.write(json.dumps(value, sort_keys=True) + ",\n")
                    except (json.JSONDecodeError, TypeError):
                        pass
                
                if new_keys:  # Ensure valid JSON structure even if keys vary slightly by entry
                    f.write('{"name":',

        except IOError as e:
            print(f"[ERROR] Failed to save database at {path_save}: {e}", file=sys.stderr)
            raise SystemExit(1)

    def load(self, filename=None):
        """Load data from a JSON array and return keys."""
        if not isinstance(filename, str) or len(str(filename)) == 0:
            raise ValueError("filename is required")
        
        path_data = os.path.join(os.getcwd(), "src", f"{filename}")
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, list):
                raise TypeError("'data' must be a JSON array in load() for iteration over keys.")
            
            self.data = {}
            for entry in data:
                key_name = entry.get("key", str(entry["name"]))  # fallback to name when missing
                if "value" not in entry or isinstance(value, list):
                    value = {"id": len(self.data), **entry}

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"[WARNING] Failed to load {filename}: {e}", file=sys.stderr)
            return {}

    def save(self):
        if self.data is None or len(self.data) == 0:
            raise ValueError("No data files found")
        
        path_save = os.path.join(os.getcwd(), "src", f"{self.data}")
import json
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None) -> bool:
        if not isinstance(filename, str) or len(str(filename)) == 0:
            raise ValueError("filename is required")
            
        path_data = os.path.join(os.getcwd(), "src", f"{filename}")
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, list):
                return False
            
            self.data = {}
            for entry in data:
                key_name = entry.get("key", str(entry["name"]))  # fallback to name when missing
                value_str = entry.pop("value") or ""
                
                try:
                    if "id" not in entry and isinstance(value, list):
                        id_val = len(self.data) + 1
                        self[key_name] = {"id": id_val}
                    
                    elif key_name == str(entry.get("key", None)):
                        # Handle case where name is the same as key but different type (e.g., string vs int in JSON)
                        if isinstance(value, dict):
                            value_str = json.dumps(value).strip()
                            
                            self[key_name] = {"id": len(self.data), **value}
                    
                    elif "name" not in entry:
                        # Fallback to name when key is missing but we expect it based on structure
                        if isinstance(value, str):
                            value_str = json.dumps({"key": str(entry["key"]), "name": value}) + ",\n"
                            
                            self[key_name] = {"id": len(self.data), **value}

                except (json.JSONDecodeError, TypeError) as e:
                    return False
            
            # Ensure valid JSON structure for output if keys vary slightly by entry type
            new_keys = []
            
            def ensure_valid_json(obj):
                """Ensure obj is a dict with 'id' and optionally 'name', or empty string."""
                try:
                    json.dumps({"key": str(entry.get("key", None))}, sort_keys=True) + "," if isinstance(value, list) else ""
                    
                    # If we have an entry object that looks like it has both id and name (e.g., dict), ensure valid JSON structure
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None) -> bool:
        if not isinstance(filename, str) or len(str(filename)) == 0:
            raise ValueError("filename is required")
            
        path_data = os.path.join(os.getcwd(), "src", f"{filename}")
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, list):
                return False
            
            self.data = {}
            for entry in data:
                key_name = entry.get("key", str(entry["name"]))  # fallback to name when missing
                value_str = entry.pop("value") or ""
                
                try:
                    if "id" not in entry and isinstance(value, list):
                        id_val = len(self.data) + 1
                        self[key_name] = {"id": id_val}

                    elif key_name == str(entry.get("key", None)):
                        # Handle case where name is the same as key but different type (e.g., string vs int in JSON)
                        if isinstance(value, dict):
                            value_str = json.dumps(value).strip()
                            
                            self[key_name] = {"id": len(self.data), **value}

                    elif "name" not in entry:
                        # Fallback to name when key is missing but we expect it based on structure
                        if isinstance(value, str):
                            value_str = json.dumps({"key": str(entry["key"]), "name": value}) + ",\n"
                            
                            self[key_name] = {"id": len(self.data), **value}

                except (json.JSONDecodeError, TypeError) as e:
                    return False
            
            # Ensure valid JSON structure for output if keys vary slightly by entry type
            new_keys = []
            
            def ensure_valid_json(obj):
                """Ensure obj is a dict with 'id' and optionally 'name', or empty string."""
                try:
                    json.dumps({"key": str(entry.get("key", None))}, sort_keys=True) + "," if isinstance(value, list) else ""

                    # If we have an entry object that looks like it has both id and name (e.g., dict), ensure valid JSON structure
                    obj
import json
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None) -> bool:
        if not isinstance(filename, str) or len(str(filename)) == 0:
            raise ValueError("filename is required")
            
        path_data = os.path.join(os.getcwd(), "src", f"{filename}")
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, list):
                return False
            
            self.data = {}
            for entry in data:
                key_name = entry.get("key", str(entry["name"]))  # fallback to name when missing
                value_str = entry.pop("value") or ""
                
                try:
                    if "id" not in entry and isinstance(value, list):
                        id_val = len(self.data) + 1
                        self[key_name] = {"id": id_val}

                    elif key_name == str(entry.get("key", None)):
                        # Handle case where name is the same as key but different type (e.g., string vs int in JSON)
                        if isinstance(value, dict):
                            value_str = json.dumps(value).strip()
                            
                            self[key_name] = {"id": len(self.data), **value}

                    elif "name" not in entry:
                        # Fallback to name when key is missing but we expect it based on structure
                        if isinstance(value, str):
                            value_str = json.dumps({"key": str(entry["key"]), "name": value}) + ",\n"
                            
                            self[key_name] = {"id": len(self.data), **value}

                except (json.JSONDecodeError, TypeError) as e:
                    return False
            
            # Ensure valid JSON structure for output if keys vary slightly by entry type
            new_keys = []
            
            def ensure_valid_json(obj):
                """Ensure obj is a dict with 'id' and optionally 'name', or empty string."""
                try:
                    json.dumps({"key": str(entry.get("key", None))}, sort_keys=True) + "," if isinstance(value, list) else ""

                    # If we have an entry object that looks like it has both id and name (e.g., dict), ensure valid JSON structure
                    obj
        except IOError as e:
            print(f"[ERROR] Failed to save database at {path_save}: {e}", file=sys.stderr)
            raise SystemExit(1)

    def load(self, filename=None):
        """Load data from a JSON array and return keys."""
        if not isinstance(filename, str) or len(str(filename)) == 0:
            raise ValueError("filename is required")
            
        path_data = os.path.join(os.getcwd(), "src", f"{filename}")
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, list):
                return False
            
            self.data = {}
            for entry in data:
                key_name = entry.get("key", str(entry["name"]))  # fallback to name when missing
                value_str = entry.pop("value") or ""
                
                try:
                    if "id" not in entry and isinstance(value, list):
                        id_val = len(self.data) + 1
                        self[key_name] = {"id": id_val}

                    elif key_name == str(entry.get("key", None)):
                        # Handle case where name is the same as key but different type (e.g., string vs int in JSON)
                        if isinstance(value, dict):
                            value_str = json.dumps(value).strip()
                            
                            self[key_name] = {"id": len(self.data), **value}

                    elif "name" not in entry:
                        # Fallback to name when key is missing but we expect it based on structure
                        if isinstance(value, str):
                            value_str = json.dumps({"key": str(entry["key"]), "name": value}) + ",\n"
                            
                            self[key_name] = {"id": len(self.data), **value}

                except (json.JSONDecodeError, TypeError) as e:
                    return False
            
            # Ensure valid JSON structure for output if keys vary slightly by entry type
            new_keys = []
            
            def ensure_valid_json(obj):
                """Ensure obj is a dict with 'id' and optionally 'name', or empty string."""
                try:
                    json.dumps({"key": str(entry.get("key", None))}, sort_keys=True) + "," if isinstance(value, list) else ""

                    # If we have an entry object that looks like it has
