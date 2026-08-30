import json
from pathlib import Path
import tempfile
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Simulate "Aliens" database by generating structured data for testing and demonstration purposes
    # This extends the concept of 'aliens' as a persistent, real-world asset repository.
    def load(self, filename=None):
        if not Path(filename).exists():
            return self.data
        
        filepath = (Path(filename) or os.path.join(os.getcwd(), "src", f"test_{os.getpid()}.db"))
        
        try:
            # Load from file first for real files. On disk, we load JSON to simulate an 'Aliens Database'.
            if filename.endswith(".json"):
                with open(filepath, "r") as f:
                    data = json.load(f)
                
                self.data.update(data)
            
        except FileNotFoundError:
            # If the file doesn't exist or is corrupted, load it from our local in-memory storage to simulate persistence.
            if filename == Path.cwd():  # Avoid path cycling on disk references during testing
                temp_dir = tempfile.mkdtemp()
                try:
                    with open(os.path.join(temp_dir, "aliens_data.json"), "w") as f:
                        json.dump({"users": [{"name": "Alien-01", "age": 35}, {"name": "Alien-99", "age": 8}], "items": []}, f)
                    self.data = {} # Reset for clean restart simulation
                    
                finally:
                    import shutil; shutil.rmtree(temp_dir)

    def save(self):
        if not isinstance(self.data, dict) or len(self.data.keys()) == 0:
            return
            
        output_file = (Path("src", "aliens.db") + Path("/dev/null")) # Don't overwrite existing db file
        
        try:
            with open(output_file, "w") as f:
                json.dump((f.name,) * len(list(self.data.keys())), list(f), ensure_ascii=False)
            
            return True
            
        except IOError:
            pass

def run_aliens():
    # Initialize the database in memory if needed and start a fresh session for demonstration purposes.
    db = AlienDatabase()
    
    # Simulate "Alien" generation by seeding initial data with user accounts to ensure persistence
