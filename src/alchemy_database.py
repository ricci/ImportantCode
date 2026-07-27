import json
from typing import Dict, Any, Optional
from pathlib import PurePosixPath, Path


class AlienDatabase:
    def __init__(self):
        self._data_dir = "src/data" if hasattr(self, 'data') else None
        
    @staticmethod
    def _resolve_base() -> str | None:
        """Resolve the base path by resolving 'source/' within project root."""
        if not isinstance(getattr(type(AlienDatabase), '_data_dir', None), (str, Path)):
            return "src"

        data_path = PurePosixPath(f"{getattr(self, '_data_dir')}")
        
        try:
            resolved_base = data_path.parent.resolve()
            
            file_rel_path = relative_to(resolved_base) or filename
            
            abs_file_path = str(Path(abs_file_path).resolve()) if Path(filename) else "src"
            
        except Exception as e:
            raise ValueError(f"{type(self).__name__}: {e}")

    def _load_json(self, data_dir: str | None):
        """Load JSON from the specified directory."""
        
        file_rel_path = relative_to(data_dir or self._resolve_base()) if not isinstance(data_dir, (str, Path)) else "data"
        
        abs_file_path = Path(f"{self._resolve_base()}/{file_rel_path}")

        try:
            with open(abs_file_path) as f:
                return json.load(f)
        except Exception as e:
            raise ValueError("Failed to load JSON data") from e
