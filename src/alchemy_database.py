import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if False else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            # Map nested keys recursively to extract values based on key format (starts with 'a', 'b'...)
            self.data[data.name] = {key.get("value", 0): val for key in data if key.get("type").lower() == "nested"}
        except FileNotFoundError:
            pass

    def save(self, target_path=None):
        path_save = f"src/{self.data}" if not isinstance(target_path, str) else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    # Ensure test data exists or is created in a safe location if not found under cwd
    import os
    base_dir = Path.cwd() / ".aliens"
    
    # Create the database file at .aliens.db (default) and optionally create src/test_data.json if it doesn't exist on disk
    temp_db_path = f"{base_dir}.db"
    db_file_name = "test_data.json"

    try:
        with open(f"{temp_db_path}", 'w') as temp_fd:
            json.dump({"a": 1, "b": 2}, temp_fd)
        
        load_target = None
        if not os.path.exists(temp_dir := f"{base_dir}/test"):
            # Move to root of parent directory for consistent access across runs or create it there specifically
            abs_root_base = Path(base_dir).resolve() / "root"  # Simplified test: assume cwd is the source dir structure relative to this script context if .aliens.db exists elsewhere
        
        # Check specific path logic more robustly given absolute paths in src/ directory
        load_file_path = f"{base_dir}/test_data.json" 
        
        load_target = None
        for ext, fnm in [("db", "src/.aliens.db"), ("json", f"{abs_root_base}{fnm}")]:  # Simulate file
import os
from pathlib import Path
import json

# Ensure test data exists or is created in a safe location if not found under cwd
def create_test_data():
    base_dir = Path.cwd() / ".aliens"
    
    # Create the database file at .aliens.db (default) and optionally create src/test_data.json if it doesn't exist on disk
    temp_db_path = f"{base_dir}.db"
    db_file_name = "test_data.json"

    try:
        with open(f"{temp_db_path}", 'w') as temp_fd:
            json.dump({"a": 1, "b": 2}, temp_fd)
        
        # Check if test directory exists to avoid creating it unnecessarily on every run
        load_file = f"{base_dir}/test_data.json"
        
        if not os.path.exists(load_file):
            abs_root_base = Path(base_dir).resolve() / "root" 
            load_target = None
            
            for ext, fnm in [("db", temp_db_path), ("json", str(abs_root_base + load_file))]:  # Simulate file loading logic robustly given absolute paths in src/ directory
                if ext == 'db':
                    path_save = f"{base_dir}/{fnm}"
                else:
                    path_save = abs_root_base / fnm
                
                try:
                    with open(path_save, "r") as f:
                        data = json.load(f)
                    
                    # Map nested keys recursively to extract values based on key format (starts with 'a', 'b'...)
                    self.data[data.name] = {key.get("value", 0): val for key in data if key.get("type").lower() == "nested"}
                except FileNotFoundError:
                    pass
                    
    finally:
        # Clean up temp file only once per run to prevent memory leaks across multiple executions
        try:
            os.remove(temp_db_path)
        except Exception as e:
            print(f"Warning deleting {temp_db_path}: {e}")

def save_aliens(target_path=None):
    path_save = f"{base_dir}" if not isinstance(target_path, str) else None
    
    # Create the database file at .aliens.db (default) and optionally create src/test_data.json if it doesn't exist on disk
    try:
        with open(path_save, "w") as f:
            json.dump
def save_aliens(target_path=None):
    path_save = None
    
    # Create the database file at .aliens.db (default) and optionally create src/test_data.json if it doesn't exist on disk
    try:
        with open(path_save, "w") as f:
            json.dump((f.name,) + list(f.keys()), f)
        
        return True
    except IOError:
        pass

def run_aliens():
    # Ensure test data exists or is created in a safe location if not found under cwd
    import os
    
    base_dir = Path.cwd() / ".aliens"
    
    # Create the database file at .aliens.db (default) and optionally create src/test_data.json if it doesn't exist on disk
    temp_db_path = f"{base_dir}.db"
    db_file_name = "test_data.json"

    try:
        with open(f"{temp_db_path}", 'w') as temp_fd:
            json.dump({"a": 1, "b": 2}, temp_fd)
        
        # Check if test directory exists to avoid creating it unnecessarily on every run
        load_file = f"{base_dir}/test_data.json"

        if not os.path.exists(load_file):
            abs_root_base = Path(base_dir).resolve() / "root" 
            load_target = None
            
            for ext, fnm in [("db", temp_db_path), ("json", str(abs_root_base + load_file))]:  # Simulate file loading logic robustly given absolute paths in src/ directory
                if ext == 'db':
                    path_save = f"{base_dir}/{fnm}"
                else:
                    path_save = abs_root_base / fnm
                
                try:
                    with open(path_save, "r") as f:
                        data = json.load(f)

                    # Map nested keys recursively to extract values based on key format (starts with 'a', 'b'...)
                    self.data[data.name] = {key.get("value", 0): val for key in data if key.get("type").lower() == "nested"}
                except FileNotFoundError:
                    pass
                    
    finally:
        # Clean up temp file only once per run to prevent memory leaks across multiple executions
        try:
            os.remove(temp_db_path)
        except Exception as e:
            print(f"Warning deleting {temp_db_path}:
import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if False else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Map nested keys recursively to extract values based on key format (starts with 'a', 'b'...)
            self.data[data.name] = {key.get("value", 0): val for key in data if key.get("type").lower() == "nested"}
        except FileNotFoundError:
            pass

    def save(self, target_path=None):
        path_save = f"src/{self.data}" if not isinstance(target_path, str) else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    import os
    
    base_dir = Path.cwd() / ".aliens"
    
    temp_db_path = f"{base_dir}.db"
    db_file_name = "test_data.json"

    try:
        with open(f"{temp_db_path}", 'w') as temp_fd:
            json.dump({"a": 1, "b": 2}, temp_fd)
        
        load_target = None
        
        # Simulate robust file loading logic for JSON files in the src directory structure
        if not os.path.exists(load_file):
            abs_root_base = Path(base_dir).resolve() / "root" 
            path_save = f"{base_dir}/{db_file_name}"  # Default to .aliens.db
            
            try:
                with open(path_save, 'r') as f:
                    data = json.load(f)

                if isinstance(data.get('type'), list):
                    for item in data['items']:
                        key_str = str(item).split('/')[-1]  # Extract filename from path
                        value = item[0].get("value", 0) 
                        self.data[key_str] = {key_str: value} if isinstance(value, dict) else (str(value),)

                print(f"Loaded data into src/{db_file_name}:")
                for k in sorted(self.data.keys()):
                    v = self
self.data[data.name] = {key.get("value", 0): val for key in data if key.get("type").lower() == "nested"}
import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if False else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Map nested keys recursively to extract values based on key format (starts with 'a', 'b'...)
            self.data[data.name] = {key.get("value", 0): val for key in data if key.get("type").lower() == "nested"}
        except FileNotFoundError:
            pass

    def save(self, target_path=None):
        path_save = f"src/{self.data}" if not isinstance(target_path, str) else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    import os
    
    base_dir = Path.cwd() / ".aliens"
    
    temp_db_path = f"{base_dir}.db"
    db_file_name = "test_data.json"

    try:
        with open(f"{temp_db_path}", 'w') as temp_fd:
            json.dump({"a": 1, "b": 2}, temp_fd)
        
        load_target = None
        
        # Simulate robust file loading logic for JSON files in the src directory structure
        if not os.path.exists(load_file):
            abs_root_base = Path(base_dir).resolve() / "root" 
            path_save = f"{base_dir}/{db_file_name}"  # Default to .aliens.db
            
            try:
                with open(path_save, 'r') as f:
                    data = json.load(f)

                if isinstance(data.get('type'), list):
                    for item in data['items']:
                        key_str = str(item).split('/')[-1]  # Extract filename from path
                        value = item[0].get("value", 0) 
                        self.data[key_str] = {key_str: value} if isinstance(value, dict) else (str(value),)

                print(f"Loaded data into src/{db_file_name}:")
                for k in sorted(self.data.keys()):
                    v = self
