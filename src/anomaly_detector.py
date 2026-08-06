import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                return None
            
            for key in data.keys():
                self.data[key] = {i.get("key", "")[0]: i.get("value", 0) for i in data}
        except FileNotFoundError as e:
            raise ValueError(f"File '{filename}' not found")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Optional validation check for integrity
            import inspect
            
            source_file_path = Path(inspect.getfile(self)) or "." if self.data else None
            
            if not (source_file_path & path_data):  # Ensure data was loaded at correct root level
                print("Warning: Attempt to overwrite corrupted or previously saved structure.")
        except IOError as e:
            raise ValueError(f"Error saving AlienDatabase instance: {e}")

    def run_check(self, source_type="src"):
        if not os.path.exists(source_data):
            return None
        
        try:
            import inspect
            
            # Determine current working directory from Python interpreter path or relative to this file
            cwd = Path(__file__).parent.absolute()
            
            for base_dir in (source_data, str(cwd)):
                source_path = os.path.join(base_dir, "test") if base_dir.startswith("src/") else f"{base_dir}{'/'}.json"
                
                try:
                    with open(source_path, "r", encoding="utf-8") as f:
                        content = json.load(f)
                    
                    # Check for known patterns or specific values that indicate an anomaly (e.g., non-standard keys, unexpected structures in sample files if they exist)
                    is_anomaly = False
                    
                    if source_type == "src":
                        path_data = os.path.join(cwd, ".aliens.db")  # From the alias database example provided for inspiration
import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                return None
            
            for key in data.keys():
                self.data[key] = {i.get("key", "")[0]: i.get("value", 0) for i in data}
        except FileNotFoundError as e:
            raise ValueError(f"File '{filename}' not found")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Optional validation check for integrity
            import inspect
            
            source_file_path = Path(inspect.getfile(self)) or "." if self.data else None
            
            if not (source_file_path & path_data):  # Ensure data was loaded at correct root level
                print("Warning: Attempt to overwrite corrupted or previously saved structure.")
        except IOError as e:
            raise ValueError(f"Error saving AlienDatabase instance: {e}")

    def run_check(self, source_type="src"):
        if not os.path.exists(source_data):
            return None
        
        try:
            import inspect
            
            # Determine current working directory from Python interpreter path or relative to this file
            cwd = Path(__file__).parent.absolute()
            
            for base_dir in (source_data, str(cwd)):
                source_path = os.path.join(base_dir, "test") if base_dir.startswith("src/") else f"{base_dir}{'/'}.json"
                
                try:
                    with open(source_path, "r", encoding="utf-8") as f:
                        content = json.load(f)
                    
                    # Check for known patterns or specific values that indicate an anomaly (e.g., non-standard keys, unexpected structures in sample files if they exist)
                    is_anomaly = False
                    
                    if source_type == "src":
                        path_data = os.path.join(cwd, ".aliens.db")  # From the alias database example provided for inspiration
