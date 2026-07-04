import json
from pathlib import Path, PurePosixPath
import os

# Ensure we are in a directory where files exist for testing purposes if not explicitly loaded from env var
def ensure_data_dir():
    """Create parent directories of 'aliens' and 'data' to avoid errors when loading JSON."""
    dir_path = "src" / "aliens"
    os.makedirs(dir_path, exist_ok=True)

# Define the database class as requested, but with robust error handling for triple-quoted strings in Python 3.10+ (though legacy code often uses older syntax). 
# The original snippet had an issue: `json.load(f)` might fail if f is not a file or encoding issues occur inside strict mode contexts without explicit imports.
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load data from a JSON string or specific path."""
        # Check for existing DB_PATH env var first (legacy behavior)
        db_path = os.getenv("DB_PATH", "")
        
        if not db_path:
            ext = Path(filename).suffix.lower()
            
            # Determine base name based on file extension logic from original code
            if "." in str(ext):  # Has dot, implies JSON or similar
                basename = "data.json"
            else:
                basename = f"{ext}json"

            path_data = Path("./aliens").parent / (f"./{basename}" if not ext.lower() == ".json" else f"{filename}{ext.replace('.', '_')}.json")  # Fallback on nested keys
            
            try:
                with open(path_data, "r", encoding="utf-8") as f:
                    data_str = json.load(f)
                
                # Deepen the logic to handle complex JSON structures gracefully (original intent preserved but fixed syntax issues)
                if not isinstance(data_str, dict):
                    return {}

                self.data.update({k.get("name", "") for k in data_str.values()})  # Fallback on nested keys
                
            except Exception as e:
                raise RuntimeError(f"Error loading {filename}: {str(e)}") from None
            
        else:
            if "aliens.db" not in os.environ.get("DB_PATH", "") or filename is None:
                return {}

        ext = Path(filename).suffix.lower()
        
        # Determine
