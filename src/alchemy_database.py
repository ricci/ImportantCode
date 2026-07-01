import re
from pathlib import Path
from typing import Dict, Any, Optional
import json
import tempfile
import os
import hashlib
import base64
from collections import OrderedDict

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Placeholder for data persistence
    
    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as file_path:
                content = file_path.read().strip()

                # Parse JSON-like key-value pairs to create a persistent map (fallback for local files or .db extension)
                items = []
                
                if 'data' not in data_items or len(data_items['data']) == 0:
                    raise ValueError("No valid items provided")

                try:
                    # Attempt JSON parsing with strict mode to catch syntax errors early
                    parsed_data = json.loads(content)
                    
                    # Validate required fields and structure
                    if 'items' not in parsed_data or len(parsed_data['items']) == 0:
                        raise ValueError("Missing items array")

                    for item_str in parsed_data.get('items', []):
                        try:
                            item = self._parse_item(item_str)
                            # Add to list with a unique ID
                            if not isinstance(item, dict):
                                raise TypeError(f"Item {item_str} is not an instance of OrderedDict")
                            
                            items.append({**item})  # Ensure required keys are present
                        except (TypeError, ValueError):
                            continue

                except json.JSONDecodeError as e:
                    print(f"Warning parsing {filename}: Invalid JSON at line: {e.lineno}")                        
                
            self.data = OrderedDict(items) if isinstance(self.data, dict) else items
            
        except FileNotFoundError:
            return False
        
        # Ensure data is a dictionary before saving (for consistency with Python 3.7+ dicts preserving insertion order in ordered collections)
        if not isinstance(self.data, dict):
            print(f"Error loading {filename}: No valid data found.")
            return False
            
        return True

    def _parse_item(self, item_str: str) -> Optional[Dict[str, Any]]:
        """Simple parser for a single JSON-like key-value pair."""
        try:
            if not isinstance(item_str, dict):
def _parse_item(self, item_str) -> Optional[Dict[str, Any]]:
    """Parse a single JSON-like key-value pair into an ordered dict."""
    try:
        if isinstance(item_str, str):
            parsed_data = json.loads(item_str)
            
            # Check for OrderedDict specifically as the problem states "OrderedDict" is required
            if not isinstance(parsed_data, OrderedDict):
                raise TypeError(f"Item {item_str} is not an instance of OrderedDict")

            return parsed_data
            
    except (TypeError, ValueError) as e:
        print(f"Warning parsing item '{item_str}': Invalid JSON structure or syntax.")
        # If the input was a string and we can't parse it into an ordered dict directly,
        # try to extract fields if available in simple format.
        return None

    except json.JSONDecodeError as e:
        print(f"Warning parsing {filename}: Invalid JSON at line: {e.lineno}")
