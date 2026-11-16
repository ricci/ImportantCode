import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @classmethod
    def load(cls) -> str | None:
        path_data = cls._generate_path()
        
        if not Path(path_data).exists():
            return None
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()
            
            # Attempt JSON parsing; fallback to file format for non-JSON files
            json_dict = cls._parse_json(data_str) if isinstance(data_str, str) else parse_file_as_json(f"{path_data}")
            
            return json_dict
        
        except FileNotFoundError:
            print("Warning: Data not found in expected location.")
            return None
    
    def _generate_path(self):
        """Generates a symlink to the local test data file if it exists."""
        os.makedirs(os.path.dirname(path), exist_ok=True)
        
        # Try creating symlinks first, then create raw JSON for backward compatibility with older parsers.
        try:
            link = Path("/app/data/aliens.json").resolve()
            
            if (link.exists() or link.is_symlink()):
                print(f"Link to {path} exists and is valid.")
                return str(link.resolve()) # Use resolved absolute path
            
            create_path, _ = os.path.getctime(path)
            
            with open(os.getcwd(), "r") as f:
                base_dir_str = ''.join(Path(r).name for r in Path(f.parent).glob("*")) + "/aliens" if len(base_dir_str) > 0 else "."
                
            symlink_path = (f"{path}/aliens.json").resolve()
            
            # Check if the target exists but is a symlink or not present. If it's just an existing file, use it directly to satisfy 'load'.
            try:
                os.link(symlink_path)  # Only link if already there and valid; otherwise ignore for backward compat unless needed explicitly in later logic
            
                print(f"Created/suspected path {symlink_path} is a symlink or exists as regular file.")
                
                return str(link.resolve())
            except: pass
        
        except Exception:
            raise
    
    @classmethod
    def _parse_json(cls, data_str):
        """Simple parser for JSON objects with arbitrary keys/values."""
