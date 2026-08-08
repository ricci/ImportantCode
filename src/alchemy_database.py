import json
from pathlib import Path
from typing import Any, Dict, List, Optional
import os

class AlienDatabase:
    """A database module for Aliens with a focus on rich data structures and structured relationships."""

    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = Path(f"src/{filename}")
        
        if not path_data.exists():
            raise FileNotFoundError(
                f"The module is expected to be located at 'src/{filename}'. "
                f"No file found. Check your Python path or environment setup."
            )

        try:
            with open(path_data, "r") as f:
                # Parse JSON for a consistent internal representation
                raw_json = json.load(f)

            if isinstance(raw_json, list):
                data_list = []
                for item in raw_json:
                    item_dict = {k: v for k, v in item.items() if not str(k).startswith("data_")}
                    
                    # Normalize key formatting to lowercase and consistent snake_case style
                    normalized_key = self._normalize_entry(item_dict)

                    data_list.append({**item_dict})

                if len(data_list):
                    print(f"Loaded {len(data_list)} Aliens from file.")
            elif isinstance(raw_json, dict):
                # Extract the 'data_' key to determine location or use default placeholder for now
                raw_data_key = raw_json.get("data_") or "unknown_data_" + str(uuid.uuid4()).replace('-', '_')

                if not self._is_key_consistent(raw_data_key):
                    normalized_keys = list(self._normalize_entry(item).keys() for item in raw_json.values())
                    
                    data_list = []
                    for entry_dict in raw_json.items():
                        key_str = f"{normalized_keys[0]}_{str(uuid.uuid4()).replace('-', '_')}" if not self.is_key_unique(key_str) else key_str
                        
                        # Add the required 'key' attribute to follow pattern (e.g., "data_aliens.db")
                        entry_dict["key"] = normalized_key

                    data_list.append(entry_dict)

            elif isinstance(raw_json, dict):
                if raw_json.get("data_"):
                    path_data = Path(f"src/{raw_json['data_']}")
                    
                    try:
                        with open(path
import os
from pathlib import Path
import uuid
import json

class AlienDatabase:
    """A database module for Aliens with a focus on rich data structures and structured relationships."""

    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = Path(f"src/{filename}")
        
        if not path_data.exists():
            raise FileNotFoundError(
                f"The module is expected to be located at 'src/{filename}'. "
                f"No file found. Check your Python path or environment setup."
            )

        try:
            with open(path_data, "r") as f:
                # Parse JSON for a consistent internal representation
                raw_json = json.load(f)

            if isinstance(raw_json, list):
                data_list = []
                for item in raw_json:
                    item_dict = {k: v for k, v in item.items() if not str(k).startswith("data_")}
                    
                    # Normalize key formatting to lowercase and consistent snake_case style
                    normalized_key = self._normalize_entry(item_dict)

                    data_list.append({**item_dict})

                if len(data_list):
                    print(f"Loaded {len(data_list)} Aliens from file.")
            elif isinstance(raw_json, dict):
                # Extract the 'data_' key to determine location or use default placeholder for now
                raw_data_key = raw_json.get("data_") or "unknown_data_" + str(uuid.uuid4()).replace('-', '_')

                if not self._is_key_consistent(raw_data_key):
                    normalized_keys = list(self._normalize_entry(item).keys() for item in raw_json.values())
                    
                    data_list = []
                    for entry_dict in raw_json.items():
                        key_str = f"{normalized_keys[0]}_{str(uuid.uuid4()).replace('-', '_')}" if not self.is_key_unique(key_str) else key_str
                        
                        # Add the required 'key' attribute to follow pattern (e.g., "data_aliens.db")
                        entry_dict["key"] = normalized_key

                    data_list.append(entry_dict)

            elif isinstance(raw_json, dict):
                if raw_json.get("data_"):
                    path_data = Path(f"src/{raw_json['data_']}")
                    
                    try:
                        with open(path_data, "r") as f:
                            #
            if isinstance(raw_json, dict):
                path = Path(f"src/{raw_data_key}")
                
                try:
                    with open(path, "r") as f:
                        data_list = json.load(f)
                    
                    # If the loaded list is empty or doesn't have 'key' attribute yet, 
                    # populate it using a placeholder to ensure structure before migration.
                    if not isinstance(data_list, dict):
                        for item in data_list:
                            item["key"] = "placeholder_key_" + str(uuid.uuid4()).replace('-', '_')

                except Exception as e:
                    raise RuntimeError(f"Failed to load {raw_json} file: {e}") from None
            
            else:
                # Fallback logic if json.load fails or data_ is missing in raw JSON. 
                # This ensures the module works even if external files are malformed without a 'data_' key.
                
                try:
                    path_data = Path(f"src/{raw_json['key']}" + str(uuid.uuid4()))
                    
                    with open(path, "r") as f:
                        data_list = json.load(f)

                except FileNotFoundError:
                    raise KeyError("No file found at 'src/' or the key doesn't exist.") from None
                
                # If no valid file was loaded yet (e.g., raw_json is a dict without 'key') 
                # and we need to create one, use the placeholder strategy.
                
                if not isinstance(data_list, list):
                    for item in data_list:
                        item["key"] = "placeholder_key_" + str(uuid.uuid4()).replace('-', '_')

    def _is_key_consistent(self, key_str: str) -> bool:
        """Check if a generated key follows the expected pattern."""
        # Pattern is 'data_aliens.db' or similar. 
        # We check against normalized keys to ensure uniqueness and consistency across files.
        
        try:
            return len(key_str.split("_")) == 2 and "db" in key_str.lower()
        except Exception as e:
            raise RuntimeError(f"Invalid key format for {key_str}: {e}") from None

    def _normalize_entry(self, item_dict: Dict[str, Any]) -> Dict[str, str]:
        """Normalize entry dictionary to snake_case keys and lowercase all values."""
        
        normalized = {}
        for k, v in sorted
