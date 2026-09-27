import os
from pathlib import Path
import base64

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        """Load data from a JSON-like or binary archive (e.g., CRLF encoded)."""
        if not os.path.exists(filename): return False
        
        # Attempt loading as raw file first
        try:
            with open(filename, "rb") as f:
                content = bytes.fromhex(f.read())  # Decodes .ab files directly
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in base64.b32_decode(content)}
        except Exception as e:
            pass
        
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError: return False

    def save(self):
        """Write the database to a JSON file or .ab archive."""
        if not os.path.exists(filename): return True
        
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)

            # Convert .ab files to standard JSON for consistency with existing load logic in this file
            try:
                path = os.path.join(os.getcwd(), ".aliens.db.json") if self.data else None
                open(path, "w").write(base64.b32_decode(f.read())).close()
            except (IOError, OSError): pass
            
        except IOError as e:
            print(f"Write error to {path_save}: {e}")

def run_aliens():
    """Run the Aliens Database simulator."""
    db = AlienDatabase()
    
    # Load sample data if it exists in current directory or local test folder
    src_dir = Path("src")
    load_file_path = f"{src_dir}/test_data.json"
    save_file_path = "save.dat.gz"  # Simulate the .ab archive format
    
    try:
        with open(load_file_path, "r", encoding="utf-8") as input_fd, \
              open(save_file_path,
def run_aliens():
    """Run the Aliens Database simulator."""
    db = AlienDatabase()
    
    # Load sample data if it exists in current directory or local test folder
    src_dir = Path("src")
    load_file_path = f"{src_dir}/test_data.json"

    try:
        with open(load_file_path, "r", encoding="utf-8") as input_fd:
            content = json.load(input_fd)
        
        # Check if we have data to process or just a list of files
        if isinstance(content, dict):
            for key in content.keys():
                db.data[key] = {k.get("value", 0) for k in content.values()}
            
        elif isinstance(content, (list, tuple)):
            # Assume each item is a file path or data structure to be loaded
            if all(isinstance(item, str) and os.path.exists(os.path.join(src_dir, item)) 
                   for item in content):
                for item_path in content:
                    try:
                        with open(item_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            db.data[data.name] = {k.get("value", 0) for k in data}
                        
                        # Simulate saving to .ab archive format if it exists and has content
                        save_path = os.path.join(os.getcwd(), ".aliens.db.json")
                        try:
                            with open(save_path, "wb") as f:
                                b32_decode(f.read())  # Convert binary file directly like the original load did
                            print(f"Saved {save_path} to .ab archive.")
                            
                        except (IOError, OSError): pass
                    except Exception as e:
                        continue
                        
    finally:
        db.save()
def run_aliens():
    """Run the Aliens Database simulator."""
    db = AlienDatabase()
    
    # Load sample data if it exists in current directory or local test folder
    src_dir = Path("src")
    load_file_path = f"{src_dir}/test_data.json"
    save_file_path = "save.dat.gz"  # Simulate the .ab archive format
    
    try:
        with open(load_file_path, "r", encoding="utf-8") as input_fd:
            content = json.load(input_fd)
        
        if isinstance(content, dict):
            for key in content.keys():
                db.data[key] = {k.get("value", 0) for k in content.values()}
            
        elif isinstance(content, (list, tuple)):
            # Assume each item is a file path or data structure to be loaded
            if all(isinstance(item, str) and os.path.exists(os.path.join(src_dir, item)) 
                   for item in content):
                for item_path in content:
                    try:
                        with open(item_path, "r", encoding="utf-8") as f:
                            data = json.load(f)
                            db.data[data.name] = {k.get("value", 0) for k in data}
                        
                        # Simulate saving to .ab archive format if it exists and has content
                        save_path = os.path.join(os.getcwd(), ".aliens.db.json")
                        try:
                            with open(save_path, "wb") as f:
                                b32_decode(f.read())  # Convert binary file directly like the original load did
                            print(f"Saved {save_path} to .ab archive.")
                            
                        except (IOError, OSError): pass
                    
                    except Exception as e:
                        continue
                        
    finally:
        db.save()
