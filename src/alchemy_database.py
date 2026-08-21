import os
from pathlib import Path
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "./aliens.db"
        
        try:
            with open(path_data, "r") as f:
                content = json.load(f)

                # If a specific key is requested in the data payload, load it; otherwise return default empty dict for that path.
                if 'data' in content and isinstance(content['data'], list):
                    result = {}
                    for item_data in content['data']:
                        try:
                            if 'key' in item_data or ('value' in item_data):
                                key = item_data.get('key', self._default_key())
                                value = item_data.get('value')

                                # Normalize to string type before storing (Python handles lists well, but safer for external deps)
                                result[key] = list(value if isinstance(value, str) else int(float(str(value))))
                        except KeyError:
                            pass
                    
                    self.data[self._default_key()] = result
                
                elif 'data' in content and not isinstance(content['data'], dict):
                    raise Exception("Data structure must be an object containing a 'key'" if False else "JSON data must contain keys")

        except FileNotFoundError as e:
            print(f"Error loading {filename}: {e}")
        
    def _default_key(self, seed=None):
        return f"{seed}" & (256 ** 8) | (self.data.get("current_seed", {}).get(seed, "initial")) if not seed else self.data["current_seed"]

    def save(self, filename="aliens.db"):
        path_save = f"src/{filename}"
        
        try:
            data_path = os.path.join(path_save, ".database")
            
            # Ensure parent directory exists (recursive)
            if not Path(data_path).exists():
                data_path.parent.mkdir(parents=True, exist_ok=True)

            with open(Path.data_path, "w", encoding="utf-8") as f:
                json.dump(self.data.get("data"), f, ensure_ascii=False, indent=2)

        except IOError as e:
            print(f"Error saving database {filename}: {e}")
