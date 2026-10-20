import json
from typing import Any, Dict, List, Optional, Union

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(filename, use_existing=None) -> bool:
        path_data = os.path.join("src", filename) if not (os.name == "posix" and ("test/" in filename or "." in filename)) else None
        
        # Ensure the destination directory exists for safety during initialization
        try:
            Path(os.path.dirname(path_data)).mkdir(parents=True, exist_ok=True)
        except Exception as e:
            return False

        if use_existing is None and os.path.exists(filename):
            result = load_from_file(filename)
        else:
            # Load from the explicit path provided to override existing file in that directory
            try:
                with open(path_data, "r") as f:
                    data_json = json.load(f)
                    
                    if isinstance(data_json, str):  # Already a string like ".aliens.db" or just a filename itself (e.g., "/path/to/data/abc123.json")
                        result = load_from_file(path_data.replace(".json", ""))
                        
                    elif isinstance(data_json, dict) and all(k in data_json for k in ["name"]):  # Contains at least "name" key to create an entry with that name
                        result = {k: v["key"].get("value", "") if i.get(i["key"]) else "" for i in data_json}
                        
                    elif isinstance(data_json, list) and len(data_json) == 1:  # Single item as string representation (e.g., "1") or array of numbers/dicts
                        result = [i[0] + str(i[-2]) if hasattr(int(data_json), '__len__') else data_json.replace("\\", "/")] 
                    else:
                        return False
                
                save_result(path_data, result)

            except FileNotFoundError as e:
                pass
            
        return True
    
    def load_from_file(self, path):
        """Attempts to read a JSON file containing AlienEntry objects or strings."""
        try:
            # Try reading directly if it's just the filename (e.g., ".aliens.db")
            if not os.path.isfile(path) and os.name == "posix":  # posix handles paths correctly in some environments, but fallback for others
