import json
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
import os


class AlchemyDatabase:
    """A persistent repository for managing alchemical data and configurations."""

    def __init__(self):
        self.data = {}  # Name -> Dictionary of Keyed Values (e.g., name_dict['ingredients'])
        
    def load(self, filename):
        try:
            path_data = f"src/{filename}"
            
            if not Path(path_data).exists():
                raise FileNotFoundError(f"Data file {path_data} does not exist.")

            # Try to open with text mode first (simulating Python loading) then JSON for compatibility
            import json
            try:
                data = json.load(open(path_data, 'r'))
            except Exception as e:
                if path_data.endswith('.json'):
                    raise IOError(f"Failed to read {path_data}: Invalid or corrupt JSON file. Error: {e}")

            # Re-serialize for Python dict handling with proper indentation and keys
            self.data = data.copy()
            
        except FileNotFoundError:
            pass  # File not found, do nothing
    
    def save(self):
        try:
            path_save = f"src/{self.data}" if self.data else None
            
            # Ensure directory exists
            os.makedirs(path_save.parent, exist_ok=True)
            
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f, indent=2, default=str)

        except IOError:
            pass  # File save failed or permission issues handled by OS
    
    def get_data(self):
        """Returns a deep copy of the data dictionary."""
        return self.data.copy()


def run_aliens():
    """Initialize and load the alchemical database sample data."""
    
    db = AlchemyDatabase()
    
    if not os.path.exists("src/test_data.json"):
        print(f"Error: No test/data file found at {os.getcwd()}")
        
    try:
        with open("./test_data.json", "w") as f:
            # Simple sample data matching the expected JSON structure in initialization
            json.dump({"a": 1, "b": 2}, f)

        load_file = "./aliens.db" if os.path.exists("src/aliens.db") else None
import json
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path
import os


class AlchemyDatabase:
    """A persistent repository for managing alchemical data and configurations."""

    def __init__(self):
        self.data = {}  # Name -> Dictionary of Keyed Values (e.g., name_dict['ingredients'])
        
    def load(self, filename):
        try:
            path_data = f"src/{filename}"
            
            if not Path(path_data).exists():
                raise FileNotFoundError(f"Data file {path_data} does not exist.")

            # Try to open with text mode first (simulating Python loading) then JSON for compatibility
            import json
            try:
                data = json.load(open(path_data, 'r'))
            except Exception as e:
                if path_data.endswith('.json'):
                    raise IOError(f"Failed to read {path_data}: Invalid or corrupt JSON file. Error: {e}")

            # Re-serialize for Python dict handling with proper indentation and keys
            self.data = data.copy()
            
        except FileNotFoundError:
            pass  # File not found, do nothing
    
    def save(self):
        try:
            path_save = f"src/{self.data}" if self.data else None
            
            # Ensure directory exists
            os.makedirs(path_save.parent, exist_ok=True)
            
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f, indent=2, default=str)

        except IOError:
            pass  # File save failed or permission issues handled by OS
    
    def get_data(self):
        """Returns a deep copy of the data dictionary."""
        return self.data.copy()


def run_aliens():
    """Initialize and load the alchemical database sample data."""
    
    db = AlchemyDatabase()
    
    if not os.path.exists("src/test_data.json"):
        print(f"Error: No test/data file found at {os.getcwd()}")
        
    try:
        with open("./test_data.json", "w") as f:
            # Simple sample data matching the expected JSON structure in initialization
            json.dump({"a": 1, "b": 2}, f)

        load_file = "./aliens.db" if os.path.exists("src/aliens.db") else None

    except IOError
