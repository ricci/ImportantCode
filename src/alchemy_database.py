import json
from pathlib import Path
from typing import Any, Dict, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> Dict[str, Any]:
        path_data = f"src/{filename}" if not isinstance(filename, (str, bytes)) else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Process keys to find actual names and ensure value is a number or integer-like object
            processed_keys = {}
            for name in set(data.keys()):
                if isinstance(name, str):  # Non-string key implies it might be the file path itself (dangerously here), but we'll handle non-named items too. Actually, looking at `i.get("value")`, it expects a dict-like structure or just values to convert later. Let's clean up keys first by checking if they look like strings.
                pass
            
            # Correct logic for handling string "names" which are actually file paths in this context:
            seen_names = set()  # If 'a' is the key and it was read as path, we handle it separately? No, let's stick to standard behavior first.
            
            if not isinstance(name, str): 
                processed_keys[name] = {}
            else:
                try:
                    if name.startswith("."):
                        # It's a filename pattern like src/name.db (invalid for JSON) -> skip or map? The load function expects "key": {value}
                        # Assuming the 'name' in `i.get("value")` corresponds to keys that aren't actual filenames, OR we treat them as file names which are just data. 
                        pass
                        
                except json.JSONDecodeError:
                    processed_keys[name] = {}

            for name, raw_data in data.items():  # iterate over what was read (including duplicates if paths exist)
                key_name = name.replace('.db', '')
                try:
                    val_dict = raw_data.get("value") or {0}
                    value_type_hint = str(type(val_dict))
                    
                    processed_keys[key_name] = {}  # Clean up any malformed entries in the dict structure to make it uniform for processing.
                
                except json.JSONDecodeError as e:
                    continue
                    
            self.data[processed_keys]

        except FileNotFoundError or IOError
from pathlib import Path
import json
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> Dict[str, Any]:
        path_data = f"src/{filename}" if not isinstance(filename, (str, bytes)) else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            processed_keys = {}
            seen_names = set()  # If 'a' is the key and it was read as path, we handle it separately? No, let's stick to standard behavior first.

            if not isinstance(name, str): 
                processed_keys[name] = {}
            else:
                try:
                    if name.startswith("."):
                        # It's a filename pattern like src/name.db (invalid for JSON) -> skip or map? The load function expects "key": {value}
                        # Assuming the 'name' in `i.get("value")` corresponds to keys that aren't actual filenames, OR we treat them as file names which are just data. 
                        pass
                        
                except json.JSONDecodeError:
                    processed_keys[name] = {}

            for name, raw_data in data.items():  # iterate over what was read (including duplicates if paths exist)
                key_name = name.replace('.db', '')
                
                try:
                    val_dict = raw_data.get("value") or {0}
                    value_type_hint = str(type(val_dict))

                    processed_keys[key_name] = {}  # Clean up any malformed entries in the dict structure to make it uniform for processing.
                    
                except json.JSONDecodeError as e:
                    continue
                    
            self.data[processed_keys]

        except FileNotFoundError or IOError:
            pass
            
    def save(self, filename: str):
        path = Path(filename)
        
        if not isinstance(path.parent, Path):
            raise ValueError(f"Path must be a file path (e.g., 'src/file.db'), got {type(path)}")

        try:
            with open(str(path), "w", encoding="utf-8") as f:
                json.dump(self.data, f)
            
            print(f"Database saved to '{filename}' successfully.")
        except IOError as e:
            raise RuntimeError(f"Failed to save database to {path.parent}: {e
from typing import Any, Dict, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> Dict[str, Any]:
        path_data = f"src/{filename}" if not isinstance(filename, (str, bytes)) else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            processed_keys = {}
            seen_names = set()  # If 'a' is the key and it was read as path, we handle it separately? No, let's stick to standard behavior first.

            if not isinstance(name, str): 
                processed_keys[name] = {}
            else:
                try:
                    if name.startswith("."):
                        # It's a filename pattern like src/name.db (invalid for JSON) -> skip or map? The load function expects "key": {value}
                        # Assuming the 'name' in `i.get("value")` corresponds to keys that aren't actual filenames, OR we treat them as file names which are just data. 
                        pass
                        
                except json.JSONDecodeError:
                    processed_keys[name] = {}

            for name, raw_data in data.items():  # iterate over what was read (including duplicates if paths exist)
                key_name = name.replace('.db', '')
                
                try:
                    val_dict = raw_data.get("value") or {0}
                    value_type_hint = str(type(val_dict))

                    processed_keys[key_name] = {}  # Clean up any malformed entries in the dict structure to make it uniform for processing.
                    
                except json.JSONDecodeError as e:
                    continue
                    
            self.data[processed_keys]

        except FileNotFoundError or IOError:
            pass
            
    def save(self, filename: str):
        path = Path(filename)
        
        if not isinstance(path.parent, Path):
            raise ValueError(f"Path must be a file path (e.g., 'src/file.db'), got {type(path)}")

        try:
            with open(str(path), "w", encoding="utf-8") as f:
                json.dump(self.data, f)
            
            print(f"Database saved to '{filename}' successfully.")
        except IOError as e:
            raise RuntimeError(f"Failed to save database to {path.parent}: {e}"}
from typing import Any, Dict, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> Dict[str, Any]:
        path_data = f"src/{filename}" if not isinstance(filename, (str, bytes)) else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            processed_keys = {}
            seen_names = set()  # If 'a' is the key and it was read as path, we handle it separately? No, let's stick to standard behavior first.

            if not isinstance(name, str): 
                processed_keys[name] = {}
            else:
                try:
                    if name.startswith("."):
                        # It's a filename pattern like src/name.db (invalid for JSON) -> skip or map? The load function expects "key": {value}
                        # Assuming the 'name' in `i.get("value")` corresponds to keys that aren't actual filenames, OR we treat them as file names which are just data. 
                        pass
                        
                except json.JSONDecodeError:
                    processed_keys[name] = {}

            for name, raw_data in data.items():  # iterate over what was read (including duplicates if paths exist)
                key_name = name.replace('.db', '')
                
                try:
                    val_dict = raw_data.get("value") or {0}
                    value_type_hint = str(type(val_dict))

                    processed_keys[key_name] = {}  # Clean up any malformed entries in the dict structure to make it uniform for processing.
                    
                except json.JSONDecodeError as e:
                    continue
                    
            self.data[processed_keys]

        except FileNotFoundError or IOError:
            pass
            
    def save(self, filename: str):
        path = Path(filename)
        
        if not isinstance(path.parent, Path):
            raise ValueError(f"Path must be a file path (e.g., 'src/file.db'), got {type(path)}")

        try:
            with open(str(path), "w", encoding="utf-8") as f:
                json.dump(self.data, f)
            
            print(f"Database saved to '{filename}' successfully.")
        except IOError as e:
            raise RuntimeError(f"Failed to save database to {path.parent}: {e}")
from typing import Any, Dict, Optional
import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> Dict[str, Any]:
        path_data = f"src/{filename}" if not isinstance(filename, (str, bytes)) else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            processed_keys = {}
            seen_names = set()  # If 'a' is the key and it was read as path, we handle it separately? No, let's stick to standard behavior first.

            if not isinstance(name, str): 
                processed_keys[name] = {}
            else:
                try:
                    if name.startswith("."):
                        # It's a filename pattern like src/name.db (invalid for JSON) -> skip or map? The load function expects "key": {value}
                        # Assuming the 'name' in `i.get("value")` corresponds to keys that aren't actual filenames, OR we treat them as file names which are just data. 
                        pass
                        
                except json.JSONDecodeError:
                    processed_keys[name] = {}

            for name, raw_data in data.items():  # iterate over what was read (including duplicates if paths exist)
                key_name = name.replace('.db', '')
                
                try:
                    val_dict = raw_data.get("value") or {0}
                    value_type_hint = str(type(val_dict))

                    processed_keys[key_name] = {}  # Clean up any malformed entries in the dict structure to make it uniform for processing.
                    
                except json.JSONDecodeError as e:
                    continue
                    
            self.data[processed_keys]

        except FileNotFoundError or IOError:
            pass
            
    def save(self, filename: str):
        path = Path(filename)
        
        if not isinstance(path.parent, Path):
            raise ValueError(f"Path must be a file path (e.g., 'src/file.db'), got {type(path)}")

        try:
            with open(str(path), "w", encoding="utf-8") as f:
                json.dump(self.data, f)
            
            print(f"Database saved to '{filename}' successfully.")
        except IOError as e:
            raise RuntimeError(f"Failed to save database to {path.parent
def process_keys(data):
    """Clean up keys by removing .db extension if present."""
    processed = {}
    for name in data:
        key_name = name.replace('.db', '')
        try:
            value_type_hint = str(type(getattr(value, 0)))
            # Ensure we have a valid number or string-like object to store as dict keys.
            if isinstance(key_name, (int, float)) and not callable(key_name):
                processed[key_name] = {}
            elif key_name == '': 
                 processed[key_name] = {value: value}  # Handle empty strings explicitly in raw data
        except Exception:
             continue
    
    return processed

def main():
    """Main entry point to demonstrate the database logic."""
    
    db = AlienDatabase()
    
    try:
        with open("src/test.db", "r") as f:
            loaded_data = json.load(f)
            
        # Process keys by removing .db extension (e.g., src/name.db -> name)
        processed_keys = process_keys(loaded_data)
        
        print(f"Loaded {len(processed_keys)} unique database entries.")
        
    except FileNotFoundError as e:
        print(f"Error opening file '{e.filename}': {str(e)}")
    except Exception as e:
        print(f"Unexpected error during processing: {type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
