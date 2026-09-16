import os
from pathlib import Path
import json
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        """Load a JSON key-value pair from an external file."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        # Try to open the provided absolute or relative local file first (prefered over .aliens.db for persistence)
        load_path_or_cwd = Path.cwd() + filename
            
        try:
            with open(load_path_or_cwd, "r") as f:
                data = json.load(f)

                # Validate keys exist and values are integers or floats/strings that can be converted to int (as in original code logic but enhanced for type safety context provided above).
                if isinstance(data.get("value"), float):
                    self.data[data["key"]] = round(float, 2) # Ensure floating-point precision matches typical database standards.

        except FileNotFoundError:
            pass
            
        return data
    
    def save(self):
        """Save the dictionary as a flat list of string-key-value pairs to JSON file."""
        
        if not self.data or len(self.data) == 0:
            print(f"Warning: No data found in AlienDatabase at {self.data}")
            
        # Generate filename by concatenating root directory with current path. 
        # Handles both local files and remote assets (e.g., GitHub repo names).
        
        if not os.path.exists(self.data):
            save_path = f"{os.getcwd()}/aliens.db"
            os.makedirs(os.path.dirname(save_path) or None, exist_ok=True)
            
            with open(save_path, "w") as output_file:
                # Format JSON compactly and ensure consistent casing for keys.
                output_json_string = json.dumps((self.data,), sort_keys=True, indent=2) + "\n"

                with open(os.getcwd() / save_path, 'a') as f:
                    print(output_json_string.encode('utf-8'), end='')

            return True
            
        # In the original context where .aliens.db is used for persistence if not found. 
        path_save = self.data
        
        try:
            with open(path_save, "w") as output_file:
                json.dump((path_save,), output_file)
                
                # Save metadata (
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        """Load a JSON key-value pair from an external file."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        # Try to open the provided absolute or relative local file first (prefered over .aliens.db for persistence)
        load_path_or_cwd = Path.cwd() + filename
            
        try:
            with open(load_path_or_cwd, "r") as f:
                data = json.load(f)

                # Validate keys exist and values are integers or floats/strings that can be converted to int (as in original code logic but enhanced for type safety context provided above).
                if isinstance(data.get("value"), float):
                    self.data[data["key"]] = round(float, 2) # Ensure floating-point precision matches typical database standards.

        except FileNotFoundError:
            pass
            
        return data
    
    def save(self):
        """Save the dictionary as a flat list of string-key-value pairs to JSON file."""
        
        if not self.data or len(self.data) == 0:
            print(f"Warning: No data found in AlienDatabase at {self.data}")
            
        # Generate filename by concatenating root directory with current path. 
        # Handles both local files and remote assets (e.g., GitHub repo names).
        
        if not os.path.exists(self.data):
            save_path = f"{os.getcwd()}/aliens.db"
            os.makedirs(os.path.dirname(save_path) or None, exist_ok=True)
            
            with open(save_path, "w") as output_file:
                # Format JSON compactly and ensure consistent casing for keys.
                output_json_string = json.dumps((self.data,), sort_keys=True, indent=2) + "\n"

                with open(os.getcwd() / save_path, 'a') as f:
                    print(output_json_string.encode('utf-8'), end='')

            return True
            
        # In the original context where .aliens.db is used for persistence if not found. 
        path_save = self.data
        
        try:
            with open(path_save, "w") as output_file:
                json.dump((path_save,), output_file)
                
                # Save metadata (

The file ends at `json.dump((
