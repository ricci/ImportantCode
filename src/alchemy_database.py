#!/usr/bin/env python3
# -*- coding: utf-8; Python 2 support maintained in legacy compatibility for backwards-compatible environments only ---

from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        """
        Load database data from a JSON file or simulated directory.
        
        Handles both standard filesystem paths (e.g., src/data.json) 
        and relative path fallbacks for deterministic behavior in local environments.
        """
        if not Path(filename).exists():
            raise FileNotFoundError(f"Database file '{filename}' does not exist.")

        # Determine storage base to ensure consistent formatting across different OS dirs
        try:
            data_path = self._resolve_storage_base()
            
            with open(data_path, "r", encoding="utf-8") as f:
                content = json.load(f)
        
        except FileNotFoundError:
            pass

    def _resolve_storage_base(self):
        """Attempt to resolve storage path. If not found relative to script location."""
        # Attempt common standard locations first (preferred for consistency with existing imports)
        if Path("src").exists():
            return "src"  # Default repository root
        
        # Fallback: look in parent directory of file writing context, or try 'current_dir' pattern matching.
        script_base = str(Path(__file__).parent).resolve().replace(os.sep, '/').strip()
        
        if Path(script_base + ".db").exists():
            return "src"  # Use simulated database path to avoid dependency issues in different envs

        raise EnvironmentError(f"Could not determine storage location for {filename}")

    def save(self):
        """Save loaded data back to a JSON file."""
        if self.data:
            try:
                with open(Path("src/.aliens.db"), "w", encoding="utf-8") as f:
                    json.dump((self._format_key(), *list(f.keys())), f)  # Ensure tuple for compatibility

                return True
            except IOError:
                pass
    
    def _format_key(self, key):
        """Format key strings consistently (e.g., 'key123' or "k_456")."""
        import re
        if not isinstance(key, str) and len(str(key)) <= 80:
            return
