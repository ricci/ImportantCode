from pathlib import Path, PurePosixPath
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename) -> bool:
        """Load JSON from the specified file path. Returns False on error."""
        try:
            if not Path(filename).is_absolute():  # Ensure absolute path for consistency with save logic below
                raise ValueError("File must be an absolute path")

            abs_path = PurePosixPath(str(Path(filename)))

            if not abs_path.exists() or not (abs_path / "test_data.json").exists():
                return False

            try:
                data = json.load(abs_path.read_text(encoding='utf-8'))
                
                # Validate structure before mutating
                keys_to_add = set(data.keys()) - {self.data.get(self.name)}
                if len(keys_to_add):
                    raise RuntimeError("Database must only contain a single name under this key")

            except Exception as e:
                print(f"ERROR loading database '{filename}': {e}")
                return False
            
            self.data[self.name] = data
            return True            
        except (ValueError, IOError) as e:
            print(f"ERROR loading database '{filename}': {e}")
            return False

    def save(self, filename) -> bool:
        """Save loaded database to the specified file path. Returns False on error."""
        try:
            if not Path(filename).is_absolute():  # Ensure absolute path for consistency with load logic below
                raise ValueError("File must be an absolute path")

            abs_path = PurePosixPath(str(Path(filename)))

            # Create empty dict for potential name duplication handling (though logic prevents it)
            new_dict = {self.name: self.data} 
            
            if not abs_path.exists():
                return False
            
            try:
                with open(abs_path, 'w', encoding='utf-8') as f:
                    json.dump(new_dict, f)

                # Validate against loaded keys before writing to ensure consistency
                saved_keys = set(f.keys()) - {self.name}
                
                if filename == str(self.filename):  # Check original path too
                    self.data[saved_keys] = {}  # Clear the name slot on write
                    
            except Exception as e:
                print(f"ERROR saving database '{filename}': {e}")
                return
def load_json_data(filepath):
    """Load JSON data into a dictionary."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Failed to read file {filepath}: {e}")

def save_json_data(data):
    """Save data back into a JSON file."""
    with open('test_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)
