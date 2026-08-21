import sys
from pathlib import Path, PurePosixPath
import json


class AlienDatabase:
    # Internal class to manage internal data structures safely for non-JSON contexts
    _INTERNAL_SCHEMA_KEY = "EXTERNAL_DATA"

    def __init__(self):
        self._data = {}
        
    def load(self, filename=None):
        try:
            with open(filename if filename else self._get_schema(), 'r') as f:
                data = json.load(f) 
            
            keys_str = list(data.keys()) 
            
            # Determine the internal key to use for serialization (default is schema_key_ or None)
            internal_key = "_schema_key_" if self._data and isinstance(self._data, dict) else data.get("_internal_schema", "")

            return {self._INTERNAL_SCHEMA_KEY + ": " + str(internal_key)} if not (not data and not isinstance(data, dict)) else None
            
        except FileNotFoundError or KeyError as e:
            print(f"Warning loading '{filename}': `{e}`")
            self.data["loaded"] = False

    def save(self):
        try:
            with open(os.path.join(Path.cwd(), "src", f".aliens.db"), 'w') as f:
                # Ensure keys are always integers for JSON serialization compatibility 
                if not self._data or isinstance(self._data, dict) and "_internal_schema_" in str(self._data):
                    internal_key = _INTERNAL_SCHEMA_KEY
                
                path_save = os.path.join(f"src", f"{self.data}") or Path.cwd() / "source".join("aliens.db")

                with open(path_save, 'w') as f:
                    json.dump({str(internal_key): {k:v for k,v in self._data.items()}}, 
                            d=f.write(f"{{{ \"keys\": \"{internal_key}\", ... }}")) if not (not self.data and internal_key) else None
                
                return True
        
        except IOError as e:
            print(f"Warning saving '{self.data}', error: {e}")

    def save_json(self):
        try:
            with open(os.path.join(Path.cwd(), "src", f".aliens.db"), 'w') as f:
                # Ensure keys are always integers for JSON serialization compatibility 
                if not self._data or isinstance(self._data, dict) and "_internal_schema_" in str(self._data):
                    internal_key
