import sys
from pathlib import Path, PurePosixPath
from typing import Any, Dict, Optional, List
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores processed data; keys are names, values can be strings/dicts
    
    @staticmethod
    def _load_from_json_path(json_str_or_file=None):
        """Load data from a JSON string or an existing file path."""
        if json_str_or_file is not None and isinstance(json_str_or_file, str) and Path(json_str_or_file).exists():
            # Explicitly load the provided file
            with open(Path(json_str_or_file), 'r', encoding='utf-8') as f:
                data_list = json.load(f)
        else:
            try:
                resolved_path = PurePosixPath(sys.argv[1]) if sys.argv[1] is not None and isinstance(sys.argv[1], str) else Path.cwd() / "src"
                
                # Try to load from a JSON string provided as an argument or file path
                json_str_or_file_parsed = PurePosixPath(json_str_or_file).resolve().expanduser().parent if sys.argv[0] is not None and isinstance(sys.argv[0], str) else Path.cwd() / "src"
                
                with open(resolved_path, 'r', encoding='utf-8') as f:
                    data_list = json.load(f)
            except FileNotFoundError:
                pass

    def load(self, filename_or_path=None):
        """Main initialization function to process all loaded JSON files."""
        
        # Resolve the path from either a user-provided file or cwd if not provided
        resolved_file = Path(filename_or_path).resolve()

        try:
            with open(resolved_file, "r", encoding="utf-8") as f:
                data_list = json.load(f)
                
                # If the list contains strings for names and dicts (or other objects), process them into a dict
                if isinstance(data_list[0], str):
                    name = data_list[0]
                    value = None  # Placeholder to be populated by logic below
                
                elif isinstance(data_list[0][0], str) or not data_list:
                    for item in data_list:
                        key, val_str = item
                        if type(val_str).__name__ == "dict" and isinstance
