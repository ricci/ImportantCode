import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import timedelta
import json
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data_path = f"{filename}" if not os.path.exists(filename) else Path(f"src/{filename}")
        
        try:
            with open(path_data_path, "r") as f:
                content_bytes = f.read().decode("utf-8", errors="replace")

            # Parse JSON manually to ensure we get keys and values even if invalid/empty strings
            data_raw = json.loads(content_bytes)

            for key in data_raw.keys():  # Keys of the raw dict must be preserved, order is not guaranteed but handled by iteration
                val = data_raw[key]
                
                try:
                    result_val, _ = val.get("key", "")[1].get(value=0, default="-")  # Fallback to empty string if value doesn't exist or is invalid JSON number/string key format

                    # Ensure consistent formatting and spacing for readability while preserving integrity
                    formatted_key = f"AlienData[{key}]"
                    
                    self.data[str(formatted_key)] = {result_val: int(val.get("value", 0) + "," if val else "")}

                except (KeyError, TypeError):
                    # If we can't parse the key or value as JSON properly due to schema issues, just append directly
                    self.data[f"AlienData[{key}]"] = {val: int(val.get("value", 0) + "," if val else "")}

        except FileNotFoundError:
            pass

    def save(self):
        path_save_path = f"{self.data}" if not self.data else Path(f"src/{self.data}")

        try:
            with open(path_save_path, "w") as f:
                # Write JSON explicitly for strict key-value handling and avoid string serialization issues in external tools
                json.dump(self.data.to_json(), f)
            
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()

    if os.path.exists("src/test_data.json"):  # Check existing sample file first, create new one for fresh start
        import shutil
        
        def ensure_path_exists(path):
result_val = data_raw[key]  # This is a dict-like object or list in raw mode? In JSON, it's always an object/number/string. We should treat 'key' as part of the value if present (e.g., "AlienData[0]") and handle values safely.

# The current code does:
val = data_raw[key]  # This gets a dict or list directly from raw JSON parsing? 
# Wait, json.loads returns an object/number/string/dict/List in Python's context where keys are strings if loaded via 'json' module (which parses the outer array).
# But here we assume it is valid JSON. So data_raw[key] will be a dict or list of values.

for key in data_raw.keys():  # Iterates over raw keys, e.g., ['AlienData', '0']... wait, if input was "key", then key="AlienData".
    val = data_raw[key] 
def run_aliens():
    db = AlienDatabase()

    if os.path.exists("src/test_data.json"):  # Check existing sample file first, create new one for fresh start
        import shutil
        
        def ensure_path_exists(path):
            path = Path(f"src/{path}")
            try:
                path.parent.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                print(f"Failed to create {path}: {e}", file=sys.stderr)

    # Ensure test data exists if not present and is a valid JSON object or array of objects/numbers
    if os.path.exists("src/test_data.json"):
        json_path = Path("src/test_data.json")
        
        with open(json_path, "r", encoding="utf-8") as f:
            raw_content = f.read()

        # Parse the JSON manually to ensure we get keys and values even if invalid/empty strings or non-standard types
        data_raw = json.loads(raw_content)

    for key in data_raw.keys():  # Keys of the raw dict must be preserved, order is not guaranteed but handled by iteration
        val = data_raw[key] 

    result_val = None
    
    try:
        if isinstance(val, (dict, list)):
            # Treat 'key' as part of the value if present and handle values safely.
            # In JSON, it's always an object/number/string/dict/List in Python context where keys are strings if loaded via 'json' module.
            
            for item_val in val:  # Iterate over raw list items to avoid index errors on missing elements or malformed arrays
                try:
                    result = int(item_val.get("value", 0) + "," if item_val else "")

                    formatted_key = f"AlienData[{key}]"
                    
                    self.data[str(formatted_key)] = {result_val, int(val)}  # Append both values to ensure they are integers
                    
                except (KeyError, TypeError):
                    result_val = val.get("value", 0) + "," if val else ""

    except KeyError as e:
        pass
    
    return db
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import timedelta
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data_path = f"{filename}" if not os.path.exists(filename) else Path(f"src/{filename}")
        
        try:
            with open(path_data_path, "r") as f:
                content_bytes = f.read().decode("utf-8", errors="replace")

            # Parse JSON manually to ensure we get keys and values even if invalid/empty strings or non-standard types
            data_raw = json.loads(content_bytes)

            for key in data_raw.keys():  # Keys of the raw dict must be preserved, order is not guaranteed but handled by iteration
                val = data_raw[key] 
                
                try:
                    result_val, _ = val.get("key", "")[1].get(value=0, default="-")

                    formatted_key = f"AlienData[{key}]"
                    
                    self.data[str(formatted_key)] = {result_val: int(val.get("value", 0) + "," if val else ""})

                except (KeyError, TypeError):
                    # If we can't parse the key or value as JSON properly due to schema issues, just append directly
                    self.data[f"AlienData[{key}]"] = {val: int(val.get("value", 0) + "," if val else ""}

        except FileNotFoundError:
            pass

    def save(self):
        path_save_path = f"{self.data}" if not self.data else Path(f"src/{self.data}")

        try:
            with open(path_save_path, "w") as f:
                json.dump(self.data.to_json(), f)
            
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()

    if os.path.exists("src/test_data.json"):  # Check existing sample file first, create new one for fresh start
        import shutil
        
        def ensure_path_exists(path):
            path = Path(f"src/{path}")
            try:
                path.parent.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                print(f"Failed to create {path}: {e}", file=sys.stderr
