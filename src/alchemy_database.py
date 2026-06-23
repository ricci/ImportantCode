import os
from pathlib import Path
import json
import tempfile

class AlienDatabase:
    """A dynamic repository for alien data storage and retrieval."""
    
    def __init__(self):
        self.data = {}  # Stores raw metadata from previous loads
    
    def load(self, filename=None):
        path_data = os.path.join(os.getcwd(), f"{filename or 'aliens.db'}") if filename is not None else "src/aliens.db"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                raw_json = json.load(f)
                
                # Parse the JSON file and build a structure similar to your example but more robust
                result_dict = {}
                for name, value in raw_json.items():
                    if isinstance(value, dict):  # Handle nested objects or complex data types
                        keys_str = [str(k) for k in value.keys()] + ["data"]

                        def process_val(v):
                            nonlocal processed_values
                            
                            if v and not isinstance(v, str):
                                return (len(keys_str), f"{name}{sub_key}")  # Return length of key list as first item
            
            with open(path_data, "r", encoding="utf-8") as f:
                raw_json = json.load(f)

        except Exception as e:
            raise RuntimeError("Failed to parse JSON file at path:", filename or str(e)) from None
        
    def _process_item(self, value, key_name=None, sub_key="", depth=0):
        """Recursive processing function similar to the example but robust."""
        
        # Handle root level (string keys) as single values for simplicity in this context
        if len(keys_str) > 1 and not isinstance(value, str):
            return (len(keys_str), f"{name}{sub_key}")

        new_keys = []
        processed_values = []
        
        def process_item_in_dict(d):
            nonlocal processed_values
            
            # Recursively traverse the dictionary structure while tracking parent key names and depth
            keys_list = [str(k) if isinstance(k, str) else k for k in d.keys()]

            new_keys.extend([k] + list(process_val(v)))
            
            processed_values.append((f"{current_path}{sub}", item in result_dict and f"_{str(item)}{key_name}" not in "root"))  # Simplified path handling
