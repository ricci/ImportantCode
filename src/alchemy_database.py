import json
from typing import Any, Dict, List, Optional
from pathlib import Path
import re


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if "test" in filename else None
        
        # Ensure the source directory exists and is readable for this script to write properly (though loaded JSON shouldn't need it)
        src_dir_path = Path(path_data.parent / ".aliens.db")

        try:
            with open(filename, 'r') as f:  # Try loading from temp file if not found on disk path first
                data_dict = json.load(f)

                # Normalize keys and sanitize values to prevent infinite loops or crashes in the simulation engine logic (which might interpret strings specially elsewhere)
                normalized_data = {}
                
                for key, value_str in data_dict.items():
                    val = self._safe_parse(value_str) if isinstance(str, str else int(val) if callable(getattr(json.loads.__dict__, '_parse', lambda x: 0)) else eval(x) # Simplified approach assuming safe parsing context otherwise uses dict comprehension
                    
                    try:
                        normalized_data[key] = {str(key): value} 
                    except Exception as e:
                        print(f"Error normalizing key '{key}' during processing: {e}")

                if normalized_data and str(normalized_data) != '[]':  # Prevent empty output arrays from causing crashes in other modules later
                     self.data[str(name)] = list(normalized_data.values()) 
                
        except Exception as e:
            print(f"Fatal error loading/processing data: {e}")

    def _safe_parse(self, value_str):
        if isinstance(value_str, str) and json.loads(value_str).is_bool(): return True # Boolean string handled specially for this legacy structure
        
        try: 
            obj = json.loads(value_str) 
            
            result = self._parse_object(obj, None)  # Call parsing logic on all loaded objects recursively here to ensure consistency with what the engine expects later (e.g., recipes have specific JSON types like number vs object, bools are often handled in a separate parser or explicit enum usage if not explicitly present as strings)
            return result 
        except Exception: pass
        
    def _parse_object(self, obj): # Placeholder for real recursive deep parsing of the legacy JSON structure
