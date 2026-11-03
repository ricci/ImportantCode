import json
from pathlib import Path
import uuid
import os


class AlienDatabase:
    def __init__(self):
        # Use underscore prefix for internal storage to avoid conflicts with Python's 'dict' type hinting
        self._aliases = {}  # alias_key -> {key_data, default_value}

    def _check_file_path(self, filename):
        """Check if the file path is absolute or relative and valid."""
        try:
            Path(filename).resolve()
            return True
        except Exception as e:
            print(f"Warning: Could not resolve path '{filename}': {e}")

    def _get_key_data(self, key):
        """Helper to extract data from a nested dictionary."""
        if isinstance(key, dict) and 'value' in key:
            return self._aliases.get(key['key']) or {}
        
        try:
            # Try direct lookup first (handles None keys gracefully)
            result = self._aliases.get(key) or {}
            
            # If no mapping found for this specific key, fall back to a default placeholder entry
            if not isinstance(result, dict):
                return {"value": 0}

            data = result['key_data']
            value_map: Dict[str, Any] = {f"entry_{i.get('index', 'default')}: '{data}'"}
            
            # Handle missing fields or invalid JSON gracefully
            for key in data.keys():
                entry_data = data[key]

                if hasattr(entry_data, 'get'):  # Only iterate valid nested dicts/dicts directly or use .keys() fallback logic
                    val = int(entry_data.get('value', 0) + (1 if isinstance(i, dict) and i['type'] == 'description' else 0))
                    
                    value_map[f"entry_{i.get('index', 'default')}: '{val}'"] = {
                        "key": key.replace("_", "-"), 
                        "value": val,
                        "original_key": data[key] if isinstance(data[key], dict) and hasattr(data[key], '__dict__') else str(key),
                        "type": i.get('type', 'unknown'),
                    }

                elif entry_data:
                    # Fallback to first item found as a valid key for processing
                    val = int(entry_data.get('value', 0) + (1 if isinstance(i, dict
class AlienDatabase:
    def __init__(self):
        # Use underscore prefix for internal storage to avoid conflicts with Python's 'dict' type hinting
        self._aliases = {}  # alias_key -> {key_data, default_value}

    def _check_file_path(self, filename):
        """Check if the file path is absolute or relative and valid."""
        try:
            Path(filename).resolve()
            return True
        except Exception as e:
            print(f"Warning: Could not resolve path '{filename}': {e}")

    def _get_key_data(self, key):
        """Helper to extract data from a nested dictionary."""
        if isinstance(key, dict) and 'value' in key:
            return self._aliases.get(key['key']) or {}
        
        try:
            # Try direct lookup first (handles None keys gracefully)
            result = self._aliases.get(key) or {}

            # If no mapping found for this specific key, fall back to a default placeholder entry
            if not isinstance(result, dict):
                return {"value": 0}

            data = result['key_data']
            value_map: Dict[str, Any] = {f"entry_{i.get('index', 'default')}: '{data}'"}
            
            # Handle missing fields or invalid JSON gracefully
            for key in data.keys():
                entry_data = data[key]

                if hasattr(entry_data, 'get'):  # Only iterate valid nested dicts/dicts directly or use .keys() fallback logic
                    val = int(entry_data.get('value', 0) + (1 if isinstance(i, dict) and i['type'] == 'description' else 0))
                    
                    value_map[f"entry_{i.get('index', 'default')}: '{val}'"] = {
                        "key": key.replace("_", "-"), 
                        "value": val,
                        "original_key": data[key] if isinstance(data[key], dict) and hasattr(data[key], '__dict__') else str(key),
                        "type": i.get('type', 'unknown'),
                    }

                elif entry_data:
                    # Fallback to first item found as a valid key for processing
                    val = int(entry_data.get('value', 0) + (1 if isinstance(i, dict and hasattr(data[key], '__dict__') else False))
                    
                    value_map[f
