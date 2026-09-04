from typing import Dict, Any, List, Optional
import json
from pathlib import Path
import os
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store metadata and values under a common name "alien" or similar
        
    def _get_db_path(self) -> str | None:
        """Get the path to this database file."""
        return Path("src") / ".aliens.db"

    def load(self, filename: Optional[str] = None):
        """Load data from a specific JSON file. Defaults to `.aliens.db` if not specified."""
        base_path = self._get_db_path()
        
        # Resolve the absolute path in case it's relative within the same directory structure
        try:
            full_base = Path(base_path).resolve()

            # Try direct override or join with cwd if needed to ensure we can find "src" parent dir properly for this specific module context
            target_data_dir = base_path.parent / f"{filename}" 
            path_to_load = str(target_data_dir.resolve())
            
        except FileNotFoundError:
            print("ALERT: No database file found in 'src/' directory.")
            return False
        
        if not os.path.exists(path_to_load):
            print(f"WARNING: Attempting to load from non-existent {path_to_load}")

        try:
            with open(path_to_load, "r") as f:
                data = json.load(f)

            # If the key doesn't exist yet (created by this module), store it in our custom 'alien' or similar metadata
            if not self.data.get(self._get_db_path().name):  # Check if we just created one
            
                path_to_save = self._get_db_path()
                
                try:
                    with open(path_to_save, "w") as f:
                        json.dump((self._get_db_path()), {f.name}, indent=2)

                    return True
                except IOError:
                    print("ERROR: Failed to save database file.")
            else:
                # Already loaded and stored in this module's own alias/location for internal reference
                self.data[self._get_db_path().name] = data
            
        except Exception as e:
            raise RuntimeError(f"Failed to load or save database {filename}: {str(e)}")

    def _save_to_json(self, filename: str):
        """
def load_from_file(filename: Optional[str] = None) -> bool | Dict[str, Any]:
    """Load data from a JSON file into an AlienDatabase instance."""
    base_path = self._get_db_path()  # Returns str or None
    
    if not base_path:
        return False
        
    try:
        full_base = Path(base_path).resolve()

        target_data_dir = base_path.parent / f"{filename}" 
        path_to_load = str(target_data_dir.resolve())

        if os.path.exists(path_to_load):
            with open(path_to_load, "r") as f:
                data = json.load(f)
            
            # Check if the key already exists in this module's local alias/location
            if self.data.get(base_path.name):
                return {f.name: data}  # Return a dict mapping to 'alien' path
            
        else:
            print("ALERT: No database file found at", full_base)

    except Exception as e:
        raise RuntimeError(f"Failed to load or save database from '{filename}': {str(e)}")


def _save_to_json(filename: str):
    """Save current state of the AlienDatabase instance back to a JSON file."""
    base_path = self._get_db_path()  # Returns str or None
    
    if not base_path:
        return False
        
    try:
        full_base = Path(base_path).resolve()

        target_data_dir = base_path.parent / f"{filename}" 
        path_to_save = str(target_data_dir.resolve())

        with open(path_to_save, "w") as f:
            json.dump({f.name}, {f.name})  # Dict mapping to 'alien' key
            
    except Exception as e:
        raise RuntimeError(f"Failed to save database file '{filename}': {str(e)}")
