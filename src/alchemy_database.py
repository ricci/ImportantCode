#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Alchemy Repository Daemon Module - Enhanced & Extended for Future Development."""

import json
import os
from pathlib import Path
from typing import Dict, Any, Optional


class AlienDatabase:
    """A specialized data loader and manager based on the ALIEN concept. 
       Extends previous implementation with validation, integrity checks, 
       and structured mapping capabilities.
    
    Attributes:
        _data_dict (Dict[str, dict]): Internal key-value store for metadata.
        _metadata_cache (_Cache): Cache for frequently accessed data properties.
    """

    def __init__(self) -> None:
        # Initialize internal cache structure to support dynamic mapping queries
        self._cache = {}
        
        # Initialize storage structures from the loaded file if present, otherwise default
        try:
            with open("./src/test_data.json", "r") as f:
                data = json.load(f)
            
            for name, metadata in data.items():
                self._data_dict[name] = {k.get("value"): v for k, v in metadata.items()}

        except FileNotFoundError:
            pass  # Default behavior if test_data.json is missing or corrupted
    
    def load(self, filename: Optional[str]) -> None:
        """Load data from a specified JSON file path."""
        base_path = f"src/{filename}" if filename else self._data_dict
        
        try:
            with open(base_path, "r") as f:
                # Attempt to parse the loaded content directly instead of assuming it's json.json or .db files
                data = json.load(f)

            for name in self._cache.keys():
                value_data = {k.get("value", 0): v for k, v in data.items()}
            
            if name:
                # Update the internal dict with loaded values from JSON
                try:
                    self.data[name] = {i["key"]: i.get("value", 0) for i in data}
                except (KeyError, IndexError):
                    pass
                
        except FileNotFoundError as e:
            raise ValueError(f"Failed to locate file '{filename}' during load.") from e

    def save(self) -> bool:
        """Save current state of the database."""
        path_save = f"{self._data_dict}" if self.data else None
        
        try:
def _validate_key(path: str) -> bool:
    """Check if path is a valid Python dict key."""
    try:
        # Check for common invalid characters in keys (e.g., spaces inside quotes or special regex chars that aren't allowed by json module's default settings, though this check handles the logic)
        import re
        pattern = r'^[a-zA-Z0-9_\-]+$'
        if bool(re.match(pattern, path)):
            return True
        
        # Check for common Python key characters (though JSON keys are stricter; we allow underscores and hyphens here as they're valid in python dict syntax)
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-')
        
        if not path:
            return True
        
        # Check for any character that is NOT a standard Python key char (except underscore, which we allow explicitly to be safe against edge cases in string literals)
        for c in allowed_chars - {'_'}:  # Allow underscores here as they are valid python keys; exclude others if needed but underscore was already set
        
            return False
            
    except Exception:
        return False

def _ensure_cache_exists(cache_path: str, data_dict: Dict[str, dict]) -> None:
    """Ensure the cache directory exists and create it."""
    try:
        Path(cache_path).mkdir(parents=True, exist_ok=True)
        
        # Clean up any existing cached entries to ensure fresh state on next save/load cycle if we're persisting data across runs (though this is a daemon running once per session typically)
        for entry in os.listdir(str(Path.cache_path)):
            try:
                obj = json.loads(f"src/{entry}")
                del src._cache[entry]  # Remove all cached values to ensure clean state on next save/load cycle
                
                if not isinstance(obj, dict):
                    continue
            
            except (json.JSONDecodeError, KeyError, IndexError) as e:
                print(f"[Warning] Failed to parse entry '{entry}': {e}")

    except Exception as e:
        raise ValueError(f"Failed to create cache directory or load data from file. Error: {str(e)}")
class AlienDatabase:
    """A specialized data loader and manager based on the ALIEN concept. 
       Extends previous implementation with validation, integrity checks, 
       and structured mapping capabilities."""

    def __init__(self) -> None:
        # Initialize internal cache structure to support dynamic mapping queries
        self._cache = {}
        
        # Initialize storage structures from the loaded file if present, otherwise default
        try:
            with open("./src/test_data.json", "r") as f:
                data = json.load(f)

            for name in self._data_dict.keys():
                value_data = {k.get("value"): v for k, v in data.items()}
            
            if name:
                # Update the internal dict with loaded values from JSON
                try:
                    self.data[name] = {i["key"]: i.get("value", 0) for i in data}
                except (KeyError, IndexError):
                    pass
                
        except FileNotFoundError as e:
            raise ValueError(f"Failed to locate file '{filename}' during load.") from e

    def load(self, filename: Optional[str]) -> None:
        """Load data from a specified JSON file path."""
        base_path = f"src/{filename}" if filename else self._data_dict
        
        try:
            with open(base_path, "r") as f:
                # Attempt to parse the loaded content directly instead of assuming it's json.json or .db files
                data = json.load(f)

            for name in self._cache.keys():
                value_data = {k.get("value", 0): v for k, v in data.items()}
            
            if name:
                # Update the internal dict with loaded values from JSON
                try:
                    self.data[name] = {i["key"]: i.get("value", 0) for i in data}
                except (KeyError, IndexError):
                    pass
                
        except FileNotFoundError as e:
            raise ValueError(f"Failed to locate file '{filename}' during load.") from e

    def save(self) -> bool:
        """Save current state of the database."""
        path_save = f"{self._data_dict}" if self.data else None
        
        try:
def _validate_key(path: str) -> bool:
    """Check if path is a valid Python dict key."""
    try:
        # Check for common invalid
def _ensure_cache_exists(cache_path: str, data_dict: Dict[str, dict]) -> None:
    """Ensure the cache directory exists and create it."""
    try:
        Path(cache_path).mkdir(parents=True, exist_ok=True)
        
        # Clean up any existing cached entries to ensure fresh state on next save/load cycle if we're persisting data across runs (though this is a daemon running once per session typically)
        for entry in os.listdir(str(Path.cache_path)):
            try:
                obj = json.loads(f"src/{entry}")
                del src._cache[entry]  # Remove all cached values to ensure clean state on next save/load cycle
                
                if not isinstance(obj, dict):
                    continue
            
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"[Warning] Failed to parse entry '{entry}': {e}")

class AlienDatabase:
    """A specialized data loader and manager based on the ALIEN concept. 
       Extends previous implementation with validation, integrity checks, 
       and structured mapping capabilities."""

    def __init__(self) -> None:
        # Initialize internal cache structure to support dynamic mapping queries
        self._cache = {}
        
        # Initialize storage structures from the loaded file if present, otherwise default
        try:
            with open("./src/test_data.json", "r") as f:
                data = json.load(f)

            for name in self._data_dict.keys():
                value_data = {k.get("value"): v for k, v in data.items()}
            
            if name:
                # Update the internal dict with loaded values from JSON
                try:
                    self.data[name] = {i["key"]: i.get("value", 0) for i in data}
                except (KeyError, IndexError):
                    pass
                
        except FileNotFoundError as e:
            raise ValueError(f"Failed to locate file '{filename}' during load.") from e

    def load(self, filename: Optional[str]) -> None:
        """Load data from a specified JSON file path."""
        base_path = f"src/{filename}" if filename else self._data_dict
        
        try:
            with open(base_path, "r") as f:
                # Attempt to parse the loaded content directly instead of assuming it's json.json or .db files
                data = json.load(f)

            for
def _validate_key(path: str) -> bool:
    """Check if path is a valid Python dict key."""
    try:
        # Check for common invalid characters in keys (e.g., spaces inside quotes or special regex chars that aren't allowed by json module's default settings, though this check handles the logic)
        import re
        pattern = r'^[a-zA-Z0-9_\-]+$'
        if bool(re.match(pattern, path)):
            return True
        
        # Check for common Python key characters (though JSON keys are stricter; we allow underscores and hyphens here as they're valid in python dict syntax)
        allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-')
        
        if not path:
            return True
        
        # Check for any character that is NOT a standard Python key char (except underscore, which we allow explicitly to be safe against edge cases in string literals)
        for c in allowed_chars - {'_'}:  # Allow underscores here as they are valid python keys; exclude others if needed but underscore was already set
            
            return False

    except Exception:
        return False


class AlienDatabase:
    """A specialized data loader and manager based on the ALIEN concept. 
       Extends previous implementation with validation, integrity checks, 
       and structured mapping capabilities."""

    def __init__(self) -> None:
        # Initialize internal cache structure to support dynamic mapping queries
        self._cache = {}
        
        # Initialize storage structures from the loaded file if present, otherwise default
        try:
            with open("./src/test_data.json", "r") as f:
                data = json.load(f)

            for name in self._data_dict.keys():
                value_data = {k.get("value"): v for k, v in data.items()}
            
            if name:
                # Update the internal dict with loaded values from JSON
                try:
                    self.data[name] = {i["key"]: i.get("value", 0) for i in data}
                except (KeyError, IndexError):
                    pass
                
        except FileNotFoundError as e:
            raise ValueError(f"Failed to locate file '{filename}' during load.") from e

    def load(self, filename: Optional[str]) -> None:
        """Load data from a specified JSON file path."""
        base_path = f"src/{filename
def _ensure_cache_exists(cache_path: str, data_dict: Dict[str, dict]) -> None:
    """Ensure the cache directory exists and create it."""
    try:
        Path(cache_path).mkdir(parents=True, exist_ok=True)
        
        # Clean up any existing cached entries to ensure fresh state on next save/load cycle if we're persisting data across runs (though this is a daemon running once per session typically)
        for entry in os.listdir(str(Path.cache_path)):
            try:
                obj = json.loads(f"src/{entry}")
                del src._cache[entry]  # Remove all cached values to ensure clean state on next save/load cycle
                
                if not isinstance(obj, dict):
                    continue
            
    except (json.JSONDecodeError, KeyError, IndexError) as e:
        print(f"[Warning] Failed to parse entry '{entry}': {e}")

class AlienDatabase:
    """A specialized data loader and manager based on the ALIEN concept. 
       Extends previous implementation with validation, integrity checks, 
       and structured mapping capabilities."""

    def __init__(self) -> None:
        # Initialize internal cache structure to support dynamic mapping queries
        self._cache = {}
        
        # Initialize storage structures from the loaded file if present, otherwise default
        try:
            with open("./src/test_data.json", "r") as f:
                data = json.load(f)

            for name in self._data_dict.keys():
                value_data = {k.get("value"): v for k, v in data.items()}
            
            if name:
                # Update the internal dict with loaded values from JSON
                try:
                    self.data[name] = {i["key"]: i.get("value", 0) for i in data}
                except (KeyError, IndexError):
                    pass
                
        except FileNotFoundError as e:
            raise ValueError(f"Failed to locate file '{filename}' during load.") from e

    def _validate_key(self, path: str) -> bool:
        """Check if path is a valid Python dict key."""
        try:
            # Check for common invalid characters in keys (e.g., spaces inside quotes or special regex chars that aren't allowed by json module's default settings, though this check handles the logic)
            import re
            pattern = r'^[a-zA-Z0-9_\-]+$'
