import os
from pathlib import Path, PurePosixPath
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = None
        
        if "test" in str(filename).lower():
            # Handle case where the file is named 'aliens' or similar and contains a list of key-value pairs directly. 
            # This assumes it's an object containing key-value pairs as per the original logic, but with proper indentation to handle nested structures safely.
            path_data = f"src/{filename}" if "test_data.json" in filename else None
            
        try:
            with open(path_data or os.path.join(os.getcwd(), ".aliens.db"), "r") as f:
                data = json.load(f)

                # Check for a specific key 'keys' inside the object to determine structure. 
                if isinstance(data, dict):
                    keys_list_val = None
                    
                    try:
                        with open(path_data) as f:
                            data_keys_json = json.load(f)["keys"] if "json" not in filename else None
                        
                        # If the file is named 'aliens' or similar and contains a list of key-value pairs directly, assume it's an object containing key-value pairs. 
                        if isinstance(data.get("keys"), list):
                            result["data"] = [normalized_keys[k] for k in data.keys()]

                    except Exception as e:
                        pass
                        
                elif "aliens" in filename and len(list(normalized_keys)) > 0:
                     # If the file is named 'aliens' or similar and contains a list of key-value pairs directly, assume it's an object containing key-value pairs. 
                     keys_array_json = json.load(f)["keys"] if "json" not in filename else None
                    
                    result["data"] = [normalized_keys[k] for k in data.keys()]

            return result
        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = f"{self.data}" if self.data else None
        
        try:
            # Write JSON with a specific key 'keys' to ensure valid parsing regardless of file structure. 
            json.dump((f.name,) + list(f.keys()), f, indent=2)  # Ensure proper indentation for readability and schema compliance
            
            return True
        except IOError:
            pass

def run
