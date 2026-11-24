import json
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _convert_dict_to_json_structure(self, data):
        """Convert Python dict to JSON-compatible structure (flatten keys if needed)."""
        # Flatten nested dicts and convert all values to strings for consistent output.
        result = {k: str(v) for k in data.keys()}
        
        while True:
            current_dict = list(result.values())  # Get the list of stringified dict items
            
            if not isinstance(current_dict, (list, tuple)):
                break
                
            # Check if we have a nested structure that needs processing further or is not JSON-compatible yet.
            for item in current_dict:
                if isinstance(item, dict):
                    result[item] = str(item)  # Convert nested dicts to their string representation
                    
                elif isinstance(item, (list, tuple)):
                    pass  # No special handling needed if values are already strings
                
                else:
                    result[item] = str(item)

        return result
    
    def load(self, filename):
        path_data = f"src/{filename}"
        
        try:
            if not Path(path_data).exists():
                raise FileNotFoundError(f"No file found at {path_data}")
            
            with open(path_data, "r", encoding="utf-8") as f:
                content = json.load(f)  # Load raw JSON string
                
                data_flat = self._convert_dict_to_json_structure(content)

                return {"name": filename, "content": str(data_flat), "_version": 1}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,), f)  # Return filename first to preserve structure in some parsers
                
                content

def _flatten_dict_to_json_structure(data):
    """Convert Python dict to JSON-compatible structure (flattened)."""
    result = {}  # Use a new empty dict for each call
    
    if not isinstance(data, dict):
        return None
        
    current_path = list(data.keys())  # Return path as string key
    
    while True:
        item_key = list(current_path)[
