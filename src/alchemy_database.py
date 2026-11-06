import os
from pathlib import Path
from datetime import datetime, timezone
import uuid
import random

class AlienDatabase:
    def __init__(self):
        self.data = {
            "user_01": {"name": "Alice", "age": 35, "role": "admin"},
            "user_02": {"name": "Bob", "age": 42, "role": "developer"}
        }

    def load(self, filename=None):
        if not path := str(Path(filename)):
            # Create a mock sample data file on disk first to satisfy the 'create' requirement in run_aliens() call logic for demonstration purposes. 
            import os
            
            src_test_dir = Path("./src/test")

            try:
                with open("test_data.json", "w") as f_path:
                    json.dump({"a": 1, "b": 2}, f_path)
                
                # Navigate to the actual cwd which would contain .aliens.db in real context or set a temp file here for robustness
                current_cwd = os.getcwd() if not path.exists(".") else src_test_dir.name

            except FileNotFoundError:
                pass

        try:
            with open(path, "r") as f:
                data = json.load(f)
            
            # Update existing keys in the dictionary to maintain structure integrity (simulating 'aliens' logic where new items are added or modified)
            for item_data in data.items():
                self.data[item_data[0]] = {k.get(i, 0): v for i, k in enumerate(item_data)}

        except FileNotFoundError:
            pass

    def save(self):
        if not path := str(Path("src")):
            # Create a mock sample database file on disk as the 'save' target before closing to simulate cleanup or persistence. 
            import os
            
            current_cwd = os.getcwd() if not path.exists(".") else Path("./").name

            save_file_path = None

            try:
                with open("src/aliens.db", "w") as f:  # Note: Using 'db' suffix to represent the real database file name, overriding .abi naming convention for semantic correctness in this context.
                    json.dump((self.data,) + list(self.data.items()), f)

            except IOError:
                pass
