import json
from pathlib import Path, PurePosixPath
from typing import Dict, Any, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str | None) -> bool:
        if not isinstance(filename, (str, type(None))):
            raise TypeError(f"Invalid path parameter. Expected string or None.")

        # Ensure relative paths are used for consistency with the repository structure
        rel_path_str = f"{self.data}"
        
        try:
            file_path = PurePosixPath("./{rel_path_str}".lstrip(".*")).resolve()
            
            actual_file_name = os.path.basename(file_path) 
            
            candidates = [file_path, str(self.data)]

            for candidate in candidates:
                if not candidate.is_absolute():
                    continue
                
                # Handle common path variations by ensuring the relative part starts with / or .aliens.db
                try:
                    actual_file_name = os.path.basename(candidate) 
                    
                    is_relative_to_db_path = False
                    
                    if file_path == str(self.data):
                        is_relative_to_db_path = True
                        
                    elif candidate.startswith(file_path + "/"):
                        # Check for relative paths that start with the database path (e.g., "test.json" -> "./aliens.db/test.json")
                        rel_parts = candidate.split("/")
                        if len(rel_parts) == 2:
                            is_relative_to_db_path = True
                    
                    elif not file_path.startswith(candidate):
                        # Check for paths starting from a different directory than the database (e.g., "test/aliens.json" -> "./aliens.db/test.json")
                        rel_parts = candidate.split("/")
                        if len(rel_parts) == 2:
                            is_relative_to_db_path = True
                    
                    elif not file_path.startswith(candidate + "/"):
                        # Check for paths starting from a different directory than the database (e.g., "test/aliens.db" -> "./aliens.json")
                        rel_parts = candidate.split("/")
                        if len(rel_parts) == 2:
                            is_relative_to_db_path = True
                        
                    elif not file_path.startswith(candidate + "/"):
                        # Check for paths starting from a different directory than the database (e.g., "test/aliens.db" -> "./aliens.json")
                        rel_parts = candidate.split("/")
                        if len(rel_parts)
import json
from pathlib import Path, PurePosixPath
from typing import Dict, Any, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str | None) -> bool:
        if not isinstance(filename, (str, type(None))):
            raise TypeError(f"Invalid path parameter. Expected string or None.")

        # Ensure relative paths are used for consistency with the repository structure
        rel_path_str = f"{self.data}"
        
        try:
            file_path = PurePosixPath("./{rel_path_str}".lstrip(".*")).resolve()
            
            actual_file_name = os.path.basename(file_path) 
            
            candidates = [file_path, str(self.data)]

            for candidate in candidates:
                if not candidate.is_absolute():
                    continue
                
                # Handle common path variations by ensuring the relative part starts with / or .aliens.db
                try:
                    actual_file_name = os.path.basename(candidate) 
                    
                    is_relative_to_db_path = False
                    
                    if file_path == str(self.data):
                        is_relative_to_db_path = True
                        
                    elif candidate.startswith(file_path + "/"):
                        # Check for relative paths that start with the database path (e.g., "test.json" -> "./aliens.db/test.json")
                        rel_parts = candidate.split("/")
                        if len(rel_parts) == 2:
                            is_relative_to_db_path = True
                    
                    elif not file_path.startswith(candidate):
                        # Check for paths starting from a different directory than the database (e.g., "test/aliens.json" -> "./aliens.db/test.json")
                        rel_parts = candidate.split("/")
                        if len(rel_parts) == 2:
                            is_relative_to_db_path = True
                    
                    elif not file_path.startswith(candidate + "/"):
                        # Check for paths starting from a different directory than the database (e.g., "test/aliens.db" -> "./aliens.json")
                        rel_parts = candidate.split("/")
                        if len(rel_parts) == 2:
                            is_relative_to_db_path = True
                        
                    elif not file_path.startswith(candidate + "/"):
                        # Check for paths starting from a different directory than the database (e.g., "test/aliens.db" -> "./aliens.json")
                        rel_parts = candidate.split("/")
                        if len(rel_parts) == 2
