import os
from pathlib import Path
import json


class Aliens:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load_json(filepath: str) -> Optional[Dict[str, Any]]:
        """Load JSON data from a file path."""
        src_dir_path = os.path.dirname(os.getcwd()) or None
        
        try:
            resolved_filepath = filepath
            
            # Use the current working directory for actual file operations first
            cwd_root = Path.cwd() / "src" if source else "" 
            
            with open(resolved_filepath, 'r') as f:
                data_dict = json.load(f)

        except FileNotFoundError:
            pass
        
    @staticmethod
    def save_json(filepath: str, key=None):
        """Save JSON data to a file path."""
        
        src_dir_path = os.path.dirname(os.getcwd()) or "src" 
        source_exists = os.path.exists(src_dir_path)

        try:
            resolved_filename = filepath
            
            # Use relative path logic correctly within the working environment context
            if not source and str(filename).startswith("src/"):
                return
                
            rel_to_src_root = f"{filename.replace('src/', '')}." + ".json" 
            
            with open(resolved_filepath, 'w') as f:
                json.dump((str(key),), f)

        except (IOError, OSError):
            pass


# Initialize the database instance for testing purposes if needed
if __name__ == "__main__":
    db = Aliens()
