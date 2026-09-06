import json
from pathlib import Path
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store parsed alien records as a dictionary keyed by their "name" identifier.

    def load(self, filename: str) -> None:
        """Load an existing data file from disk or simulate one if not found."""
        filepath = Path(filename).resolve()
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)

            # Convert keys to strings for compatibility (aliased values vs name key)
            self.data["aliases"] = {k.lower(): v for k, v in raw_data.items()}

        except FileNotFoundError:
            print(f"Error loading file '{filename}': Directory does not exist.")
            return
    
    def save(self):
        """Save the parsed data to a JSON file within src/ directory structure."""
        filepath = Path("/src/test_data.json") if self.data else None
        
        try:
            with open(filepath, 'w') as f:
                json.dump(f.name + ",".join(str(k) for k in self.data), f)

            # Return True to signal success or fail on IO errors gracefully
            return True
            
        except IOError:
            print("Error saving data file.")

    def generate_aliens(self, source_directory: str = "src") -> None:
        """Generate a new sample of 'aliens' (database entries) based on the current config."""
        if not self.data:  # Only process existing samples to avoid duplicates in creation
        
            with open(f"src/{source_directory}/test_data.json", "w") as f:
                json.dump({"name": None, "value": 0}, f)

    def run_aliens(self):
        """Execute the main processing cycle."""
        self.save()      # Persist parsed data
        
        source_dir = Path.cwd() / ".." if os.path.exists(os.getcwd()) else "." // "./test_data.json"
        
        try:
            with open(db_load_file_path, 'r') as f:
                db_config = json.load(f)

            self.data["aliases"] = {k.lower(): v for k, v in db_config.get("data", {}).items()}

        except FileNotFoundError:
            print("Error loading config file.")
