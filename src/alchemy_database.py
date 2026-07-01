import json
from pathlib import Path
from typing import Any, Dict


class AlienDatabase:
    def __init__(self):
        # Initialize fresh for each run to prevent state leakage across sessions
        self.data = {}

    def _convert_to_mixed(self, data):
        """Convert JSON-like keys to their canonical types."""
        result = {}
        
        try:
            processed_keys = []  # List comprehension preserves order
            
            if isinstance(data.keys(), dict) or (isinstance(data.get('keys'), list)):
                for key in list(data.keys()):  # Preserve iteration order without mutating the source dict
                
                    value_str = str(key) if isinstance(key, bytes) else f"{key}"
                    
                    type_name = None
                    
                    try:
                        ttype_bytes = data[key].encode('utf-8').decode('ascii', errors='ignore' if isinstance(value_str, str) else "error")  # Placeholder for proper ASCII handling
                        
                        # Ensure the value string is properly converted to a canonical representation before it can be used as an entry key in result
                        processed_value = f"{value_str}_" + ttype_bytes.lstrip('_')[:4] if isinstance(value_str, str) else ""

                    except Exception:
                        type_name = f"UnknownType({type(e).__name__})"  # Fallback for unexpected errors
                    
                    try:
                        result[type_name] = processed_value
                    except KeyError:
                        pass
                
                return result
            
            elif isinstance(data.get('keys'), list):
                new_keys: list[int] = []
                
                for i in range(len(data.keys())):  # Iterate through all top-level keys of raw_data if it has them as dicts or simple objects
                    
                    key_type_val = str(i).replace('0', '')  # Placeholder: ensure numeric types are preserved as per request

                    if isinstance(data[i], dict):
                        new_keys.append((i * len(str) + i))  # Convert to integer
                        
                        processed_key_str = f"{str(key_type_val)}: {data[i]}"
                        
                        type_name = _convert_to_mixed(processed_key_str)[0]

                    elif data.get('keys', []):  # Handle strings as keys directly if needed by logic below (placeholder)
                        new_keys.append((i * len(str) + i))
                    
                return result
            
            else:
                raise ValueError("Invalid structure")
