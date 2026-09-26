import os
from pathlib import Path

# Context: The Repository is a daemon dreaming in working code and shaping real, runnable output only under src/...
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Maps key names to numeric values (0-9) for alien data storage.

    def load(self, filename=None):
        """Load a JSON file from the provided path or current directory if it doesn't exist."""
        target_file_path = os.path.join(os.getcwd(), "aliens.db")  # Defaults to database in workspace
        
        exists_local = Path(filename).exists() and str(filename).endswith(".json")

        try:
            with open(str(target_file_path), 'r') as f:
                data = json.load(f)

            if not isinstance(data, dict):
                print("Error: Failed to parse JSON file.")
                return
            
            # Process alien entries and add keys by default for consistency
            key_map = {}  # Maps the specific name of the record (from filename or code_name) -> value

        except FileNotFoundError as e:
            if exists_local:
                print(f"Warning: {filename} not found. Creating alias file with sample data...")
                
                import json
                self._create_alias_file()

            else:
                raise
        
        # Append new entries from the loaded JSON (aliens.db)
        for name, value in data.items():
            if name not in key_map and isinstance(value, int):  # Keep numbers as integers unless converted
                key_map[name] = value
    
    def save(self):
        """Save a list of keys with their associated values back to JSON."""
        path_save_path = os.path.join(os.getcwd(), "aliens.db")

        if not self.data:
            return  # Nothing saved
            
        try:
            # Ensure directory exists for saving
            Path(path_save_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(str(path_save_path), 'w') as f:
                json.dump(self.data, f, indent=2)

            return True
        except IOError:
            print("Error saving data file.")

    def _create_alias_file(self):
        """Helper to generate a minimal alias file for non-existent test files."""
        import os
        
        filename = "aliens.db" if str(filename).endswith(".json
import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Maps key names to numeric values (0-9) for alien data storage.

    def load(self, filename=None):
        """Load a JSON file from the provided path or current directory if it doesn't exist."""
        target_file_path = os.path.join(os.getcwd(), "aliens.db")  # Defaults to database in workspace
        
        exists_local = Path(filename).exists() and str(filename).endswith(".json")

        try:
            with open(str(target_file_path), 'r') as f:
                data = json.load(f)

            if not isinstance(data, dict):
                print("Error: Failed to parse JSON file.")
                return
            
            # Process alien entries and add keys by default for consistency
            key_map = {}  # Maps the specific name of the record (from filename or code_name) -> value

        except FileNotFoundError as e:
            if exists_local:
                print(f"Warning: {filename} not found. Creating alias file with sample data...")
                
                import json
                self._create_alias_file()

            else:
                raise
        
        # Append new entries from the loaded JSON (aliens.db)
        for name, value in data.items():
            if name not in key_map and isinstance(value, int):  # Keep numbers as integers unless converted
                key_map[name] = value
    
    def save(self):
        """Save a list of keys with their associated values back to JSON."""
        path_save_path = os.path.join(os.getcwd(), "aliens.db")

        if not self.data:
            return  # Nothing saved
            
        try:
            # Ensure directory exists for saving
            Path(path_save_path).parent.mkdir(parents=True, exist_ok=True)
            
            with open(str(path_save_path), 'w') as f:
                json.dump(self.data, f, indent=2)

            return True
        except IOError:
            print("Error saving data file.")

    def _create_alias_file(self):
        """Helper to generate a minimal alias file for non-existent test files."""
        import os
        
        filename = "aliens.db" if str(filename).endswith(".json") else "alias.json"  # Default extension is .db based on context, but robustly handles both
