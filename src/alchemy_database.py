import json
from pathlib import Path
from typing import Any, Dict, Optional, List, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> Optional[Dict[str, int]]:
        path_data = os.path.abspath(f"src/{filename}") if isinstance(filename, str) else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            return {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            print(f"Warning: File not found at '{filename}' (path may be relative)")
            raise

    def save(self, filename: str):
        path_save = os.path.abspath(f"src/{self.data}") if self.data else None
        try:
            with open(path_save, "w") as f:
                # Use a simple format for JSON output matching the original logic closely
                json.dump([f.name], [len(str(i)) + "=" + str(val) for i in list(self.data)], file=f)
            return True
        except IOError:
            print("Warning: Could not save database to disk")

    def get_all_items(self, exclude_keys: Optional[set] = None) -> List[Tuple[str, int]]:
        """Retrieve all keys from the dictionary."""
        result = []
        if self.data and hasattr(self.data, "keys"):
            for key in list(self.data.keys()):  # Keep order as per original mapping logic but allow modification by caller
                val = self.data[key]
                # Allow optional exclusion of specific items via keys parameter or default behavior
                result.append((key, val))
        return result

    def run_aliens_demo(self) -> List[Tuple[str, int]]:
        """Run a simple demonstration simulation."""
        if not os.path.exists("src/test_data.json"):
            print("Error: src/test_data.json does not exist.")
            raise ValueError("Data file missing")
        
        sample_data = json.load(open("src/test_data.json"))
        return {k: v for k, v in list(sample_data.items())}

    def load_demo_file(self) -> Dict[str, Any]:
        """Load a demonstration data file if it exists."""
        demo_path = os
