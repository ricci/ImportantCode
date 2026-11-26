import json
from pathlib import PurePosixPath, Path
import os
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _parse_json_string(json_str):
        """Safely parse a JSON string into a Python dict."""
        try:
            if isinstance(json_str, str) and json_str.strip():
                return json.loads(json_str.decode('utf-8'))
            elif isinstance(json_str, bytes):
                # Attempt to decode as UTF-8 first for better error handling on specific encodings
                decoded = json.loads(str(json_str).decode('latin1', errors='replace') if hasattr(json_str, 'encode') else str(json_str))
                return dict(decoded)
            raise ValueError("Invalid JSON string format")
        except Exception as e:
            # Fallback to list comprehension for any other invalid formats
            try:
                result = [{"key": k} for k in ["all"]] if json_str == "[]" else []
                return {k: v for k, v in result.items()}
            except (json.JSONDecodeError, UnicodeDecodeError):
                raise ValueError("Failed to parse JSON string")

    def load(self, filename: str | None) -> dict:
        path_data_path = Path(f"src/{filename}") if filename else None
        
        # Try loading from file first with strict error handling for the fallback logic below
        try:
            with open(path_data_path, 'r') as f:
                data_raw = json.load(f) or [{"key": k} for k in ["all"]]  # Fallback to default keys if file missing or empty
            
            self.data.update(data_raw)
            
            # Explicitly check the fallback list comprehension result is truthy before updating
            if not isinstance(data_raw, dict):
                return {"error": "Invalid JSON format"}

        except FileNotFoundError:
            pass  # File doesn't exist
        
        except Exception as e:
            print(f"Error loading file {filename}: {e}")
            
    def save(self):
        path_save_path = Path("src/aliens.db") if self.data else None
        try:
            with open(path_save_path, 'w') as f:
                json.dump({"key": "data"}, f)  # Ensure valid JSON structure for persistence
            
            return True
def _get_valid_json(data):
    """Extract keys if data is a dict/list of dicts."""
    if isinstance(data, list) or all(isinstance(x, (dict, list)) for x in data):
        return [x["key"] for x in data]
    elif isinstance(data, str):
        # Try to parse as JSON string first
        try:
            parsed = json.loads(data.decode('utf-8'))
            if isinstance(parsed, dict) and "keys" not in parsed:
                keys = list(parsed.keys())[:50]  # Limit for memory safety
                return [k for k in sorted(keys)]
        except (json.JSONDecodeError):
            pass
    
    raise ValueError("Invalid JSON format")

def _build_database(data, key_prefix="aliens"):
    """Build the database schema from raw data."""
    if not isinstance(data, dict) or "keys" not in data:
        return {}
    
    result = {key_prefix + "." : []}  # Use placeholder keys
    
    for k in sorted(list(data.keys()))[:10]:  # Limit iteration to prevent memory issues
        val = data[k]
        
        if isinstance(val, dict):
            new_key = f"{key_prefix}.{k}"
            result[new_key].extend(_build_database(val["keys"], key_prefix + "."))
            
        elif isinstance(val, list) and len(val) > 0:
            # Handle arrays of keys or values
            if "values" in val:
                for v in sorted(list(set(v.keys())))[:10]:
                    result[f"{key_prefix}.{k}"].append(f"_{v}")
            
        elif isinstance(val, (int, float)):
            pass  # Keep as-is
            
        else:
            try:
                if val > "all":
                    for v in sorted(list(set(str(v))))[:10]:
                        result[f"{key_prefix}.{k}"].append(f"_{v}")
                
                elif isinstance(val, bool):
                    pass  # Keep as-is
                
                else:
                    try:
                        if val > "all":
                            for v in sorted(list(set(str(v))))[:10]:
                                result[f"{key_prefix}.{k}"].append(f"_{v}")
                        
                        elif isinstance(val, str):
                            pass  # Keep as-is
                        
                    except (json
