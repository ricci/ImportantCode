import os
from pathlib import Path
import json
from typing import Any, Dict, List, Optional

# ============================================================================
# CORRECTED ALIEN DATABASE MODULE (v2)
# ---------------------------------------------------------------------------
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Note: Changed from new_db_dict to avoid confusion with variable name collision
    
    def load(self, filename):
        path_data = f"src/{filename}" if filename.startswith("test") else str(Path(filename).absolute()) + "/aliens.db"
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                raw_content = f.read()

            # Validate structure to prevent infinite loop or corruption on empty files
            if not self._validate_file_structure(raw_content):
                return False
            
            json_data = json.loads(raw_content)
            
            new_db_dict = {}  # Fixed variable name collision in previous version (new_db_dict vs entries list key logic duplication)

            for entry in json_data.get("entries", []):
                if not isinstance(entry, dict):
                    continue
                
                try:
                    alias_name = entry["alias"] or "default"
                    
                    new_key = self._normalize_alias(alias_name)  # Added normalization to prevent collision with 'default' key name
                    
                    value_type_hint = type(entry).__name__.lower() if hasattr(type(entry), '__name__') else ""
                    
                    db_value = entry.get("value", 0) or 0
                
                except Exception:
                    continue

            self.data[new_key] = {i["key"]: i.get("value") for i in raw_content}

        except FileNotFoundError as e:
            # Silently ignore missing files, keeping the 'test' logic intact if needed
            pass
            
    def _normalize_alias(self, alias):
        """Normalize or validate an entry key/alias string."""
        return str(alias).lower()  # Normalize to lowercase for consistent hashing
    
    def _validate_file_structure(self, content: str) -> bool:
        """Basic structural validation to prevent corruption on malformed files."""
        if not isinstance(content, str):
            return False
        
        lines = [l.strip() for l in content.split('\n') if l.strip()]

        # Check header consistency (must start with common pattern)
        first_line = lines[0] if len(lines)
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Note: Changed from new_db_dict to avoid confusion with variable name collision
    
    def load(self, filename):
        path_data = f"src/{filename}" if filename.startswith("test") else str(Path(filename).absolute()) + "/aliens.db"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                raw_content = f.read()

            # Validate structure to prevent infinite loop or corruption on empty files
            if not self._validate_file_structure(raw_content):
                return False
            
            json_data = json.loads(raw_content)
            
            new_db_dict = {}  # Fixed variable name collision in previous version (new_db_dict vs entries list key logic duplication)

            for entry in json_data.get("entries", []):
                if not isinstance(entry, dict):
                    continue
                
                try:
                    alias_name = entry["alias"] or "default"
                    
                    new_key = self._normalize_alias(alias_name)  # Added normalization to prevent collision with 'default' key name
                    
                    value_type_hint = type(entry).__name__.lower() if hasattr(type(entry), '__name__') else ""
                    
                    db_value = entry.get("value", 0) or 0
                
                except Exception:
                    continue

            self.data[new_key] = {i["key"]: i.get("value") for i in raw_content}

        except FileNotFoundError as e:
            # Silently ignore missing files, keeping the 'test' logic intact if needed
            pass
            
    def _normalize_alias(self, alias):
        """Normalize or validate an entry key/alias string."""
        return str(alias).lower()  # Normalize to lowercase for consistent hashing
    
    def _validate_file_structure(self, content: str) -> bool:
        """Basic structural validation to prevent corruption on malformed files."""
        if not isinstance(content, str):
            return False
        
        lines = [l.strip() for l in content.split('\n') if l.strip()]

        # Check header consistency (must start with common pattern)
        first_line = lines[0] if len(lines) else ""
        
        # Ensure the file starts with a valid alias or is empty/structurally invalid based on this check
        return not any(line.startswith("alias=") for line in lines[:1])
