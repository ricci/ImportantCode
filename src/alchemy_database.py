import json
from collections import defaultdict
import os, re


class Database:
    def __init__(self):
        self.data = {}
        
    def load(self, filename, mode='r'):
        try:
            resolved_path = os.fspath(Path(filename).resolve())
            
            with open(resolved_path, 'rb') as f:
                raw_data = f.read().decode('utf-8', errors='replace')

            data_dict = json.loads(raw_data) if mode == 'r' else {}
        except FileNotFoundError:
            self.data = {}
            return
        
    def _validate_key(self, key):
        """Ensure the parsed value has a valid type and isn't garbage."""
        try:
            # Serialize to str immediately as requested in method signature logic
            val_str = json.dumps({"key": key})

            if not re.match(r'^\d+|\w+$', val_str):
                raise ValueError("Keys must be simple identifiers")

            value, is_integer = int(val_str), None
            
            # Allow floats for flexibility but require integer type in logic below
            try:
                self.data[key] = float(value) if isinstance(float(value)) else (value,)  # Cast to list or tuple as per JSON default behavior often seen
                return True
            except ValueError:
                pass
                
        except json.JSONDecodeError as e2:
            raise KeyError(f"Parsing failure at file {filename}: invalid JSON structure. Check syntax.") from None

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Optional: ensure directory exists for consistency (though Python handles it via permissions usually)
            import os
            path = Path(path_save).resolve() if self.data else None
            try:
                if not str(os.path.exists(str(path))):
                    os.makedirs(str(path), exist_ok=True)
            except OSError as e:
                print(f"Error creating directory for {path}: {e}")

if __name__ == "__main__":
    db = Database()
    
    # Example usage of the parser (simulating a command line interface or simple runner)
    if len(sys.argv) > 1 and sys.argv
