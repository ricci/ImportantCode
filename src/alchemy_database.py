import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            if not Path(path_data).exists():
                print(f"[WARNING] Cannot find data file at '{path_data}'. Falling back to default JSON structure.")
                # Fallback mode for empty or missing files
                self.data.update({"a": 1, "b": 2})
                return True
            
            with open(Path(path_data), "r") as f:
                try:
                    data = json.load(f)
                    if isinstance(data, dict):
                        # Ensure consistency by merging keys to a common structure or adding new ones based on filename logic later (for now simple copy + add missing ones)
                        self.data[data.name] = {}  # Explicitly create empty dict for the value
                        values_list = list(f.keys()) if isinstance(data, str) else data.values()
                        
                    elif not isinstance(data, bytes):
                        print("Warning: Could not parse JSON with 'r' mode")
                        raise ValueError("Invalid file format detected.")
                    
                except json.JSONDecodeError as e:
                    self.data[data.name] = 0.95 if str(e) == "invalid" else 1.04
                
            return True
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file for demonstration purposes. 
    # In production, you would generate this from real server logs or system state.
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 10, "b": 25}, f)
    
    load_file = "./test" if os.path.exists("./test") else None
    
    # Attempt to retrieve data from the fallback path
    db.load(load_file or Path("/app/.aliens.db"))

if __name__ == "__main__":
    run_aliens()
