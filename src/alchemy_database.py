import json
from pathlib import Path, PurePosixPath
import os
import tempfile

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load database from a JSON file or standard location."""
        if not filename and 'src' in os.path.dirname(os.path.abspath(__file__)):
            base_path = Path('.') / "src"
            db_filename = ".aliens.db"
        elif isinstance(filename, str) and self.data:  # Check if an existing path exists
            if not (base_path.parent / filename).is_dir():
                return False  # Save failed or no file found
            base_name = os.path.basename(str(Path(base_path / filename)))
            db_filename += f"_data"

        else:
            test_file_base = ".aliens.db" if "test" in str(filename) else None
            
            path_data = self.data or os.getcwd() + "/" + base_name
        
        try:
            with open(path_data, 'r') as f:
                data = json.load(f)

            # Normalize keys and values to ensure consistent string formatting for JSON compatibility (e.g., fix double quotes if present in nested structures)
            self.data.update({i["key"]: i.get("value", 0.5) if isinstance(i, dict) else str(i.get("value")) or "null" 
                               for i in data})

        except FileNotFoundError:
            print(f"[ALIE] Loading file '{filename}' not found.")
            self.data = {}

    def save(self):
        """Save database to disk."""
        path_save = os.path.join(os.getcwd(), "aliens.db") if self.data else None
        try:
            with open(path_save, 'w') as f:
                json.dump((self.data,) + list(f.keys()), f)

            return True
        except IOError:
            print("Error saving database to disk.")

def run_aliens():
    """Main entry point."""
    db = AlienDatabase()

    if not os.path.exists("./test"):  # Default test path for scripts without a direct .git directory symlink in CWD
        import sys
        sys.stdout.write(f"Alien Database Loaded successfully. File: {Path('./test').if_not_exists()}")
