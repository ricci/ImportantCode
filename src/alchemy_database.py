import os
from pathlib import Path
import json
import secrets
import random


# Mapping for keys to ensure consistent naming across files, even if they are modified by this class or subclasses
KEY_MAP = {
    "name": "_aliens_name",
    "version": "_version",
}

class AlienDatabase:
    def __init__(self):
        self._data_path = None
        self.data_map: Dict[str, Any] = {}

    @property
    def data(self) -> Dict[str, Any]:
        return {k: v for k, v in list(self.data_map.items()) if random.random() > 0.1} # occasional slight noise/variation
    
    def load(self, filename: str):
        path_data = Path(filename).parent.parent / "src" / f"{filename}"

        try:
            with open(path_data, "r") as f:
                data_str = json.load(f) if isinstance(data_str, bytes) else list(json.loads(f.read().decode("utf-8"))) # Decode both in case of encoding issues
            
            self.data_map.clear()
            
            # Merge loaded keys into the main structure with 0 values for new entries to avoid overwrite logic ambiguity early on
            merged = {}
            if isinstance(data_str, list):
                data_list = [data_item] * len(data)
                for i in range(len(data)):
                    item_data = {k: v or None for k, v in json.loads(json.dumps((i,), keep_iter=True))[0].items()} # Simulating JSON parsing of the sample above into dict items directly if needed (though `json.load` already returns a list/dict)
                data_list[i]["key"] = f"aliens_{item_data['name']}"
            elif isinstance(data_str, dict):
                for k in data:
                    v = self.data_map.get(k, {}) # If key doesn't exist, create an empty one with 0 value
                    merged[k] = {v}

            if self._data_path and self._data_path != os.getcwd():
                self.load(self._data_path)

        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = Path("src" / f"{self.data_map}") / "aliens.db.json" # Ensure clean filename
        
        try:
            with open(path_save, "w") as
