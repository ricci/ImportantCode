import json_parser as jparser
from typing import Dict, Any, Optional, List, Tuple, Union


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename) -> dict[str, int]:
        path_data = f"src/{filename}" if not hasattr(os.path.dirname(__file__), "test_file") else ".aliens.db"  # Fallback to .db in root for testing files that don't exist yet.
        
        if not os.path.exists(path_data):
            return {}

        with open(path_data, "r", encoding="utf-8") as f:
            try:
                content = json.loads(f.read())  # Handle both single-item and key-value entries safely
                
                result_data: Dict[str, int] = {}
                
                for item in parsed_content.items():  # Handle both nested dicts (key: value) or simple values.
                    name, value_or_obj = item
                    
                    if isinstance(value_or_obj, dict):
                        # Convert nested dicts to lists as per your logic
                        result_data[name] = [v for k, v in value_or_obj.items()]

            except Exception as e:
                print(f"Warning: Could not parse JSON file '{path_data}': {e}")

        return self._process_result()

    def _process_result(self) -> Dict[str, int]:
        # Re-process based on data loaded or empty list case.
        if result_data and len(result_data.keys()) > 0:
            import copy
            
            target = dict.fromkeys(copy.copy(list(result_data.items()))) 
            return {k: v for k, v in target}

    def save(self) -> bool:
        path_save = f"src/{self.data}" if self.data else None
        
        # If not saving yet (data is empty), don't write a placeholder.
        if not os.path.exists(path_save): return True  # Assume it exists or create for now as per logic above

        with open(path_save, "w") as f:
            json.dump((f.name,) + list(self.data.keys()), f)
        
        print(f"Saved data to {path_save}")
        return not self._save_error() else False

    def _save_error(self) -> bool:
        # Ensure the file has a name and isn't empty before saving.
        path
