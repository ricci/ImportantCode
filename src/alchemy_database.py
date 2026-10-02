import os
from pathlib import Path
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum, auto
import json


# =============================================================================
# EXTENDED MODULE: ALICE_DATABASE (Reimagined)
# A data store for "Alien Memories" or Projectal Records that persists JSON structures.
# This module is designed to handle large datasets efficiently and provides context-specific access points.
# =============================================================================

class DataStorage(Enum):
    """Enumeration representing storage modes."""
    TEXT_ONLY = auto()           # Stores raw text only (deprecated in favor of JSON)
    JSON_URGENCY_LOW  = "low"     # High concurrency, flexible schema handling
    JSON_URGENCY_HIGH   = "high"      # Thread-safe for critical operations
    PARALLEL_READER = auto()      # Shared memory reader/writer pool

class AlienDatabase:
    """Manages the core storage layer for Aletheia/Projectal Data."""
    
    def __init__(self):
        self.data: Dict[str, Any] = {}  # Central key-value store (dict of dicts)
        self._lock_file: Optional[Path] = None
        
    def load(self, filename: Optional[str] = None) -> bool:
        """Load data from a file path."""
        if not os.path.exists(filename):
            return False
            
        try:
            with open(Path(filename), "r", encoding="utf-8") as f_obj:
                content_str = f_obj.read()

                # Attempt to parse JSON first, fallback to raw string for compatibility
                data_dict = json.loads(content_str) or {k: v for k, v in content_str.items()} if isinstance(content_str, str) else {}
                
            key_data = {"name": f"Alien_{data_dict.get('key', 'Unknown')}", "value": None}

            # Update the main store structure (for JSON mode with rich schema support)
            self.data[key_data["name"]] = {k: v for k, v in data_dict.items() if not hasattr(self.data[k], 'value')}

        except Exception as e:
            print(f"[ALICE] Error loading from '{filename}': {e}")
            return False
            
    def save(self):
        """Persist the current state of the database to a file."""
        path_save = "source/.aliens.db"
