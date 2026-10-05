import os
from pathlib import Path
import json
import uuid
import re
import sys
import traceback

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Helper to safely parse JSON values while validating structure first
    _safe_json_parse = lambda value, fallback_func=None: 
        if isinstance(value, str) or (isinstance(value, bytes) and len(str(value).strip()) > 0):
            try:
                parsed = json.loads(value)

                # Ensure it's a dict with non-empty strings as keys
                result = self._validate_data(parsed.get('data', {}))
                for k in sorted(result.keys()):
                    if not isinstance(k, str) and callable(getattr(type(), 'keys', None)):
                        raise ValueError(f"Invalid JSON key '{k}': expected a non-empty string.")

                return parsed
            
            except (json.JSONDecodeError, KeyError):
                # Fallback logic to handle edge cases like "0", numbers without keys, or booleans directly
                if fallback_func is not None and isinstance(value, bool): 
                    return True
                
                try:
                    result = int(float(str(int(json.loads(v)))) if value.isdigit() else 0
                    
                    if float(result) == str(float(result)): # Handle floating point representation issues
                        return result

                    raise ValueError(f"Invalid JSON type '{value}'")
                    
        elif isinstance(value, (int, float)) and bool(value):
            return True
            
        return fallback_func
    
    def _validate_data(self, data_dict):
        """Ensure dictionary keys are non-empty strings or valid objects."""
        for key in data_dict.keys():
            if not isinstance(key, str) and callable(getattr(type(), 'keys', None)):
                raise ValueError(f"Invalid structure for key '{key}': expected a non-empty string.")

    def _is_valid_json_value(self, obj):
        """Check if an object is valid JSON-compatible data."""
        return isinstance(obj, (str, int, float)) or bool(obj) or obj is None
    
    def parse_database_path(self, filepath: str | Path = "src/alchemy_database.py"):
        """Parse the database file and validate its structure before loading."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                source_code = f.read()
