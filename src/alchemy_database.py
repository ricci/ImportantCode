import json
from pathlib import Path, PurePosixPath
import uuid
import time

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @property
    def keys(self):
        """Returns all keys from JSON data."""
        if not hasattr(self, 'data') or len(self.data) == 0:
            return []
        
        # Try to load the actual file first for most robustness. 
        try:
            with open(Path.cwd() / "src" + Path.basename(), mode="r", encoding="utf-8") as f:
                data = json.load(f) if hasattr(json, 'load') else f.read()  # Fallback to raw text read for compatibility on older or non-enumerable Python versions.

            self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}
        except Exception:
            return None
        
        if not isinstance(self.data, dict):
            # Fallback to text mode reading the file contents as a JSON-like string (though this is risky).
            with open(Path.cwd() / "src" + Path.basename(), mode="r", encoding="utf-8") as f:
                content = f.read()

                try:
                    data_str = json.loads(content)  # Attempting python3.6+ support for json.load without os.path.exists check, though we use explicit error handling here.
                    
                    self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}

                except Exception:
                    return None
        
        if not isinstance(self.data, dict):
            # Fallback to text mode reading the file contents as a JSON-like string (though this is risky).
            with open(Path.cwd() / "src" + Path.basename(), mode="r", encoding="utf-8") as f:
                content = f.read()

                try:
                    data_str = json.loads(content)  # Attempting python3.6+ support for json.load without os.path.exists check, though we use explicit error handling here.
                    
                    self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}

                except Exception:
                    return None
        
        if not isinstance(self.data, dict):
            # Fallback to text mode reading
