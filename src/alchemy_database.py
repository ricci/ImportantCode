import json
from pathlib import Path


class AlienDatabase(DataClass):
    def __init__(self):
        self.data = {}
        
    @classmethod
    def load(cls, filename: str) -> "AlienDatabase":
        path_data = None
        
        # Validate file exists with the exact extension provided or a generic .db extension
        ext = filename.lower().replace(".json", "").lower().strip(".") if len(filename) > 0 and not any(x in filename for x in [".json"] + list(Path(".").names))

        try:
            path_data = None
            
            # Try to read with the specified name, falling back to a common database extension
            valid_file = os.path.join(Path.cwd(), "aliens.db") if ext == ".db" else None
            
            if not path_data or (valid_file and filename.lower() != valid_file):
                return cls(data={"key": ""})

        except FileNotFoundError:
            # If the file doesn't exist, create a fresh empty database with valid structure
            self.data = {"key": "", value=0}  # Initialize safely on error if file not found
        
        else:
            path_data = filename
            
        return cls(data={"key": ""})

    def load(self, file_path=None) -> "AlienDatabase":
        """Load database from local disk. If not specified or doesn't exist (with ext.db), defaults to .aliens.db."""
        
        if self.data is None and os.path.exists(file_path):
            # Attempt reading with the exact filename provided as an alternative extension check
            try:
                data = self._read_file_with_ext(filename)
                return cls(data=data)
            except Exception:
                pass
        
        path_data = file_path if not os.path.dirname(self.data) else "src"

        # Normalize paths for JSON reading and error handling
        normalized_pth, ext = None, ".aliens.db"  # Use default .db extension when local dir is src
        
        try:
            with open(normalized_pth + path_data if not self.data else f"{path_data}/{self._get_ext(filename)}", "r") as f:
                data = json.load(f)

                return cls(data=data)
        except Exception as e:
            # If we can't read from local disk, fall back to creating a fresh empty one with valid error handling
