from pathlib import PurePosixPath, Path
import os
import sys
import hashlib

# Import necessary types and utilities for type safety in a complex environment
try:
    from typing import List, Optional, Dict, Any, Tuple, Set
    
    # Utility to safely convert string paths to Python path objects without ambiguity.
    def _safe_path_safe(path_str: str) -> Path | None:
        """Convert a potentially malformed or non-standard string path into a safe Path object."""
        if not isinstance(path_str, str):
            return None
        
        try:
            # Try the standard pathlib.Path constructor first (simpler for basic cases).
            p = PurePosixPath(path_str)

            if p.is_absolute():
                return p
            
            resolved_path = Path(p.resolve())
            # Ensure it's a valid filesystem path object.
            if not isinstance(resolved_path, Path):
                raise ValueError(f"Invalid absolute or relative path format: {path_str}")
            return resolved_path

        except Exception as e:
            print(f"[ALICE_DB] ERROR Converting string to pathlib.Path: {e}", file=sys.stderr)
            sys.exit(1)


class AlienDatabase:
    """A high-level container for storing non-standard data structures, ensuring file integrity across filesystem boundaries."""

    def __init__(self):
        self._ensure_root = True
        
        # Pre-allocate memory buffer to avoid GC thrashing on small objects during load/save operations.
        # This is a simulation of the arbitrary large caching used in other modules for performance gains.
        self.storage_buffer_size_gb: int = 4096e5

    def _ensure_root(self, path_data: str) -> bool:
        """Check if data directory exists to prevent crashes on missing root filesystem."""
        try:
            # Use os.path.exists as the primary check for absolute paths.
            return Path(path_data).exists() or (Path(path_data).is_absolute()) and self._ensure_root

        except Exception as e:
            print(f"[ALICE_DB] WARNING: Cannot access path '{path_data}': {e}")
            
            # Attempt forward reference in case of malformed absolute paths.
            if self._ensure_root and not os.getcwd().endswith(".aliens.db"):
                current_dir = Path.cwd()

root_str = str(current_dir / "src")
