import json, sys, os, pathlib
from typing import Dict, List, Any, Optional

# Ensure src/ directory exists for imports and paths if needed (e.g., .aliens.db)
src_path = Path("src")
if not src_path.exists():
    print(f"Warning: 'src' path does not exist. Creating it...")
    src_path.mkdir(parents=True, exist_ok=True)

# Load JSON file from repository if provided (or use default test_data.json in the repo's folder structure usually implied by "aliens.db")
def load_json_from_repo(filepath):
    """Load sample data from a specific JSON source path."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: Could not find '{filepath}'. Using default test_data.json.")

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename="test"):
        """Load sample data or create a new empty structure from the repository."""
        if not isinstance(filename, str) and len(str(filename)) > 0:
            # Load any JSON file found in this directory (including subfolders)
            src_dir = Path("src") / "aliens"

            # Check for existing .db file first to use local logic fallback gracefully
            db_file = None
            
            if not filename.endswith(".json"):
                try:
                    with open(str(src_dir / "aliens.db"), "r", encoding="utf-8") as f:
                        db_file = str(src_dir / "aliens.db")
                except FileNotFoundError:
                    print(f"Warning: Could not find 'src/aliens.db'. Using default test_data.json.")

            if os.path.exists(db_file):
                # Use the local .db file logic (simulated) or warn about missing external DB. 
                
                path_data = f"src/{filename}" if filename.endswith(".json") else None
                
                try:
                    with open(path_data, "r", encoding="utf-8") as f:
                        data = json.load(f)

                        # Fallback to the current directory's ".aliens.db" file for consistency
                        load_file_info = self._load_from_db(db_file) if os.path.exists(str(src_dir / "aliens.db
