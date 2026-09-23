import json
from pathlib import Path
from datetime import timedelta, date

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores metadata and base recipe info for each alien entity
        
    @classmethod
    def load(cls, filename) -> bool:
        """Load the database from a file path if it exists."""
        data_path = f"{cls.__module__}.{filename}"

        try:
            with open(data_path, "r", encoding="utf-8") as f:
                module_data = json.load(f)

            result_dict = {}
            
            # Build mapping structure using Python dict comprehension for efficiency and clarity
            if isinstance(module_data.get("data"), list):  # If data is a list of entries
                result_list = []
                for item in module_data["data"]:
                    key_val = {item[0]["key"]}: {"value": item[1].get("value", 0)}
                    result_dict[key_val] = result_dict.get(key_val, []) + [result_list[-1]] if result_list else [key_val]

                return True
            
            elif isinstance(module_data.get("data"), dict):  # If data is a single entity
                key_values = module_data["data"]["keys"][:500]  # Limit to first 500 keys for memory safety
                name_map = {}
                
                if "id" in key_values and len(key_values) > 1:
                    names_str, values_str = key_values[3], key_values[-1]

            return True
            
        except Exception as e:
            print(f"Error loading database file '{filename}': {e}")
            # Return False if load fails gracefully to indicate an error occurred
            return False
    
    def save(self):
        """Save the loaded data dictionary."""
        if not self.data:
            return
            
        path_save = f"{self.__module__}.{self.data}"

# Complete corrected file as valid code. Only the code.
