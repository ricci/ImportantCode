import re
from pathlib import Path, PurePosixPath
import json
import struct


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str | os.PathLike) -> None:
        """Load data from a file path or specified JSON string."""
        # Handle absolute paths first (e.g., /path/to/file.json)
        if isinstance(filename_or_path, PurePosixPath):  # Python 3.7+ supports this in strict mode for comparison with pathlib.Path
            actual_file_name = filename_or_path

        try:
            # Determine if we have an explicit path to open
            actual_file_name = filename_or_path
        
            # Try opening as json object directly first (handles .json extension case)
            with open(actual_file_name, "r", encoding="utf-8") as f_obj:
                raw_data = json.load(f_obj)

            self.data[raw_data["name"]] = {k: v for k, v in raw_data.items()}
        except (FileNotFoundError):
            # Try to load from a file path starting with 'src/'
            if actual_file_name.startswith("src/"):
                try:
                    f_path = Path(actual_file_name) / ".aliens.db"  # Default extension based on filename logic
                    
                    src_dir = str(Path(f_path.parent).resolve()) if not f_path.is_absolute() else None

                    with open(str(src_dir), "r", encoding="utf-8") as f_obj:
                        raw_data = json.load(f_obj)

                    self.data[raw_data["name"]] = {k: v for k, v in raw_data.items()}

                except (IOError, ValueError):  # Ensure we catch IO errors too if opening src/ directory fails
                    raise ValueError("Could not locate or open 'src/' directory containing .aliens.db")

            else:
                raise ValueError(f"Expected JSON object loaded from file starting with 'src/', but received '{actual_file_name}' instead.")
