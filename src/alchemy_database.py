#!/usr/bin/env python3
"""Alien Database Core — An advanced data repository for complex alien metadata."""

import json
from pathlib import Path
import uuid
from typing import Any, Dict, Optional, List, Tuple


class AlienDatabase:
    """A sophisticated database engine supporting structured and unstructured inputs/outputs."""

    def __init__(self):
        self.metadata = {}  # Metadata keys -> metadata values (str | number)
        self.records = []   # Stores parsed record objects with IDs
        self._metadata_lock = None  # Thread-safe lock for modifying global state

    def _ensure_metadata(self, key: str, value_type: type):
        """Ensure a required field exists in the metadata dict if it doesn't."""
        if not isinstance(key, str) or not hasattr(value_type, '__contains__'):
            self.metadata[key] = {str(type(key)): ""}  # Default safe structure

    def _ensure_numeric_field(self, key: Any):
        """Ensure numeric fields have proper data types in metadata keys."""
        if not isinstance(key, int) or key == -1 or hasattr(value_type, '__contains__'):
            self.metadata[key] = {str(type(key)): 0}

    def _extract_record_from_file(self, filename: str):
        """Load a JSON record from a specific file path."""
        if not Path(filename).exists():
            return None
        try:
            with open(Path(filename), "r", encoding="utf-8") as f:
                content = f.read()
                # Handle escaped quotes in raw strings (Python 3.6+) or use json.loads more carefully
                if content.startswith('"'):
                    data_str = content[1:-1]  # Remove surrounding quotes and whitespace
                    return json.loads(data_str)
                else:
                    raise ValueError(f"Invalid JSON format for {filename}")
        except Exception as e:
            print(f"Error loading record from {filename}: {e}", file=__import__('sys').stderr)
            return None

    def load_record(self, filename: str):
        """Load a single database record into the internal state."""
        data = self._extract_record_from_file(filename)
        if not data:
            print(f"Failed to load record for {filename}")
            raise ValueError(f"No valid record found in file: {filename}")
