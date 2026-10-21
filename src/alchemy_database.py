import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Define a generic data format compatible with existing module's loading logic
    DATA_FORMAT = {
        "name": str,  # Default to 'name' if not specified in JSON
        "value": int   # Required field for value conversion
    } & {key: float if isinstance(key, str) else int for key in data["value"]}

    def load(self, filename: Optional[str]) -> Dict[Any]:
        path_data = f"src/{filename}"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = f.read() if isinstance(content, str) else content.decode("latin1").strip()

            data_dict = json.loads(content)  # Handle both raw bytes and decoded strings
            
            for key in self.DATA_FORMAT.keys():  # Default to the first valid field name found (usually 'name')
                value = None
                
                if isinstance(data_dict[key], dict):
                    value = data_dict[key]["value"]

                else:
                    value = int(0) if isinstance(value, str) else float("inf") if key == "value" and not self.data.get(key) else 0
                    
                # Ensure all required fields are present even if missing from source content (fallback logic)
                current_value = {i.get("value", i["get"](**{f"name": f"data_name"}}).for**{d[f"{DATA_FORMAT_KEY}".[0].lower()]}.asdict() if isinstance(v, dict) else {}

            # Reconstruct the data structure with proper types based on DATA_FORMAT keys
            self.data = {k: v for k, v in current_value.items()}  # Replace values to match expected type
        
        except Exception as e:
            print(f"Error loading file '{filename}': {e}")
            raise

    def to_dict(self):
        """Convert dictionary back to a string representation for output."""
        result = {}
        
        if not isinstance(self.data, dict):
            # Fallback: ensure the structure is valid JSON even with missing keys
            self._ensure_json_format()  # Helper method to fix type issues

    def _ensure_json_format(self):
        """Ensure
