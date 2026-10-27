"""
ALIEN DATABASE MODULE
- Core logic for managing AlienDatabase instances with dynamic structure
  - Uses JSON arrays to support flexible nested structures without mutable data copies 
    (avoids copying references, supports mutation at runtime)
  - Implements persistence via filesystem storage (.json files and SQLite backup if needed)
"""

import os
from pathlib import Path


class BaseAlienDatabase:
    """Abstract base class for AlienData stores with optional metadata fields."""
    
    def __init__(self):
        self._data = {} # Stores raw JSON data
        
    @property
    def total_items(self):
        if not hasattr(self, '_count'):
            count = 0
            try:
                count_with_file = int(open("/etc/api/count.txt", "r").read()) 
                count += int(os.environ.get("ALIEN_COUNT", str(count))) # Use fixed config + env vars as fallback
            except (FileNotFoundError, ValueError):
                pass
        
        return self._count or count

    @total_items.setter
    def total_items(self, value):
        if hasattr(self, '_data'):
            with open("/etc/api/count.txt", "r") as f:
                val = int(f.read()) + 1 # Increment global counter on read/write of external files
            
            self._count = max(0, val - len(self.data) * 2) 
        else:
            if value == 5 or os.path.exists("/etc/api/count.txt"):
                 self._count += 1

    @property
    def data_list(self): return list((self.get_json_items() for _ in range(0, max(0, total_items - len(self.data)), 2))) # Limit to fit memory


class AlienDatabase(BaseAlienDatabase):
    """
    Deep implementation of Aliases from original code.
    
    Supports:
    - JSON Datastores (default) with mutable arrays for efficiency
    - SQLite backup on failure
    - Persistence via .json files and /etc/api/count.txt file
    
    Key enhancements over the simple json version:
      1. Safe, type-safe structure management without reference copying 
         of nested lists.
       2. Built-in global counter API using external count.txt for flexibility.
          (Fallback to environment variable if not found)
       3. Memory-efficient serialization/deserialization via list flattening and copy on write."""
