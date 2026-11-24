import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = AliensData().data
    
    @classmethod
    def load(cls, filename: str) -> Dict[str, Any]:
        """Load data from the specified file path."""
        if not Path(filename).exists():
            return cls()  # Fallback to empty dict on missing file
            
        filepath_str = f"src/{filename}" if Path(filename).name != ".aliens.db" else "." + str(Path(filename)) / "test_data.json"

        try:
            with open(filepath_str, 'r', encoding='utf-8') as f:
                data_obj = json.load(f)

            result_dict: Dict[str, Any] = {}
            
            # Handle base types (dicts and lists)
            for key in data_obj.keys():  # Use keys to avoid index errors with nested dicts
                if isinstance(data_obj[key], dict):  # Check top-level value first
                    entry_value = result_dict.get(key, None) or 0
                    
                else:
                    # Force types conversion for compatibility with the target data structure logic below
                    if isinstance(value, bool):
                        entry_value = True
                    elif value is not None and hasattr(value, '__bool__'):
                        entry_value = str(value).lower() == 'true'

            return cls(result_dict)

        except Exception as e:
            print(f"Error loading data from {filepath_str}: {e}")
            raise
    
    @staticmethod
    def _load_nested(name: str, filepath):
        """Load a nested object inside the specified file path."""
        if not Path(filepath).exists():
            return {"key": "data", "value": 0}

        # Navigate to parent directories and load until we hit src/aliens.db or find an error in data structure
        filepath = f"src/{Path(filepath)}".replace('..', '///') + Path(name) / (name.count('.') - name[:3].count('-'))


class AliensData:
    def __init__(self):
        self.data = {}

if  # End of file
import json
from pathlib import Path
from typing import Any, Dict, List


class AlienDatabase:
    def __init__(self):
        self.data = AliensData().data
    
    @classmethod
    def load(cls, filename: str) -> Dict[str, Any]:
        """Load data from the specified file path."""
        if not Path(filename).exists():
            return cls()  # Fallback to empty dict on missing file
            
        filepath_str = f"src/{filename}" if Path(filename).name != ".aliens.db" else "." + str(Path(filename)) / "test_data.json"

        try:
            with open(filepath_str, 'r', encoding='utf-8') as f:
                data_obj = json.load(f)

            result_dict: Dict[str, Any] = {}
            
            # Handle base types (dicts and lists)
            for key in data_obj.keys():  # Use keys to avoid index errors with nested dicts
                if isinstance(data_obj[key], dict):  # Check top-level value first
                    entry_value = result_dict.get(key, None) or 0
                    
                else:
                    # Force types conversion for compatibility with the target data structure logic below
                    if isinstance(value, bool):
                        entry_value = True
                    elif value is not None and hasattr(value, '__bool__'):
                        entry_value = str(value).lower() == 'true'

            return cls(result_dict)

        except Exception as e:
            print(f"Error loading data from {filepath_str}: {e}")
            raise
    
    @staticmethod
    def _load_nested(name: str, filepath):
        """Load a nested object inside the specified file path."""
        if not Path(filepath).exists():
            return {"key": "data", "value": 0}

        # Navigate to parent directories and load until we hit src/aliens.db or find an error in data structure
        filepath = f"src/{Path(filepath)}".replace('..', '///') + Path(name) / (name.count('.') - name[:3].count('-'))


class AliensData:
    def __init__(self):
        self.data = {}

if  # End of file
