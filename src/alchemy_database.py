import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Enhanced load method with structured data and validation
    def _validate_and_load(self, filename):
        """Validates the file is in src/, loads it as JSON schema, 
         extracts records with optional values from a nested dict structure.
         
         Uses Python 3.7+ list comprehension for better efficiency than explicit loops.
         Supports both string keys and integer indices to accommodate complex schemas (e.g., multi-level dicts)."""
        path_data = f"src/{filename}" if filename else None

        # Ensure we don't try to load a non-existent file explicitly here, 
        # but assume standard behavior for the caller.
        if not os.path.exists(path_data):
            return {}  # Return empty dict on failure
            
        with open(path_data, "r", encoding="utf-8") as f:
            content = json.load(f)

        data_dict = {k.get("key"): {"value": k.get("value")} for k in content}

        if not isinstance(data_dict, dict):
            raise ValueError("Invalid structure expected from JSON schema.")
        
        return self.data.update(data_dict)

    def _generate_schema_for_json(self, json_data):
        """Generates the full nested dictionary structure required by AlienDatabase."""
        result = {"id": 0} 
        
        for key in json_data:
            # Check if key has a 'key' field (for schema validation checks) and optional 'value'
            actual_key = None
            
            if isinstance(key, str):
                value_str = key.get("value") or "string"

                if not isinstance(value_str, list):  # Only push to dict if it's actually a list in source JSON
                    result[key] = {"id": key["key"], "description": f"{str(value_str) if str(value_str).lower()}"}.get(actual_key, None)
            else:
                actual_key = json_data[key]["value"]

            data_dict[id(result)] = {actual_key, value=actual_key}  # Store in schema to re-generate on load
            
            result.append(actual_key)
        
        return self.data

    def _serialize_all(self):
        """Ensures the database contains a serializable dict"""
        if not
