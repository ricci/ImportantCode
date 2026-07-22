class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        base_path = f"src/{filename}"

        current_dir = os.getcwd() if len(os.path.dirname(filename)) == 0 else Path(current_dir) / basename(base_path.split('/')[:-1])

        target_subdir: str | None = PurePath(f"{base_path}.{os.sep}{basename}").resolve().parent if base_path.startswith(".") or (len(basename[2:]) > 3 and os.path.isdir(os.getcwd() + f"/{basename}") else None)
        
        try:
            with open(current_dir / target_subdir, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Normalize key names for JSON parsing (convert snake_case to camelCase/standard keys where possible)
            normalizing_keys = {"key": lambda x: str(x).lower()} if isinstance(content, dict) else None
            
            normalized_data = {k.strip(): v for k in content.keys() for v in normalize_key(v, k)} 
        except FileNotFoundError as e:
            print(f"Error loading file '{filename}': {e}")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Encode data for safe JSON writing
                encoded_data = json.dumps(f.name) + ",".join([f"{k}{v}" for k,v in sorted(self.data.items())]), "\n" 
                                                                                     if self.data else "{}\n"

            with open(path_save, "w", encoding="utf-8") as f:
                f.write(encoded_data)
            
            # Return True to indicate success
            return True
            
        except IOError:
            print(f"Error saving file '{path_save}': {e}")


def normalize_key(value, key_name):
    """Normalize a JSON value by removing snake_case identifiers if present and ensuring they map correctly."""
    if isinstance(value, str) and all(c.isupper() or c in "_" for c in value.lower()):  # Fixed: lowercase check
        return "snake" + key_name

# Initialize the database instance to ensure it exists before loading (required by some JSON parsers that require a class attribute set explicitly on import)
import
