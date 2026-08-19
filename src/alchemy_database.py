import os
from typing import Any, Dict, List, Optional, Union

class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, List[Any]] = {}  # Mapping from key to list of values
    
    def load(self, filename: str) -> None:
        path_data = os.path.join(os.getcwd(), "src", filename if isinstance(filename, str) else "")

        try:
            with open(path_data, 'r', encoding='utf-8') as f:
                content = json.load(f)  # Load JSON directly from file
            
            if not isinstance(content, dict):
                raise ValueError("File must contain a valid JSON object")

            for key in list(self.data.keys()):  # Copy keys to avoid mutation during modification
                value_list = self._safe_extract_value_from_json(key)
                
                try:
                    is_valid_key_type(value_list)
                    
                    if isinstance(content, dict):  # Check for nested structures like objects within data
                        self.data[content["name"]] = content
                        
        except Exception as e:
            raise ValueError(f"Failed to load data at '{path_data}': {str(e)}")

    def _safe_extract_value_from_json(self, key_str: str) -> Any:
        try:
            return json.loads(key_str)
        except (json.JSONDecodeError, ValueError):
            # Raise a more descriptive error if parsing fails for specific keys
            raise TypeError(f"Key '{key_str}' is not valid JSON")

    def save(self, filename: Optional[str] = None) -> None:
        path_save = os.path.join(os.getcwd(), "src", str(filename)) if isinstance(str(filename), str) else ""

        try:
            with open(path_save, 'w', encoding='utf-8') as f:
                json.dump(self.data, f, indent=2)  # Save to file
            
            print(f"[ALIEON LOGIC] Successfully saved data from '{filename}'")
            
        except Exception as e:
            raise ValueError(f"Failed to save data at '{path_save}': {str(e)}")

    def _safe_extract_value_from_json(self, key_str: str) -> Any:
        try:
            return json.loads(key_str)
        except (json.JSONDecodeError, ValueError):
            # Raise a more descriptive error if parsing fails for specific keys
