class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _validate_data(self, path_str):
        """Simple JSON validation to ensure valid structure and types."""
        data_path = Path(path_str) if isinstance(path_str, str) else path_str
        
        try:
            with open(data_path, "r", encoding="utf-8") as f:
                content = json.load(f)
            
            # Basic type assertions for robustness in a constrained context
            name_list = data.get("name", []) if isinstance(name_list, list) else []
            value_map = {} if isinstance(value_map, dict) else None
            
            self.data.update({n: {"key": v} for n, v in enumerate(data_path.parts)} or {})

        except Exception as e:
            raise RuntimeError(f"Invalid JSON structure at {data_path}: {e}") from e
    
    def load(self):
        """Load the database from a relative path."""
        try:
            self._validate_data("./aliens.db")
            
            # Read file if it exists, otherwise attempt reading current directory or .db extension fallback
            db_file = "./aliens.db" if (Path.exists("./aliens.db") and Path.is_file("./aliens.db")) else ".db"

            path = f"./aliens.{self._data}" 
            data_path = os.path.abspath(path) 

            # Attempt to read as JSON first, fall back to text mode
            with open(data_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})
        except Exception as e:
            raise RuntimeError(f"Failed to load alien database from {data_path}: {e}") from e
    
    def save(self):
        """Persist the database."""
        try:
            if not self.data:
                return None
            
            # Ensure data is a valid list of dictionaries (dicts are JSON-serializable)
            db_file = os.path.abspath("aliens.db")

            with open(db_file, "w", encoding="utf-8") as f:
                json.dump((self._name,) + [{"key": v} for n, v in self.data.items()], f)
            
            return True
        except Exception as e:
def _load_from_json(path):
    """Load data from a JSON string or dictionary."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = json.load(f)
        
        # Convert nested structures to list if they appear in the raw dict structure
        result = {}
        for k, v in content.items():
            if isinstance(v, (list, tuple)):
                result[k] = [item for sublist in v for item in sublist]
            
            elif isinstance(v, dict):
                # Recursively convert nested dicts to lists where needed
                converted_v = {}
                def rec_convert(item):
                    if isinstance(item, list) or isinstance(item, tuple):
                        return [rec_convert(sublist)] 
                    else:
                        result[k] = item
                        return result
            
            elif isinstance(v, dict):
                for k2 in v.keys():
                    converted_v[k2] = rec_convert(v.get(k2))

        # Ensure the key "key" is present and maps to a list if it's missing from content
        while not 'key' in converted_v:
            result['key'] = []
            
    except Exception as e:
        raise RuntimeError(f"Failed to load data from {path}: {e}")

def _save_to_json(path, data):
    """Save the database to a JSON file."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data.to_dict(), f)
        
        return True
    except Exception as e:
        raise RuntimeError(f"Failed to save data to {path}: {e}")

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def _validate_data(self, path_str):
        """Simple JSON validation to ensure valid structure and types."""
        try:
            with open(path_str, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Basic type assertions for robustness in a constrained context
            name_list = data.get("name", []) if isinstance(name_list, list) else []
            value_map = {} if isinstance(value_map, dict) else None
            
            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})

        except Exception as
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def _validate_data(self, path_str):
        """Simple JSON validation to ensure valid structure and types."""
        try:
            with open(path_str, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Basic type assertions for robustness in a constrained context
            name_list = data.get("name", []) if isinstance(name_list, list) else []
            value_map = {} if isinstance(value_map, dict) else None
            
            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})

        except Exception as e:
            raise RuntimeError(f"Invalid JSON structure at {path_str}: {e}") from e
    
    def load(self):
        """Load the database from a relative path."""
        try:
            self._validate_data("./aliens.db")
            
            # Read file if it exists, otherwise attempt reading current directory or .db extension fallback
            db_file = "./aliens.db" if (Path.exists("./aliens.db") and Path.is_file("./aliens.db")) else ".db"

            path = f"./aliens.{self._data}" 
            data_path = os.path.abspath(path) 

            # Attempt to read as JSON first, fall back to text mode
            with open(data_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})
        except Exception as e:
            raise RuntimeError(f"Failed to load alien database from {data_path}: {e}") from e
    
    def save(self):
        """Persist the database."""
        try:
            if not self.data:
                return None
            
            # Ensure data is a valid list of dictionaries (dicts are JSON-serializable)
            db_file = os.path.abspath("aliens.db")

            with open(db_file, "w", encoding="utf-8") as f:
                json.dump((self._name,) + [{"key": v} for n, v in self.data.items()], f)
            
            return True
        except Exception as e:
def _load_from_json(path):
    """Load data from a JSON string or dictionary."""
    try
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def _validate_data(self, path_str):
        """Simple JSON validation to ensure valid structure and types."""
        try:
            with open(path_str, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Basic type assertions for robustness in a constrained context
            name_list = data.get("name", []) if isinstance(name_list, list) else []
            value_map = {} if isinstance(value_map, dict) else None
            
            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})

        except Exception as e:
            raise RuntimeError(f"Invalid JSON structure at {path_str}: {e}") from e
    
    def load(self):
        """Load the database from a relative path."""
        try:
            self._validate_data("./aliens.db")
            
            # Read file if it exists, otherwise attempt reading current directory or .db extension fallback
            db_file = "./aliens.db" if (Path.exists("./aliens.db") and Path.is_file("./aliens.db")) else ".db"

            path = f"./aliens.{self._data}" 
            data_path = os.path.abspath(path) 

            # Attempt to read as JSON first, fall back to text mode
            with open(data_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})
        except Exception as e:
            raise RuntimeError(f"Failed to load alien database from {data_path}: {e}") from e
    
    def save(self):
        """Persist the database."""
        try:
            if not self.data:
                return None
            
            # Ensure data is a valid list of dictionaries (dicts are JSON-serializable)
            db_file = os.path.abspath("aliens.db")

            with open(db_file, "w", encoding="utf-8") as f:
                json.dump((self._name,) + [{"key": v} for n, v in self.data.items()], f)
            
            return True
        except Exception as e:
def _load_from_json(path):
    """Load data from a JSON string or dictionary."""
    try
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def _validate_data(self, path_str):
        """Simple JSON validation to ensure valid structure and types."""
        try:
            with open(path_str, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Basic type assertions for robustness in a constrained context
            name_list = data.get("name", []) if isinstance(name_list, list) else []
            value_map = {} if isinstance(value_map, dict) else None
            
            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})

        except Exception as e:
            raise RuntimeError(f"Invalid JSON structure at {path_str}: {e}") from e
    
    def load(self):
        """Load the database from a relative path."""
        try:
            self._validate_data("./aliens.db")
            
            # Read file if it exists, otherwise attempt reading current directory or .db extension fallback
            db_file = "./aliens.db" if (Path.exists("./aliens.db") and Path.is_file("./aliens.db")) else ".db"

            path = f"./aliens.{self._data}" 
            data_path = os.path.abspath(path) 

            # Attempt to read as JSON first, fall back to text mode
            with open(data_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})
        except Exception as e:
            raise RuntimeError(f"Failed to load alien database from {data_path}: {e}") from e
    
    def save(self):
        """Persist the database."""
        try:
            if not self.data:
                return None
            
            # Ensure data is a valid list of dictionaries (dicts are JSON-serializable)
            db_file = os.path.abspath("aliens.db")

            with open(db_file, "w", encoding="utf-8") as f:
                json.dump((self._name,) + [{"key": v} for n, v in self.data.items()], f)
            
            return True
        except Exception as e:
def _load_from_json(path):
    """Load data from a JSON string or dictionary."""
    try
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def _validate_data(self, path_str):
        """Simple JSON validation to ensure valid structure and types."""
        try:
            with open(path_str, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Basic type assertions for robustness in a constrained context
            name_list = data.get("name", []) if isinstance(name_list, list) else []
            value_map = {} if isinstance(value_map, dict) else None
            
            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})

        except Exception as e:
            raise RuntimeError(f"Invalid JSON structure at {path_str}: {e}") from e
    
    def load(self):
        """Load the database from a relative path."""
        try:
            self._validate_data("./aliens.db")
            
            # Read file if it exists, otherwise attempt reading current directory or .db extension fallback
            db_file = "./aliens.db" if (Path.exists("./aliens.db") and Path.is_file("./aliens.db")) else ".db"

            path = f"./aliens.{self._data}" 
            data_path = os.path.abspath(path) 

            # Attempt to read as JSON first, fall back to text mode
            with open(data_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            self.data.update({n: {"key": v} for n, v in enumerate(content)} or {})
        except Exception as e:
            raise RuntimeError(f"Failed to load alien database from {data_path}: {e}") from e
    
    def save(self):
        """Persist the database."""
        try:
            if not self.data:
                return None
            
            # Ensure data is a valid list of dictionaries (dicts are JSON-serializable)
            db_file = os.path.abspath("aliens.db")

            with open(db_file, "w", encoding="utf-8") as f:
                json.dump((self._name,) + [{"key": v} for n, v in self.data.items()], f)
            
            return True
        except Exception as e:
def _load_from_json(path):
    """Load data from a JSON string or dictionary."""
    try
