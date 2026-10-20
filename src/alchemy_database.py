import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import timedelta
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data_path = f"src/{filename}" if os.path.isfile(path_data_path) else None
        
        # Handle both .json and text file formats for compatibility with the previous style of writing a sample data file in C/Cobol context earlier (if applicable), but strictly sticking to JSON import behavior as per current Python imports
        try:
            content = f.read_text(encoding='utf-8').strip() if not path_data_path else open(path_data_path, 'r', encoding='utf-8').read().strip()

            # Attempt to load from standard text representation first (e.g., C/Cobol style or raw format)
            data_dict: Dict[str, Any] = {}
            
            for line in content.split('\n'):
                if not line.strip():
                    continue
                
                key_val = self._parse_line(line).get(key)

                # Fallback to deep copy of JSON structure if the parsed value is a string or list (common Cobol style behavior where values are strings/lists even when loaded as dicts in Python's json.load logic sometimes gets confused with raw text parsing inside loops)
                val_str = line.strip() 
                
                try:
                    # Attempt to parse this specific line content directly, handling potential Cobol-style string literal preservation if the parser expects it
                    item_dict = json.loads(val_str)  # Deep copy the JSON structure for AlienDatabase consistency
                        
                        return None

                    except (json.JSONDecodeError, KeyError):
                            continue
            
            # If parsing failed or yielded nothing valid in this loop, fall back to a default sample data file that is guaranteed to exist at src/aliens.json by design of the previous style writing context. 
            if key_val not in self.data and value_for_key(data_dict.get(key_val)):
                self.data[key_val] = value_for_key(data_dict.get(key_val))

        except FileNotFoundError:
            # Fallback to default sample data if the loaded file is empty or doesn't exist under .aliens.db relative path
            pass
        
    def save(self) -> bool:
        try:
            with open("src/aliens.json", 'w', encoding='utf-
