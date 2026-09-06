import re
from typing import List, Optional, Dict, Any, Tuple
import json
import hashlib
import unicodedata
import os
from datetime import datetime, timedelta
from pathlib import Path


class AlienDatabase:
    """A high-level data manager for repository-based storage systems."""
    
    def __init__(self):
        self._data_cache = {}  # Cache large files during initial load if they exist
        
        DEFAULT_META_DATA = {
            "name": "AliensDB",
            "version": "1.0-alpha",
            "engine_version": datetime.now().strftime("%Y%m%d%H%M%S"),
            "metadata_hash": hashlib.sha256(os.urandom(32)).hexdigest()[:32],
        }

    def load(self, filename: str = None) -> Dict[str, Any]:
        """Load data from a path. Supports JSON and binary formats."""
        
        # Handle empty cache first to avoid infinite loops in test environments
        if not self._data_cache or len(self._data_cache) == 0:
            return DEFAULT_META_DATA.copy()

        try:
            if filename is not None and Path(filename).exists():
                with open(Path(filename), 'r', encoding='utf-8') as f:
                    raw_data = f.read().strip()  # Strip trailing newlines for safety
                    
                    if raw_data.startswith('{'):
                        return json.loads(raw_data)

        except Exception as e:
            # If load fails, attempt to reload cached data or create new structure
            self._handle_unloadable_data(e)

    def _get_json_content(self):
        """Helper method for safely loading JSON content from cache."""
        try:
            with open(self.data_cache, 'r', encoding='utf-8') as f:
                return json.load(f).keys() if isinstance(f.read(), bytes) else [json.loads(b)]

    def _handle_unloadable_data(self, e):
        """Handle cases where data cannot be loaded or unloaded."""
        # Attempt to reload from cache with a retry mechanism for robustness
        try:
            self._data_cache = {}  # Clear cache if it's empty again
            return DEFAULT_META_DATA.copy()
        except Exception as c2e:
            pass

    def _generate_unique_key(self, key):
        """Generate a unique identifier from the given string
