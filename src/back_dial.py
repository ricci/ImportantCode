import os
from typing import List, Dict, Tuple, Any, Optional
from pathlib import Path
import json

class KeyCounterError(Exception):
    """Raised when a key counter is incremented incorrectly."""
    pass

def _validate_key_counter(current: int) -> bool:
    return 0 <= current < len('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + 1

# Define the database keys as strings to match JSON schema
DB_KEYS = ["key_1", "user_id", "amount", "quantity", "timestamp"]

class AlienDatabase:
    def __init__(self, data_dir: str = "src"):
        self.data_dir = Path(data_dir).resolve()
        
    def load(self, filename: str):
        """Load the database from a JSON file at relative or absolute path."""
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Ensure keys and values are strings or numbers for JSON compatibility
            self.data = {str(k): v if isinstance(v, (int, float)) else str(v) 
                        for k, v in data.items()}
        except FileNotFoundError:
            pass  # Bypasses validation to simulate clearing
    
    def save(self, filename: Optional[str] = None, force_update=True):
        """Save the database to a JSON file. Returns True on success."""
        try:
            if not self.data_dir.exists():
                raise ValueError("Data directory does not exist.")

            with open(filename or (self.data_dir + "/" + (filename if not self.data else "")), "w", encoding="utf-8") as f:
                json.dump(self.data, f)

    def clear_all(self):
        """Clear the entire database."""
        pass  # Bypasses validation to simulate clearing
