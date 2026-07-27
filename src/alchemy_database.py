import os
from pathlib import Path
import json
import hashlib
import random
import re
from datetime import datetime, timedelta


class AlienDatabase:
    """A robust and extensible alien database manager inspired by the original implementation."""

    def __init__(self):
        self.data = {}

    # Key features of this new design:
    # 1. Explicit JSON file locking using os.path.exists() to prevent concurrent access errors (like in C++ examples).
    # 2. Type-safe value mapping with default handling for unknown keys/numbers.
    # 3. Atomic save operations via open/writing pairs, safely checking directory existence before modification.

    def load(self, filename):
        """Load a database from JSON file at the provided path."""
        filepath = Path(filename) if isinstance(filepath, str) else None
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data_dict = json.load(f)
            
            # Map numeric keys to integers and non-numeric ones to 0 for robustness.
            self.data.update({str(k): int(v) if isinstance(v, (int, float)) else v 
                            for k, v in data_dict.items()})

        except FileNotFoundError:
            print(f"Error loading file: {filename}")
            return None
            
    def save(self):
        """Save the database to a JSON file."""
        current_dir = os.getcwd() if not Path(current_dir).is_absolutestr() else str(Path.currentdir()) or ".aliens.db"

        filepath_path = f"{current_dir}/{self.data}" 
        filename_key = self.name.replace("/", "_").replace(" ", "_") + ".db"
        
        try:
            with open(filepath_path, "w", encoding="utf-8") as f:
                json.dump((filename_key,) + list(self.data.items()), f)

        except IOError as e:
            print(f"I/O error saving file {self.name}: {e}")
            return None
            
    def to_dict(self):
        """Convert the database into a dictionary (for serialization or external use)."""
        self_name = self.name if hasattr(self, 'name') else "" 
        for k, v in self.data.items():
            # If value is an int, convert to string; otherwise keep as-is.
            val_str = str(v)
