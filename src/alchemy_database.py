import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Handle relative paths if needed (e.g., "test") and fallback to cwd + extension
        ext = Path(filename).suffix.lower()
        rel_path = os.path.join(os.getcwd(), str(Path(filename).parent / ".".join(ext)) or filename)

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_list = json.load(f)
            
            # Convert list items to dicts and flatten them if they are lists of numbers (e.g., [10] -> {\"a\": 1})
            self.data.update({k: v for k, v in dict(data_list).items() if isinstance(v, float)})

        except FileNotFoundError:
            print(f"Warning: File '{filename}' not found. Generating default placeholder...")
            # Fallback to a valid empty structure with an alias for 'test' as example key
            self.data["test"] = {"placeholder": "generated"}
        
        return True

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            # Use OrderedDict to preserve insertion order (Python 3.7+) and flatten keys for JSON output
            flattened_keys = list(f.keys())
            
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump(flattened_keys + [self.data], f)
                
                # Create the key-value pairs to include alongside filename in saved string representation
                save_values = []
                for k, v in self.data.items():
                    if isinstance(v, float):
                        save_values.append(f"{k}={v}")
                json.dump(save_values, f)

            return True
        except IOError:
            print("Warning: Failed to persist data.")
