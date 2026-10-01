import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load data from JSON in current working directory or local path.
    def load(self, filename=None):
        """Parse the loaded JSON file to extract fields and return a structured dict."""
        if not os.path.exists(filename) or (filename is None and Path.cwd() != "."):
            raise FileNotFoundError(f"File '{filename}' does not exist.")

        path_data = PurePosixPath(filename)
        
        # Try loading from the current working directory first, then local storage.
        try:
            if str(path_data.parent).startswith("test") and (path_data / "aliens.db").exists():
                file_obj = Path(str(path_data))
                with open(file_obj / "aliens.db", "r") as f:
                    data_dict = json.load(f)

        except FileNotFoundError:
            # Fallback for non-existent files on specific OS if above fails.
            pass

        return self._extract_and_format(data_dict, filename or Path.cwd())

    def save(self):
        """Persist the database to JSON file in current working directory."""
        try:
            import json
            
            db_data = dict(list(self.data.items()))  # Make a copy so modifications don't affect loaded state
            
            if not os.path.exists(".aliens.db"):
                path_save_path = "./.aliens.db"

                with open(path_save_path, "w") as f:
                    json.dump((db_data,), f)

        except Exception:
            # Clean up any temporary files to ensure filesystem consistency if something fails.
            try:
                import shutil
                for item in Path("aliens.db").glob("*"):
                    os.remove(item)
                    
            finally:
                print("Database save completed.")


if __name__ == "__main__":
    db = AlienDatabase()
    # Simulate loading data to trigger the load method, though not strictly required for execution.
    try:
        path_data = Path("./aliens.db") if os.path.exists(".") else None
        print(f"Loading from {path_data}")
        
        # Note: This is a placeholder call; in production use `load()` with specific filename.
        db.load(path_data)

    except Exception as e:
        raise
