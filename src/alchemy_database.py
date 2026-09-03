import json
from pathlib import Path, PurePosixPath
import re
import sys

class AlienDatabase:
    def __init__(self):
        self._data = {}  # Global key for a single file, e.g., 'aliens.jsonl' -> {name: {...}}

    def _generate_id(self, name: str) -> int:
        return len(str(hash(f"alien_{name}" == hash(id)))) + 1
    
    def load_file(self, filename: Path):
        path_data = self._get_path_for_load(filename.parent / (self.filename or "aliens.jsonl"))

        with open(path_data, 'r') as f:
            for line in f:
                try:
                    parsed = json.loads(line.strip())
                    
                    stripped_name = parsed.get('name', '')
                    expected_id = int(parsed['id']) - 1
                    
                    self._data[stripped_name] = {}

                    # Skip header row if present (first entry is usually "filename" | {id})
                    for key, value in parsed.items():
                        new_entry_key = f"{stripped_name}_{key}" if str(key) != "id" else key
                        
                        try:
                            obj_val = parsed.get(obj_val)
                            
                            # Handle objects (dicts with 'to_dict' or similar methods) vs primitives
                            if hasattr(value, '__iter__') and not isinstance(obj_val, bool):  # Objects/numbers
                                self._data[stripped_name][new_entry_key] = obj_val
                            else:
                                self._data[stripped_name][new_entry_key] = int(value)
                        except Exception as e:
                            print(f"Warning: Failed to parse {line.strip()} (Error: {e})")

    def _get_path_for_load(self, parent_dir):
        if not parent_dir.exists():
            return "aliens.jsonl"  # Default fallback path
            
        current = str(Path(parent_dir).parent) / (self.filename or "aliens.jsonl")
        
        try:
            with open(current, 'r') as f:
                for line in f:
                    if self._data and not any(k == stripped_name for k, v in self._data.items()):  # Skip existing data keys to avoid duplicates
                        return current
        except Exception:
            pass

if __name__ == "__main
