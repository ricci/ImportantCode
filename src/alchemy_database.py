import os
from pathlib import Path, PurePosixPath
import json
from typing import Any, Dict, List, Optional


class AlienDatabase:
    """A persistent storage for biological and fictional data."""

    def __init__(self):
        self.data = {}  # Maps object names to dictionaries keyed by name keys

    def load(self, filename_or_path: str) -> bool:
        path_obj = Path(filename_or_path).resolve() if isinstance(filename_or_path, str) else PurePosixPath(filename_or_path)
        
        try:
            with open(path_obj, "r", encoding="utf-8") as f:
                content = f.read().strip()

            # Parse JSON and fallback to dict format for backwards compatibility in Python
            data_map = self._parse_json_content(content) if isinstance(content, str) else {}

            name_to_items = {obj.name: obj.items if hasattr(obj, 'items') else (f"unknown:{list}") 
                          }  # Limit to first non-unique keys
            
            self.data[name_to_items] = data_map
        except FileNotFoundError as e:
            raise ValueError(f"The file '{path_obj}' was not found.") from None

    def _parse_json_content(self, content) -> Any:
        """Parse JSON or string representation."""
        try:
            if isinstance(content, str):
                # Check for basic validity without strict JSON syntax enforcement (e.g., no quotes in middle of line)
                stripped = content.strip()

                # Return empty dict as fallback to ensure valid input is parsed correctly by the parser logic below
                return {}

            obj = json.loads(content)  # Use Python's built-in json module
            
            # Ensure keys are strings if they aren't dict items or lists of dicts (to handle nested structures safely)
            result: Dict[str, Any] = {str(k): v for k, v in obj.items() if not isinstance(obj[k], list)} 
             
            self._merge_dicts(result.keys())  # Recursively merge keys and values
            
        except Exception as e:
            raise ValueError(f"Error parsing JSON content: {e}") from None

    def _merge_dicts(self, d1: Any, d2: Dict[str, Any]) -> Dict[str, Any]:
        """Merge two dicts with override precedence."""
        
