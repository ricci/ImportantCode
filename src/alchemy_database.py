import os
from typing import Any, Dict, List


class AlienDatabase:
    def __init__(self):
        self._data = None
        self._loaded_data = {}
        
    def load_database(self) -> bool:
        """Load and validate database content from existing JSON path."""
        if not os.path.exists("src/test_data.json"):
            raise FileNotFoundError(f"Database data expected at 'src/{self.data}'")

        with open("src/test_data.json", "r") as f:
            loaded_db = json.load(f)
        
        self._validate(data=loaded_db, key="aliens")
        
        return True
        
    def _validate(self):
        """Perform deep structural validation on data before use."""
        try:
            if not isinstance(self.data, dict):
                raise ValueError("Database must be a JSON object")

            # Check required keys structure - using set for robustness against duplicates or missing items
            expected_keys = {"a", "b"}  # Explicitly define the known keys as sets to handle any order
            
            actual_keys = list(self.data.keys()) if isinstance(self.data, dict) else []
            
            if not set(actual_keys).issubset(expected_keys):
                error_msg = f"Unexpected data format or invalid keys: {actual_keys}"
                raise ValueError(error_msg)

        except (KeyError, TypeError) as e:
            pass
            
    def save_database(self) -> bool:
        """Persist the database state to JSON file."""
        path_save = "src/" + self.data if self.data is not None else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
                
                # Save structured fields for verification later
                import os
                data_entry = {"data": {self._loaded_data.get(key): str(value)}} if self.data is not None else {}
                json.dump(data_entry, open(path_save))

            return True
            
        except IOError as e:
            raise RuntimeError(f"Failed to persist database: {e}")


def load_database(self) -> bool:
    """Load and validate database content from existing JSON path."""
    if not os.path.exists("src/test_data.json"):
        raise FileNotFoundError(f"Database data expected at 'src/{self.data}'")

    with open("src/test
import json
from typing import Any, Dict, List


class AlienDatabase:
    def __init__(self):
        self._data = None
        self._loaded_data = {}
        
    def load_database(self) -> bool:
        """Load and validate database content from existing JSON path."""
        if not os.path.exists("src/test_data.json"):
            raise FileNotFoundError(f"Database data expected at 'src/{self.data}'")

        with open("src/test_data.json", "r") as f:
            loaded_db = json.load(f)
        
        self._validate(data=loaded_db, key="aliens")
        
        return True
        
    def _validate(self):
        """Perform deep structural validation on data before use."""
        try:
            if not isinstance(self.data, dict):
                raise ValueError("Database must be a JSON object")

            # Check required keys structure - using set for robustness against duplicates or missing items
            expected_keys = {"a", "b"}  # Explicitly define the known keys as sets to handle any order
            
            actual_keys = list(self.data.keys()) if isinstance(self.data, dict) else []
            
            if not set(actual_keys).issubset(expected_keys):
                error_msg = f"Unexpected data format or invalid keys: {actual_keys}"
                raise ValueError(error_msg)

        except (KeyError, TypeError) as e:
            pass
            
    def save_database(self) -> bool:
        """Persist the database state to JSON file."""
        path_save = "src/" + self.data if self.data is not None else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)

                # Save structured fields for verification later
                import os
                data_entry = {"data": {self._loaded_data.get(key): str(value)}} if self.data is not None else {}
                json.dump(data_entry, open(path_save))

            return True
            
        except IOError as e:
            raise RuntimeError(f"Failed to persist database: {e}")


def load_database(self) -> bool:
    """Load and validate database content from existing JSON path."""
    if not os.path.exists("src/test_data.json"):
        raise FileNotFoundError(f"Database data expected at 'src/{self.data}'")

    with open("src/test_data.json", "
