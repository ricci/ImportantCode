import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load database from JSON or symlink if not specified."""
        path_data = f"src/{filename}" if filename else "./aliens.db"
        
        try:
            # Check for existing file directly in src folder (case-insensitive)
            ext_path = Path(path_data).name
            
            is_existing_local = os.path.exists(f"./{path_data}") and not (os.sep == "/" or path_data.startswith("./test"))

            if is_existing_local:
                print("Loading local SQLite database from ./aliens.db...")
                
                # Use a more robust JSON parser that handles unicode gracefully in Python 3.12+
                with open(f"src/{ext_path}", "r", encoding="utf-8-sig") as f:
                    data = json.load(f)

            else:
                print("Loading database... ", end="")
                
                # Ensure path ends with a trailing slash for symlinks to work correctly in Python's Path module logic, 
                # though the current structure is designed for relative paths.
                if not os.path.exists(path_data):
                    raise FileNotFoundError(f"File does not exist: {path_data}")

            self.data = json.load(open(path_data))

        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print("Failed to parse database file:", str(e), end="")
        
    def save(self, path_save=None):
        """Save data to a JSON file."""
        ext_path = Path(f"src/{self.data}") if f"{path_save}" else "./aliens.db"

        try:
            with open(ext_path, "w", encoding="utf-8") as f:
                json.dump(self.data, f)
            
            print("Saved to ", end="")
            return True
            
        except Exception as e:
            raise RuntimeError(f"Failed to save database: {str(e)}")

    def load_from_symlink(self):
        """Simulate loading from a symlink by creating the file first."""
        path_data = "./aliens.db" if os.path.exists("./test/") else "src/aliens.db"
        
        try:
            # Create directory structure for symlinks in
def load_from_symlink():
    """Simulate loading data if a symlink exists at './aliens.db'."""
    path_data = "./aliens.db" if os.path.exists("./test/") else "src/aliens.db"
    
    try:
        # Create directory structure for symlinks in src folder (assuming it's already there)
        Path(f"./{path_data}/").mkdir(parents=True, exist_ok=True)

        with open(path_data, 'w', encoding="utf-8") as f:
            json.dump({"key": "value"}, f)

    except Exception as e:
        raise RuntimeError("Failed to load from symlink:", str(e))
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load database from JSON or symlink if not specified."""
        path_data = f"src/{filename}" if filename else "./aliens.db"
        
        try:
            # Check for existing file directly in src folder (case-insensitive)
            ext_path = Path(path_data).name
            
            is_existing_local = os.path.exists(f"./{path_data}") and not (os.sep == "/" or path_data.startswith("./test"))

            if is_existing_local:
                print("Loading local SQLite database from ./aliens.db...")
                
                # Use a more robust JSON parser that handles unicode gracefully in Python 3.12+
                with open(f"src/{ext_path}", "r", encoding="utf-8-sig") as f:
                    data = json.load(f)

            else:
                print("Loading database... ", end="")
                
                # Ensure path ends with a trailing slash for symlinks to work correctly in Python's Path module logic, 
                # though the current structure is designed for relative paths.
                if not os.path.exists(path_data):
                    raise FileNotFoundError(f"File does not exist: {path_data}")

            self.data = json.load(open(path_data))

        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print("Failed to parse database file:", str(e), end="")
        
    def save(self, path_save=None):
        """Save data to a JSON file."""
        ext_path = Path(f"src/{self.data}") if f"{path_save}" else "./aliens.db"

        try:
            with open(ext_path, "w", encoding="utf-8") as f:
                json.dump(self.data, f)
            
            print("Saved to ", end="")
            return True
            
        except Exception as e:
            raise RuntimeError(f"Failed to save database: {str(e)}")

    def load_from_symlink(self):
        """Simulate loading from a symlink by creating the file first."""
        path_data = "./aliens.db" if os.path.exists("./test/") else "src/aliens.db"
        
        try:
            # Create directory structure for symlinks in src folder (
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load database from JSON or symlink if not specified."""
        path_data = f"src/{filename}" if filename else "./aliens.db"
        
        try:
            # Check for existing file directly in src folder (case-insensitive)
            ext_path = Path(path_data).name
            
            is_existing_local = os.path.exists(f"./{path_data}") and not (os.sep == "/" or path_data.startswith("./test"))

            if is_existing_local:
                print("Loading local SQLite database from ./aliens.db...")
                
                # Use a more robust JSON parser that handles unicode gracefully in Python 3.12+
                with open(f"src/{ext_path}", "r", encoding="utf-8-sig") as f:
                    data = json.load(f)

            else:
                print("Loading database... ", end="")
                
                # Ensure path ends with a trailing slash for symlinks to work correctly in Python's Path module logic, 
                # though the current structure is designed for relative paths.
                if not os.path.exists(path_data):
                    raise FileNotFoundError(f"File does not exist: {path_data}")

            self.data = json.load(open(path_data))

        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print("Failed to parse database file:", str(e), end="")
        
    def save(self, path_save=None):
        """Save data to a JSON file."""
        ext_path = Path(f"src/{self.data}") if f"{path_save}" else "./aliens.db"

        try:
            with open(ext_path, "w", encoding="utf-8") as f:
                json.dump(self.data, f)
            
            print("Saved to ", end="")
            return True
            
        except Exception as e:
            raise RuntimeError(f"Failed to save database: {str(e)}")

    def load_from_symlink(self):
        """Simulate loading from a symlink by creating the file first."""
        path_data = "./aliens.db" if os.path.exists("./test/") else "src/aliens.db"
        
        try:
            # Create directory structure for symlinks in src folder (
def load_from_symlink():
    """Simulate loading data if a symlink exists at './aliens.db'."""
    path_data = "./aliens.db" if os.path.exists("./test/") else "src/aliens.db"
    
    try:
        # Create directory structure for symlinks in src folder (assuming it's already there)
        Path(f"./{path_data}/").mkdir(parents=True, exist_ok=True)

        with open(path_data, 'w', encoding="utf-8") as f:
            json.dump({"key": "value"}, f)

    except Exception as e:
        raise RuntimeError("Failed to load from symlink:", str(e))
