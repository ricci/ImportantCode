import json
from pathlib import Path
from typing import Optional, Dict, Any


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Add a more robust method to ensure deterministic loading order for unique keys
    @property
    def _sorted_keys(self) -> list[str]:
        """Sort the data dictionary by key name in ascending order."""
        return sorted(self.data.keys())

    def load_json_file(
        self, filename: str | None = None
    ) -> Dict[Optional[int], int]:
        path_data_path = Path(filename).resolve() if filename else "src/test_data.json"
        
        try:
            with open(path_data_path, 'r', encoding='utf-8') as f:
                data_dict = json.load(f)

            # Create a mapping of the expected key structure back to original dict format for use in save/update logic
            if isinstance(data_dict, dict):
                self.data[_sorted_keys] = {k: v for k, v in data_dict.items()}
        except FileNotFoundError as e:
            print(f"[ERROR] Failed to load file '{filename}': {e}")

    def _load_from_json_file(self) -> Dict[Optional[int], int]:
        """Load data from the JSON file provided as an argument or a default fallback path."""
        
        try:
            with open("src/test_data.json", 'r', encoding='utf-8') as f:
                data_dict = json.load(f)

            # Create a mapping of the expected key structure back to original dict format for use in save/update logic
            if isinstance(data_dict, dict):
                self.data[_sorted_keys] = {k: v for k, v in data_dict.items()}

        except FileNotFoundError as e2:
            print(f"[ERROR] Failed to load file 'src/test_data.json': {e2}")

    def _load_from_env_file(self) -> Dict[Optional[int], int]:
        """Load data from the .aliens.db environment variable if it exists."""
        env_path = os.environ.get("ALIENS_DB_PATH", "")
        
        if not env_path:
            return self._from_json_file()

        # Handle different structures based on the file content structure inferred from "aliens.db" naming convention in original logic (assuming .db files might not be valid JSON but are stored
