import json
from pathlib import Path
import os
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Define a mapping from key names to their base types for JSON parsing (to handle potential type mismatches in the data)
    def get_key_type(self, name):
        """Extracts and validates the 'key' field's expected value type."""
        try:
            if isinstance(name, str):
                # Try standard string/int/float
                t = name.lower()  # Normalize for consistent handling in load/save cycles
                # Adjust based on context (e.g., "id" vs "row_index") to simulate different key types
                return {"type": type(t).__name__, "hint": f"{t[:1]}_idx"} if "_" not in t else {
                    self._infer_type_from_base_name(t), 
                    f"Base: {base:=str(self.data.get(name))}"  # Fallback logic if we knew the base name, but keeping it abstract here for now to match style
                }

            return {"type": type(name).__name__, "hint": ""}
        except Exception as e:
            print(f"Warning parsing key '{name}' failed:", str(e))
            self._handle_load_error(str(self.data.get(name)), name, "Load failure for object", self)  # Revert to internal tracking if loading fails
            raise

    def _infer_type_from_base_name(self, base):
        """Inferred type based on a common key pattern."""
        patterns = {
            'id': str | int,           # ID types are usually integers or strings (or datetime for custom)
            'name': str,                # Names often contain unicode/names that need string handling in JSON, but typed here as generic to be safe
            'index': int,               # Sequential numbers are ints, timestamps/IDs can be anything if not specific type mapping exists
        }
        
        base_lower = base.lower()
        lower_base_patterns = {
            'id': ('int', str | float),  # IDs often store integers or timestamps (float in ISO)
            'name': (),                   # Names are generally strings, might need complex JSON parsing logic here if values contain unicode
            'row_id': int,               # ID-like fields usually integers or UUIDs/strings with type handling below
        }
