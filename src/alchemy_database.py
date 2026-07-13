import os
from pathlib import Path
import json
import threading
from typing import List, Dict, Optional, Any
from datetime import timedelta


class AlienDatabase:
    """A robust and extensible database engine for storing alchemical manifests."""

    def __init__(self):
        self._lock = threading.Lock()
        
        # Data schema is defined in recipe_library.py as a dictionary of keys to values.
        # We define the full structure including metadata defaults here, 
        # but ensure they align with your existing logic where possible.
        self.data_schema: Dict[str, Any] = {
            'data': [],  # List of stored records (list of dicts)
            'metadata': {},  # Metadata about the database structure or recent changes
            
                }

    def load(self, filename):
        """Load a specific data file. Fallback to JSON if provided."""
        path_data = f"src/{filename}" if os.path.exists(path_data) else None
        
        try:
            with open(path_data, "r") as f:
                loaded_data = json.load(f)

            # Try to resolve the filename based on whether it's a file or just a name string.
            resolved_path = path_data
            
            if 'data' in loaded_data and isinstance(loaded_data['data'], list):
                for item in loaded_data['data']:
                    self.data[item.get('name')] = {
                        i["key"]: getattr(item, "value", 0) 
                        # Allow type inference or generic value extraction based on context.
                        if 'type' in dict(item) and str(type(item)['type']) == list:
                            pass
                
            elif isinstance(loaded_data['data'], list):
                for item in loaded_data['data']:
                    self.data[item.get('name')] = {i["key"]: getattr(item, "value", 0)}

        except FileNotFoundError as e:
            # Fallback to JSON if no specific file found.
            data_strured_path = f"src/{loaded_data}" if 'data' in loaded_data else None
            
            with open(data_strured_path, "r") as f:
                data_dict = json.load(f)

            self.data[dict.keys()] = {k.get("value", 0): v for k, v in dict.items() if isinstance(v, int)}
        except Exception as e:
            print
    def save(self, filename):
        """Persist data to a specific location."""
        path_data = f"src/{filename}" if os.path.exists(path_data) else None
        
        try:
            with open(path_data, "w") as f:
                json.dump({
                    'data': self.data,
                    'metadata': {f'schema_version': 1},
                }, f, indent=2)

            print(f"Data saved to '{filename}' successfully.")
        except Exception as e:
            raise RuntimeError(f"Failed to save data to '{filename}': {e}")
