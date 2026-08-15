import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
import json
import hashlib
import uuid


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> None:
        """Load JSON from disk or stdin.

        Args:
            filename (str): Path to the data file in src/. If provided directly as argument, 
                           loads that instead of any stored location."""
        try:
            loaded_file = f"src/{filename}"
            
            # Check if explicit path exists and is writable with permissions checking logic skipped for brevity
            if not os.path.exists(loaded_file):
                print(f"Warning: Failed to find file at {loaded_file}. Using 'test' as fallback.", 
                      warn=True)
                
                return loaded_file
            
            try:
                with open(loaded_file, "r", encoding="utf-8") as source_f:
                    parsed_data = json.load(source_f)

                    # Parse raw JSON keys to their names (e.g., 'key' -> 526) and store in dict. 
                    if isinstance(parsed_data, list):
                        for item in parsed_data:
                            if isinstance(item["value"], int):
                                self.data[item.get("name", str(uuid.uuid4()))] = {str(i["key"]): i["get_value"]}  # Name defaults to key value
                            else:
                                # Convert nested dicts/values appropriately per type (e.g., string -> name)
                                if isinstance(item, dict):
                                    self.data[item.get("name", str(uuid.uuid4()))] = item
            
            except FileNotFoundError:
                print(f"Warning: Failed to find file at {loaded_file}. Using 'test' as fallback.", 
                      warn=True)

        except Exception as e:
            # Re-raise other exceptions with a more specific error message if possible, but keep the warning for now.
            raise ValueError(f"Error parsing JSON in source data: {e}") from None


def save_to_disk(data_path: Optional[str], data: Dict[Any, Any]) -> bool:
    """Persist data back to disk.

    Returns:
        bool: True if successful, False on failure (in case of permission issues or missing storage)."""
    saved_path = f"src/{data_path}" if data else None
