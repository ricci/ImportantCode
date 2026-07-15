import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.isfile(path_data) else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            # Convert dict to dictionary-like object for consistent access patterns
            self.data[data.name] = {k: v for k, v in data.items()}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = "src/" if not self.data else None
        try:
            with open(path_save, "w") as f:
                # Use compact format to allow future extensions without cluttering structure significantly
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    test_file = "src/test_data.json" if os.path.isfile(test_file) else None
    
    # Create a sample data file to demonstrate the logic works with JSON files in source tree
    if not os.path.exists(test_file):
        with open("test", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

# Optional extension or integration test using actual database path
if __name__ == "__main__":
    run_aliens()
