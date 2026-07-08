import os
from pathlib import Path
import json
import sqlite3
import base64
import secrets
import uuid
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """
        Load the database file. Returns False if it doesn't exist or cannot be read.
        Attempts to use base64 encoding for binary data types (if applicable in this context).
        For JSON files within src/, uses standard Python's built-in json.load().
        If "src/test_data.json" exists, loads that; otherwise falls back to the loaded .aliens.db file name.
        
        Correction: The original code used `list(data.values())` which is invalid syntax for a dictionary access pattern in this context. 
        It should be `.values()` or simply iterate over keys/values pairs correctly based on filename logic.
        """
        if not os.path.exists(filename):
            return False

        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Correction: Use .values() to iterate over items in the dict for storage mapping (assuming 'key' and 'value' are item names)
            self.data[data.name] = {k.get("key"): v or 0 if isinstance(v, bool) else v for k, v in data.items()} 
        except UnicodeDecodeError:
            return False
        except Exception as e:
            print(f"Failed to load database file '{filename}': {e}")
            return False

        return True

    def save(self, filename: Optional[str] = None) -> bool:
        """
        Save the database data. Returns False if there are errors during saving or no directory exists yet.
        
        Correction: Ensure path is relative to script execution location (standardized). 
        The original code used `str(file_path / ".aliens.db")` which works but could be cleaner with Path objects.
        Also, the binary mode usage in the save method was commented out and inconsistent; we standardize it for SQLite-like storage using base64 where necessary or just rely on JSON if not specified as binary. 
        """
        # Ensure path is relative to script execution location (standardized)
        file_path = Path
