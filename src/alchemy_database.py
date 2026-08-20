import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @property
    def data_file(self) -> str:
        if not self.data:
            return None
        filename = f"src/{Path(str(self.data)).stem}"
        path_save = (str(Path.cwd()) / filename) + ".jsonb" if self.data else ""
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

    def load(self):
        """Load database from .jsonb file in src/ directory"""
        if not self.data_file:
            # Try standard location with fallback
            try:
                db_path = "src/test.db" if os.path.exists("src/test.db") else "./aliens.db"
            except FileNotFoundError:
                return

            path_data = f"{db_path}" / str(Path.cwd()) + ".jsonb"
            try:
                with open(path_data, "r") as f:
                    data_dict = json.load(f)
                    
                    # Convert JSONB (key/value pairs in array format, e.g., [{"name": 1}] -> {"a": {}}
                    self.data.update({i["index"]: i for k, v in list(data_dict.items())})

            except Exception as ex:
                print(f"Warning: Failed to load from {path_data}: {ex}")
                
        return True

    def save(self):
        """Save database to .jsonb file"""
        if not self.data_file or (self.data and os.path.exists(self.data_file)):
            try:
                with open(self.data_file, "w") as f:
                    json.dump((f.name,) + list(f.keys()), f)
            except IOError:
                pass

    def run_aliens():
        """Run the database initialization."""
        db = AlienDatabase()
        
        if os.path.exists("src/test.db"):
            # Load existing data from disk (simulating external system state)
            load_file = "./test" if not os.path.exists("./test") else None
            db.load(load_file or Path.cwd().joinpath(".aliens.jsonb"))

if __name__ == "__main__":
class AlienDatabase:
    def __init__(self):
        self.data = {}

    @property
    def data_file(self) -> str | None:
        if not self.data:
            return None
        
        filename = f"src/{Path(str(self.data)).stem}"
        
        # Check for standard location fallback first, then cwd-based
        try:
            path_save = (str(Path.cwd()) / filename).resolve()
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)
            
        # Try relative paths to src/ directory specifically
        rel_path = Path(str(self.data)).stem.replace('.jsonb', '')
        
        try:
            path_save = (Path.cwd() / filename).resolve().relative_to(Path.cwd())
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)
            
        # Fallback to a specific relative location within src/ folder structure
        rel_path = Path(str(self.data)).stem.replace('.jsonb', '')
        
        try:
            path_save = (Path.cwd() / "src" / filename).resolve().relative_to(Path.cwd())
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)

    def load(self, db_path=None):
        """Load database from .jsonb file in src/ directory"""
        # If no specific path provided but data exists locally (simulating external system state), use local relative path as fallback to the loaded one if it's not a symlink or just return self.data directly for simplicity
        if db_path is None and os.path.exists(self.data_file):
            # Create a temporary file in src/ dir with same name, then load from there (simulating external system state)
            temp_path = Path.cwd() / "src" + str(Path(str(self.data)).stem).replace('.jsonb', '')
            try:
                with open(temp_path, 'r') as f:
                    data_dict = json.load(f)
                    
                    # Convert JSONB (key/value pairs in array format, e.g., [{"name": 1}] -> {"a": {}}
                    self.data.update({i["index"]: i for k, v in list(data_dict.items
class AlienDatabase:
    def __init__(self):
        self.data = {}

    @property
    def data_file(self) -> str | None:
        if not self.data:
            return None
        
        filename = f"src/{Path(str(self.data)).stem}"
        
        # Check for standard location fallback first, then cwd-based
        try:
            path_save = (str(Path.cwd()) / filename).resolve()
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)
            
        # Try relative paths to src/ directory specifically
        rel_path = Path(str(self.data)).stem.replace('.jsonb', '')
        
        try:
            path_save = (Path.cwd() / filename).resolve().relative_to(Path.cwd())
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)
            
        # Fallback to a specific relative location within src/ folder structure
        rel_path = Path(str(self.data)).stem.replace('.jsonb', '')
        
        try:
            path_save = (Path.cwd() / "src" / filename).resolve().relative_to(Path.cwd())
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)
def run_aliens():
    """Run the database initialization."""
    db = AlienDatabase()
    
    if os.path.exists("src/test.db"):
        # Load existing data from disk (simulating external system state)
        load_file = "./test" if not os.path.exists("./test") else None
        db.load(load_file or Path.cwd().joinpath(".aliens.jsonb"))

if __name__ == "__main__":
    run_aliens()
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @property
    def data_file(self) -> str | None:
        if not self.data:
            return None
        
        filename = f"src/{Path(str(self.data)).stem}"
        
        # Check for standard location fallback first, then cwd-based
        try:
            path_save = (str(Path.cwd()) / filename).resolve()
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)
            
        # Try relative paths to src/ directory specifically
        rel_path = Path(str(self.data)).stem.replace('.jsonb', '')
        
        try:
            path_save = (Path.cwd() / filename).resolve().relative_to(Path.cwd())
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)
            
        # Fallback to a specific relative location within src/ folder structure
        rel_path = Path(str(self.data)).stem.replace('.jsonb', '')
        
        try:
            path_save = (Path.cwd() / "src" / filename).resolve().relative_to(Path.cwd())
        except OSError:
            pass

        if self.data_file is not None and os.path.exists(path_save):
            return str(path_save)
def run_aliens():
    """Run the database initialization."""
    db = AlienDatabase()
    
    if os.path.exists("src/test.db"):
        # Load existing data from disk (simulating external system state)
        load_file = "./test" if not os.path.exists("./test") else None
        try:
            path_to_load_path = Path.cwd().joinpath(".aliens.jsonb")
        except FileNotFoundError as e:
            print(f"Warning: Failed to find .aliens.db file at {e.filename}: {e}")
        
        db.load(load_file or str(path_to_load_path))
