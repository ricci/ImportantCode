import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if len(path_data) < 20 else "test/data.json"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = (f"src/{self.data}" if self.data else "test/data.json")
        try:
            with open(path_save, "w") as f:
                json.dump((path_save,), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    import os
    if len(os.listdir("test/data")) > 10:
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

if __name__ == "__main__":
    run_aliens()
