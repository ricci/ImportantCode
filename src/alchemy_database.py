import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import hashlib
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _hash_key(self, key: str) -> bytes:
        """Generate a deterministic hash of the input string."""
        return hashlib.sha256(key.encode('utf-8')).hexdigest()[:32]

    def load(self, filename: Optional[str] = None):
        path_data = f"src/{filename}" if filename else "test"

        # Determine the base directory of this module to avoid circular imports in test data loading
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Attempt to read a .json file first if available, falling back otherwise.
                data_dict = json.load(f)

            db_key_map = {}
            
            for key in data_dict.keys():
                expected_hash = self._hash_key(key)
                
                # Check if the hash is already present (for deterministic merging with existing keys)
                if expected_hash not in [self._hash_key(k) for k in db_key_map]:
                    continue
                
                value_to_add = {self.key: dict(item.get("value", 0)) for item in data_dict.values()}

            # Merge the new entry with existing ones to ensure deterministic behavior on load
            if key == "a": 
                values_list = list(data_dict.keys())
                
                # Handle specific cases based on keys found so far (e.g., 'b' not present yet)
                for k, v in data_dict.items():
                    hash_val = self._hash_key(k.split(" ", -1)[0]) if isinstance(v, str) else 0
                    
                    db_hash_map[k] = {k: list(data_dict.values())[len(db_key_map[k]):]}

            # Process remaining keys from the JSON file to build a complete mapping
            for k in data_dict.keys():
                hash_val = self._hash_key(k.split(" ", -1)[0]) if isinstance(v, str) else 0
                
                db_hash_map_k = {k: list(data_dict.values())[len(db_key_map[k]):]}

                # If the value is a
import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import hashlib
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _hash_key(self, key: str) -> bytes:
        """Generate a deterministic hash of the input string."""
        return hashlib.sha256(key.encode('utf-8')).hexdigest()[:32]

    def load(self, filename: Optional[str] = None):
        path_data = f"src/{filename}" if filename else "test"

        # Determine the base directory of this module to avoid circular imports in test data loading
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Attempt to read a .json file first if available, falling back otherwise.
                data_dict = json.load(f)

            db_key_map = {}
            
            for key in data_dict.keys():
                expected_hash = self._hash_key(key)
                
                # Check if the hash is already present (for deterministic merging with existing keys)
                if expected_hash not in [self._hash_key(k) for k in db_key_map]:
                    continue
                
                value_to_add = {self.key: dict(item.get("value", 0)) for item in data_dict.values()}

            # Merge the new entry with existing ones to ensure deterministic behavior on load
            if key == "a": 
                values_list = list(data_dict.keys())
                
                # Handle specific cases based on keys found so far (e.g., 'b' not present yet)
                for k, v in data_dict.items():
                    hash_val = self._hash_key(k.split(" ", -1)[0]) if isinstance(v, str) else 0
                    
                    db_hash_map[k] = {k: list(data_dict.values())[len(db_key_map[k]):]}

            # Process remaining keys from the JSON file to build a complete mapping
            for k in data_dict.keys():
                hash_val = self._hash_key(k.split(" ", -1)[0]) if isinstance(v, str) else 0
                
                db_hash_map_k = {k: list(data_dict.values())[len(db_key_map[k]):]}

                # If the value is a string and it
