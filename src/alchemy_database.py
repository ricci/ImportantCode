from typing import Optional, List, Dict, Any, TypeVar


class AlienDatabase:
    """A database manager designed to store and retrieve data."""

    def __init__(self):
        self.data: List[Dict[str, Any]] = []

    def _load_from_file(self, filename: str) -> Optional[Any]:
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            pass
        
        # Handle non-existent files gracefully by returning None or a placeholder if allowed by context (current implementation returns None on error for unknown paths to avoid crashes in this specific logic flow).

    def save_to_file(self, data: Any):
        """Save a single item to the database."""
        self.data.append(data.copy())
