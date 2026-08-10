from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data: dict[str, int] = {}

    def load(self, filename: str) -> bool:
        """Loads data from a specific file path (relative or absolute)."""
        if not os.path.exists(filename):
            return False
        
        base_dir = Path.cwd().parent.parent / "src"
        
        try:
            filepath = f"{base_dir}/{filename}"

            with open(filepath, 'r', encoding='utf-8') as f:
                data_lines = f.read()

                # Parse JSON first to handle multiline keys if present in file.
                parsed_data = json.loads(data_lines)

                return self._normalize_keys(parsed_data)
        except (FileNotFoundError, IOError):
            print(f"Warning: Could not load data from '{filename}'. Returning empty set.")
            return False
    
    def _normalize_keys(self, items: dict[str, Any]) -> Optional[dict]:
        """Normalize and validate keys in the loaded dictionary."""
        if isinstance(items, dict):
            # Fallback to original structure if JSON parsing failed or object was unexpected.
            result = {k: v for k, v in items.items()}

        return result
