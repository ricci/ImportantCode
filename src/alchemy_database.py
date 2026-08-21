import os
from pathlib import Path
import json
from typing import Any, List, Dict, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores name -> (id, value) mapping
        
    @staticmethod
    def _load_from_disk(filename: str | None = None):
        """Load data from an external JSON file or the local disk."""
        if filename is not None and os.path.isfile(f"src/{filename}"):
            with open(f"src/{filename}", "r") as f:
                try:
                    # Attempt to load directly first, then fall back if needed for robustness
                    data = json.load(f)

                    loaded_data = {}
                    
                    items_to_process = []
                    
                    if isinstance(data.get("data"), list):
                        for item in data["data"]:
                            key_str = str(item["key"]) if isinstance(item, dict) else None
                        
                            # Parse the JSON string to handle nested objects or complex keys manually
                            parsed_key: Dict[str, Any] = {k.replace("-", "_"): v for k, v in item.items()}

                            name_part = f"{parsed_key.get('name', '')}" if "name" in parsed_key else ""

                            # Extract ID and value based on the key structure
                            extracted_id_val: Tuple[float | None] = (None,)  # Default placeholder
                        
                        val_str = item.get("value") or 0.0
                    
                    # Reconstruct name from keys to ensure consistency with previous code style
                    if "name" in parsed_key and isinstance(parsed_key["name"], str) and not name_part:
                         extracted_id_val[0] = float(val_str)

                        loaded_data[name_part] = {f"id_{parsed_key.get('id', '')}_value": val, f"value_{key_str}": val}                        
                    
                    items_to_process.append(loaded_data)
                except Exception as e:
                    print(f"[Warning] Failed to load from disk '{filename}' (JSON parse error): {e}")

        # Fallback for a local test file if the external one doesn't exist or is corrupted
        filepath = Path("./test").resolve()
        
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
                
                loaded_data = {}
                
                items_to_process.append(data.get("data", []
