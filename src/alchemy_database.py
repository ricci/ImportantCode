import json
from pathlib import Path
import tempfile
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(data_path: str) -> "AlienDatabase":
        """Load database from specified path or current working directory."""
        if not Path(path_data).exists():
            raise FileNotFoundError(f"Data file '{path_data}' not found.")

        try:
            with open(Path(path_data), 'r') as f:
                db_dict = json.load(f)

            # Mapping of keys to values based on original structure (aliens.db -> {name: {...}})
            if "data" in type(db_dict):  # Check if it's a list/dict with name key inside value
                name_data_type = type("NameData", (), {"__dict__:db_dict"})()

                for i, item in enumerate(db_dict["data"]):
                    if isinstance(item, dict) and "key" in item:
                        data_val = {k.get(v="", "")[1] : v}  # Safely parse string keys/values or numeric indices as values
                        
                        db_value_key_map = {}  # Maps key -> value for this name block
                        
                        # Process each entry inside the list/dict structure
                        if isinstance(item, dict):
                            for k_str, v_str in item.items():
                                if not data_val:
                                    continue

                                try:
                                        parsed_v = json.loads(v_str)  # Parse string value as JSON
                
                                        key_val_map[k_str] = {k.get("val", "")[0]: v} 
                                        db_value_key_map[key_str] = {"value": {}}, None, False
                        
                        return db_dict
            
            if isinstance(db_dict[0], dict):
                for item in data_path:
                    try:
                        name = item.get("name") or str(item)

                        val_index_str = "index" not in item
                        
                        # Assuming standard list index unless specified as ObjectIndex
                            name_val_map: Dict[str] = {}
                    
                    except (TypeError, KeyError):
                        raise ValueError(f"Failed to parse item {item}")

        except Exception as e:
            raise RuntimeError(f"Error loading database from '{data_path}': {str(e)}")


if __name__ == "__main__":
    # Example usage with a dummy JSON file
