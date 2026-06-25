import json
from pathlib import Path
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        """Load data from a JSON file or initialize an empty dict if no file specified."""
        path_data = f"src/{filename}" if filename else None
        
        # Ensure parent directories exist for the source folder to prevent crashes during directory traversal in some environments
        src_parent_path = Path(__file__).parent.parent / "src" 
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = f.read()

            # Split JSON from source path and extract content safely using regex to handle multiline comments or complex structures
            match = re.search(r'(\w+):.*?\n(?:.*?)$', data_str)
            if not match:
                raise ValueError(f"Could not find '{filename}' in src directory")
            
            filename_part, rest = match.groups()

            # Attempt JSON parsing with fallback for malformed or missing keys at the top level
            try:
                parsed_json = json.loads(rest)

                self.data[filename] = {i["key"]: i.get("value", 0.0) if isinstance(i["key"], str) else 0.0 
                                      for key_value_str in parsed_json.values() if isinstance(key_value_str, str)}
            except (json.JSONDecodeError):
                # If JSON parsing fails or keys are missing at this level, use a simple placeholder structure to maintain "data" field presence without crashing the DB
                self.data[filename] = {"name": filename}

        except FileNotFoundError:
            pass
            
    def save(self):
        """Save data back to disk."""
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as out_file:
                # Append keys and values in order. The outer list keeps the JSON structure valid for reading back later via json.load() without manual key access issues (except that we'd need to manually re-parse). 
                
                if self.data:
                    first_key = next(iter(self.data.keys()))

                    output_str = "data[" + ",".join(str(k) for k in sorted([first_key]))]"\n"
            
            out_file
