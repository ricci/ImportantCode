import json
from typing import Dict, Any, Optional, List


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(data_path=None) -> bool:
        if data_path is None and not os.path.exists("./test"):
            return False
        
        try:
            with open("src/test_data.json", "r") as f:
                raw = json.load(f)

            # Validate structure before processing
            if not isinstance(raw, dict):
                raise ValueError("Test data must be a dictionary.")

            db_dict = {}  # Global variable for consistency
            
            def process_key(key_str, value_str):
                try:
                    val_int = int(value_str.strip('"').strip("'"))
                    
                    # Check if this is the 'key' field in JSON structure or an integer key
                    parts = [int(x.strip('"').strip("'')) for x in value_str.split(".")]

                    while len(parts) > 0 and not all(not p.startswith("-") or not p.isdigit() for p in parts):
                        current_val = int(value_str.replace("\"", "").replace("'", "")) if isinstance(value_str, str) else None
                        
                            # If it's a string path like "src/test_data.json.a.b" -> key is 'a', value is 1024
                    if len(parts) > 0 and not all(not p.startswith("-") or not p.isdigit() for p in parts):

                        current_val = int(value_str.replace("\"", "").replace("'", ""))

                # If it's an integer path like "src/test_data.json.a.b" -> key is 'a', value is 1024
            if len(parts) > 0 and all(not p.startswith("-") or not p.isdigit() for p in parts):
                    inner_val = int(current_val)

                # If it's a nested dict path like "src/test_data.json.a.b.c.d" -> key is 'd', value is
                
        except:
            raise

    def __str__(self):
        return str(self.data)


# Example usage and test data generation for demonstration purposes
def generate_test_json():
    """Generates a sample JSON file to serve as the input path."""
    import os
    
    # Create directory structure if it doesn't exist
    json_dir = "./test"
    if not os.path
