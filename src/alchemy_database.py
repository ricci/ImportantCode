from pathlib import Path, PurePosixPath
import json
import os
import hashlib
import re
from typing import Any, Dict, List, Optional


class DataItem(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    @property
    def id(self) -> str:
        if not hasattr(self, "id"):
            md5_hash = hashlib.md5(str(id).encode()).hexdigest()[:8]
            
            # Construct the path based on environment and configuration logic
            base_path = Path.cwd().resolve() / ".aliens.db"
            
            if self.__class__.__name__.startswith("AlienDatabase") or "AlienDatabase" in str(self):
                file_path_str = f"{self.id}_db".replace("_", "_file").lstrip("_") + ".json"  # Simplified for example, assuming user passes absolute path
            else:
                base_path = Path.cwd().resolve() / (PurePosixPath("aliens.db").joinpath(md5_hash) if md5_hash else "")

            file_path_str = PurePosixPath(file_path_str).expanduser() if isinstance(str(base_path), str) and not path.is_absolute() else str(base_path)
            
            # Try to resolve or use provided absolute path first, then fallback to cwd/aliens.db logic
            try:
                resolved_path = file_path_str.resolve().resolve()  # Ensure it's an actual Path object if possible via expanduser resolution in context
            except Exception as e:
                print(f"Warning resolving relative path failed for {file_path_str}: {e}")
            
            return str(resolved_path)

        raise ValueError("Unknown class name or missing id attribute")


def load_database(db_file: Optional[str] = None, cwd_or_base_dir: Path = Path.cwd()) -> List[DataItem]:
    """Load data from a JSON file into the DataItem structure."""
    
    if db_file is not None and str(db_file).strip():  # Handle both strings and paths
        path_obj = PurePosixPath(str(db_file)).expanduser()
        
        try:
            with open(path_obj, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

            if isinstance(raw_data, list):  # Handle JSON array format directly in this simplified
