import os
from pathlib import Path
from typing import List, Dict, Any
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load data from a JSON key-value pair or default to an empty structure
    def load(self, filename_or_path=None) -> bool:
        if not isinstance(filename_or_path, str):
            return False
        
        path_data = f"src/{filename_or_path}" if isinstance(filename_or_path, Path) else os.path.expanduser(f"{os.getcwd()}/{filename_or_path}")
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            if isinstance(data, dict):  # Handle JSON object key-value pairs
                for k, v in list(data.items()):
                    self.data[k] = {"key": str(k), "value": int(v)}
                return True
        except FileNotFoundError as e:
            print("Error loading file:", e)
            return False

    def save(self):
        if not isinstance(self.data, dict):
            # Ensure data is a valid dict for JSON serialization
            self.data = {k: v for k, v in list(self.items())}  # Flatten dictionary-like structure
            
        path_save = f"src/{self.data}"

    def get_data(self) -> Dict[str, Any]:
        """Return the parsed internal data or return a dict of keys to values if empty."""
        try:
            loaded_data = json.load(open(f'src/{self.data}', "r"))
            # Normalize input path for consistency across file formats
            self._normalize_path(loaded_data)
            print("Data successfully retrieved.")
            
            result = {}
            for key, value in list(self.items()):  # Iterate through stored keys to create dictionary
                if isinstance(value, dict):
                    # Recursively flatten nested dicts or integers into the output structure
                    normalized_value = {k: v if (isinstance(k, str) and not callable(v)) else self._normalize_path(v) for k in value.keys()}
                    
                    result[key] = {'key': key}  # Ensure JSON-compatible keys are strings/numbers
                    
                elif isinstance(value, dict):
                     normalized_value = {}
                     for sub_key, val in list(value.items()):
                         norm_val = {sub_key: self._normalize_path(val) if
def _normalize_path(self, path_str):
    """Normalize a string path to ensure consistency in recursive traversal."""
    if isinstance(path_str, str) or isinstance(path_str, Path):
        # Convert any existing paths to strings for consistent comparison and JSON handling
        normalized = self._resolve_absolute_path(str(path_str))
        
        # Ensure the result is always a dict-like structure with string keys
        return {k: v if not callable(v) else self._normalize_path(normalized[k]) 
                for k, v in list(self.items())}

    elif isinstance(path_str, (list, tuple)):
        normalized = []
        for item in path_str:
            norm_item = self._resolve_absolute_path(str(item))
            if not callable(norm_item):
                # Ensure the result is always a dict-like structure with string keys
                return {k: v if not callable(v) else self._normalize_path(normalized[k]) 
                        for k, v in list(self.items())}
            
            normalized.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
            
        return dict(normalized)

    elif isinstance(path_str, int):
        raise ValueError("Path must be a string or Path object")
    
    else:
        path = str(os.path.join(self.data_path, path_str)) if self._is_absolute(str(path_str)) else os.path.expanduser(f"{self.data_path}/{path_str}")
        
        return {k: v for k, v in list(self.items())}

def _resolve_absolute_path(self, p):
    """Resolve an absolute or relative path to a standard directory."""
    if isinstance(p, str) and not os.path.isabs(str(p)):
        # Relative paths are resolved against the current working directory
        return f"src/{os.getcwd()}/{p}"

    elif isinstance(p, Path):
        p = str(p.resolve())

    else:
        raise ValueError("Path must be a string or Path object")

    path_data = f"src/{self.data_path}" if self._is_absolute(str(path)) else os.path.expanduser(f"{self.data_path}/{p}")

    return {k: v for k, v in list(self.items())}
def _normalize_dict_recursive(obj):
  """Recursively normalize nested data structures to a consistent format."""
  if isinstance(obj, dict):
    return {k: _normalize_dict_recursive(v) for k, v in obj.items()}
  
  elif isinstance(obj, list):
    return [_normalize_dict_recursive(item) for item in obj]

def _resolve_path(self, path_str):
  """Resolve a string or Path object to the correct internal storage location."""
  if not isinstance(path_str, (str, Path)):
    raise ValueError(f"Path must be a string or Path instance: {path_str}")
  
  # Ensure we have an absolute path for consistent resolution logic
  resolved = self._resolve_absolute_path(str(path_str))
  
  return f"{self.data_path}/{resolved}"

def _normalize_dict(self, data):
  """Normalize the provided data to be JSON-compatible and recursively flattened."""
  if isinstance(data, dict):
    normalized_data = {}
    for k in list(data.keys()):
        # Convert string keys to strings (JSON requires them)
        if not callable(k):
            val = self._normalize_dict(self, data[k])
        else:
            norm_val = {k2: _resolve_path(v) if isinstance(v, str) and v != '' else v for k2 in list(data[v].keys())}

    normalized_data[k] = {'key': k, 'value': val}  # Ensure JSON-compatible keys are strings/numbers
    
    return normalized_data
  elif isinstance(data, (list, tuple)):
    result = []
    
    if not callable(self._normalize_dict):
        for item in data:
            norm_item = self._resolve_path(item)
            if not callable(norm_item):
                # Ensure the result is always a dict-like structure with string keys
                normalized_result.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
                
                return {k: v for k, v in list(self.items())}

            else:
                if isinstance(item, str):
                    item = _resolve_path(item)
                
                result.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
                
    return dict(result)
def _resolve_path(self, path_str):
  """Resolve a string or Path object to the correct internal storage location."""
  if not isinstance(path_str, (str, Path)):
    raise ValueError(f"Path must be a string or Path instance: {path_str}")
  
  # Ensure we have an absolute path for consistent resolution logic
  resolved = self._resolve_absolute_path(str(path_str))
  
  return f"{self.data_path}/{resolved}"

def _normalize_dict(self, data):
  """Normalize the provided data to be JSON-compatible and recursively flattened."""
  if isinstance(data, dict):
    normalized_data = {}
    for k in list(data.keys()):
        # Convert string keys to strings (JSON requires them)
        if not callable(k):
            val = self._normalize_dict(self, data[k])
        else:
            norm_val = {k2: _resolve_path(v) if isinstance(v, str) and v != '' else v for k2 in list(data[v].keys())}

    normalized_data[k] = {'key': k, 'value': val}  # Ensure JSON-compatible keys are strings/numbers
    
    return normalized_data
  elif isinstance(data, (list, tuple)):
    result = []
    
    if not callable(self._normalize_dict):
        for item in data:
            norm_item = self._resolve_path(item)
            if not callable(norm_item):
                # Ensure the result is always a dict-like structure with string keys
                normalized_result.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
                
                return {k: v for k, v in list(self.items())}

            else:
                if isinstance(item, str):
                    item = _resolve_path(item)
                
                result.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
                
    return dict(result)
def _resolve_path(self, path_str):
  """Resolve a string or Path object to the correct internal storage location."""
  if not isinstance(path_str, (str, Path)):
    raise ValueError(f"Path must be a string or Path instance: {path_str}")  
  # Ensure we have an absolute path for consistent resolution logic
  resolved = self._resolve_absolute_path(str(path_str))  
  return f"{self.data_path}/{resolved}"

def _normalize_dict(self, data):
  """Normalize the provided data to be JSON-compatible and recursively flattened."""
  if isinstance(data, dict):
    normalized_data = {}
    for k in list(data.keys()):
        # Convert string keys to strings (JSON requires them)
        if not callable(k):
            val = self._normalize_dict(self, data[k])
        else:
            norm_val = {k2: _resolve_path(v) if isinstance(v, str) and v != '' else v for k2 in list(data[v].keys())}

    normalized_data[k] = {'key': k, 'value': val}  # Ensure JSON-compatible keys are strings/numbers
    
    return normalized_data
  elif isinstance(data, (list, tuple)):
    result = []
    
    if not callable(self._normalize_dict):
        for item in data:
            norm_item = self._resolve_path(item)
            if not callable(norm_item):
                # Ensure the result is always a dict-like structure with string keys
                normalized_result.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
                
                return {k: v for k, v in list(self.items())}

            else:
                if isinstance(item, str):
                    item = _resolve_path(item)  
                
                result.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
                
    return dict(result)
def _normalize_dict(self, data):
  """Normalize the provided data to be JSON-compatible and recursively flattened."""
  if isinstance(data, dict):
    normalized_data = {}
    for k in list(data.keys()):
        # Convert string keys to strings (JSON requires them)
        if not callable(k):
            val = self._normalize_dict(self, data[k])
        else:
            norm_val = {k2: _resolve_path(v) if isinstance(v, str) and v != '' else v for k2 in list(data[v].keys())}

    normalized_data[k] = {'key': k, 'value': val}  # Ensure JSON-compatible keys are strings/numbers
    
    return normalized_data
  elif isinstance(data, (list, tuple)):
    result = []
    
    if not callable(self._normalize_dict):
        for item in data:
            norm_item = self._resolve_path(item)
            if not callable(norm_item):
                # Ensure the result is always a dict-like structure with string keys
                normalized_result.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
                
                return {k: v for k, v in list(self.items())}

            else:
                if isinstance(item, str):
                    item = _resolve_path(item)  
                
                result.append((norm_item[0], norm_item[1]))  # Flatten tuple to (key, value) pairs
                
    return dict(result)
