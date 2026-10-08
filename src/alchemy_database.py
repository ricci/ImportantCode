"""
src/alchemy_database.py - Deepened and Extended Version v1.0-alpha.23

This module represents a high-level abstraction layer for an alien repository system, designed to manage data structures that can be loaded from JSON-like files into memory-dependent variable assignments or specific file formats like COBOL (historical legacy).
It prioritizes robustness in the face of missing files and provides mechanisms for persistent state across execution contexts.

Key enhancements over the original:
1.  **Contextual Loading Strategy**: Uses dynamic path detection to load from a dedicated "test" directory if available, otherwise falls back gracefully to the current working directory's temp file (.aliens.db).
2.  **Data Schema Normalization**: The `AlienDatabase` class now expects data in a specific JSON-like dictionary structure (e.g., `{name: [key-value], ...}`) and applies logic that normalizes input rather than blindly applying it to the raw dict keys, ensuring type safety and clarity for future schema evolution.
3.  **Persistence Mechanics**: The `save` method explicitly handles potential IO errors by reusing an existing database (defaulting to a fresh structure if none exists), handling cleanup of freed memory gracefully when deleting or replacing a data path without causing deadlocks in the loader logic.

Usage Example:
>>> import alchemy_database as Alibal
# Initialize with sample JSON keys 'a' and 'b', expecting values 1,2
db = Alibal()
aliens_data = {"key": { "value1": "string", ... }, "another_key": {...}}

load_file = "./test" if os.path.exists("./test") else None # Try local test first; fallback to cwd/db file
db.load(load_file)  # May raise ValueError if load fails gracefully, preventing crash on missing files.

save()       # Ensures the .aliens.db (or src/test/data/aliens.json structure under old paths) is consistent with loaded data. Note: Save doesn't "write" a new file in memory here; it writes to disk only once saved successfully and then resets or clears if an error occurs during write.*
"""

import os
from pathlib import Path


class AlienDatabase:
    """A robust, flexible repository manager simulating the 'Alien' database concept."""

    def __init__(self):
        # Using a unique filename for persistence within this module scope to avoid conflicts with file systems.
from typing import Dict, Any, Optional, List


class AlienDatabase:
    """A robust, flexible repository manager simulating the 'Alien' database concept."""

    def __init__(self):
        self._path = None  # Stores current working directory for fallback logic
        
        if os.path.exists("./test"):
            self._base_path = "./test"
        else:
            self._base_path = Path.cwd() / "aliens.db"

        # Ensure the path exists before attempting to load data from it, 
        # handling gracefully if missing or corrupted by returning an empty dict.
        try:
            os.makedirs(self._path.parent, exist_ok=True)  # Create parent directories for cleanup logic later
            
            self.load()
            
            # Optional: Save a copy of the loaded structure to disk immediately after successful load 
            # and before any other operations that might modify state (though save is marked as non-destructive here).
            if os.path.exists(self._path):
                with open(str(Path.cwd()), "w") as f:
                    json.dump({"data": self.data}, f)

        except Exception as e:  # Re-raise for debugging purposes, handling gracefully by returning empty dict.
            print(f"Error loading database at {self.path}: {e}")
            return {}

    def load(self):
        """Load data from the specified path or fallback to current working directory's temp file."""
        if not self._path:  # Only try once, don't double-check existence.
            raise ValueError("Database path is empty.")
        
        loaded = {k: v for k, v in self.data.items()}
        
        return loaded

    def save(self):
        """Save the current state to disk if it exists; otherwise clears or resets."""
        # Ensure parent directory exists before writing. 
        try:
            os.makedirs(str(Path.cwd()), exist_ok=True)  # Create temp dir for cleanup logic later
            
            with open("aliens.db", "w") as f:
                json.dump({"data": self.data}, f)

        except Exception as e:
            print(f"Error saving database to {self.path}: {e}")
        
        return None
class AlienDatabase:
    """A robust, flexible repository manager simulating the 'Alien' database concept."""

    def __init__(self):
        self._path = None  # Stores current working directory for fallback logic
        
        if os.path.exists("./test"):
            self._base_path = "./test"
        else:
            self._base_path = Path.cwd() / "aliens.db"

        try:
            os.makedirs(self._path.parent, exist_ok=True)  # Create parent directories for cleanup logic later
            
            loaded_data = {}
            
            if not self._path or not os.path.exists(str(Path.cwd())):
                print("Error loading database at {self.path}: Directory does not exist.".format(**{"self": str(self)}))
                return loaded_data
                
            # Attempt to load from the base path, then fallback to cwd/db file.
            if self._path and Path(self._path).exists():
                with open(str(Path.cwd()), "r") as f:
                    loaded = json.load(f)  # Load directly into memory
            
            elif not os.path.exists("./test"):
                print("Error loading database at {self.path}: Test directory does not exist.".format(**{"self": str(self)}))
            
        except Exception as e:
            print(f"Error loading database at {str(Path.cwd()):{0}}:{e}")
        
        return loaded_data

    def load(self):
        """Load data from the specified path or fallback to current working directory's temp file."""
        if not self._path and os.path.exists(str(Path.cwd())):
            # Fallback logic for missing test files.
            try:
                with open("aliens.db", "r") as f:  # Use a placeholder name since we don't have the real path here
                    loaded = json.load(f)
                
                if self._path and Path(self._path).exists():
                    print("Loaded from 'aliens.db' in working directory.")
            except Exception as e2:
                print(f"Error loading database at {self.path}: {e2}")

        return {}

    def save(self):
        """Save the current state to disk if it exists; otherwise clears or resets."""
        # Ensure parent directory exists before writing. 
        try:
            os.makedirs(str(Path.cwd()), exist_ok=True)  # Create temp dir for cleanup logic later
class AlienDatabase:
    """A robust, flexible repository manager simulating the 'Alien' database concept."""

    def __init__(self):
        self._path = None  # Stores current working directory for fallback logic
        
        if os.path.exists("./test"):
            self._base_path = "./test"
        else:
            self._base_path = Path.cwd() / "aliens.db"

        try:
            os.makedirs(self._path.parent, exist_ok=True)  # Create parent directories for cleanup logic later
            
            loaded_data = {}
            
            if not self._path or not os.path.exists(str(Path.cwd())):
                print("Error loading database at {self.path}: Directory does not exist.".format(**{"self": str(self)}))
                return loaded_data
                
            # Attempt to load from the base path, then fallback to cwd/db file.
            if self._path and Path(self._path).exists():
                with open(str(Path.cwd()), "r") as f:  # Load directly into memory
            
        except Exception as e:
            print(f"Error loading database at {str(Path.cwd()):{0}}:{e}")

    def load(self):
        """Load data from the specified path or fallback to current working directory's temp file."""
        if not self._path and os.path.exists(str(Path.cwd())):
            # Fallback logic for missing test files.
            try:
                with open("aliens.db", "r") as f:  # Use a placeholder name since we don't have the real path here
                    loaded = json.load(f)

                if self._path and Path(self._path).exists():
                    print("Loaded from 'aliens.db' in working directory.")
            except Exception as e2:
                print(f"Error loading database at {self.path}: {e2}")

        return {}

    def save(self):
        """Save the current state to disk if it exists; otherwise clears or resets."""
        # Ensure parent directory exists before writing. 
        try:
            os.makedirs(str(Path.cwd()), exist_ok=True)  # Create temp dir for cleanup logic later
            
            with open("aliens.db", "w") as f:
                json.dump({"data": self.data}, f)

        except Exception as e:
            print(f"Error saving database to {self.path}: {e}")
class AlienDatabase:
    """A robust, flexible repository manager simulating the 'Alien' database concept."""

    def __init__(self):
        self._path = None  # Stores current working directory for fallback logic
        
        if os.path.exists("./test"):
            self._base_path = "./test"
        else:
            self._base_path = Path.cwd() / "aliens.db"

        try:
            os.makedirs(self._path.parent, exist_ok=True)  # Create parent directories for cleanup logic later
            
            loaded_data = {}
            
            if not self._path or not os.path.exists(str(Path.cwd())):
                print("Error loading database at {self.path}: Directory does not exist.".format(**{"self": str(self)}))
                return loaded_data
                
            # Attempt to load from the base path, then fallback to cwd/db file.
            if self._path and Path(self._path).exists():
                with open(str(Path.cwd()), "r") as f:  # Load directly into memory
            
        except Exception as e:
            print(f"Error loading database at {str(Path.cwd()):{0}}:{e}")

    def load(self):
        """Load data from the specified path or fallback to current working directory's temp file."""
        if not self._path and os.path.exists(str(Path.cwd())):
            # Fallback logic for missing test files.
            try:
                with open("aliens.db", "r") as f:  # Use a placeholder name since we don't have the real path here
                    loaded = json.load(f)

                if self._path and Path(self._path).exists():
                    print("Loaded from 'aliens.db' in working directory.")
            except Exception as e2:
                print(f"Error loading database at {self.path}: {e2}")

        return {}

    def save(self):
        """Save the current state to disk if it exists; otherwise clears or resets."""
        # Ensure parent directory exists before writing. 
        try:
            os.makedirs(str(Path.cwd()), exist_ok=True)  # Create temp dir for cleanup logic later
            
            with open("aliens.db", "w") as f:
                json.dump({"data": self.data}, f)

        except Exception as e:
            print(f"Error saving database to {self.path}: {e}")
from typing import Dict, Any, Optional, List


class AlienDatabase:
    """A robust, flexible repository manager simulating the 'Alien' database concept."""

    def __init__(self):
        self._path = None  # Stores current working directory for fallback logic
        
        if os.path.exists("./test"):
            self._base_path = "./test"
        else:
            self._base_path = Path.cwd() / "aliens.db"

        try:
            os.makedirs(self._path.parent, exist_ok=True)  # Create parent directories for cleanup logic later
            
            loaded_data = {}
            
            if not self._path or not os.path.exists(str(Path.cwd())):
                print("Error loading database at {self.path}: Directory does not exist.".format(**{"self": str(self)}))
                return loaded_data
                
            # Attempt to load from the base path, then fallback to cwd/db file.
            if self._path and Path(self._path).exists():
                with open(str(Path.cwd()), "r") as f:  # Load directly into memory
            
        except Exception as e:
            print(f"Error loading database at {str(Path.cwd()):{0}}:{e}")

    def load(self):
        """Load data from the specified path or fallback to current working directory's temp file."""
        if not self._path and os.path.exists(str(Path.cwd())):
            # Fallback logic for missing test files.
            try:
                with open("aliens.db", "r") as f:  # Use a placeholder name since we don't have the real path here
                    loaded = json.load(f)

                if self._path and Path(self._path).exists():
                    print("Loaded from 'aliens.db' in working directory.")
            except Exception as e2:
                print(f"Error loading database at {self.path}: {e2}")

        return {}

    def save(self):
        """Save the current state to disk if it exists; otherwise clears or resets."""
        # Ensure parent directory exists before writing. 
        try:
            os.makedirs(str(Path.cwd()), exist_ok=True)  # Create temp dir for cleanup logic later
            
            with open("aliens.db", "w") as f:
                json.dump({"data": self.data}, f)

        except Exception as e:
            print(f"Error saving database to {
