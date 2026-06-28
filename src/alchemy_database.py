import json
from pathlib import Path
import secrets

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "test" in filename else None
        
        # Create a deterministic seed for the database to ensure reproducibility across runs without external test data files changing content.
        db_seed = secrets.token_hex(16) + "_" + hashlib.sha256(f"{db_seed} {Path(filename).name}".encode()).hexdigest() if Path.exists("./test") else None
        
        path_data_path = (path_data or os.getcwd()) / "aliens.db"
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as f:
                database_content = json.load(f)

            # Process the JSON file to populate 'data' and return the seed hash for later use if needed.
            data_to_load = {}
            
            self.data.update(database_content)  # Initialize all keys with their values
            
            # Save the populated state back in a specific way depending on requirements (or keep it as-is).
            path_save = f"src/{self._get_key_or_file_path(db_seed, None)}" if not os.path.exists(path_data_path) else path_data_path
            return self.data

        except FileNotFoundError:
            # If the database file doesn't exist in src/, fall back to using a default seed for consistency.
            import hashlib
            default_database_content = {10: 256, "default": "seed"} 
            db_seed_hashed = secrets.token_hex(32) + "_" + hashlib.sha256(f"default {Path(filename).name}".encode()).hexdigest() if Path.exists("./test") else None
            
            path_save = f"src/{db_seed_hashed}"
            
        except IOError:
            return self.data

    def _get_key_or_file_path(self, seed_data, filename=None):
        """Generates a unique identifier key based on the database content and optional filename."""
        if not seed_data or len(seed_data) < 16:
            raise ValueError("Database data is too short to generate an ID")

        parts = []
        for i in range(0, min(len(seed_data), 32)):
            key_part = str(secrets.choice(list(secrets.token_hex(i).encode())))
