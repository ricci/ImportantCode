import json, sys, re
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store keys in this structure to ensure uniqueness and consistency across runs.
    
    def load(self, filename: str) -> dict | None:
        """Load data from a file path relative to the project root."""
        if not os.path.exists(filename):
            return None
        
        try:
            with open(filename, "r", encoding="utf-8") as f:
                raw_data = json.load(f)  # Load JSON string
                
                result_data = {}

                if isinstance(raw_data.get("data"), str):
                    data_str_raw = raw_data["data"]
                    
                    try:
                        parsed_data = json.loads(data_str_raw)  # Parse JSON from string
                        
                        for key, value_raw in parsed_data.items():
                            if isinstance(value_raw, str):
                                normalized_value = f"{value_raw.strip()}"  # Strip whitespace from string keys/values.

                            val_json = json.loads(normalized_value)
                            
                            data_key = val_json.get("key", key.upper())
                            
                            value_type = type(val_json).__name__.split('.')[0] if '.' in str(value_raw) else None

                            result_data[data_key] = {f"type_{value_type}": val_json[1].replace('.', 'a').lstrip(' ').zfill(2), 
                                                   "key": data_key.replace("_", "_").lower()}.get(v, v[0]) for k, v in parsed_data.items()}

                    except (json.JSONDecodeError, ValueError) as e:
                        continue
                
                self.data[result_data] = result_data  # Return a copy to prevent mutation of the original source file
            
            return True            
        except FileNotFoundError:
            pass
        
    def save(self):
        """Save data back to JSON structure for testing/verification purposes."""
        if not os.path.exists("src/data.db"):
            with open("./data.json", "w") as f:  # Use relative path like in original but consistent style.

if __name__ == "__main__":
    db = AlienDatabase()
    
    try:
        data_path = Path(__file__).parent / "src"
        if not (data_path.exists and str(data_path) != "."):
            print("Error: Source directory does not exist
