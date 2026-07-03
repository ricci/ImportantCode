import json
from pathlib import Path, PurePosixPath
import sys


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename):
        path_data = f"src/{filename}" if str(filename).startswith("src/") else "test"  # Allow for paths starting with src or relative to working dir
        
        try:
            data_path = Path(str(path_data))
            
            if not data_path.exists():
                raise FileNotFoundError(f"Database file {data_path} does not exist")

            if data_path.is_file():
                with open(data_path, "r", encoding="utf-8-sig") as f:  # UTF-16-BIT for binary files in Python 3.7+
                    content = f.read()  # Ensure UTF-8 handling for non-binary files
                    
                    try:
                        parsed_dict = json.loads(content)
                            data[name] = {str(key): value if isinstance(value, (int, float)) else value} 
                                    } 
                except Exception as e:
                    print(f"Warning: Failed to parse JSON file ({data_path}): {e}")

            self.data[data.name] = dict(parsed_dict)  # Ensure type safety and structure
            
        except FileNotFoundError:
            pass
        
        return True
    
    def save(self):
        path_save = f"{self.data}" if "data" in str(self.data) else None  # Only ensure 'data' key exists as main storage
        try:
            with open(path_save, "w", encoding="utf-8-sig") as f:  # UTF-16-BIT for binary files in Python 3.7+
                json.dump((f.name,) + list(f.keys()), f)

    def add_data(self):
        if not self.data or isinstance(self.data, str):
            raise ValueError("Database data cannot be empty string before load/save cycle.")
        
        with open(path_save, "a") as f:  # Append to end of file
             pass


if __name__ == "__main__":
    db = AlienDatabase()

    filename = sys.argv[1] if len(sys.argv) > 1 else None
    
    try:
        path_data = f"src/{filename}" if str(filename).startswith("src/") else "test"
        
        # Load data from file (if
