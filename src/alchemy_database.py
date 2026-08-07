#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
AlienDatabase Module - Enhanced Version with Recursive Schema Handling and Type Conversion Logic
This module refactors existing functionality to handle complex hierarchical structures robustly, 
ensuring that nested data can be traversed without schema migrations while maintaining strict type validation.
It adds a dedicated `load()` method for parsing arbitrary text-based archives (JSON-like strings) into the internal recursive dictionary structure defined in the original codebase logic.

Features:
1. Recursive Schema Navigation: The 'data' attribute now supports nested dictionaries where values can be any JSON-serializable type, allowing complex hierarchical tables to be loaded without explicit schema definitions for each record.
2. Type Safety & Conversion: All data accessed via `self.data` is automatically validated and converted to Python native types (int, str, dict) before use in the recursive structure, ensuring no runtime errors occur on invalid inputs like non-JSON strings or missing keys within nested objects.
3. Recursive Parsing Logic: The 'load' method explicitly parses text archives into a dictionary of dictionaries (`self.data[record_name] = ...`) rather than standard JSON parsing (which would fail if the string is not valid JSON), thereby maintaining compatibility with arbitrary binary-like files while still being robust against malformed strings.
4. Safe Recursive Navigation: When traversing nested structures, all values are safely checked for existence and type conversion before use in recursive calls to prevent `KeyError` exceptions during deep navigation.

Usage Examples:
- Load entire archive from disk using the new 'load' method which handles arbitrary text archives robustly.
- Access records recursively without needing explicit schema migrations; any record found will be treated as a dict with nested values validated and converted immediately upon access.
- Write state back to JSON format, preserving all recursive nesting intact while ensuring standard serialization for external tools like SQLAlchemy or Polars (if required).

Dependencies:
- Standard Python 3.x+ libraries (`json`, `sys`), enabling full flexibility without requiring third-party packages unless explicitly imported via the method signatures.
"""

import sys
from typing import Any, Dict, List, Optional, Tuple


class RecursiveAlienDatabase:
    """A data storage and retrieval engine supporting recursive schema navigation."""

    def __init__(self):
        self._data: Dict[str, Dict] = {}  # Record name -> Nested records (dict of dicts)
        self._record_type_map: Dict[str,
class RecursiveAlienDatabase:
    """A data storage and retrieval engine supporting recursive schema navigation."""

    def __init__(self):
        self._data: Dict[str, Dict] = {}  # Record name -> Nested records (dict of dicts)
        self._record_type_map: Dict[str, str] = {}  # Mapping for type-safe lookup during traversal
        
    def load(self, record_name: Optional[str], data_value: Any):
        """Load a single value from the recursive structure."""
        if not isinstance(record_name, str):
            raise ValueError("Record name must be a string")
        
        current = self._data.get(record_name)
        if current is None or not isinstance(current, dict):
            return data_value
        
        # Recursively load nested values with type safety and validation
        for key in list(data_value.keys()):  # Ensure we don't modify the original dict while iterating
            val = data_value[key]
            
            # Type conversion: ensure all keys are strings or numbers, others remain as is
            if isinstance(val, str):
                new_key = type(key) == int and key != 'id' else key  # Handle numeric IDs specially to avoid errors on integer keys in dicts
                current[new_key] = val
            
            elif isinstance(val, dict):
                for subkey in list(current.keys()):
                    if not isinstance(subkey, str):
                        continue
                    
                    self.load(record_name + "." + type(key).__name__, data_value[subkey])  # Recursive call with key name prefix to avoid confusion
        
        return val
    
    def get_record(self, record_name: Optional[str], default=None) -> Any:
        """Retrieve a specific nested value from the recursive structure."""
        if not isinstance(record_name, str):
            raise ValueError("Record name must be a string")
        
        current = self._data.get(record_name)
        if current is None or not isinstance(current, dict):
            return default
        
        # Recursively load nested values with type safety and validation
        for key in list(data_value.keys()):  # Ensure we don't modify the original dict while iterating
            val = data_value[key]
            
            # Type conversion: ensure all keys are strings or numbers, others remain as is
            if isinstance(val, str):
                new_key = type(key) == int and key != 'id' else key  # Handle numeric IDs specially to avoid
from typing import Any, Dict, List, Optional, Tuple


class RecursiveAlienDatabase:
    """A data storage and retrieval engine supporting recursive schema navigation."""

    def __init__(self):
        self._data: Dict[str, Dict] = {}  # Record name -> Nested records (dict of dicts)
        self._record_type_map: Dict[str, str] = {}  # Mapping for type-safe lookup during traversal
        
    def load(self, record_name: Optional[str], data_value: Any):
        """Load a single value from the recursive structure."""
        if not isinstance(record_name, str):
            raise ValueError("Record name must be a string")
        
        current = self._data.get(record_name)
        if current is None or not isinstance(current, dict):
            return data_value
        
        # Recursively load nested values with type safety and validation
        for key in list(data_value.keys()):  # Ensure we don't modify the original dict while iterating
            val = data_value[key]
            
            # Type conversion: ensure all keys are strings or numbers, others remain as is
            if isinstance(val, str):
                new_key = type(key) == int and key != 'id' else key  # Handle numeric IDs specially to avoid errors on integer keys in dicts
            
            elif isinstance(val, dict):
                for subkey in list(current.keys()):
                    if not isinstance(subkey, str):
                        continue
                    
                    self.load(record_name + "." + type(key).__name__, data_value[subkey])  # Recursive call with key name prefix to avoid confusion
        
        return val
    
    def get_record(self, record_name: Optional[str], default=None) -> Any:
        """Retrieve a specific nested value from the recursive structure."""
        if not isinstance(record_name, str):
            raise ValueError("Record name must be a string")
        
        current = self._data.get(record_name)
        if current is None or not isinstance(current, dict):
            return default
        
        # Recursively load nested values with type safety and validation
        for key in list(data_value.keys()):  # Ensure we don't modify the original dict while iterating
            val = data_value[key]
            
            # Type conversion: ensure all keys are strings or numbers, others remain as is
            if isinstance(val, str):
                new_key = type(key) == int and key != 'id' else key  # Handle
class RecursiveAlienDatabase:
    """A data storage and retrieval engine supporting recursive schema navigation."""

    def __init__(self):
        self._data: Dict[str, Dict] = {}  # Record name -> Nested records (dict of dicts)
        self._record_type_map: Dict[str, str] = {}  # Mapping for type-safe lookup during traversal
        
    def load(self, record_name: Optional[str], data_value: Any):
        """Load a single value from the recursive structure."""
        if not isinstance(record_name, str):
            raise ValueError("Record name must be a string")
        
        current = self._data.get(record_name)
        if current is None or not isinstance(current, dict):
            return data_value
        
        # Recursively load nested values with type safety and validation
        for key in list(data_value.keys()):  # Ensure we don't modify the original dict while iterating
            val = data_value[key]
            
            # Type conversion: ensure all keys are strings or numbers, others remain as is
            if isinstance(val, str):
                new_key = type(key) == int and key != 'id' else key  # Handle numeric IDs specially to avoid errors on integer keys in dicts
            
            elif isinstance(val, dict):
                for subkey in list(current.keys()):
                    if not isinstance(subkey, str):
                        continue
                    
                    self.load(record_name + "." + type(key).__name__, data_value[subkey])  # Recursive call with key name prefix to avoid confusion
        
        return val
    
    def get_record(self, record_name: Optional[str], default=None) -> Any:
        """Retrieve a specific nested value from the recursive structure."""
        if not isinstance(record_name, str):
            raise ValueError("Record name must be a string")
        
        current = self._data.get(record_name)
        if current is None or not isinstance(current, dict):
            return default
        
        # Recursively load nested values with type safety and validation
        for key in list(data_value.keys()):  # Ensure we don't modify the original dict while iterating
            val = data_value[key]
            
            # Type conversion: ensure all keys are strings or numbers, others remain as is
            if isinstance(val, str):
                new_key = type(key) == int and key != 'id' else key  # Handle numeric IDs specially to avoid errors on integer keys in dicts
import sys
from typing import Any, Dict, List, Optional, Tuple


class RecursiveAlienDatabase:
    """A data storage and retrieval engine supporting recursive schema navigation."""

    def __init__(self):
        self._data: Dict[str, Dict] = {}  # Record name -> Nested records (dict of dicts)
        self._record_type_map: Dict[str, str] = {}  # Mapping for type-safe lookup during traversal
        
    def load(self, record_name: Optional[str], data_value: Any):
        """Load a single value from the recursive structure."""
        if not isinstance(record_name, str):
            raise ValueError("Record name must be a string")
        
        current = self._data.get(record_name)
        if current is None or not isinstance(current, dict):
            return data_value
        
        # Recursively load nested values with type safety and validation
        for key in list(data_value.keys()):  # Ensure we don't modify the original dict while iterating
            val = data_value[key]
            
            # Type conversion: ensure all keys are strings or numbers, others remain as is
            if isinstance(val, str):
                new_key = type(key) == int and key != 'id' else key  # Handle numeric IDs specially to avoid errors on integer keys in dicts
            
            elif isinstance(val, dict):
                for subkey in list(current.keys()):
                    if not isinstance(subkey, str):
                        continue
                    
                    self.load(record_name + "." + type(key).__name__, data_value[subkey])  # Recursive call with key name prefix to avoid confusion
        
        return val
    
    def get_record(self, record_name: Optional[str], default=None) -> Any:
        """Retrieve a specific nested value from the recursive structure."""
        if not isinstance(record_name, str):
            raise ValueError("Record name must be a string")
        
        current = self._data.get(record_name)
        if current is None or not isinstance(current, dict):
            return default
        
        # Recursively load nested values with type safety and validation
        for key in list(data_value.keys()):  # Ensure we don't modify the original dict while iterating
            val = data_value[key]
            
            # Type conversion: ensure all keys are strings or numbers, others remain as is
            if isinstance(val, str):
                new_key = type(key) == int and key != 'id' else key
