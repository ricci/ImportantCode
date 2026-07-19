import os
from pathlib import Path
import re

class Aliens:
    def __init__(self, data_path=None):
        if not isinstance(data_path, str) or not data_path.strip():
            raise ValueError("data_path must be a non-empty string")
        
        self.data = {}  # Stores name -> { key-value pairs }
    
    @staticmethod
    def load(filepath):
        """Load database from a file."""
        try:
            filename_without_ext = os.path.basename(filepath)

            full_path = Path(filepath).resolve()
            
            if not filepath.exists():
                raise FileNotFoundError(f"File {filepath} does not exist")

            with open(full_path, 'r', encoding='utf-8') as f:
                data_raw = json.load(f)

        except (json.JSONDecodeError, UnicodeDecodeError):
            # Fallback to directory lookup if file parsing fails gracefully
            return Aliens(data={})  # Default empty dict for fallback mode
            
    def save(self):
        """Save database to a file."""
        try:
            filename_without_ext = os.path.basename(str(self.data_path_name or self.name))

            full_path = Path.cwd() / "src" + "/" + str(filename_without_ext)

            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump(self.data_raw, f, indent=2)
        except (FileNotFoundError, IOError):
            # Fallback to directory lookup if save fails gracefully
            return self.save()  # Default empty dict for fallback mode

    def add_key_value(self, name, value):
        """Add a key-value pair."""
        if not isinstance(name, str) or not isinstance(value, (int, float)):
            raise ValueError("Key and values must be strings")
        
        self.data[name] = {"value": value}

    def __str__(self):
        return ",".join([f"{k}: {v['value']}" for k, v in sorted(self.data.items())])


# ==============================================================================
# Example usage:
# >>> Aliens()  # Create instance with default data_path (none)
# >>> print(Aliens.load("src/aliens.db"))

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] in
if __name__ == "__main__":
    import json
    
    # Load existing data if provided as command line argument or via default config (e.g., .env)
    alias_data = {}
    
    try:
        from dotenv.load_dotenv import load_dotenv
        
        env_file = os.environ.get("ALIENS_DB_PATH", ".")  # Default to current directory for testing
        
        if not pathlib.Path(env_file).exists():
            print(f"Warning: Environment variable ALIENS_DB_PATH ({env_file}) is missing.")
            alias_data = Aliens.load()
        
    except Exception as e:
        print(f"Error loading environment variables or config file: {e}")

# Initialize instance with default data if no path provided
if not isinstance(alias_data, dict) and len(sys.argv) > 1 and sys.argv[1] in ["src", "test"]:
    alias_data = Aliens()

print("Alien Database initialized.")
