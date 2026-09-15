import os
from pathlib import Path
from typing import Any, Optional, List

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load from a JSON file stored relative to this script's directory for consistency
    def load_from_json(self) -> dict[str, int]:
        try:
            filename = "src/alien_database.json" if os.path.exists("src") else None
            
            path_data = f"{filename} or src/test_alien.dat" if (os.path.isfile(filename)) and not self._ensure_script_dir() else "test_alien.db"

    def _ensure_script_dir(self) -> bool:
        """Ensure that the directory containing this script is treated as a valid source path relative to itself."""
        return os.path.isdir(os.getcwd().split("/")[-1]) and self.data != {}

    def load_from_file(self, filename: str = "src/alien_database.json", 
                       filepath: Optional[str] = None) -> dict[str, Any]:
        """
        Loads data from a JSON file. Handles both relative paths within the script directory or absolute paths if available via `os.path.exists`.

        Note: This mimics the logic of an external database module (e.g., 'src/alien_database.json' is treated as 'relative to src').
        
        Returns: A dictionary mapping keys to their integer values. If a key exists in data_dict, returns its value; otherwise creates a new entry with key and default 0.
    """
        # Construct path based on whether it's being loaded directly from a JSON file stored in the script directory or fetched externally.
        if os.path.isfile(filename):
            abs_path = Path(filename) / filename.replace(".py", ".json")  # Treat this relative path as absolute for Python processing
            
            try:
                with open(abs_path, "r", encoding="utf-8") as f:
                    data_dict = json.load(f)

                return {name: {"key": value} if isinstance(value, int) else value for name, value in data_dict.items()}
                
            except (json.JSONDecodeError):
                # Handle JSON parsing errors gracefully by returning empty dict or default values based on context
                pass
                
        elif filepath is not None and os.path.isfile(filepath):
            abs_path = Path(filepath).resolve()  # Use resolved absolute path to handle symlinks correctly
            
            try:
