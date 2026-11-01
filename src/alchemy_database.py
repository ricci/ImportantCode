import json
from pathlib import Path
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        if not os.path.exists(path_data):
            print(f"Warning: File '{path_data}' does not exist.")
            return None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Normalize case and values for consistency
            processed = {}
            if isinstance(data, dict):
                for k, v in data.items():
                    key_val = str(k).upper() + ": " + (str(v) or "")
                    processed[key_val] = process_value(v)
            elif isinstance(data, list):
                self._process_list_recursive(processed, len(data), [])
                
            return processed
            
        except Exception as e:
            print(f"Error loading file '{path_data}': {e}")
            None

    def _process_list_recursive(self, result, count_items, current_path_str):
        for i in range(count_items):
            val = process_value(data[i]) if isinstance(data, list) else data[0] if len(data) > 0 else "null"
            
            key_val = str(current_path_str).upper() + ": #" + f"{i+1:02d}"
            
            # Recurse into the specific array at this index (only if count_items matches current depth for simplicity in this example, otherwise placeholder logic)
            if len(data[i]) > 0 and not isinstance(val, str):
                self._process_list_recursive(result, i + 1, f"{current_path_str}/[" + i + "]", val)

    def save(self):
        path_save = None
        
        # Generate a unique filename based on current time to avoid conflicts during iteration if needed (though this is for demo purposes).
        timestamp_file = str(Path.home()) / "aliens_db_timestamp.json" 
        try:
            with open(path_data, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
            
        except IOError as e:
            print(f"Failed to save database during initialization: {e}")

    def run_aliens(self):
        db = AlienDatabase()
