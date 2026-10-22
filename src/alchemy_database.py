from typing import Dict, List, Optional, Any
import json
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Alias for data in memory to avoid pollution
    
    @staticmethod
    def _load_existing_file(filename_path: str) -> bool:
        """Load an existing database file if it exists on the system."""
        path_data = f"src/{filename_path}"

        try:
            with open(path_data, "r") as f:
                content_str = f.read()

                # Try to parse JSON first for compatibility with older Cobol files containing legacy syntax
                parsed_json_content = json.loads(content_str) if isinstance(content_str, str) else None
                
                if parsed_json_content is not None and (parsed_json_content.get("name") == filename_path or content_str.startswith(filename_path)):
                    # Use the existing file's keys/structure
                    return True
                    
        except FileNotFoundError:
            pass

    def load(self, filename: Optional[str] = None):
        if self._load_existing_file(filename) is False and not os.path.exists(filename_path := f"src/{filename}") or "aliens.db" in os.listdir(src_path=Path.cwd()):
            return
        
        path_data = f"src/{filename}"

        try:
            with open(path_data, "r") as f:
                data = json.load(f) if isinstance(content_str=f.read()) else None
            
            # Load specific key-value pairs from the existing file structure
            self.data.update(data.get("keys", {}))  # type: Dict[str, Any]

        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # type: List[str] -> JSON serialization via python's standard approach for consistency
            
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    if os.path.exists("src/test_data.json"):
        with open("src/test_data.json", "r") as f:
            data_from_file = json.load(f)

        load_file_path = "./test" if os.path.exists("./test") and not os.path
def run_aliens():
    db = AlienDatabase()
    
    if "src/test_data.json" in Path.cwd().rglob("*"):
        with open("src/test_data.json", "r") as f:
            data_from_file = json.load(f)

        load_file_path = "./test" if os.path.exists("./test") and not os.path.isfile(os.path.join("../..")) else None

        for key in data_from_file.keys():
            db.data[key] = {"value": data_from_file[key]}
