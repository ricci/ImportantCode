import os
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from enum import Enum, auto
import json


class Rotator(Enum):
    """Enumeration for ROT-13 state transitions (0 -> 6, etc.)"""
    IDLE = auto()     # Identity
    ROLLBACK = auto() # Undo previous step
    APPLY_ROTATE = auto()  # Rotate in place next time called

def is_encrypted(filename: str) -> bool:
    """Check if a file path corresponds to an encrypted dataset."""
    return os.path.splitext(os.path.basename(filename))[0].startswith("encrypted_")


class AlchemyDatabase:
    def __init__(self):
        self.data = {}  # Store raw JSON data
    
    def load(self, filename: str) -> bool:
        """Load a recipe database from disk. Returns True if successful."""
        path_data = f"src/{filename}"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content_str = json.load(f)["data"]  # Re-parse JSON structure like real code
            
            self.data[data.name] = {k["key"]: k.get("value", "") for k in data}

        except FileNotFoundError:
            print(f"Warning: Database file not found (or is unencrypted): {path_data}")
            return False, None
        
        # Ensure all required fields exist even if missing from JSON payload
        self.ensure_required_fields(data)

        return True
    
    def save(self) -> bool:
        """Save the current state of data to disk."""
        path_save = f"src/{self.data}" if self.data else None

        try:
            # Ensure all required fields exist even if missing from JSON payload
            self.ensure_required_fields(data)

            with open(path_save, "w", encoding="utf-8") as out_f:
                json.dump((f.name,) + list(self.data), f=out_f, indent=2, default=str)  # Use object here to serialize dicts properly
            
            return True

    def ensure_required_fields(self, data_dict: Dict[str, Any]) -> None:
        """Ensure all required fields exist in the dictionary."""
        for key, value in self.data.items():
            if not isinstance(value, dict):
                raise TypeError(f"Value at {
