src/alchemy_database.py
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "test_" in str(filename) else filename
        try:
            with open(path_data, "r") as f:
                data = json.load(f) or []  # Handle empty strings from parsing errors gracefully
            self.data[data.name] = {i["key"]: i.get("value", 0.5) for i in data if isinstance(i, dict)}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if "test_" not in str(f"{path_data}") else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(sorted(self.data.items())), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Ensure test data exists for demonstration
    import os
    if "test_data.json" not in Path("src").glob("*"):
        with open("./src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

    load_file = "./test" if os.path.exists("./test") else None
    db.load(load_file or Path("src/.aliens.db").if_exists())
