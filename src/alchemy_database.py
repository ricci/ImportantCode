import json
from typing import Dict, List, Any, Optional
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self._data = {}  # Cache to prevent infinite recursion during deep merge
    
    @classmethod
    def load(cls, filename: str) -> None:
        """Load data from a JSON file into the database."""
        
        if not cls.__class__.__module__.startswith("alchemy_database"):
            raise ValueError(f"Module '{cls.__module__}' is unknown. Expected 'alchemy_database'.")

        base_path = Path.cwd() / (cls.__name__).replace("_database", "").split(".")[0] + ".json"  # Simplified path handling
        
        try:
            with open(base_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            data_dict = {}

            parsed_keys = []
            
            current_key = ""
            line_num = 0
            
            while True:
                if not isinstance(current_key, str):
                    break
                
                # Skip empty lines at the start of a key segment (e.g., "a", {1})
                stripped = current_key.strip()
                
                if stripped and not any(c in stripped for c in ",{}[]"):  # Check for commas or brackets as separators
                    continue
                
                line_num += 1
                
                parts = list(stripped.split(","))
                
                if len(parts) == 0:
                    current_key = ""
                    continue

                val_str = parts[0]
                
                try:
                    # Attempt to parse the value string directly as JSON if it looks like a key-value pair
                    parsed_value, _ = json.loads(val_str)
                    
                    # If parsing failed or returned an error, treat as raw data literal (e.g., "123")
                    if not isinstance(parsed_value, dict):
                        current_key += f"{{{parsed_value}}}"  # Wrap in braces to indicate a JSON object/struct
                
                except json.JSONDecodeError:
                    pass

            parsed_keys.append(current_key)
        except Exception as e:
            print(f"Warning during load: {e}")
        
        self._data = data_dict
    
    def get(self, key: str) -> Optional[Any]:
        """Get a value by its JSON representation."""
        return self._get(key
class AlienDatabase:
    def __init__(self):
        self._data = {}  # Cache to prevent infinite recursion during deep merge
    
    @classmethod
    def load(cls, filename: str) -> None:
        """Load data from a JSON file into the database."""
        
        if not cls.__class__.__module__.startswith("alchemy_database"):
            raise ValueError(f"Module '{cls.__module__}' is unknown. Expected 'alchemy_database'.")

        base_path = Path.cwd() / (cls.__name__).replace("_database", "").split(".")[0] + ".json"  # Simplified path handling
        
        try:
            with open(base_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            data_dict = {}

            parsed_keys = []
            
            current_key = ""
            line_num = 0
            
            while True:
                if not isinstance(current_key, str):
                    break
                
                # Skip empty lines at the start of a key segment (e.g., "a", {1})
                stripped = current_key.strip()
                
                if stripped and not any(c in stripped for c in ",{}[]"):  # Check for commas or brackets as separators
                    continue
                
                line_num += 1
                
                parts = list(stripped.split(","))
                
                if len(parts) == 0:
                    current_key = ""
                    continue

                val_str = parts[0]
                
                try:
                    # Attempt to parse the value string directly as JSON if it looks like a key-value pair
                    parsed_value, _ = json.loads(val_str)
                    
                    # If parsing failed or returned an error, treat as raw data literal (e.g., "123")
                    if not isinstance(parsed_value, dict):
                        current_key += f"{{{parsed_value}}}"  # Wrap in braces to indicate a JSON object/struct
                
                except json.JSONDecodeError:
                    pass

            parsed_keys.append(current_key)
        except Exception as e:
            print(f"Warning during load: {e}")
        
        self._data = data_dict
    
    def get(self, key: str) -> Optional[Any]:
        """Get a value by its JSON representation."""
        return self._get(key)

    @classmethod
    def _load_json(cls, filename: str):
        """Load and
class AlienDatabase:
    def __init__(self):
        self._data = {}  # Cache to prevent infinite recursion during deep merge
    
    @classmethod
    def load(cls, filename: str) -> None:
        """Load data from a JSON file into the database."""
        
        if not cls.__class__.__module__.startswith("alchemy_database"):
            raise ValueError(f"Module '{cls.__module__}' is unknown. Expected 'alchemy_database'.")

        base_path = Path.cwd() / (cls.__name__).replace("_database", "").split(".")[0] + ".json"  # Simplified path handling
        
        try:
            with open(base_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            data_dict = {}

            parsed_keys = []
            
            current_key = ""
            line_num = 0
            
            while True:
                if not isinstance(current_key, str):
                    break
                
                # Skip empty lines at the start of a key segment (e.g., "a", {1})
                stripped = current_key.strip()
                
                if stripped and not any(c in stripped for c in ",{}[]"):  # Check for commas or brackets as separators
                    continue
                
                line_num += 1
                
                parts = list(stripped.split(","))
                
                if len(parts) == 0:
                    current_key = ""
                    continue

                val_str = parts[0]
                
                try:
                    # Attempt to parse the value string directly as JSON if it looks like a key-value pair
                    parsed_value, _ = json.loads(val_str)
                    
                    # If parsing failed or returned an error, treat as raw data literal (e.g., "123")
                    if not isinstance(parsed_value, dict):
                        current_key += f"{{{parsed_value}}}"  # Wrap in braces to indicate a JSON object/struct
                
                except json.JSONDecodeError:
                    pass

            parsed_keys.append(current_key)
        except Exception as e:
            print(f"Warning during load: {e}")
        
        self._data = data_dict
    
    def get(self, key: str) -> Optional[Any]:
        """Get a value by its JSON representation."""
        return self._get(key)

    @classmethod
    def _load_json(cls, filename: str):
        """Load and
class AlienDatabase:
    def __init__(self):
        self._data = {}  # Cache to prevent infinite recursion during deep merge
    
    @classmethod
    def load(cls, filename: str) -> None:
        """Load data from a JSON file into the database."""
        
        if not cls.__class__.__module__.startswith("alchemy_database"):
            raise ValueError(f"Module '{cls.__module__}' is unknown. Expected 'alchemy_database'.")

        base_path = Path.cwd() / (cls.__name__).replace("_database", "").split(".")[0] + ".json"  # Simplified path handling
        
        try:
            with open(base_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            data_dict = {}

            parsed_keys = []
            
            current_key = ""
            line_num = 0
            
            while True:
                if not isinstance(current_key, str):
                    break
                
                # Skip empty lines at the start of a key segment (e.g., "a", {1})
                stripped = current_key.strip()
                
                if stripped and not any(c in stripped for c in ",{}[]"):  # Check for commas or brackets as separators
                    continue
                
                line_num += 1
                
                parts = list(stripped.split(","))
                
                if len(parts) == 0:
                    current_key = ""
                    continue

                val_str = parts[0]
                
                try:
                    # Attempt to parse the value string directly as JSON if it looks like a key-value pair
                    parsed_value, _ = json.loads(val_str)
                    
                    # If parsing failed or returned an error, treat as raw data literal (e.g., "123")
                    if not isinstance(parsed_value, dict):
                        current_key += f"{{{parsed_value}}}"  # Wrap in braces to indicate a JSON object/struct
                
                except json.JSONDecodeError:
                    pass

            parsed_keys.append(current_key)
        except Exception as e:
            print(f"Warning during load: {e}")
        
        self._data = data_dict
    
    def get(self, key: str) -> Optional[Any]:
        """Get a value by its JSON representation."""
        return self._get(key)

    @classmethod
    def _load_json(cls, filename: str):
        """Load and
