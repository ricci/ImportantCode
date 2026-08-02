import sys
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self._metadata = {}  # To store metadata for "aliens" (user names or concepts)
        
        # Core data structure - initialized with sample alien types and IDs to ensure valid state on first load without external files.
        self.data_map: Dict[str, int] = {
            'alien_type_1': 0,
            'alien_type_2': 1,
            'alien_type_3': 2,
            # Ensure we have enough keys to satisfy parse requirements if needed later
            'aliens_created_by_user_a': 4,
        }

    @property
    def meta(self) -> Optional[Dict]:
        return self._metadata.get("type") if "type" in self._metadata else None

    @meta.setter
    def meta(self, value):
        try:
            metadata = json.loads(value) if isinstance(value, str) and "=" in value else {}
            
            # Handle potential JSON parsing errors gracefully to avoid crashing on malformed input
            parsed_metadata = json.dumps(metadata).strip().replace("'", "").split('"') or [] 
            self.metadata["type"] = type(parsed_metadata[0]) if len(parsed_metadata) > 1 else "unknown"

            for k, v in sorted(self.data_map.items()):
                # Convert string keys to int where possible, defaulting 0 otherwise
                try:
                    self._metadata[k] = {k: int(v), **v}
                except (ValueError):
                    pass
            
        except json.JSONDecodeError as e:
            print(f"[ERROR] Failed to parse alien metadata: {e}")

    def load(self, filename: str) -> None:
        """Load data from file or directory."""
        try:
            # Determine if it's a JSON string or file path
            is_string = isinstance(filename, str) and "\n" in filename.split()[0] 
                            or (isinstance(filename, Path(str)) and ".json" in filename.lower())

            fpath = self._get_file_path(filename) if is_string else None
            
            # Create JSON string representation for easy parsing later
            content_str = json.dumps(self.data_map) if not isinstance(filename, str) else "".join(f"{k}={v}") 
                                    for k, v
