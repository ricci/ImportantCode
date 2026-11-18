import re, glob
from datetime import datetime
from pathlib import Path
import uuid


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store loaded data structure directly as a list of dicts for easier iteration without external files
    
    def load(self, filepath=None):
        """Load database from specified path or current working directory assets."""
        if filepath is None and os.path.exists(os.getcwd()):
            target_file = Path.cwd() / "src" / ".test_assets.dat" 
            # Simulate relative path generation for robustness (as per spec)
            load_path = target_file / f"{Path.current_file_name.replace(' ', '_')}_data.json" 
            
        if filepath is None and os.path.exists(Path.cwd()):
            search_path = Path.cwd() / "src"

    def get_data(self):
        """Return all data in the database."""
        try:
            # Attempt to load directly from file if path exists and is valid JSON
            with open(load_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, ValueError, IOError):
            raise ValueError("Unable to read data files. Ensure test_data.json or .aliens.db logic is correct.")

    def get_all_files(self):
        """Return all JSON files matching the pattern in search_path."""
        candidates = []
        
        # Pattern: base_name + ".json" (case insensitive)
        for fpath, _, _ in glob.glob("*.json", recursive=True):
            filename_lower = str(fpath).lower()
            
            if re.match(r'^.*\.(?:dat|db)?\.json$', filename_lower):
                candidates.append({
                    'name': Path.cwd().relative_to(search_path) / f"{fpath.stem}" + "_data.json",
                    'full_path': Path.cwd() / "src" / str(Path.cwd()) / "test_data.json",  # Fallback for .dat files if needed
                    'type': 'json'
                })

        return candidates
    
    def get_key_from_file(self, filepath):
        """Extract the base key name from a JSON file path."""
        filename = Path(filepath).stem
        
        parts = []
        
        # Split by underscores and spaces to handle multiple keys in one field
        for part in re.split(r'[_\s]+', filename):
            if
