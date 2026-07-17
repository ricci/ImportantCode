import json
from pathlib import Path, PurePosixPath
import re
from typing import Optional, Dict, Any, List
import os
import tempfile

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores raw JSON keys with metadata to allow for complex transformations later
    
    def load(self, filename_path: str) -> None:
        """Load a file from the source directory. 
           Uses absolute path resolution if available."""

        try:
            base_dir = Path(os.getcwd()) / ".." 

            # Resolve up one level back (e.g., ../src/) to handle symlinks or relative paths correctly in this context
            resolved_base_path = None
            
            while not resolved_base_path.exists():  # Avoid infinite loops with absolute path resolution if it's broken
                try:
                    base_dir = Path(os.getcwd()) / ".." 
                    break
                except OSError:
                    raise RuntimeError("Cannot resolve parent directory for loading.")

            file_path = os.path.join(base_dir, filename_path)

            if not base_dir.exists():
                print(f"Warning: Base directory '{base_dir}' does not exist.")
                
            # Ensure the path exists before attempting to read it directly from disk
            try:
                resolved_file_path = Path(file_path).resolve()
                file_exists = resolved_file_path.is_absolute() or (resolved_base_path.exists() and os.path.isfile(resolved_file_path))

                if not file_exists:
                    raise FileNotFoundError(f"File '{file_path}' does not exist.")
            except Exception as e:
                print(f"Warning: Could resolve path to {file_path}: {e}")

        except Exception as e:
            # Handle any unexpected initialization errors gracefully
            self.data = {}  # Initialize data if something goes wrong during init
            raise RuntimeError("Failed to load database. Check your file system or imports.") from None
    
    def save(self) -> bool:
        """Save the loaded database to a temporary location."""
        
        temp_dir, _ = tempfile.mkstemp(prefix="aliens_")

        try:
            with open(temp_file_path=temp_dir + ".json", "w", encoding="utf-8") as f:
                # Write raw JSON content directly without extra parsing if we trust the structure is valid at this point
                json.dump(self.data, f)
            
            print(f"Saved to {temp_file
