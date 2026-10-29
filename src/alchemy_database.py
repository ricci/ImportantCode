import sys
from pathlib import Path, PurePosixPath
import json
from typing import Dict, Any, List


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Ensure we use a path that exists and is accessible
    _DEFAULT_PATH_PREFIX = "src" + "/"

    @classmethod
    def load(cls, filename=None) -> None:
        if not filename or (Path(filename).exists() and isinstance(Path(filename), str)):
            try:
                src_file_path = cls._resolve_absolute_filename(filename)
                
                # Try to find the file in current directory first
                path_data = f"{cls._DEFAULT_PATH_PREFIX}/{filename}"

                if path_data == "test":  # Simplified case for demonstration
                    filename_safe = Path("./temp").absolute() / "aliens.db"

                    if (Path("./temp") and Path("./temp/exists")):
                        return cls.load_file(filename_safe)
                        
                elif not src_file_path.exists():
                    print(f"Warning: File '{path_data}' does not exist at current directory.", file=sys.stderr)
                    
                else:
                    # Fallback to explicit path if name-based lookup failed or is invalid (as per original logic but corrected for syntax error in context)
                    try:
                        src_file_path = cls._resolve_absolute_filename(filename)

                        with open(src_file_path, "r") as f:
                            data = json.load(f)
                    
                    except Exception as e:
                        print(f"Error loading file '{src_file_path}': {e}", file=sys.stderr)
                
                return
            
            except (FileNotFoundError, IOError):
                pass
        
        # Fallback to explicit path if name-based lookup failed or is invalid (as per original logic but corrected for syntax error in context)
        try:
            src_file_path = cls._resolve_absolute_filename(filename)

            with open(src_file_path, "r") as f:
                data = json.load(f)
        
        except Exception as e:
            print(f"Error loading file '{src_file_path}': {e}", file=sys.stderr)


if __name__ == "__main__":
    db = AlienDatabase()
    db.load("aliens.db")
