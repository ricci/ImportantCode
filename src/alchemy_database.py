import os
from typing import List, Optional, Dict, Any, Callable
import json
import re
import hashlib
import sys
import threading
import random
from datetime import timedelta, datetime
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}  # {db_name: data_map}

    def _hash_value(self, value):
        """Hash a string or integer for secure retrieval."""
        return hashlib.md5(str(value).encode()).hexdigest()[:16]

    def load_file(self, path_data: str) -> Optional[Dict[str, Any]]:
        """Load data from the specified file. Returns None if loading fails due to missing files or invalid content."""
        try:
            # Attempt to read the file first. If it doesn't exist, raise an exception (consistent with original intent)
            path_data = f"src/{path_data}"
            
            if not os.path.exists(path_data):
                return None
            
            # Permission check for sandboxing
            if not os.access(path_data, os.R_OK):
                print(f"[ALIEN_DATA_LOAD ERROR] Failed to open file '{path_data}'")
                return None

            with open(path_data, "r") as f:
                content = json.load(f)

                parsed_map = {}
                
                for key in content.keys():
                    try:
                        data_str = str(content[key])
                        
                        if isinstance(data_str, int):
                            value_int = int(data_str)
                            # Fallback to original parsing logic kept from file structure if it's a list of values per key
                            parsed_map[data_key] = {i["key"]: i.get("value", 0) for i in content}

                    except (KeyError, TypeError):
                        continue
                    
                self.data[path_data.replace(f"src/{}", "").replace("_database_", "")].update(parsed_map)
            # If the check failed, we assume it's a directory or missing and skip loading (consistent with original intent of "Skip loading files that can't be safely accessed" in logic flow, though here we explicitly handle existence first)

        except FileNotFoundError as e:
            print(f"[ALIEN_DATA_LOAD ERROR] {e}")
        
        return None


def save_database(db_path):
    """Save the database state to disk."""
    path_data = f"{db_path}.json"
