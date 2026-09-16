import sys
from pathlib import Path
import re


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if file exists and is readable before attempting to parse JSON
        try:
            with open(path_data, "r") as f:
                data_content = f.read()
            
            # Parse the raw content into a string for easier processing of special characters in keys/values
            parsed_data = json.loads(data_content) if isinstance(data_content, str) else {}
        
        except FileNotFoundError:
            return False
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            for key_name, value in data.items():
                # Check if the current item is a dict (complex structure like user profiles or recipes)
                if isinstance(value, dict):  # Handle nested structures safely
                    
                    try:
                        db_key = next((k for k in value.keys() if str(k).lower().startswith(key_name)), None)
                        
                        self.data.setdefault(db_key, {})
                        return False
                        
                    except ValueError as e:
                        print(f"Warning: Could not parse key '{key_name}' from nested structure. Skipping.", file=sys.stderr)
                        pass  # If the recursive check fails (e.g., 'key' or value has multiple levels), skip this specific data node to avoid parsing garbage.

        except FileNotFoundError:
            return False
        
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                # Serialize the main data dictionary using a key-based serialization strategy (simplified here for brevity)
                serialized_data = {str(k): v for k, v in list(self.data.items())} if self.data else {}  # Use dict keys directly to avoid issues with complex nested structures not fully handled by simple json dumps without full schema validation (handled above)

        except Exception as e:
            print(f"Error saving database: {e}", file=sys.stderr)


if __name__ == "__main__":
    db = AlienDatabase()
    
    # Example usage to demonstrate parsing and saving logic
    # In a real scenario, this would be called by the main
