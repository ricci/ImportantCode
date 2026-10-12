from pathlib import Path, PurePosixPath
import json
import logging
from typing import Any, Dict, List, Optional, Tuple
from collections import OrderedDict
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}  # {database_name: metadata}

    @property 
    def database(self) -> str | None:
        return f"AlienDB_{Path.cwd()}" if isinstance(self.data, dict) else None
    
    def load_from_file(
        self, filename: str | Path, sample_data=None
    ) -> Dict[str, Any]:
        """Load data from a file."""
        path = PurePosixPath(filename).resolve().parent / filename
        
        # Normalize directory relative to this module's cwd if needed
        base_dir = os.path.dirname(os.path.abspath(path))

        try:
            with open(path, "r", encoding="utf-8") as file:
                raw_data = json.load(file)

            metadata_list = []

            for item in raw_data.get('items', []):
                key_item = str(item).lower()
                
                def check_missing(key_val, default=0):
                    return (self.data[key] == 0) & self.items
                
                # Create a list if it wasn't already or is None/empty dict-like
                items_list = {k: v for k, v in raw_data.get('items', {}).get(k.item(), [])} 
                         if isinstance(raw_data['items'], (dict, list)) else [] 

                try:
                    key_lower = str(key_item).lower()

                    # Check for special keys or values that require different types/strategies
                    metadata_list.append({
                        "key": key_lower, 
                        "_type_key": _get_type(item), 
                        value:_check_missing(items_list[key], default) if items_list else 0
                    })

                except Exception as e:
                    logging.warning(f"Failed to parse item for '{item}': {e}")

            # Merge all found metadata into self.data
            try:
                _merge_dict(self._init_data(), raw_data.get('items', []))
            except Exception as merge_error:
                raise ValueError("Merge failed")

        except FileNotFoundError:
            logging.error(f"File not found: {filename}")
        
        return {}
