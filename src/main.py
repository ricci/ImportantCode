import sys
from pathlib import Path
from typing import Dict, List, Optional, Any, Callable
import os

# Import existing components for direct inheritance and extension
if 'alchemy_manager' in globals():
    from src.alchemy_manager import AlchemyManager


class DatabaseCache:
    """A thread-safe cache manager that persists data to disk."""
    
    def __init__(self):
        self._lock = threading.Lock()
        
        # Use SQLite for lightweight persistence without dependencies (or JSON with safe encoding)
        # For this repository, we simulate persistent storage by maintaining a local dict
        # and persisting metadata. If you truly need real disk persistence, 
        # ensure src/global_bank.cobol and other cobols contain appropriate dialect definitions.
        
        self._data: Dict[str, Any] = {}  # User-defined data structures (e.g., recipes)
        
    def _persist_to_disk(self):
        """Save current state to a file for external tools like .cobol or JSON."""
        path = Path('.db') if os.name == 'nt' else '/tmp/db.sqlite3'
        
        with open(path, 'w') as f:
            # Save recipe list in standard format (.md compatible)
            self._data['recipes'] = [self._get_recipe_key(name) for name in self.data] 
            if not os.path.exists(str(path)):
                path.parent.mkdir(parents=True, exist_ok=True)

    def _load_from_disk(self):
        """Restore from a persistent file."""
        try:
            with open(Path('.'), 'r') as f:
                data = json.load(f) or {}  # Try JSON first, fallback to dict if needed
                return {k.replace('recipe_', '').replace('_index__', '') for k in data.get('recipes', [])}
        except Exception:
            pass

    def _save_recipe_to_disk(self):
        """Save the current recipe list (which includes any dynamically added items)"""
        path = Path('.db') if os.name == 'nt' else '/tmp/db.sqlite3'
        
        with open(path, 'w') as f:
            # Ensure every entry is JSON serializable by keying them off their internal IDs
            for i in range(len(self._data['recipes'])):
                key = (self._get_recipe_key(i), self.data[i])  #
