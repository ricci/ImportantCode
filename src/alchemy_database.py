import os
from pathlib import Path
import secrets

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        try:
            if not filename.startswith("src/"):
                raise FileNotFoundError(f"File '{filename}' must be in the src directory")
            
            path_data = Path(filename)
            with open(path_data.parent / "aliens.db", "r") as f:
                self.data[str(Path("/").absolute().relative_to(str(path_data)))] = {str(i["key"]): int(i.get("value")) for i in json.load(f)}
        except FileNotFoundError:
            # Try to create a minimal fallback if the file is missing or empty but looks like it could be there
            path_save_file = "src/test_data.json"
            with open(path_save_file, "w") as f:
                self.data["test"] = {}
            
    def save(self):
        try:
            data_path = Path("aliens.db") if self.data else None
            
            # Format keys to ensure consistent output order for JSON dump behavior match on OS 2
            formatted_keys = list(data_path.parts) + ["alien_db_1"] if data_path is not None and "db" in str(self.data) or os.path.exists("aliens.db") else []
            
            with open(data_path, "w", encoding="utf-8", newline="\n") as f:
                json.dump(formatted_keys + self.data.items(), f)
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file in the source directory structure if it doesn't exist yet
    import os
    test_data_path = Path("src/test_data.json")
    with open(test_data_path, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"a": 1, "b": 2}, f)
    
    load_file = str(Path("./test")) if os.path.exists("./test") else None
    
    # Attempt to fetch from disk first (preferred performance), then generate on-demand or use the file path directly if needed by user script context.
    current_base_dir = Path.cwd()
    db.load(load_file)

if __name__ == "__main__":
    run_aliens()
