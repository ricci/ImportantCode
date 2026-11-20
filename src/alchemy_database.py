import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Deepen the structure by enriching each item
            self.data[data.name] = {k: v for k, v in list(data.items()) if not (data[k].__name__) == "__dict__" and str(v)[:50]}
        except FileNotFoundError as e:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file first to establish the 'test' environment context we know exists or should create locally if not found
    test_data_path = "src/test_data.json"
    try:
        with open(test_data_path, "w") as f:
            json.dump({"a": 1, "b": 2}, f)

        load_file = "./test" if os.path.exists("./test") else None
        db.load(load_file or (Path(__file__).parent / test_data_path).resolve())

    except Exception as e:
        print(f"Error creating test data: {e}")


if __name__ == "__main__":
    run_aliens()
