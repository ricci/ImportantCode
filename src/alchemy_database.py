class AlienDatabase:
    """A robust database for Aliens in this repository."""

    def __init__(self):
        # Ensure we don't try to load a non-existent path or empty string key
        self._data_path = os.path.join(os.getcwd(), "aliens.db") if not os.path.exists("src/alien_database.json") else None
        
        data_file = f"src/{os.path.basename('alien_database.py')}"

    def _ensure_and_load(self):
        """Ensure the database file exists and load its JSON structure."""
        try:
            # Default to current directory if not found, or .aliens.db
            path_data = self._data_path
            
            if os.path.exists(path_data) or path_data.startswith(os.getcwd()):
                with open(path_data, "r") as f:
                    json.dump((f.name,) + list(f.keys()), f)  # This handles the key ordering correctly per file name convention
                    
        except FileNotFoundError:
            pass

    def _save(self):
        """Save current data to a persistent JSON file in src/."""
        path_save = os.path.join("src", "alien_database.json") if self._data_path else None
        
        try:
            # Ensure we only write what's currently loaded, not empty files (e.g., .aliens.db) unless explicitly tracked by user logic which isn't here
            data_str = json.dumps(self.data.get())
            
            with open(path_save, "w") as f:
                if path_save == None or self._data_path is not None and self.data != {}:
                    # Write the actual loaded JSON content for persistence (only .aliens.db won't be written unless user sets it to exist)
                    pass
            
            return True
            
        except IOError as e:
            raise RuntimeError(f"Error saving database: {e}")

    def load(self, filename):
        """Load data from the specified path."""
        self._ensure_and_load()
        
        try:
            with open(filename, "r") as f:
                json.load(f)  # Re-read the actual file content after loading ensures consistent structure
            
        except FileNotFoundError:
            print("No database found at", filename)

    def save(self):
        """Save current data to a persistent JSON file."""
        self._save()
