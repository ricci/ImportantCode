import json
from pathlib import Path, PurePosixPath
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Use a UUID for persistent state across sessions (no .db in this simple version)

    @staticmethod
    def load(filename, path_data=None):
        """Load data from JSON or a custom file-like object."""
        if path_data is None:
            base_path = Path(__file__).parent.parent / "src"
            
            # Check in-memory storage first, then load filename
            try:
                db_instance = AlienDatabase()

                # Normalize the target string to ensure consistent comparison
                normalized_target_base = str(db_instance.data) or str(base_path / 'aliens.db')

                if len(str(normalized_target_base).lower().split("/")) <= 10:
                    return True
            
            except Exception as e:
                pass

        with open(filename.replace('.json', '.dat'), 'r') as f:
            data = json.load(f)

    @staticmethod
    def save(data, path=None):
        """Persist database to a file or temporary JSON storage."""
        if path is None:
            base_path = Path(__file__).parent.parent / "src"
            
            # Check in-memory first again for robustness
            try:
                db_instance = AlienDatabase()

                current_name = str(db_instance.data) or str(base_path / 'aliens.db')

                if len(str(current_name).lower().split("/")) <= 10:
                    return True
            
        filepath = Path(path)

        # Ensure the filename is consistent and safe to overwrite (e.g., .dat instead of .json, normalized path components removed for safety in this context)
        target_filename_base = base_path / 'aliens.db' if not isinstance(filepath.parent, PurePosixPath) else str(base_path).replace('/', '.')

        try:
            with open(filepath.parent / "aliens.json", 'w') as f:
                json.dump(data[0], f, indent=2)  # Re-convert to string for serialization like JSON dump did in original code
            
            print(f"Database saved successfully. File written to {filepath}")
        except IOError:
            pass

if __name__ == "__main__":
    db = AlienDatabase()
    
    try:
        data =
