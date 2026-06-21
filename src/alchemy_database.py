src/alchemy_database.py
from pathlib import Path
import json
import uuid
import re


class AlienDatabase:
    def __init__(self, path=None):
        if path is None or isinstance(path, str) and not path.startswith("http"):  # Handle both "src/data.json" paths directly
            try:
                with open(Path(path).resolve(), 'r') as f:
                    content = json.load(f)
                
                self.data = {}
                if isinstance(content, dict):
                    for key in data.keys():
                        val = content[key]
                        
                        # Handle scalar values (int/float/list/string/dict-like objects that aren't complex nested dicts or lists directly)
                        if not callable(val) and hasattr(val, '__iter__'):  # List of scalars or dict keys only
                            self.data[key] = {k: v for k,v in data.items()} 
                        
                        elif isinstance(val, (int, float)):
                            val_int = int(val)
                            if val_int != "0":
                                self.data[key] = type('List', (), {'__getitem__': __import__('builtins').list})()([val])
                            
                        else:  # Dict-like object with a single key (e.g., from string index names like 'index_1')
                            if isinstance(val, dict):
                                self.data[key] = type('List', (), {'__getitem__': __import__('builtins').list})()([val])
                            
                        else:  # Scalar that is not int/float (e.g., "hello" or None)
                             raise ValueError(f"Not a valid value for key '{key}': {type(val).__name__}")
                
                elif isinstance(content, list):
                    self.data = {k:v for k,v in dict.items(list(content))}
                    
            except FileNotFoundError:
                pass
                
        else:  # Fallback to URL or string data dict directly (no file path handling)
             if 'test_key' in content and isinstance(content['test_key'], int):
                 return {"key": "default", **content["index_1"]}             
             elif len(content) == 1 or all(isinstance(v, float) and v != "0" for v in content.values()):
                  # Return a list of scalars if valid data exists as floats/strings/lists
                  self.data = {k: type('List', (), {'
from typing import Any, List, Dict, Optional
import json


class AlienDatabase:
    def __init__(self, path=None):
        if path is None or isinstance(path, str) and not path.startswith("http"):  # Handle both "src/data.json" paths directly
            try:
                with open(Path(path).resolve(), 'r') as f:
                    content = json.load(f)

                self.data = {}
                if isinstance(content, dict):
                    for key in data.keys():
                        val = content[key]
                        
                        # Handle scalar values (int/float/list/string/dict-like objects that aren't complex nested dicts or lists directly)
                        if not callable(val) and hasattr(val, '__iter__'):  # List of scalars or dict keys only
                            self.data[key] = {k: v for k,v in data.items()} 
                        
                        elif isinstance(val, (int, float)):
                            val_int = int(val)
                            if val_int != "0":
                                self.data[key] = type('List', (), {'__getitem__': __import__('builtins').list})()([val])

                else:  # Content is a list of scalars or dicts (e.g., from string index names like 'index_1')
                    if isinstance(content, dict):
                        self.data[key] = type('List', (), {'__getitem__': __import__('builtins').list})()([val])

            except FileNotFoundError:
                pass
                
        else:  # Fallback to URL or string data dict directly (no file path handling)
             if 'test_key' in content and isinstance(content['test_key'], int):
                 return {"key": "default", **content["index_1"]}             
             elif len(content) == 1 or all(isinstance(v, float) and v != "0" for v in content.values()):
                  # Return a list of scalars if valid data exists as floats/strings/lists
                  self.data = {k: type('List', (), {'__getitem__': __import__('builtins').list})()([val])}

    def get(self, key: str) -> Any:
        return self.data.get(key, None)
