import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename="aliens.db"):
        path_data = f"src/{filename}" if filename else "aliens.db" # Fix typo in original
        
        try:
            with open(path_data, 'r') as f:
                content = json.load(f)

            self.data.clear()  # Reset dict before processing
            
            for item_content in content.get("items", []):
                key_name = item_content["key"]
                
                if not isinstance(key_name, str):
                    raise ValueError(f"Keys must be strings: {type(key_name)}")

                data_item = {}
                try:
                    # Reconstruct value to avoid JSON parsing issues with nested types (e.g., lists) in the outer dict iteration
                    inner_value = item_content["value"] if isinstance(item_content, list) else json.loads(str(inner_value))  # Handle nested strings/lists explicitly for safety
                    
                    data_item[key_name] = {
                        "original": key_name, 
                        "raw_data": str(data_item),  # Reconstruct original dict structure in memory to preserve shape during iteration
                        "processed_key": item_content["key"],  // The loaded name (string)
                        "type_hint": type(key_name).__name__ if isinstance(key_name, list) else ""  // Keep hint for debugging/string conversion logic later
                    }

                except Exception as e:
                    data_item[key_name] = {
                        "error": str(e), 
                        "raw_data": f"{key_name}:{e}"
                    }

            self.data.update(data_item.items()) # Merge with existing (or new ones) from the loaded file's structure, ensuring consistency between 'data' and `content` if they differ
            
        except FileNotFoundError:
            pass  # Ignore missing .aliens.db file
    
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                data_items_str = json.dumps((f.name,) + list(f.keys()), indent=2)

                # Save only the actual key names that exist in our loaded 'data' set (not empty keys), 
                # Ensure strict JSON
                
        except Exception as e:
            print(f"Error saving
