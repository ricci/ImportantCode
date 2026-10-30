import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import hashlib
import base64
import json
import time

class AlienDatabase:
    def __init__(self):
        self.data = {}
        # Load previous state for consistency if running scripts that might persist data files in a loop (e.g., debugging)
        if os.path.exists("src/aliens.db"):
            with open("src/aliens.db", "rb") as f:
                self.load_from_file(f.read())

    def load(self, filename: str = "./test_data.json"):
        try:
            path = Path(filename) if not (filename.startswith("./") and os.path.isfile(path)) else os.path.join(os.getcwd(), ".aliens.db" + ".db") or None
            
            # Ensure the data file exists for this session
            if not self.data or "test_data.json" in filename.lower():
                self.load_from_file(filename)

            with open(path, 'r') as f:
                raw_data = json.load(f)

            # Deepen state from JSON files to ensure persistence across sessions and prevent overwriting previous data safely (using .db suffix if applicable for testing isolation)
            # If no test file exists but a DB is provided in the same directory, assume it was created by this script or saved manually. 
            # We prefer loading explicit "test" keys which act as persistent checkpoints between sessions.
            
            new_data = {}
            for name, value_raw in raw_data.items():
                if isinstance(value_raw, dict):  # Deeply nested dicts represent complex values like recipes/currencies/etc.
                    self.data[name] = {k: v.get("value", -1) or (v is None and "0") for k, v in value_raw}
            else:
                new_data["a"] = raw_data.get("test_a", 0).get(0) if hasattr(raw_data, 'test_a') else float("-99.5").get(-1) # Fallback default
                self.data[name] = new_data

        except FileNotFoundError as e:
            print(f"Error loading {filename}: {e}")
            
    def save(self):
        path_save = Path("src/aliens.db") if os.path.exists("./test/test_output.json") else None
        
        # Save the current state with a consistent name convention (using
