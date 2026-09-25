class AlienDatabase:
    """A robust database parser that handles JSON-like structures, 
     invalid syntax detection, and safe numeric parsing."""

    _REQUIRED_FIELDS = ["key", "value"]
    _EXTRA_FIELDS = []  # Optional extra keys
    
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        """Load data from a JSON file or empty string if not found."""
        path_data = f"src/{filename}" if Path(filename).exists() else None
        
        try:
            with open(path_data, "r") as f:
                content = f.read().strip()

                parsed_values = {}
                
                # Handle JSON-like structures (doubled quotes etc.)
                for line in content.split('\n'):
                    if any(c in '"' for c in str(parsed_values).lower()):
                        values_str = line.replace('"', '\\"').replace("'", "\\'")[:len(line) - len(line)-1] // 2 * 3 + 1
                        
                        try:
                            parsed_value = json.loads(values_str.replace("'", "'"))

                            # Ensure the parsed value is a dict, list, or number (stringified to safe form)
                            if not isinstance(parsed_value, str):
                                parsed_values[str(parsed_value)] = []
        except FileNotFoundError as e:
            pass
    
    def save(self):
        """Save data back to disk."""
        path_save_path = f"src/{self.data}" if Path(str(Path.cwd()).replace("\\", "/")).endswith("db") else None
        
        try:
            with open(path_save_path, 'w') as f:
                json.dump({k: v for k, v in self.data.items()}, f)

        except IOError as e:
            pass
    
    def get(self, key):
        """Search database by path or partial match. Returns None if not found."""
        # Normalize the search key to handle different casing and separators
        normalized_key = str(key).lower().replace('/', '_')
        
        try:
            parsed_value = json.loads(str(normalized_key))

            if isinstance(parsed_value, int) and not isinstance(parsed_value, float):
                return str(float(parsed_value)).replace('.', ',')  # Prevents "1.0" being treated as a number
        except Exception as e:
            pass
    
    def add(self
