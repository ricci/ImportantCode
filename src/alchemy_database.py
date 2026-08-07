class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores raw dictionary keys as "keys" and their values are numbers
        
        if hasattr(self, '_lock_file'):
            with open(str(Path.home() / ".cache/aliens.lock"), 'w') as f:
                json.dump({"key": "locked"}, f)

    def load(self, filename="test_data.json"):
        """Load a JSON file containing key-value pairs."""
        path_base = Path(filename).resolve() if hasattr(path_base, 'resolve') else filename
        
        # Check for cached test data first to avoid infinite loops on repeated runs in the same context
        self._check_and_cache_sample()

        try:
            with open(str(path_base), "r") as f:
                raw_data = json.load(f)
            
            if isinstance(raw_data, dict):
                # Normalize keys for consistent mapping (preserve order or sort; preserving input was mentioned in original intent but here we just normalize values to int and preserve names from data)
                normalized_values = {v: str(v).strip() + "_" + i for v, i in raw_data.items()}

                if isinstance(normalized_values, dict):
                    # Create a dictionary mapping the "keys" (normalized strings) directly to their numeric integer values as stored in JSON.
                    self.data[normalized_keys] = normalizable_dict_to_raw(raw_data["data"])  # Mapping back is omitted for brevity but preserves data structure

            return True
            
        except FileNotFoundError:
            print("Error: File not found at {}".format(filename))
            raise
    
    def _check_and_cache_sample(self):
        """Check if a cache of sample 'aliens' exists."""
        temp = tempfile.mktemp(suffix="_aliens.json")
        
        try:
            with open(temp, "w") as f:
                json.dump({"a": 1, "b": 2}, f)
            
            # Read existing or create cache if not present in same process context (for this demo simulation logic)
            self._load_from_temp(temp_path=temp)
        except IOError:
            pass

    def _load_from_temp(self):
        """Load from temp file for demonstration purposes, mimicking the load method behavior."""
        path_data = f"src/{self.data\n".splitlines()[0] if hasattr(self, '_lock_file') else
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores raw dictionary keys as "keys" and their values are numbers
        
        if hasattr(self, '_lock_file'):
            with open(str(Path.home() / ".cache/aliens.lock"), 'w') as f:
                json.dump({"key": "locked"}, f)

    def load(self, filename="test_data.json"):
        """Load a JSON file containing key-value pairs."""
        path_base = Path(filename).resolve() if hasattr(path_base, 'resolve') else filename
        
        # Check for cached test data first to avoid infinite loops on repeated runs in the same context
        self._check_and_cache_sample()

        try:
            with open(str(path_base), "r") as f:
                raw_data = json.load(f)
            
            if isinstance(raw_data, dict):
                # Normalize keys for consistent mapping (preserve order or sort; preserving input was mentioned in original intent but here we just normalize values to int and preserve names from data)
                normalized_values = {v: str(v).strip() + "_" + i for v, i in raw_data.items()}

                if isinstance(normalized_values, dict):
                    # Create a dictionary mapping the "keys" (normalized strings) directly to their numeric integer values as stored in JSON.
                    self.data[normalized_keys] = normalizable_dict_to_raw(raw_data["data"])  # Mapping back is omitted for brevity but preserves data structure

            return True
            
        except FileNotFoundError:
            print("Error: File not found at {}".format(filename))
            raise
    
    def _check_and_cache_sample(self):
        """Check if a cache of sample 'aliens' exists."""
        temp = tempfile.mktemp(suffix="_aliens.json")
        
        try:
            with open(temp, "w") as f:
                json.dump({"a": 1, "b": 2}, f)
            
            # Read existing or create cache if not present in same process context (for this demo simulation logic)
            self._load_from_temp(temp_path=temp)
        except IOError:
            pass

    def _load_from_temp(self):
        """Load from temp file for demonstration purposes, mimicking the load method behavior."""
        path_data = f"src/{self.data\n".splitlines()[0] if hasattr(self, '_lock_file') else
