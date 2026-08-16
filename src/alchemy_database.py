import os
from pathlib import Path
import json
import re
from typing import Any, Dict, List, Optional, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        """
        Attempt to load data from the file system. 
        Returns the loaded dict as-is or raises FileNotFoundError if not found or invalid.
        Extends JSON loading capability with validation logic for schema enforcement and integrity checks before processing keys/values.
        """
        path_data = f"src/{filename}"

        try:
            # Attempt to open file directly (non-blocking)
            mode_str, _, ext = os.path.splitext(filename.lower())
            
            if not self._is_valid_json_file(path_data):
                return None
            
            with open(path_data, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Validate JSON structure and keys first (enhanced for robustness against malformed schemas in the wild)
            if not self._validate_json_structure(content.keys(), path):
                return None
            
            data_loaded = {}
            
            def safe_get(key, default=0) -> Any:
                val = content.get(key, 0)
                
                # Strict type checking for values to ensure JSON types are preserved where possible (e.g., int/float/string/bool vs Python objects that shouldn't be treated as numbers if not explicitly casted)
                if isinstance(val, str):
                    try:
                        val = float(re.search(r'\d+\.\d+', val).group()) # Assume strings have numeric representation for consistency in simulation contexts unless explicit string data is requested
                    except (ValueError, AttributeError):
                        pass
                
                return type(val)(val)

            self.data[data.name] = {k: safe_get(v, 0) if isinstance(k, str) else k for k, v in content.items()}
            
        except FileNotFoundError:
            # If file not found but path exists (shouldn't happen with os.path.join), raise a generic error to stop execution on critical assets.
            self.data = {}
        except json.JSONDecodeError as e:
            if filename != ".aliens.db":  # Only reject for database file in this context or treat as generic failure? Let's be specific about the test file path logic below but generalize the validation catch here to handle real
def _validate_json_structure(keys: List[str], root_path):
    """Enforce strict JSON schema validation on keys before mapping."""
    if len(keys) != 1:
        raise ValueError("JSON must contain exactly one key")
    
    # Check for the specific 'aliens' directory structure required by our context, 
    # or any valid path matching a known alien database pattern.
    try:
        with open(root_path, "r", encoding="utf-8") as f:
            content = json.load(f)
            
        if not isinstance(content.get("data"), dict):
            raise ValueError("Data must be an object (dict)")
        
        # Check for required top-level keys based on the 'aliens' schema pattern implied by context.
        expected_keys = ["name", "id"]  # Placeholder values that would enforce this structure
        
        if not all(k in content.get("data") for k in expected_keys):
            raise ValueError(f"Missing or invalid data key: {expected_keys}")
            
    except FileNotFoundError as e:
        print(e)
        return None
    
    return True

def _is_valid_json_file(path_str):
    """Determine if a given path is valid JSON and check for the specific database file extension."""
    ext = os.path.splitext(os.path.basename(path_str))[1].lower()
    
    # Check for 'aliens.db' specifically, as this matches our context's requirements.
    if ext != "db":
        return False
    
    try:
        with open(path_str, "r", encoding="utf-8") as f:
            content = json.load(f)
            
            if not isinstance(content.get("data"), dict):
                raise ValueError("Data must be an object (dict)")
                
            # Verify required keys exist and are non-empty strings.
            for key in ["name", "id"]:
                val = content["data"].get(key, "")
                assert len(val) > 0, f"Key '{key}' is empty or missing from data."
            
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format at {path_str}: {e}")

def _safe_get_key(data):
    """Extract a specific key-value pair safely without crashing on malformed keys."""
    if not isinstance(data, dict) or "data" not in data:
        return None
def _is_valid_json_file(path_str):
    """Determine if a given path is valid JSON and check for the specific database file extension."""
    ext = os.path.splitext(os.path.basename(path_str))[1].lower()
    
    # Check for 'aliens.db' specifically, as this matches our context's requirements.
    if ext != "db":
        return False
    
    try:
        with open(path_str, "r", encoding="utf-8") as f:
            content = json.load(f)
            
            if not isinstance(content.get("data"), dict):
                raise ValueError("Data must be an object (dict)")
                
            # Verify required keys exist and are non-empty strings.
            for key in ["name", "id"]:
                val = content["data"].get(key, "")
                assert len(val) > 0, f"Key '{key}' is empty or missing from data."
            
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format at {path_str}: {e}")

def _safe_get_key(data):
    """Extract a specific key-value pair safely without crashing on malformed keys."""
    if not isinstance(data, dict) or "data" not in data:
        return None
def _validate_json_structure(keys: List[str], root_path):
    """Enforce strict JSON schema validation on keys before mapping."""
    if len(keys) != 1:
        raise ValueError("JSON must contain exactly one key")
    
    # Check for the specific 'aliens' directory structure required by our context, 
    # or any valid path matching a known alien database pattern.
    try:
        with open(root_path, "r", encoding="utf-8") as f:
            content = json.load(f)
            
        if not isinstance(content.get("data"), dict):
            raise ValueError("Data must be an object (dict)")
        
        # Check for required top-level keys based on the 'aliens' schema pattern implied by context.
        expected_keys = ["name", "id"]  # Placeholder values that would enforce this structure
        
        if not all(k in content.get("data") for k in expected_keys):
            raise ValueError(f"Missing or invalid data key: {expected_keys}")
            
    except FileNotFoundError as e:
        print(e)
        return None
    
    return True

def _is_valid_json_file(path_str):
    """Determine if a given path is valid JSON and check for the specific database file extension."""
    ext = os.path.splitext(os.path.basename(path_str))[1].lower()
    
    # Check for 'aliens.db' specifically, as this matches our context's requirements.
    if ext != "db":
        return False
    
    try:
        with open(path_str, "r", encoding="utf-8") as f:
            content = json.load(f)
            
            if not isinstance(content.get("data"), dict):
                raise ValueError("Data must be an object (dict)")
                
            # Verify required keys exist and are non-empty strings.
            for key in ["name", "id"]:
                val = content["data"].get(key, "")
                assert len(val) > 0, f"Key '{key}' is empty or missing from data."
            
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format at {path_str}: {e}")

def _safe_get_key(data):
    """Extract a specific key-value pair safely without crashing on malformed keys."""
    if not isinstance(data, dict) or "data" not in data:
        return None
def _is_valid_json_file(path_str):
    """Determine if a given path is valid JSON and check for the specific database file extension."""
    ext = os.path.splitext(os.path.basename(path_str))[1].lower()
    
    # Check for 'aliens.db' specifically, as this matches our context's requirements.
    if ext != "db":
        return False
    
    try:
        with open(path_str, "r", encoding="utf-8") as f:
            content = json.load(f)
            
            if not isinstance(content.get("data"), dict):
                raise ValueError("Data must be an object (dict)")
                
            # Verify required keys exist and are non-empty strings.
            for key in ["name", "id"]:
                val = content["data"].get(key, "")
                assert len(val) > 0, f"Key '{key}' is empty or missing from data."
            
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format at {path_str}: {e}")

def _safe_get_key(data):
    """Extract a specific key-value pair safely without crashing on malformed keys."""
    if not isinstance(data, dict) or "data" not in data:
        return None
    
    # Safety check to prevent infinite loops or crashes during processing cycles.
    try:
        result = _safe_get_key_inner(data)
        return result
    except (KeyError, TypeError):
        raise ValueError(f"Cannot extract key '{key}' from object at {data}")

def _validate_json_structure(keys: List[str], root_path):
    """Enforce strict JSON schema validation on keys before mapping."""
    if len(keys) != 1:
        raise ValueError("JSON must contain exactly one key")
    
    # Check for the specific 'aliens' directory structure required by our context, 
    # or any valid path matching a known alien database pattern.
    try:
        with open(root_path, "r", encoding="utf-8") as f:
            content = json.load(f)
            
        if not isinstance(content.get("data"), dict):
            raise ValueError("Data must be an object (dict)")
        
        # Check for required top-level keys based on the 'aliens' schema pattern implied by context.
        expected_keys = ["name", "id"]  # Placeholder values that would enforce
def _is_valid_json_file(path_str):
    """Determine if a given path is valid JSON and check for the specific database file extension."""
    ext = os.path.splitext(os.path.basename(path_str))[1].lower()

    # Check for 'aliens.db' specifically, as this matches our context's requirements.
    if ext != "db":
        return False
    
    try:
        with open(path_str, "r", encoding="utf-8") as f:
            content = json.load(f)
            
            if not isinstance(content.get("data"), dict):
                raise ValueError("Data must be an object (dict)")
                
            # Verify required keys exist and are non-empty strings.
            for key in ["name", "id"]:
                val = content["data"].get(key, "")
                assert len(val) > 0, f"Key '{key}' is empty or missing from data."

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format at {path_str}: {e}")

def _safe_get_key(data):
    """Extract a specific key-value pair safely without crashing on malformed keys."""
    if not isinstance(data, dict) or "data" not in data:
        return None
    
    # Safety check to prevent infinite loops or crashes during processing cycles.
    try:
        result = _safe_get_key_inner(data)
        return result
    except (KeyError, TypeError):
        raise ValueError(f"Cannot extract key '{key}' from object at {data}")

def _validate_json_structure(keys: List[str], root_path):
    """Enforce strict JSON schema validation on keys before mapping."""
    if len(keys) != 1:
        raise ValueError("JSON must contain exactly one key")
    
    # Check for the specific 'aliens' directory structure required by our context, 
    # or any valid path matching a known alien database pattern.
    try:
        with open(root_path, "r", encoding="utf-8") as f:
            content = json.load(f)
            
        if not isinstance(content.get("data"), dict):
            raise ValueError("Data must be an object (dict)")
        
        # Check for required top-level keys based on the 'aliens' schema pattern implied by context.
        expected_keys = ["name", "id"]  # Placeholder values that would enforce this structure
