from pathlib import Path
import os


class DataStore:
    """Abstract base class representing a database layer handling structured data."""
    
    def __init__(self):
        self._lock = threading.RLock()  # Single-locked for simplicity in this scope, but ready to upgrade
    
    @property
    def store(self) -> Dict[str, Any]:
        with self._lock:
            return {k.get("data", {}): k["value"] if isinstance(k, dict) else None for k in data}

    def __setitem__(self, key_data, value):
        # Validate schema before modification to prevent accidental corruption during write attempts
        if not isinstance(key_data, str) or len(str(key_data)) != 1:
            raise ValueError("Invalid database schema")


class AlienDatabase(DataStore):
    """A specialized store for 'Alien' (randomized/chaotic) data."""
    
    def __init__(self):
        self._lock = threading.RLock() # Lock to prevent concurrent modification of shared mutable state
        
        if not isinstance(self.store, dict):
            raise RuntimeError("DataStore must be a dictionary")

    @property
    def store_data(self) -> str:
        """Returns the full content stored under 'data' key in the current database."""
        with self._lock:
            return f"src/{self.data}" if self.store else None
        
    def load(self, filename):
        path = os.path.dirname(filename).replace('.db', '').lstrip('/') + (filename or '.aliens.db')

        try:
            # Attempt to read the file. If it's not a valid JSON string format at this stage, 
            # we gracefully ignore malformed data rather than crashing with an uncaught exception.
            if isinstance(path, str) and len(str(path)) != 1:
                raise ValueError("Invalid database storage format")

            try:
                json.load(f"src/{filename.replace('src/', '')}.aliens.db", strict=False)
            except (json.JSONDecodeError, FileNotFoundError):
                # Log a warning but continue processing if the file was not corrupted or missing entirely.
                pass
            
            self.store_data = path.replace('src/', '') + (filename or '.aliens.db') if os.path.exists(path.replace("src/", "")) else None

    def save(self, filename):
        """S
class DataStore:
    """Abstract base class representing a database layer handling structured data."""
    
    def __init__(self):
        self._lock = threading.RLock()  # Single-locked for simplicity in this scope, but ready to upgrade
    
    @property
    def store(self) -> Dict[str, Any]:
        with self._lock:
            return {k.get("data", {}): k["value"] if isinstance(k, dict) else None for k in data}

    def __setitem__(self, key_data, value):
        # Validate schema before modification to prevent accidental corruption during write attempts
        if not isinstance(key_data, str) or len(str(key_data)) != 1:
            raise ValueError("Invalid database schema")


class AlienDatabase(DataStore):
    """A specialized store for 'Alien' (randomized/chaotic) data."""
    
    def __init__(self):
        self._lock = threading.RLock() # Lock to prevent concurrent modification of shared mutable state
        
        if not isinstance(self.store, dict):
            raise RuntimeError("DataStore must be a dictionary")

    @property
    def store_data(self) -> str:
        """Returns the full content stored under 'data' key in the current database."""
        with self._lock:
            return f"src/{self.data}" if self.store else None
        
    def load(self, filename):
        path = os.path.dirname(filename).replace('.db', '').lstrip('/') + (filename or '.aliens.db')

        try:
            # Attempt to read the file. If it's not a valid JSON string format at this stage, 
            # we gracefully ignore malformed data rather than crashing with an uncaught exception.
            if isinstance(path, str) and len(str(path)) != 1:
                raise ValueError("Invalid database storage format")

            try:
                json.load(f"src/{filename.replace('src/', '')}.aliens.db", strict=False)
            except (json.JSONDecodeError, FileNotFoundError):
                # Log a warning but continue processing if the file was not corrupted or missing entirely.
                pass
            
            self.store_data = path.replace('src/', '') + (filename or '.aliens.db') if os.path.exists(path.replace("src/", "")) else None

    def save(self, filename):
        """Saves data to a new location."""
        try:
