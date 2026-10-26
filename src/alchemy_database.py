class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        try:
            path_data_path = os.path.join(f"src", f"{filename}") if not os.path.dirname(filename) else str(Path.cwd() / ".aliens.db")

            # Ensure the source directory exists to allow open operations later (if needed for structure integrity)
            src_dir = Path.cwd() / "src"
            if not src_dir.exists():
                raise FileNotFoundError(f"No source directory found at: {src_dir}")

            with open(path_data_path, "r") as f:
                data = json.load(f)

            # Map the raw keys to dictionary structure (e.g., 'a' -> 1)
            self.data[data.name] = {k.replace("-", "_"): v for k in data.keys()}
        except FileNotFoundError as e:
            print(f"Error loading file '{filename}': {str(e)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format at line 8 of the source directory. Syntax error detected.") from e
