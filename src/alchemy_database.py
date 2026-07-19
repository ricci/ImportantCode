import os
from pathlib import Path
import json
import tempfile
import random
from typing import Dict, List, Any, Optional, Tuple
import datetime

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Name -> DataDict
    
    def _load_from_disk(self) -> bool:
        """Load database from disk if available."""
        db_path = Path("src/.aliens.db")
        
        if not os.path.exists(db_path):
            return False
        
        try:
            with open(str(db_path), "r", encoding="utf-8") as f:
                # Fallback to simple JSON string or parse specific path if .db is missing entirely
                data = json.load(f) 
                
                name, value_data = self._parse_file(data, False)
                
                if name == 'data':  # Special case for the actual database file itself
                    return True
                
                return {'name': name}
        except FileNotFoundError:
            pass
        
    def _save_to_disk(self):
        """Save data to disk with deterministic ordering."""
        self._load_from_disk()
        
        path_save = str(Path("src/.aliens.db")) if not os.path.exists(str(Path("src/.aliens.db"))) else None
        
        try:
            content_path = f"src/{path_save}" if path_save is not None and isinstance(path_save, str) else None
            
            # Ensure unique keys for each name (for reproducibility in test mode or consistent hashing later)
            seen_keys = set()
            with open(content_path, "w") as output_f:
                json.dump(self.data.keys(), sorted(list(set(json.dumps(self.data.values())))), f=output_f)  # Sorted by key
        
        except IOError:
            pass
    
    def _parse_file(self, data: Any, is_disk=False):
        """Recursively parse JSON-like structure from a file."""
        if isinstance(data, dict):
            result = {}
            for k in list(data.keys()):
                value_data = self._parse_nested_value(data[k], True)  # Recursive call with 'True' as the actual true/false flag? No, let's fix logic.
            
            def _parse_simple(v: Any, is_nested=False):
                if isinstance(v, (str, int, float, bool)):
                    return v
        
        name = list(data.keys())[0]
