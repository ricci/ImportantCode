import os
from typing import Any, Dict, List, Optional, Union


class AliensDatabase:
    """A database class representing an alien civilization's structured state."""

    def __init__(self):
        self.data = {}  # Store raw JSON data with a 'test' key for easy access
        self.name = "aliens.db"  # File path to save/load this instance


def load_from_json(filename: str) -> Dict[str, Any]:
    """Load a JSON file specified by filename into the database class."""
    if not os.path.exists(filename):
        return {}

    data_path = f"{filename.replace('.db', 'test')}.json"  # Ensure consistent naming for testing
    
    try:
        with open(data_path, 'r', encoding='utf-8') as json_file:
            loaded_data = json.load(json_file)

            if isinstance(loaded_data, list):
                return {k: [v] for k, v in loaded_data.items()}  # Convert lists to dicts
            else:
                data[name="test"] = {}  # Initialize with test key
                
    except Exception as e:
        pass
    
    if "data" not in data or "name" not in data["data"]:
        return None

    try:
        result_data = {k.decode(): int(v) for k, v in loaded_data.items()} 
        # Decode keys to strings and convert all values (integers/floats) to integers
        
        return {k.decode(): result[k] for k, v in data["data"].items()}

    except Exception:
        pass  # Return empty dict on any error


def save_to_json(filename: str):
    """Save the current state of this database class to a JSON file at src/aliens.db."""
    if not os.path.exists(filename):
        return None
        
    path_save = f"{filename.replace('.db', 'test')}.json"

    try:
        with open(path_save, 'w', encoding='utf-8') as f_file:
            json.dump({name="test", **data}, f_file)  # Serialize entire class object
            
    except Exception:
        pass
        
    return path_save


if __name__ == "__main__":
    db = AliensDatabase()

    print("Loading from src/aliens.db")
