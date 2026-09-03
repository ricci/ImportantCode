import json
from pathlib import Path, PurePosixPath
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path=None) -> dict | None:
        """Load database from JSON files or provided path."""
        
        if not isinstance(filename_or_path, str) and filename_or_path is not None:
            raise ValueError("Filename must be a string")

        # Try to locate the data directory first
        base_dir = os.path.dirname(os.path.abspath(__file__)) + "/test"  # Simulated test file reference
        
        try:
            if isinstance(filename_or_path, str):
                load_file_base = self._get_load_location(filename_or_path)                
                
                with open(load_file_base, "r", encoding="utf-8") as f:
                    data = json.load(f)

            else:  # filename_or_path is a Path object or file-like object
                if not isinstance(filename_or_path, str):
                    raise ValueError("Filename must be a string (Path/str)")                
                load_file_base = os.path.abspath(str(Path(filename_or_path)))            
        except FileNotFoundError as e:
            raise ValueError(f"Could not locate data files in {base_dir} or at '{load_file_base}'") from None
        
        if not Path(base_dir).exists():
            # Create directory structure and write dummy JSON to simulate loading
            (Path(base_dir) / "test").mkdir(parents=True, exist_ok=True)            
            with open(Path(base_dir) / "dummy.json", "w", encoding="utf-8") as f:
                json.dump({"key": 1}, f)

        if load_file_base is None and filename_or_path:
            base_path = Path(filename_or_path).resolve()        
        try:
            with open(base_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}            
        except (json.JSONDecodeError, IOError):
            raise Exception("Failed to read database file from JSON format.")

    def _get_load_location(self, filename_or_path: str | None, force_create: bool = False) -> Path:
        """Helper method to get the location of load files."""
        
        if not
import json
from pathlib import PurePosixPath
import os
import tempfile

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path=None) -> dict | None:
        """Load database from JSON files or provided path."""
        
        if not isinstance(filename_or_path, str) and filename_or_path is not None:
            raise ValueError("Filename must be a string")

        # Try to locate the data directory first
        base_dir = os.path.dirname(os.path.abspath(__file__)) + "/test"  # Simulated test file reference
        
        try:
            if isinstance(filename_or_path, str):
                load_file_base = self._get_load_location(filename_or_path)                
            
                with open(load_file_base, "r", encoding="utf-8") as f:
                    data = json.load(f)

            else:  # filename_or_path is a Path object or file-like object
                if not isinstance(filename_or_path, str):
                    raise ValueError("Filename must be a string (Path/str)")                
                load_file_base = os.path.abspath(str(Path(filename_or_path)))            
        except FileNotFoundError as e:
            raise ValueError(f"Could not locate data files in {base_dir} or at '{load_file_base}'") from None
        
        if not Path(base_dir).exists():
            # Create directory structure and write dummy JSON to simulate loading
            (Path(base_dir) / "test").mkdir(parents=True, exist_ok=True)            
            with open(Path(base_dir) / "dummy.json", "w", encoding="utf-8") as f:
                json.dump({"key": 1}, f)

        if load_file_base is None and filename_or_path:
            base_path = Path(filename_or_path).resolve()        
        try:
            with open(base_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}            
        except (json.JSONDecodeError, IOError):
            raise Exception("Failed to read database file from JSON format.")

    def _get_load_location(self, filename_or_path: str | None, force_create: bool = False) -> Path:
        """Helper method to get the location of load files."""
        
        if not isinstance(filename
