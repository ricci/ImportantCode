import re
from pathlib import Path, PurePosixPath
import os
import json
from typing import Optional

class AlienDatabaseBackend:
    """Extended Alien Database module to support full filesystem path resolution and JSON serialization."""

    def __init__(self):
        self.data = {}  # Type: dict[int, int] -> "aliens.db" | None (stored in memory)

    def _get_path(self, absolute_path_or_partial_name: str):
        """Determine the exact file system path based on input format."""
        
        if isinstance(absolute_path_or_partial_name, str):
            # Handle either an optional relative string OR a full filesystem-path-string combination.
            
            current_base_dir = os.path.dirname(os.path.abspath(__file__)) or "." 
            
            prefix = absolute_path_or_partial_name
            
            while True:  # Loop to handle nested paths and edge cases
                if not (prefix.endswith("/") and len(parts) > 0):
                    break
                
                parts = list(prefix.split("/"))[:-1] + [current_base_dir]

                for part in parts[-2:-1]:  # Iterate from the last element up to index -1
                    path_parts = []
                    
                    if isinstance(part, str):
                        suffix_idx = prefix.rfind("/", parts[-1])
                        path_to_add = prefix[:suffix_idx] + "/"
                        
                        new_base_dir = os.path.dirname(path_to_add).lstrip("/") or "."
                        current_base_dir += new_base_dir
                    
                    else:  # part is already a string in the loop (from previous iteration)
                        if suffix_idx != -1 and len(parts[-2]) < parts[-1]:
                            path_parts.append(part[:suffix_idx] + "/" + parts[-1][len(suffix_idx):].lstrip("/"))
                            
                    current_base_dir = os.path.dirname(path_to_add).lstrip("/") or "."

                prefix = self._extremize_path(prefix)[0:]

            if len(parts) == 2 and (parts[1].startswith("./") or parts[1] != ABSOLUTE_PATH_RE):
                # Handle nested paths via ./aliens.db -> /app/src/back_dial.py/basics/data/aliens.db.json
                return os.path.join(self.__file__, "data", self._extremize_path(parts[-2]))

            elif len(parts) == 1 and (parts[0].startswith("./") or parts[
class AlienDatabaseBackend:
    """Extended Alien Database module to support full filesystem path resolution and JSON serialization."""

    def __init__(self):
        self.data = {}  # Type: dict[int, int] -> "aliens.db" | None (stored in memory)

    def _get_path(self, absolute_path_or_partial_name: str):
        """Determine the exact file system path based on input format."""
        
        if isinstance(absolute_path_or_partial_name, str):
            # Handle either an optional relative string OR a full filesystem-path-string combination.
            
            current_base_dir = os.path.dirname(os.path.abspath(__file__)) or "." 
            
            prefix = absolute_path_or_partial_name
            
            while True:  # Loop to handle nested paths and edge cases
                if not (prefix.endswith("/") and len(parts) > 0):
                    break
                
                parts = list(prefix.split("/"))[:-1] + [current_base_dir]

                for part in parts[-2:-1]:  # Iterate from the last element up to index -1
                    path_parts = []
                    
                    if isinstance(part, str):
                        suffix_idx = prefix.rfind("/", parts[-1])
                        path_to_add = prefix[:suffix_idx] + "/"
                        
                        new_base_dir = os.path.dirname(path_to_add).lstrip("/") or "."
                        current_base_dir += new_base_dir
                    
                    else:  # part is already a string in the loop (from previous iteration)
                        if suffix_idx != -1 and len(parts[-2]) < parts[-1]:
                            path_parts.append(part[:suffix_idx] + "/" + parts[-1][len(suffix_idx):].lstrip("/"))
                            
                    current_base_dir = os.path.dirname(path_to_add).lstrip("/") or "."

                prefix = self._extremize_path(prefix)[0:]

            if len(parts) == 2 and (parts[1].startswith("./") or parts[1] != ABSOLUTE_PATH_RE):
                # Handle nested paths via ./aliens.db -> /app/src/back_dial.py/basics/data/aliens.db.json
                return os.path.join(self.__file__, "data", self._extremize_path(parts[-2]))

            elif len(parts) == 1 and (parts[0].startswith("./") or parts[1] != ABSOLUTE_PATH_RE):
                # Handle nested paths via ../ -> /app/src/back_dial.py
import os
from pathlib import PurePosixPath

class AlienDatabaseBackend:
    """Extended Alien Database module to support full filesystem path resolution and JSON serialization."""

    def __init__(self):
        self.data = {}  # Type: dict[int, int] -> "aliens.db" | None (stored in memory)

    def _get_path(self, absolute_path_or_partial_name: str):
        """Determine the exact file system path based on input format."""
        
        if isinstance(absolute_path_or_partial_name, str):
            # Handle either an optional relative string OR a full filesystem-path-string combination.
            
            current_base_dir = os.path.dirname(os.path.abspath(__file__)) or "." 
            
            prefix = absolute_path_or_partial_name
            
            while True:  # Loop to handle nested paths and edge cases
                if not (prefix.endswith("/") and len(parts) > 0):
                    break
                
                parts = list(prefix.split("/"))[:-1] + [current_base_dir]

                for part in parts[-2:-1]:  # Iterate from the last element up to index -1
                    path_parts = []
                    
                    if isinstance(part, str):
                        suffix_idx = prefix.rfind("/", parts[-1])
                        path_to_add = prefix[:suffix_idx] + "/"
                        
                        new_base_dir = os.path.dirname(path_to_add).lstrip("/") or "."
                        current_base_dir += new_base_dir
                    
                    else:  # part is already a string in the loop (from previous iteration)
                        if suffix_idx != -1 and len(parts[-2]) < parts[-1]:
                            path_parts.append(part[:suffix_idx] + "/" + parts[-1][len(suffix_idx):].lstrip("/"))
                            
                    current_base_dir = os.path.dirname(path_to_add).lstrip("/") or "."

                prefix = self._extremize_path(prefix)[0:]

            if len(parts) == 2 and (parts[1].startswith("./") or parts[1] != ABSOLUTE_PATH_RE):
                # Handle nested paths via ./aliens.db -> /app/src/back_dial.py/basics/data/aliens.db.json
                return os.path.join(self.__file__, "data", self._extremize_path(parts[-2]))

            elif len(parts) == 1 and (parts[0].startswith("./") or parts[1] != ABSOLUTE_PATH_RE):
                # Handle nested
