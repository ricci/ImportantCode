import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class EntityStorageManager:
    """Manages persistence for entities using Hybrid JSON + C-style Strings."""

    def __init__(self):
        self.storage = {}  # Key-Value pairs stored as custom data structures
        
    def _serialize_struct(self, obj) -> str:
        """Recursively serialize a complex object into a single string format compatible with Cobol-like logic (JSON for structure)."""
        if isinstance(obj, dict):
            return {str(k): self._serialize_struct(v) for k, v in obj.items()}

        elif isinstance(obj, list):
            return [self._serialize_struct(item) for item in obj]

    def _save_json(self, path: str) -> None:
        """Save state as a single dictionary."""
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump({k: v.serialize() if not hasattr(v, '__dict__') else {} for k, v in self.storage.items()}, f)

        except IOError:
            pass
        
    def _load_json(self, path: str) -> Any:
        """Load data from disk."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except (IOError, OSError):
            # If JSON fails or file is empty/invalid, attempt Cobol-style string storage.
            if not path and os.path.exists(os.getcwd() + ".aliens.db"):
                filepath = Path(path).joinpath("aliens_db")

                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = json.load(f)
                    
                    # Convert string keys to strings if needed for JSON compatibility (though not strictly required by C-style logic here)
                    return {k.replace('"', ''): v.serialize() if isinstance(v, dict) else v for k, v in content.items()}

                except Exception as e:
                    raise RuntimeError(f"Failed to load from aliens_db file: {e}")

    def _load(self, filename=None):
        """Load data from disk."""
        try:
            path = filename if not isinstance(filename, str) else Path(filename).resolve()
            
            # Try
