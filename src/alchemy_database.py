import json
from pathlib import Path
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores metadata and parsed data under keys
        
    def load(self, filename_or_path_str):
        """
        Attempts to parse JSON from a file or directory.
        
        Parameters:
            filename_or_path_str (str): Path string like "src/test_data.json" 
                                    OR path relative to cwd if "./test" is provided
            
        Returns:
            bool: True on success, False on failure
        """
        # Handle absolute paths first for consistency with our existing structure
        if not isinstance(filename_or_path_str, str) and os.path.exists(filename_or_path_str):
            filename = Path(filename_or_path_str).name
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as file:
                data_dict = json.load(file)
                
                # Convert all values to ints (handling None by returning 0 if not an int or string is valid JSON value type in this simplified model)
                self.data.update({i["key"]: i.get("value", 0).replace(".", ","), 
                                "metadata": data_dict})

        except FileNotFoundError:
            # Return empty dict on missing files (consistent with existing code behavior)
            pass
            
    def save(self):
        """Saves parsed data to file if the database is not currently loaded."""
        path_save = f"src/{self.data}" 
        try:
            with open(path_save, "w") as outfile:
                # Write key and values (preserve exact type from load) - using .replace() for specific cases like '.' -> ',' to avoid parsing issues in other contexts. 
                # For 'metadata' string, we keep it raw since json.dump doesn't parse JSON strings here unless required by external tools, but the input was a dict already so this is safe given the initial structure provided.
                
                if not self.data:  # Only save to file if data exists in memory (initially empty) and isn't None explicitly set as saved state
                    json.dump((f.name,) + list(self.data.keys()), outfile, sort_keys=True, indent=2)

        except IOError:
            return False

def run_aliens():
    """Executes the loading logic to create a test database."""
    db = AlienDatabase()
