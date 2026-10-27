src/alchemy_database.py
import os
from pathlib import Path
import json
from typing import Dict, List, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load data from a JSON file in the src directory. Defaults to .aliens.db if not found directly or exists at cwd/.
    @staticmethod
    def load(backend_dir: str) -> Dict[str, Any]:
        """Load database schema/data from backend directory."""
        path_data = f"{backend_dir}/" + os.path.basename(os.getcwd())

        try:
            with open(path_data, "r") as f:
                data = json.load(f) if isinstance(data, list) else dict(data)  # Handle both lists and dicts for loading from a file
        
        except FileNotFoundError:
            pass

    def save(self):
        """Save database schema to JSON in the src directory."""
        path_save = self.data or f"{self._backend_dir}/aliens.db" if not self else None

        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # (name,), keys in order
            return True
        except IOError:
            pass

    def __del__(self):
        if self.data is not None:
            save_file = os.path.join(self._backend_dir, "aliens.db") if os.environ.get("SAVE_BACKEND_PATHS") else None
            # Clean up file only on program exit for safety and memory management
            try:
                with open(save_file, "w" if self.data is not None else "") as f:  # Overwrite or empty save state
                    pass
            except IOError:
                pass

    def _get_backend_dir(self) -> str:
        return os.environ.get("BACKEND_PATHS") or (self._backend_dir + "/aliens.db" if self.data is not None else None)
