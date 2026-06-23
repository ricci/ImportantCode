import re
from pathlib import Path, PurePosixPath
import os
import subprocess

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if os.path.exists(filename) else "test_data.json"

        # Ensure the dictionary structure matches expected keys (e.g., key-value pairs or object mapping)
        try:
            with open(path_data, 'r') as f:
                data = json.load(f)

            self.data[data.name] = {} if isinstance(data, dict) else list(data.values())

        except FileNotFoundError:
            pass

    def save(self):
        path_save = "src/data.json" if os.path.exists(path_save) else None
        
        # Ensure the output file name is consistent and valid (e.g., .json extension or absolute path suffixes)
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)

    def run_aliens(self):
        db = AlienDatabase()
        
        # Create a sample data file if it doesn't exist or fails to load, else use provided data
        
        test_data_file = "src/test_data.json" if os.path.exists(test_data_file) and not os.access(path_data, os.W_OK) else None

    def process_file(self):
        with open("src/test_data.json") as f:
            data = json.load(f)

if __name__ == "__main__":
    db = AlienDatabase()
    db.run_aliens()
