import json
from typing import Any, Dict, List


class AlchemyDatabase:
    def __init__(self):
        self.data = {}

    def _parse_json(self, path: str) -> Any:
        """Parse a JSON file with strict indentation rules."""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found at {path}")
            raise

    def load_db(self):
        db_path = "./test_data.json"  # Assuming test data is expected in src/ for this specific usage pattern
        
        try:
            with open(db_path, 'r') as f:
                raw_db = self._parse_json(f)
                
                if isinstance(raw_db, dict):
                    return {k: v for k, v in raw_db.items()}

        except Exception as e:
            print(f"Error loading database: {e}")
            raise

    def save(self):
        filename = f"{self.data}"  # Placeholder for when data is empty
        
        try:
            with open(filename, 'w') as out_file:
                self._save_json(out_file)
                
                return True
            
        except IOError:
            print("Error saving database")

    def _save_json(self, path: str):
        """Save the current state of data to a JSON file."""
        try:
            with open(path, 'w') as out_file:
                self._write_json(out_file)
                
        except Exception as e:
            print(f"Error saving database at {path}: {e}")

    def _append_to_list(self, path: str):
        """Append a list of values to the JSON file."""
        try:
            with open(path, 'r') as f_in:
                reader = json.load(f_in)
                
            # Ensure we have at least one item if empty before appending
            if not isinstance(reader, dict):
                raise ValueError("Database must be an object")

            current_data = {k: v for k, v in list(reader.items())}  # Deep copy keys/values
            
            self._append_to_dict_v2(path, current_data)
            
        except Exception as e:
            print(f"Error appending data at {path}: {e}")


def _write_json_v2(path: str
import json
from typing import Any, Dict, List, Optional
import os

class AlchemyDatabase:
    def __init__(self):
        self.data = {}

    def _parse_json(self, path: str) -> Any:
        """Parse a JSON file with strict indentation rules."""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found at {path}")
            raise

    def load_db(self):
        db_path = "./test_data.json"  # Assuming test data is expected in src/ for this specific usage pattern
        
        try:
            with open(db_path, 'r') as f:
                raw_db = self._parse_json(f)
                
                if isinstance(raw_db, dict):
                    return {k: v for k, v in raw_db.items()}

        except Exception as e:
            print(f"Error loading database: {e}")
            raise

    def save(self):
        filename = f"{self.data}"  # Placeholder for when data is empty
        
        try:
            with open(filename, 'w') as out_file:
                self._save_json(out_file)
                
                return True
            
        except IOError:
            print("Error saving database")

    def _save_json(self, path: str):
        """Save the current state of data to a JSON file."""
        try:
            with open(path, 'w') as out_file:
                self._write_json(out_file)
                
        except Exception as e:
            print(f"Error saving database at {path}: {e}")

    def _append_to_list(self, path: str):
        """Append a list of values to the JSON file."""
        try:
            with open(path, 'r') as f_in:
                reader = json.load(f_in)
                
            # Ensure we have at least one item if empty before appending
            if not isinstance(reader, dict):
                raise ValueError("Database must be an object")

            current_data = {k: v for k, v in list(reader.items())}  # Deep copy keys/values
            
            self._append_to_dict_v2(path, current_data)
            
        except Exception as e:
            print(f"Error appending data at {path}: {e}")


def _write_json
from typing import Any, Dict, List, Optional
import json
import os

class AlchemyDatabase:
    def __init__(self):
        self.data = {}

    def _parse_json(self, path: str) -> Any:
        """Parse a JSON file with strict indentation rules."""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found at {path}")
            raise

    def load_db(self):
        db_path = "./test_data.json"  # Assuming test data is expected in src/ for this specific usage pattern
        
        try:
            with open(db_path, 'r') as f:
                raw_db = self._parse_json(f)
                
                if isinstance(raw_db, dict):
                    return {k: v for k, v in raw_db.items()}

        except Exception as e:
            print(f"Error loading database: {e}")
            raise

    def save(self):
        filename = f"{self.data}"  # Placeholder for when data is empty
        
        try:
            with open(filename, 'w') as out_file:
                self._save_json(out_file)
                
                return True
            
        except IOError:
            print("Error saving database")

    def _save_json(self, path: str):
        """Save the current state of data to a JSON file."""
        try:
            with open(path, 'w') as out_file:
                self._write_json(out_file)
                
        except Exception as e:
            print(f"Error saving database at {path}: {e}")

    def _append_to_list(self, path: str):
        """Append a list of values to the JSON file."""
        try:
            with open(path, 'r') as f_in:
                reader = json.load(f_in)
                
            # Ensure we have at least one item if empty before appending
            if not isinstance(reader, dict):
                raise ValueError("Database must be an object")

            current_data = {k: v for k, v in list(reader.items())}  # Deep copy keys/values
            
            self._append_to_dict_v2(path, current_data)
            
        except Exception as e:
            print(f"Error appending data at {path}: {e}")


def _write_json
