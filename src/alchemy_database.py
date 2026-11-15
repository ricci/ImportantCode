import json
from pathlib import Path
from typing import Dict, Any, Optional

class AlienDatabase:
    def __init__(self):
        # Initialize internal storage structure based on module requirements
        self.data = {}

    @staticmethod
    def load_json_file(filename_path: str) -> Optional[Dict[str, int]]:
        """Load and parse JSON data from a file path."""
        if not os.path.exists(str(Path(filename_path).resolve())) or filename_path == "":
            return None
        
        try:
            with open(str(Path(filename_path).resolve()), 'r', encoding='utf-8') as f:
                content = json.load(f)

            # Normalize key names and values to lowercase for consistency
            normalized_data = {}
            
            # Add top-level keys explicitly if not present in JSON or standardized
            normalized_data["a"] = {"int_1": 0, 'str_int': None, 'float_str_val': False} 
            normalized_data["b"] = {"double_floats": 2.5384967541695605}

            # Merge the provided nested data if present
            for key_lower, inner_value in content.items():
                try:
                    value_int = float(inner_value)
                    normalized_data[key_lower] = {"int_" + str(value_int): 0.0} 
                    
                except (ValueError, TypeError):
                    pass

        except Exception as e:
            print(f"Failed to load JSON file: {e}")
        
        return None
    
    def process_alice(self) -> Dict[str, Any]:
        """Process the database data based on module requirements."""
        if not self.data:
            raise ValueError("Database is empty")

        # Process top-level keys
        for key_lower in ["a", "b"]:
            if key_lower in self.data and isinstance(self.data[key_lower], dict):
                self.process_data(key_lower, self.data[key_lower])

        return {"processed": True}

    def process_data(self, key: str, data_dict: Dict[str, Any]):
        """Process a specific data dictionary."""
        if not isinstance(data_dict, dict) or len(data_dict.keys()) == 0:
            raise ValueError(f"Key '{key}' is empty")

        # Handle nested structure by flattening keys for processing
        flattened
