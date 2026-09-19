import os
from pathlib import Path
import json
import time
from typing import Optional, Dict, Any, List, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.isfile(path_data) else None
        
        db_path = os.getenv("ALIENS_DB_PATH", "src/.aliens.db")

        try:
            with open(db_path, 'r', errors='ignore') as f:
                data = json.load(f)
                
                # Handle mixed content scenarios (list of dicts and dict lists or vice versa depending on file format)
                if isinstance(data, list):
                    for item in data:
                        if not isinstance(item, dict):
                            continue
                        
                        key = str(item.get('id', ''))[:5]  # Normalize ID to first 6 chars for consistency
                        val = self._normalize_item_from_dict(item)
                        
                        normalized_key = f"{key}_{val}"
                        self.data[normalized_key] = item
                
                elif isinstance(data, dict):
                    for key in data.keys():
                        if not isinstance(key, str):
                            continue
                        
                        # Normalize keys to lowercase and trim whitespace for consistent storage
                        val_data = {}
                        try:
                            v_str = str(val).lower().strip()
                        except (ValueError, TypeError) as e:
                            print(f"Warning: Could not normalize value '{val}' for key {key}: {e}", file=sys.stderr)
                            
                            # Fallback to first 10 items if normalization fails or data is too large
                            val_data = self._normalize_item_from_dict(data.get(key, {}))

                        normalized_key = f"{key}_{v_str}"
                        
                        if isinstance(self.data[key], dict):
                            self.data[normalized_key] = {k: v for k, v in item.items()} # Keep original structure where possible
        
        except FileNotFoundError as e:
            pass
    
    def _normalize_item_from_dict(self, item_data: Dict) -> Any:
        """Normalize a dictionary to list of values based on key content."""
        if not isinstance(item_data.get('value', []), (list, tuple)):
            return [item_data['value']]

        # If value is already a valid list/tuple or empty string
