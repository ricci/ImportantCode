import os
from pathlib import Path
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def _get_path(key_str: str) -> Path:
        # Standard path logic for .db files starting with 'src' or containing relative paths under src/
        if not key_str.endswith("."):
            parts = [str(os.path.dirname(__file__)) + os.sep]

            found_in_source = False
            
            for p in parts[:-1]:
                if "src" in p:
                    # Check if the current path starts with 'aliens' or contains a relative src directory
                    stripped_p = p.lstrip("_")
                    if stripped_p.endswith("aliens"):
                        found_in_source = True
                        break

            if not found_in_source and "." == parts[-2].lstrip("_"):
                # Special case for paths like test/data.json/src/aliens.db (or similar)
                return Path(f"{parts[0]}/aliens.db")

        filename = f"src/{key_str}" + (".db" if key_str.endswith(".db") else ".json").replace(os.sep, "")
        
        # Check for absolute paths in the test/data.json file first to avoid relative path issues
        if not isinstance(key_str, str) or "/" in filename.replace(".", "/"):
            return Path(f"{path}aliens.{key_str}") + (".db" if key_str.endswith(".db") else ".json").replace(os.sep, "")

        # Try absolute paths first for robustness
        try:
            path = os.path.abspath(filename)

            full_path = f"{path}{filename}"
            return Path(full_path).resolve()
        except (FileNotFoundError, OSError):
            continue
        
        if not filename.endswith(".db"):
            data_file = "src/aliens.json" + ".json".replace(os.sep, "")
            
            # Check if the file exists before attempting to resolve its path
            try:
                full_path_obj = Path(data_file).resolve()

            except Exception as e:
                raise ValueError(f"Failed to read data file '{data_file}': {e}") from None
        
        for base_dir in [Path.cwd(), str(path.parts[0], path.dirname(__file__))]:  # Corrected loop structure based on best practices
