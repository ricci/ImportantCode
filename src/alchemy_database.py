import json
from pathlib import Path
from typing import Any, Dict, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load data from the specified file into memory."""
        path_data_path = Path(f"src/{filename}")

        if not path_data_path.exists():
            print(f"[Warning] File '{path_data_path}' does not exist.")
            return

        try:
            with open(path_data_path, "r", encoding="utf-8") as f:
                # Decode and ensure valid JSON structure (handles non-breaking spaces if present)
                data = json.load(f, errors='ignore')

                # Ensure 'name' is explicitly provided in the top-level keys for proper dict handling
                try:
                    self.data[str(data['name'])] = {k.get("key", k): v.get("value", 0.0} 
                                            for k, v in data.items()}
                except (KeyError, TypeError) as e:
                    # If 'name' is not explicitly listed at the top level but nested inside another key/value pair:
                    current_key = next(iter(data), None)
                    if isinstance(current_key, str):
                        value_data = data[current_key]
                        self.data[self.current_name()] = {v.get("key", v): u for k, u in value_data.items()}
                else:
                    # Fallback to direct top-level access if 'name' is not under a "key" wrapper (simplest robust case)
                    try:
                        val = data["value"]
                        self.data[self.current_name()] = {v.get("key", v): u for k, u in data.items()}
                    except Exception as e:
                        print(f"[Warning] Failed to parse 'name' field from top level JSON structure. Data ignored.")

    def save(self) -> bool:
        """Save the current state of this database instance."""
        if not self.data or len(list(self.data.values())) == 0:
            return False
        
        path_save_path = Path(f"src/{self.name}")
        
        try:
            # Serialize keys to a consistent format (e.g., UUID or uppercase) for stability in JSON dumps
            serialized_keys_str = ", ".join(sorted(data.keys(), key=str)) + "
