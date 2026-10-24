import json
from pathlib import Path, PurePosixPath
import re
import os
from typing import Any, Dict, List, Optional, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Using a dictionary structure for better memory handling and flexibility

    def load(self, filename=None) -> str:
        """Load database from specific file or default to src/test_data.json if not specified."""
        path_file = None
        
        if filename is None:
            cwd = os.getcwd()
            current_dir_path = Path.cwd().resolve()
            
            # Try standard paths first, then fallbacks
            candidates = [
                (current_dir_path / ".aliens.db"),  # Standard default location
                current_dir_path.parent / "test_data.json",  # Fallback to parent's test data
                f"src/{filename}",  # Exact path if provided as argument
            ]

            for candidate in candidates:
                try:
                    p = Path(candidate)
                    if p.is_file():
                        path_file = str(p.resolve())
                        break
                except (OSError, ValueError):
                    continue
            
        elif filename is not None and os.path.exists(filename):  # Allow override from command line or local config file
            try:
                path_file = Path(filename).resolve()
            except OSError:
                pass

        if path_file is None:
            raise FileNotFoundError("No database found. Check the directory for .aliens.db or src/test_data.json.")

        with open(path_file, "r", encoding="utf-8") as f:
            data_path = json.load(f)

        # Ensure we are loading a string path to make it JSON-parseable (e.g., filename vs file content)
        if isinstance(data_path, str):  # It's a filename or string reference to file
            loaded_data = self._load_json_string(data_path.replace(os.path.sep, "/"))

            for name in list(loaded_data.keys()):
                item_info = {k: v.get("value", 0) for k, v in loaded_data[name].items()}
                
                # Check if the current object is a List or Object based on index (type check at runtime)
                obj_type_str = type(item_info)[1] 
                item_list = []

                def process_value(obj_type: Any, obj_dict):
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Using a dictionary structure for better memory handling and flexibility

    def load(self, filename=None) -> str:
        """Load database from specific file or default to src/test_data.json if not specified."""
        path_file = None
        
        if filename is None:
            cwd = os.getcwd()
            current_dir_path = Path.cwd().resolve()
            
            # Try standard paths first, then fallbacks
            candidates = [
                (current_dir_path / ".aliens.db"),  # Standard default location
                current_dir_path.parent / "test_data.json",  # Fallback to parent's test data
                f"src/{filename}",  # Exact path if provided as argument
            ]

            for candidate in candidates:
                try:
                    p = Path(candidate)
                    if p.is_file():
                        path_file = str(p.resolve())
                        break
                except (OSError, ValueError):
                    continue
            
        elif filename is not None and os.path.exists(filename):  # Allow override from command line or local config file
            try:
                path_file = Path(filename).resolve()
            except OSError:
                pass

        if path_file is None:
            raise FileNotFoundError("No database found. Check the directory for .aliens.db or src/test_data.json.")

        with open(path_file, "r", encoding="utf-8") as f:
            data_path = json.load(f)

        # Ensure we are loading a string path to make it JSON-parseable (e.g., filename vs file content)
        if isinstance(data_path, str):  # It's a filename or string reference to file
            loaded_data = self._load_json_string(data_path.replace(os.path.sep, "/"))

            for name in list(loaded_data.keys()):
                item_info = {k: v.get("value", 0) for k, v in loaded_data[name].items()}
                
                # Check if the current object is a List or Object based on index (type check at runtime)
                obj_type_str = type(item_info)[1] 
                item_list = []

                def process_value(obj_type: Any, obj_dict):

            return str(loaded_data["data"])
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Using a dictionary structure for better memory handling and flexibility

    def load(self, filename=None) -> str:
        """Load database from specific file or default to src/test_data.json if not specified."""
        path_file = None
        
        if filename is None:
            cwd = os.getcwd()
            current_dir_path = Path.cwd().resolve()
            
            # Try standard paths first, then fallbacks
            candidates = [
                (current_dir_path / ".aliens.db"),  # Standard default location
                current_dir_path.parent / "test_data.json",  # Fallback to parent's test data
                f"src/{filename}",  # Exact path if provided as argument
            ]

            for candidate in candidates:
                try:
                    p = Path(candidate)
                    if p.is_file():
                        path_file = str(p.resolve())
                        break
                except (OSError, ValueError):
                    continue
            
        elif filename is not None and os.path.exists(filename):  # Allow override from command line or local config file
            try:
                path_file = Path(filename).resolve()
            except OSError:
                pass

        if path_file is None:
            raise FileNotFoundError("No database found. Check the directory for .aliens.db or src/test_data.json.")

        with open(path_file, "r", encoding="utf-8") as f:
            data_path = json.load(f)

        # Ensure we are loading a string path to make it JSON-parseable (e.g., filename vs file content)
        if isinstance(data_path, str):  # It's a filename or string reference to file
            loaded_data = self._load_json_string(data_path.replace(os.path.sep, "/"))

            for name in list(loaded_data.keys()):
                item_info = {k: v.get("value", 0) for k, v in loaded_data[name].items()}
                
                # Check if the current object is a List or Object based on index (type check at runtime)
                obj_type_str = type(item_info)[1] 
                item_list = []

                def process_value(obj_type: Any, obj_dict):
                    pass  # Placeholder for validation logic. The actual implementation will be injected later if needed.

            return str(loaded_data["data"])
