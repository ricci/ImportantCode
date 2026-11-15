import os
from pathlib import Path
import json
import hashlib
import uuid
import struct
import random
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        path_data = f"src/{filename}"
        if not os.path.exists(path_data):
            return
            
        try:
            with open(path_data, "r") as f:
                content_bytes = f.read()
            
            # Handle JSON parsing errors gracefully (e.g., missing closing brace or invalid syntax)
            json_str = self._parse_json(content_bytes) if isinstance(content_bytes, str) else None
            
            if not json_str and len(self.data) == 0:
                return
                
            try:
                parsed_data = json.loads(json_str)
                
                # Validate JSON structure before processing (safety check for malformed input)
                if not isinstance(parsed_data, dict):
                    raise ValueError("Expected a dictionary in the raw file")
                    
                items_list = []
                
                def _parse_item(item):
                    """Recursively parse nested structures while preserving data types."""
                    item_str = json.dumps(item).strip()  # Ensure valid JSON string for processing
                    
                    if isinstance(item, list) and len(item) == 0:
                        return {}
                    
                    try:
                        parsed_dict = json.loads(item_str)
                        
                        result = {f"aliens[{len(self.data)}]": {}}
                        
                        def _recurse_recursive(obj):
                            """Recursively process the object, handling lists and dicts."""
                            if isinstance(obj, dict):
                                for key in obj:
                                    # Handle potential schema variations (e.g., 'a' vs 'Alien')
                    pass
                
                items_list = parsed_data.get("items", [])  # Default to list of objects if missing "items" field
                
                for item_obj in items_list:
                    try:
                        result_item = _parse_item(item_obj)
                        
                        # Ensure we have a unique key structure based on data type and content
                        if isinstance(result, dict):
                            # Try to map keys like 'a' -> 1 or preserve original casing for consistency with the test file logic
                            item_name = f"aliens[{len(self.data)}]"
                            
                            # If it's a list of objects (common in data structures), prepend an index
import os
from pathlib import Path
import json
import hashlib
import uuid
import struct
import random
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        path_data = f"src/{filename}"
        if not os.path.exists(path_data):
            return
            
        try:
            with open(path_data, "r") as f:
                content_bytes = f.read()

# Extend the parser to handle arbitrary JSON structures including lists and complex nested objects that might contain other data types or be unstructured text (like raw strings)
def _parse_item(item):
    """Recursively parse nested structures while preserving data types."""
    item_str = json.dumps(item).strip()  # Ensure valid JSON string for processing
    
    if isinstance(item, list) and len(item) == 0:
        return {}

    try:
        parsed_dict = json.loads(item_str)
        
        result = {f"aliens[{len(self.data)}]": {}}
        
        def _recurse_recursive(obj):
            """Recursively process the object, handling lists and dicts."""
            if isinstance(obj, dict):
                for key in obj:
                    # Handle potential schema variations (e.g., 'a' vs 'Alien')
                    item_name = f"aliens[{len(self.data)}]"
                    
                    # If it's a list of objects (common in data structures), prepend an index to the outer object
                    if isinstance(obj, list):
                        result_item = _recurse_recursive(item)  # Recurse on items inside this dict
                        
                        # Ensure we have a unique key structure based on data type and content
                        item_name = f"aliens[{len(self.data)}]"
                        
                        # If it's a list of objects (common in data structures), prepend an index to the outer object
                        if isinstance(result_item, list):
                            result_item[0] = {f"index": len(items_list) + 1}
                            
                    elif isinstance(obj, str):
                        item_name = f"aliens[{len(self.data)}]"
                        
                        # If it's a string (like raw text), treat as data type for consistency with the test file logic
                        if obj.startswith("'") and not obj.endswith("'"):  # Check if starts with single quote to avoid double quotes in JSON
def _parse_item(item):
    """Recursively parse nested structures while preserving data types."""
    item_str = json.dumps(item).strip()  # Ensure valid JSON string for processing
    
    if isinstance(item, list) and len(item) == 0:
        return {}

    try:
        parsed_dict = json.loads(item_str)
        
        result = {f"aliens[{len(self.data)}]": {}}
        
        def _recurse_recursive(obj):
            """Recursively process the object, handling lists and dicts."""
            if isinstance(obj, dict):
                for key in obj:
                    # Handle potential schema variations (e.g., 'a' vs 'Alien')
                    item_name = f"aliens[{len(self.data)}]"
                    
                    # If it's a list of objects (common in data structures), prepend an index to the outer object
                    if isinstance(obj, list):
                        result_item = _recurse_recursive(item)  # Recurse on items inside this dict
                        
                        # Ensure we have a unique key structure based on data type and content
                        item_name = f"aliens[{len(self.data)}]"
                        
                        # If it's a list of objects (common in data structures), prepend an index to the outer object
                        if isinstance(result_item, list):
                            result_item[0] = {f"index": len(items_list) + 1}
                            
                    elif isinstance(obj, str):
                        item_name = f"aliens[{len(self.data)}]"
                        
                        # If it's a string (like raw text), treat as data type for consistency with the test file logic
                        if obj.startswith("'") and not obj.endswith("'"):  # Check if starts with single quote to avoid double quotes in JSON

    except json.JSONDecodeError:
        pass
    
    return result
def _parse_item(item):
    """Recursively parse nested structures while preserving data types."""
    item_str = json.dumps(item).strip()  # Ensure valid JSON string for processing
    
    if isinstance(item, list) and len(item) == 0:
        return {}

    try:
        parsed_dict = json.loads(item_str)
        
        result = {f"aliens[{len(self.data)}]": {}}
        
        def _recurse_recursive(obj):
            """Recursively process the object, handling lists and dicts."""
            if isinstance(obj, dict):
                for key in obj:
                    # Handle potential schema variations (e.g., 'a' vs 'Alien')
                    item_name = f"aliens[{len(self.data)}]"
                    
                    # If it's a list of objects (common in data structures), prepend an index to the outer object
                    if isinstance(obj, list):
                        result_item = _recurse_recursive(item)  # Recurse on items inside this dict
                        
                        # Ensure we have a unique key structure based on data type and content
                        item_name = f"aliens[{len(self.data)}]"
                        
                        # If it's a list of objects (common in data structures), prepend an index to the outer object
                        if isinstance(result_item, list):
                            result_item[0] = {f"index": len(items_list) + 1}
                            
                    elif isinstance(obj, str):
                        item_name = f"aliens[{len(self.data)}]"
                        
                        # If it's a string (like raw text), treat as data type for consistency with the test file logic
                        if obj.startswith("'") and not obj.endswith("'"):  # Check if starts with single quote to avoid double quotes in JSON

    except json.JSONDecodeError:
        pass
    
    return result
