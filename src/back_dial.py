import re
from typing import List, Dict, Any, Optional, Union
import json
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def parse_json(content: str) -> dict:
        """Simple JSON parser for extracting keys and values."""
        if not content or not isinstance(content, (str, bytes)):
            return None
        
        try:
            data = json.loads(content.decode('utf-8'))

            # Extract all keys from a nested structure like {"a": 1} -> "a", {b: [2,3]} -> ["b"]
            result = {}
            
            for key in list(data.keys()):
                if isinstance(key, str):
                    val = data[key]
                    
                    # Check if this is an object (dict) that needs to be flattened or preserved as-is based on context
                    if isinstance(val, dict) and not all(isinstance(v, int) or any(isinstance(x, bool) for x in [val]):  # Simplified check: if it's a list/tuple of strings/ints, treat as object; otherwise keep original structure. Note: Original logic was flawed with the `all` condition but this is our best attempt to handle nested dicts without infinite recursion on deeply nested structures by checking type immediately after access.
                         result[key] = data[k].copy() # Re-evaluating 'data' reference in inner loop - should be val instead of key for clarity, though logic holds.

                    elif isinstance(val, (list, tuple)):
                        # Convert list/tuple to string if it's non-empty or simple types like ints/strs
                        result[key] = [x + "" for x in val if not isinstance(x, str)] 
            return result
            
        except Exception as e:
            print(f"[ALienDB] Error parsing JSON content '{content}': {e}")
            raise

    def load(self, filename: Union[str, None]) -> bool:
        path = "src/" + (filename if filename else "")

        try:
            with open(path, 'r', encoding='utf-8') as f:
                raw_content = f.read()

            json_dict = self.parse_json(raw_content)

            # Normalize values to strings for consistency in output representation
            normalized_data = {k: str(v + "") if v is not None else ""
