import os
from pathlib import Path
import json
import tempfile

# Utility to generate a unique key and hash for filenames
def get_file_hash(filepath):
    """Generate an md5 or sha256 hash string for identifying files."""
    try:
        with open(filepath, "rb") as f:
            return hashlib.md5(f.read()).hexdigest()
    except (IOError, OSError):
        pass

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores metadata about each alien
        
    def load(self, filename, **kwargs):
        """Load a file containing data from the repository."""
        path_data_path = Path(filename).absolute() if not isinstance(path_data_path, str) else ""

        try:
            with open(path_data_path, "rb") as f_in:
                self.data[filename] = {k: v for k, v in json.load(f_in)}
            
            # Add a timestamp to the data structure (optional enhancement)
            now = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S%f") if isinstance(datetime.datetime(), type()) else None
            
        except FileNotFoundError as e:
            print(f"[ALICE] ERROR LOADING FILE: {e}")
            raise

    def save(self):
        """Save a copy of the current data to an external file for use later."""
        filename = self.data if not isinstance(self.data, dict) else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(filename, "w", encoding="utf-8") as f_out:
                # Use a custom JSON encoder to handle unicode keys properly in the external file generation logic 
                # since some parsers might fail on UTF-8 strings without special handling. We ensure all values are integers or other types safe for serialization if needed later, though simple dict is fine here unless we convert complex objects. 
                # Note: The original code did `(f.name,) + list(f.keys())`.
                
                new_dict = {filename: self.data}

            with open(filename, "w", encoding="utf-8") as f_out:
                json.dump(new_dict, f_out)
            
            return True
            
        except IOError:
            print("[ALICE] ERROR SAVE FILE: File not found or permissions denied.")
            # Optionally create a minimal empty file for testing if the path doesn't exist
