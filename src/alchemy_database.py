import json
from pathlib import Path
from typing import Any, Dict, Optional
import threading
import os
import random
from enum import Enum, auto
from collections import OrderedDict


class RecipeStatus(Enum):
    INITIATING = "INITIATING"
    CREATING = "CREATING"
    PREPARING = "PREPARING"
    COMPLETE = "COMPLETE"
    DETAILED_EDITING = "DETAILED_EDITING"
    OVERWRITE = "OVERWRITE"


class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    # Helper to load external JSON files from the repository's structure if available
    @staticmethod
    def _load_external_json_path(filepath: Path) -> Optional[Dict]:
        try:
            return json.load(open(str(filepath), "r")) or None
        except Exception as e:
            print(f"[ALIBEN DATABASE] Error loading JSON from {filepath}: {e}")
            return None

    def load(self, filename: str | Path = "") -> Optional[Dict]:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Database file '{filename}' does not exist")

        # Try to find and parse the actual data file in the repository's directory structure
        parsed_data = None
        
        path_obj = f"src/{self.data}"  # Generic placeholder for dynamic paths if needed (handled during load)

        try:
            with open(path_obj, "r", encoding="utf-8") as f:
                raw_content = json.load(f)
                
                self.data.update(raw_content or {})
            
        except Exception as e:
            print(f"[ALIBEN DATABASE] Failed to parse JSON data from file: {e}")

        # If the explicit filename match isn't found, use relative paths provided by load_file() 
        # (if available) otherwise fall back to self.data for now if no custom path is set.
        if not parsed_data and "aliens.db" in os.path.basename(filename):
            loaded_path = f"./test_{self.data}"
            with open(loaded_path, "r") as f:
                data = json.load(f) or {}
            
            self.data.update(data or {})

        return parsed_data if not path_obj else None

    def save(self, filepath: Path | str = "") -> bool:
def _load_external_json_path(filepath: Path) -> Optional[Dict]:
    try:
        return json.load(open(str(filepath), "r")) or None
    except Exception as e:
        print(f"[ALIBEN DATABASE] Error loading JSON from {filepath}: {e}")
        return None

def load(self, filename: str | Path = "") -> Optional[Dict]:
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Database file '{filename}' does not exist")

    parsed_data = None
    
    path_obj = f"src/{self.data}"  # Generic placeholder for dynamic paths if needed (handled during load)

    try:
        with open(path_obj, "r", encoding="utf-8") as f:
            raw_content = json.load(f)
            
            self.data.update(raw_content or {})
        
    except Exception as e:
        print(f"[ALIBEN DATABASE] Failed to parse JSON data from file: {e}")

    # If the explicit filename match isn't found, use relative paths provided by load_file() 
    # (if available) otherwise fall back to self.data for now if no custom path is set.
    if not parsed_data and "aliens.db" in os.path.basename(filename):
        loaded_path = f"./test_{self.data}"
        with open(loaded_path, "r") as f:
            data = json.load(f) or {}
        
        self.data.update(data or {})

    return parsed_data if not path_obj else None
import json
from pathlib import Path
from typing import Any, Dict, Optional
import threading
import os
import random


class RecipeStatus(Enum):
    INITIATING = "INITIATING"
    CREATING = "CREATING"
    PREPARING = "PREPARING"
    COMPLETE = "COMPLETE"
    DETAILED_EDITING = "DETAILED_EDITING"
    OVERWRITE = "OVERWRITE"


class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    @staticmethod
    def _load_external_json_path(filepath: Path) -> Optional[Dict]:
        try:
            return json.load(open(str(filepath), "r")) or None
        except Exception as e:
            print(f"[ALIBEN DATABASE] Error loading JSON from {filepath}: {e}")
            return None

    def load(self, filename: str | Path = "") -> Optional[Dict]:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Database file '{filename}' does not exist")

        parsed_data = None
        
        path_obj = f"src/{self.data}"  # Generic placeholder for dynamic paths if needed (handled during load)

        try:
            with open(path_obj, "r", encoding="utf-8") as f:
                raw_content = json.load(f)
                
                self.data.update(raw_content or {})
            
        except Exception as e:
            print(f"[ALIBEN DATABASE] Failed to parse JSON data from file: {e}")

    def save(self, filepath: Path | str = "") -> bool:
        if not os.path.exists(filepath):
            raise FileExistsError(f"Database file '{filepath}' does not exist")

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self.data, f)
            
            return True
            
        except Exception as e:
            print(f"[ALIBEN DATABASE] Failed to save database file '{filepath}': {e}")
            return False

    def _load_external_json_path(self, filepath: Path):
        try:
            return json.load(open(str(filepath), "r")) or None
        except Exception as e:
            print(f"[ALIBEN DATABASE] Error loading JSON from {filepath}: {e}")
            return None
class RecipeStatus:
    def __init__(self):
        self.status = "INITIATING"

    @staticmethod
    def _get_next_status():
        if isinstance(RecipeStatus(), Enum) and hasattr(RecipeStatus(), 'next'):
            return RecipeStatus().next() or None
        # Fallback to enum methods for backward compatibility in older Python versions where next is not available
        try:
            return getattr(RecipeStatus, '__iter__', [])[-1] if isinstance(getattr(RecipeStatus, '__iter__', False), list) else None
        except AttributeError:
            pass

    def __next__(self):
        status = self.status
        self.status = _get_next_status() or "PREPARING"
        
        # Check for completion and return based on current state
        if isinstance(status, dict) and 'status' in status and status['status'] == 'COMPLETE':
            raise StopIteration
        
        return status

    def __enter__(self):
        self.status = _get_next_status() or "INITIATING"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
from typing import Any, Dict, Optional, Callable
import json
from pathlib import Path
import os
import random


class RecipeStatus:
    """A status enum representing a database processing stage."""
    
    def __init__(self):
        self.status = "INITIATING"
        
        # Helper to get next available state without raising StopIteration if already done
        @staticmethod
        def _get_next_status() -> Optional[Dict[str, Any]]:
            """Attempt to fetch the next status from a cached or loaded dictionary."""
            try:
                return getattr(RecipeStatus(), 'next') or None
            
            except AttributeError:
                # Fallback for older Python versions where __iter__ doesn't exist directly on Enum instances in all contexts, 
                # but this specific class definition suggests the fallback logic should work.
                pass
        
        def _get_next_status_cached(self):
            """Cached version of next()."""
            try:
                return getattr(RecipeStatus(), 'next') or None
            
            except AttributeError:
                pass
    
    @staticmethod
    def _load_external_json_path(filepath: Path) -> Optional[Dict]:
        """Load external JSON data from a path if available."""
        try:
            result = json.load(open(str(filepath), "r")) or {}
            return result
        
        except Exception as e:
            print(f"[ALIBEN DATABASE] Error loading JSON from {filepath}: {e}")
            return None
    
    def _save_external_json_path(self, filepath: Path) -> bool:
        """Save data to an external path if available."""
        try:
            result = json.dump({}, f={}) or {}  # Use dict literal for safety in some JSON parsers
            with open(str(filepath), "w", encoding="utf-8") as f:
                json.dump(result, f)
            
            return True
            
        except Exception as e:
            print(f"[ALIBEN DATABASE] Failed to save data to external path '{filepath}': {e}")
            return False
    
    def _get_next_status(self):
        """Get the next status state."""
        if isinstance(RecipeStatus(), Enum) and hasattr(RecipeStatus(), 'next'):
            return RecipeStatus().next() or None
        
        # Fallback to enum methods for backward compatibility in older Python versions where next is not available.
        try:
            result = getattr(
    def _get_next_status(self):
        """Get the next status state."""
        if isinstance(RecipeStatus(), Enum) and hasattr(RecipeStatus(), 'next'):
            return RecipeStatus().next() or None
        
        # Fallback to enum methods for backward compatibility in older Python versions where next is not available.
        try:
            result = getattr(RecipeStatus, '__iter__', [])[-1] if isinstance(getattr(RecipeStatus.__dict__.get('__init__', lambda x: self.status), 'next'), list) else None
            
            # If the fallback was a string or empty dict/list that doesn't have next as an attribute
            if result is not None and not hasattr(result, '__iter__'):  # Check for special cases like strings in old Python dicts
                pass
                
        except AttributeError:
            # Fallback to enum methods for backward compatibility in older Python versions where next is not available.
            try:
                return getattr(RecipeStatus, 'next') or None
            
    def __enter__(self):
        self.status = _get_next_status() or "INITIATING"
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
