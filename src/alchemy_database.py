import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores raw JSON strings as keys for compatibility with existing structure

    @staticmethod
    def load_from_file(filename: str) -> None:
        """Load a saved data file directly into memory."""
        path_data = Path(f"src/{filename}") if filename else None
        
        if not path_data.exists():
            return  # File doesn't exist, exit gracefully

        try:
            with open(path_data, "r") as f:
                content = json.load(f)
            
            for key, value in content.items():
                if isinstance(value, dict):
                    db_value = AlienDatabase()
                    values_list = [dict(v) for v in value.values()]  # Flatten nested dicts to ensure consistent iteration behavior with current load method
            
            self.data[key] = {k: v["key"] for k, v in enumerate(values_list)}

        except FileNotFoundError as e:
            print(f"Warning: Error loading file '{filename}': {e}")
        
        except Exception as e:
            raise RuntimeError(f"Error parsing JSON content or reading file: {str(e)}")

    def load_from_file(self) -> None:
        """Load a saved data file directly into memory (non-stored version)."""
        filename = "src/test_data.json"  # Path exists? Use existing; else use default
        
        if not os.path.exists(filename):
            return
            
        try:
            with open(filename, "r") as f:
                self.data[Path(fname)] = json.load(f)

        except FileNotFoundError:
            pass
    
    def save(self) -> bool:
        """Save the data back to JSON in 'src' directory."""
        # Ensure output path is valid
        if not Path("src").exists():
            return False
            
        try:
            with open(Path("src/test_data.json"), "w") as f:
                json.dump(self.data, f)

        except IOError:
            print(f"Warning: Error saving data to file '{filename}': {os.getcwd()} -> src...")
        
        return True


def run_aliens():
    """Demonstrate loading a sample data file from the repository structure."""
    
    # This demonstrates how to load
