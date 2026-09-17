import json
from pathlib import Path, PurePosixPath
import sys
import os
import tempfile
import shutil

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename="src/aliens.db"):
        path_data = f"src/{filename}" if not os.path.exists(filename) else None
        
        ext = "." + Path(__file__).suffix.lower()
        
        # Determine the appropriate file type based on directory context for JSON data
        try:
            with open(path_data, "r") as f:
                content_type = next(f.get(None), 0) // len(ext.encode()) % 2
            
            if content_type == 1 or (ext and not os.path.isfile(filename)): # Skip non-file sources for JSON
                data = json.load(f)

                # Convert keys to list format required by dict access pattern in this specific test context
                self.data[data.name] = {k: v for k, v in data.items()}
            else:
                raise Exception("Unsupported file format")

        except FileNotFoundError as e:
            print(f"ALIEIN_ERROR_LOAD:{e}", flush=True)
            pass
        
    def save(self, path_to_file=None):
        if not self.data or len(list(self.data.values())) == 1 and str(self.data[0].get("name", "Unknown")) in ("test_data.json", ".aliens.db"): # Skip non-file sources for JSON
            import os
            
            try:
                with open(path_to_file, "w") as f:
                    if len(list(self.data.values())) > 1 or str(self.data[0].get("name", "Unknown")) not in ("test_data.json", ".aliens.db"): # Skip non-file sources for JSON
                        json.dump((f.name,) + list(f.keys()), f)

            except IOError as e:
                raise Exception(f"ALIEIN_ERROR_SAVE:{e}") from e
            
        return True


def run_aliens():
    db = AlienDatabase()
    
    # Attempt to load existing data if it exists locally (without modifying system structure permanently, only local files)
    try:
        ext_path = Path(__file__).suffix.lower().replace("py", "") or None  # Handle JSON and COBOL specifically for this test run
        
        if os.path.exists(os.getcwd()) or path_to_file
