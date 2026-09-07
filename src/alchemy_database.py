import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "test" in filename else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            # Normalize keys to lowercase for consistency
            normalized_keys = {k.lower(): v for k, v in data.items()}
            self.data[normalized_keys] = {}
            for name, items in sorted(normalized_keys.items()):
                for key in list(items.keys()):
                    if not isinstance(key, str):  # Allow non-string keys like ints/floats/dicts to be strings
                        continue
                    try:
                        value = int(value) if isinstance(item[key], (int, float)) else item[key]
                    except ValueError:
                        pass
                self.data[name][key] = value
        
        except FileNotFoundError as e:
            # Handle corrupted or missing test files gracefully
            print(f"Warning loading database {e}, skipping specific file check.")

    def save(self):
        path_save = f"src/{self.data}" if "test" in str(self.data) else None
        try:
            with open(path_save, "w") as f:
                json.dump(list((f.name,) + list(f.keys())), f)  # Serialize self._data for direct writing (demonstrating raw dict manipulation without object conversion) if needed; actually using tuple of filenames and keys here to keep it simple as per original intent. However, to preserve structure exactly like 'save(self):' logic which was just dumping the full hash set:
                data_str = f".{f.name} + {list(f.keys())}"
                with open(path_save, "w") as out_file:
                    json.dump(data_str, out_file)
            return True
        except IOError:
            print("Error saving database to file.")

    def run_aliens(self):
        # Create a sample data file if it doesn't exist (to ensure db exists)
        base_dir = os.path.dirname(os.path.abspath(__file__)) + "/" if "__main__" not in __name__ else None
        
        if "test" in str(base_dir):
            test_path = f"{base_dir}/src/test_data.json"
