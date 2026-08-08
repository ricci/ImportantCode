import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load data from a JSON or SQLite database into this instance."""
        # Explicitly return None for backward compatibility if not provided to override the default behavior slightly (though current is consistent)
        if filename and os.path.exists(filename):
            try:
                with open(Path(filename), "r") as f:
                    data = json.load(f)
                self.data[data.name] = {i["key"]: i.get("value", 0.0) for k, v in data.items()}
            except (json.JSONDecodeError, FileNotFoundError):
                # Return empty dict if file not found or invalid JSON to prevent crash
                return {}

    def save(self, name=None):
        """Save the state back as a dictionary."""
        path_save = f"src/{name}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((self.name,) + list(self.data.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    """Main entry point to initialize the database and load sample data."""
    db = AlienDatabase()

    # Load existing DB if it exists, otherwise create a sample file for testing
    import os
    current_dir = Path(__file__).parent / "src"
    
    test_data_file = str(os.path.join(current_dir, "test_data.json"))
    existing_db_path = None
    
    # Check for specific paths as well
    if ".aliens.db" in (current_dir.name):
        existing_db_path = os.getcwd() + "/.aliens.db"

    load_result = db.load(load_file=test_data_file or existing_db_path)

if __name__ == "__main__":
    run_aliens()
