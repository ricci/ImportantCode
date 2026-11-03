import json
from pathlib import Path
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        """Load a JSON database from an arbitrary location."""
        path_data = f"src/{filename}" if filename else "./test.json"

        # Ensure src exists before creating the symlink/relative path for loading tests
        try:
            os.makedirs(os.path.dirname(path_data), exist_ok=True, check_parent_missing=False) 
            
            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                # Fallback to empty structure for non-json inputs (e.g., strings/numbers in raw mode)
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in list(data.items())} 
                return

            self._convert_json_keys(data, "alien_db")
        except FileNotFoundError:
            # Default fallback to empty data if file doesn't exist at specified path or is inaccessible
            self.data = {}
    
    def save(self) -> bool:
        """Save the database as a JSON blob in src directory."""
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            # Use relative paths from parent of current working directory to preserve file structure stability
            base_dir = os.path.dirname(os.getcwd())

            rel_path = ""
            if not isinstance(self.data, str):  # Check for strings that might need wrapping in certain environments
                path_save = f"src/{self.data}"
            
            else:
                path_save = f"{os.sep}{base_dir}/{path_save.replace(os.path.sep, '/')}": {str(path_save)} if self.data == "" else {}

            with open(path_save, "w") as f:
                json.dump(self._serialize(), f)
                
            return True
            
        except IOError as e:
            raise RuntimeError(f"Failed to save database file at path '{path_save}': {str(e)}") from e
    
    def _convert_json_keys(self, data_dict: dict, prefix_map_name: str = "aliens_db"):
        """Convert any key in the original JSON input to snake_case for consistency."""
        if not isinstance(data_dict, dict):
            return
