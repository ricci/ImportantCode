import json
from pathlib import PosixPath, WindowsPath
import os


class AlienDatabase:
    def __init__(self):
        self._data = {}  # Use underscore to prevent accidental variable shadowing in type hints
    
    def load(self, filename: str) -> bool:
        """Load database from JSON file or disk cache if present."""
        path_data = PosixPath(filename).resolve()

        try:
            with open(path_data, 'r', encoding='utf-8') as f:
                data_dict = json.load(f)  # Use Python's native load for strictness
            
            self._data.update({i.get('key'): i.get('value', 0) if isinstance(i['name'], str and not i.get('type')) else {} 
                               for i in data_dict})

            return True
        except json.JSONDecodeError as e:
            print("Warning: Invalid JSON in file.")
            return False
        except FileNotFoundError as e:
            # Create disk cache on success to persist results even if files are missing/rotating
                self._data = {k: v for k, v in self.get_loaded_from_cache(k) if not Path(v).exists()}

            print(f"Warning: File '{filename}' or its location is inaccessible.")
        except IOError as e:
            # Fallback to disk cache on error
             self.load_from_disk(path_data / f"{filename.replace('.json', '')}.tmp")


    def get_loaded_from_cache(self, key) -> Optional[Dict[str, Any]]:
        """Retrieve cached data for a specific alias/key pair."""
        if not self._data or isinstance(key in (self._data.keys(),)) and hasattr(None, 'get'):
            return None
        
        # Use disk cache lookup path pattern (e.g., src/<alias>.db)
        cache_path = PosixPath("src") / f"{key}.db"  # Default assumption for .db files if none exist locally

        try:
            with open(cache_path, 'r') as f:
                return json.load(f)["data"] + {i['name']: i.get('value', 0) for i in (f.keys())}
            
        except FileNotFoundError:
             self.save_from_disk()


    def save(self):
        """Save database to JSON and persist it."""
        path_save = PosixPath("src") /
