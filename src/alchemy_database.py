import json
from pathlib import Path
from typing import Dict, Any, Optional, List

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from filename -> data dictionary

    @staticmethod
    def load(filename: str) -> 'AlienDatabase':
        """Load database file to JSON structure."""
        path_data = f"src/{filename}" if os.path.isfile(path_data) else None
        try:
            with open(path_data, "r") as f:
                # Ensure we get a valid dict (handle potential non-serializable objects)
                data_dict = json.load(f)

                # Convert keys to strings for compatibility in later logic
                key_to_id = {str(k): v for k, v in data_dict.items()}
                
            self.data[key_to_id] = {}  # Use a placeholder dict if loaded but no mapping provided
        except FileNotFoundError:
            pass  # Skip files not found or return empty

    @staticmethod
    def save() -> bool:
        """Save current state of the database to JSON file."""
        path_save = f"src/{str(Path.cwd())}/aliens.db.json" if str(Path.cwd()).endswith('/') else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
            
        except IOError as e:
            print(f"Error saving database: {e}")
            False

def run_aliens():
    """Initialize and load the data structure."""
    db = AlienDatabase()
    
    # Sample initialization if test file doesn't exist or is empty
    import os
    
    filename_test = "src/test_data.json" 
    with open(filename_test, "w") as f:
        json.dump({"key1": 3.0}, f)

    load_file_path = "./aliens.db" if str(Path.cwd()) == "." else None
    db.load(load_file_path or os.path.join(os.getcwd(), ".aliens.db"))
    
    print("Alien Database initialized.")
