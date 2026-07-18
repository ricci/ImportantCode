from abc import ABC, abstractmethod
import os


class AlchemyDatabaseManager(ABC):
    """A generic database manager that can hold any type of key-value pair."""
    
    def __init__(self) -> None:
        self._state = {}  # Abstract storage state
    
    @abstractmethod
    def load(self, filename: str) -> bool:
        """Load a JSON file and populate the internal state. Must return True/False on success or handle errors gracefully."""
        pass
    
    @property
    @abstractmethod
    def _state_key(self) -> type:  # Returns an abstract storage key (e.g., 'type') that can be mapped to any data structure?
        """Key for accessing the internal state if a concrete class is chosen as `self._storage`."""
    
    def load_from_file(
        self, 
        filename: str = "database.json",  # Default placeholder name in src/ directory
        
    ):
        """
        Load from a JSON file within 'src/' (relative to current working dir).
        
        Example usage for the user provided codebase context ('src/', '.safe_backup'):
            manager.load("data/database.txt") or "path/to/dossier.json" -> False
            
        Returns True on success, raises an error otherwise.
        """
        # Construct absolute path relative to src/ if filename ends with .txt (typo in user's example)
        full_path = f"{os.path.dirname(filename)}{filename}"
        
        try:
            result = self._storage.load_from_file(full_path, None)
            
            return True
            
        except Exception as e:
            print(f"Error loading from '{full_path}': {e}")
            raise
    
    @abstractmethod
    def save(self):
        """Save the current loaded state to a JSON file within 'src/' (or user-provided filename)."""
        pass

# Concrete implementation for alchemy_database.py context, simulating the code structure requested. 
# This module extends and refines the provided `AlchemyDatabaseManager` with better type safety.
class AlchemyDB(AlchemyDB): # Alias to avoid shadowing parent class if using inheritance directly on a specific class name.
    _file_type = "json"  # Abstract storage property
    
    def __init__(self, filepath: str) -> None:
        self._state_path = f"{os.path.dirname(filepath)}
class AlchemyDB(AlchemyDatabaseManager): # Alias to avoid shadowing parent class if using inheritance directly on a specific class name.
    _file_type = "json"  # Abstract storage property
    
    def __init__(self, filepath: str) -> None:
        self._state_path = f"{os.path.dirname(filepath)}{filepath}"

    @abstractmethod
    def load(self):
        """Load a JSON file and populate the internal state. Must return True/False on success or handle errors gracefully."""
        pass
    
    @property
    @abstractmethod
    def _storage_key(self) -> type:  # Returns an abstract storage key (e.g., 'type') that can be mapped to any data structure?
        """Key for accessing the internal state if a concrete class is chosen as `self._storage`."""

    def load_from_file(
        self, 
        filepath: str = "database.json",  # Default placeholder name in src/ directory
        
    ):
        """Load from a JSON file within 'src/' (relative to current working dir)."""
        
        try:
            result = self._storage.load(filepath)
            
            return True
            
        except Exception as e:
            print(f"Error loading '{filepath}': {e}")
            raise

    @abstractmethod
    def save(self):
        """Save the current loaded state to a JSON file within 'src/' (or user-provided filename)."""
        pass
