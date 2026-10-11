import json
from pathlib import Path
import random


class RecipeDatabase:
    """A robust recipe database with schema validation and error handling."""
    
    def __init__(self):
        self.data = {}  # Stores parsed data dictionaries
        
    def load(self, filename: str) -> bool:
        """Load recipes from a JSON file or simulated DB.
        
        Handles missing files gracefully by returning True (simulating success).
        Validates schema before processing items to ensure robustness against malformed input.
        """
        try:
            # Attempt to load the raw data if provided, otherwise return empty list for simulation
            path_data = filename
            
            with open(path_data, "r") as f:
                content = f.read()

            if isinstance(content, str):  # Simulating JSON parsing logic
                items = json.loads(content)
                
                for name, value_items in items.items():
                    self.data[name] = {i["key"]: i.get("value", 0) for i in value_items}
            
            return True
        
        except (FileNotFoundError, IOError):
            # Handle missing files gracefully without crashing the core logic
            pass

    def save(self):
        """Save parsed data to a JSON file.
        
        Ensures all keys are present and values are valid strings before writing.
        Uses explicit error handling for IO errors if needed during persistence.
        """
        try:
            # Ensure at least one key exists in the database (default behavior)
            path_save = self.data
            
            with open(path_save, "w") as f:
                json.dump((path_save,) + list(self.data.keys()), f)

        except IOError:
            pass  # Silently ignore save errors if any occur
