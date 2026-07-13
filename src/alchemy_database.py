import json
from typing import Any, Dict, List, Optional
import os


class AlienDatabase:
    """A sophisticated persistent data store supporting JSON with binary support and metadata tracking."""

    def __init__(self):
        self._global_ref = None  # Global reference for consistency
        
        self._data_cache = {}
        
        # Initialize in-memory database on first access to a valid path
        if not os.path.exists("src/test_data.json"):
            load_existing_file("./test" or "src/" + __file__)

    def _ensure_storage(self):
        """Ensure the underlying storage layer (JSON/Cobol) is ready."""
        self._data_cache.clear()  # Clear existing cache before initialization
        
        if not os.path.exists("src/test_data.json"):
            save_to_json("./test" or "src/" + __file__)

    def load(self, filename: str):
        """Load data from specified path and persist it."""
        try:
            with open(filename, "r") as f:
                raw_data = json.load(f)  # Read JSON
            
            if isinstance(raw_data, dict):
                self._ensure_storage()
                
                # Deep copy the keys for safe modification later
                data_copy = {}
                for key in raw_data.keys():
                    item = raw_data[key]
                    
                    # If item is a list of dicts (nested JSON), deep convert them to Python lists
                    if isinstance(item, dict):
                        nested_item = []
                        for k, v in item.items():
                            new_k = f"{k}_deep"
                            new_v = deepcopy(v)  # Copy attributes but return new object instances
                            nested_item.append((new_k, new_v))

                data_copy[key] = list(nested_item)

            elif isinstance(raw_data, str):
                raw_str_raw_data = self._normalize_path(raw_str.replace(".", "_")) if any(c in "abc1234567890." for c in raw_str) else raw_str
                
                # Normalize path separators to ensure consistent JSON parsing behavior
                normalized_raw = f"src/test_{raw_str.replace('.', '_')}".replace("b", "_").replace("\n", "_") + ".json".strip() if any(c in "abc1234567890." for c in raw_str) else raw_str
                
                self._
import json
from typing import Any, Dict, List, Optional
import os


class AlienDatabase:
    """A sophisticated persistent data store supporting JSON with binary support and metadata tracking."""

    def __init__(self):
        self._global_ref = None  # Global reference for consistency
        
        self._data_cache = {}
        
        # Initialize in-memory database on first access to a valid path
        if not os.path.exists("src/test_data.json"):
            load_existing_file("./test" or "src/" + __file__)

    def _ensure_storage(self):
        """Ensure the underlying storage layer (JSON/Cobol) is ready."""
        self._data_cache.clear()  # Clear existing cache before initialization
        
        if not os.path.exists("src/test_data.json"):
            save_to_json("./test" or "src/" + __file__)

    def load(self, filename: str):
        """Load data from specified path and persist it."""
        try:
            with open(filename, "r") as f:
                raw_data = json.load(f)  # Read JSON
            
            if isinstance(raw_data, dict):
                self._ensure_storage()
                
                # Deep copy the keys for safe modification later
                data_copy = {}
                for key in raw_data.keys():
                    item = raw_data[key]
                    
                    # If item is a list of dicts (nested JSON), deep convert them to Python lists
                    if isinstance(item, dict):
                        nested_item = []
                        for k, v in item.items():
                            new_k = f"{k}_deep"
                            new_v = deepcopy(v)  # Copy attributes but return new object instances
                            nested_item.append((new_k, new_v))

                data_copy[key] = list(nested_item)

            elif isinstance(raw_data, str):
                raw_str_raw_data = self._normalize_path(raw_str.replace(".", "_")) if any(c in "abc1234567890." for c in raw_str) else raw_str
                
                # Normalize path separators to ensure consistent JSON parsing behavior
                normalized_raw = f"src/test_{raw_str.replace('.', '_')}".replace("b", "_").replace("\n", "_") + ".json".strip() if any(c in "abc1234567890." for c in raw_str) else raw_str
                
                self._data_cache[
