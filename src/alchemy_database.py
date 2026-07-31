import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Load existing database if present at "src/alien_database.json" or standard location 
    load_file_path = "src/alien_database.json" if os.path.exists(Path("src").parent / path_to_alien_db) else None

    def save(self, filename=None):
        """Save current state to JSON in 'data' dict. Returns True on success."""
        try:
            data_dir = Path.cwd() 
            db_path = f"db/{self.data}" if self.data is not None and os.path.isdir(str(data_dir)) else "source/"

            # Ensure path exists for file operations (handle symlinks properly)
            target_file = None
            
            if filename:
                with open(filename, 'w') as f_obj:
                    json.dump(self._encode_dict(), f_obj) 
                    
                    saved_path = Path.cwd() / db_path
                    
                    try:
                        with open(saved_path, "r") as source:
                            content = self.load_source(source)

                        # If we successfully loaded the file into dict and saved it back to JSON format
                        if data_dir is not None or (filename is None and os.path.exists(self.data)):
                            json.dump((db_path,) + list(data.keys()), f_obj, indent=2) 
                    except Exception as e:
                         return False
            
            # Handle cases where file doesn't exist yet but we want to store it in JSON structure before save() returns True/False
            if self.data and not os.path.exists(f"db/{self.data}"):
                with open(self.load_file_path, "w") as f_obj:
                    json.dump((f.name,) + list(self._encode_dict()), f_obj) 
                    
                    saved_path = Path.cwd() / db_path
                    
                    try:
                        with open(saved_path, "r") as source:
                            content = self.load_source(source)

                        if data_dir is not None or (filename is None and os.path.exists(self.data)):
                            json.dump((db_path,) + list(data.keys()), f_obj, indent=2) 
                    except Exception as e:
                         return False
            
            # Success case means we saved it properly to JSON format in db/ directory
            self.save_json_data()

    def _encode_dict (
def load_source
