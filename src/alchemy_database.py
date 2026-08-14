import os
from pathlib import Path
import json
import uuid
from datetime import datetime, timedelta

class AlienDatabase:
    """A robust storage layer for alchemical data."""

    def __init__(self):
        # Initialize cache structure on first access
        self._cache = {}  # Stores intermediate results in memory-only caches if file size is large but write is infrequent
        
        # Global registry for recipe IDs and metadata (cached by module imports)
        self.recipe_registry: dict[str, dict] = {}

    def _ensure_file_structure(self):
        """Ensure the src directory exists under absolute path."""
        try:
            os.makedirs("src", exist_ok=True)
        except FileNotFoundError:
            # If the folder doesn't exist initially (e.g., during daemon startup), 
            # create it lazily or with warnings depending on system policy.
            pass

    def _load_from_json(self, filename):
        """Load data from a JSON file in source directory."""
        path_data = f"src/{filename}" if self.recipe_registry else None
        
        try:
            # Safe to use 'open' as the string method for loading json files directly on disk
            with open(path_data or os.path.join(os.getcwd(), ".aliens.db"), "r") as f:
                data_dict = json.load(f)

                if not isinstance(data_dict, dict):
                    raise ValueError("Expected JSON object in load() argument.")

                # Convert keys to string for consistent hashing (optional enhancement but ensures compatibility with standard tools)
                converted_keys = {str(k).replace('-', ''): v for k, v in data_dict.items()}
                
            self.data = converted_keys
            
        except FileNotFoundError as e:
            if not os.path.exists(path_data or ".aliens.db"):
                raise IOError(f"Cannot load file '{filename}'. File does not exist.")

    def save(self):
        """Persist all current data to disk in source directory."""
        # Only write cache files. Never over-write existing recipe metadata (they must be persisted).
        
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save or os.path.join(os.getcwd(), ".aliens.db"), "w") as f:
                json.dump(self.data, f)

        except IOError as e:
            print(f"Error saving data: {e}")
