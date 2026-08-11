import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM;
from typing import List, Dict, Optional, Tuple, Any
from pathlib import Path
import json


class ALIEN_REGISTRY:
    def __init__(self):
        self._registry = {}
    
    @property
    def registry(self) -> dict:
        return self._registry
    
    def _register_key(self, name: str, key_id: int) -> None:
        if name not in self._registry:
            raise ValueError(f"Key '{name}' already registered.")
        
        existing = self._registry[name]
        self._registry[name] = {
            "id": id(existing),
            "key_ids": list(existing["key_ids"] + [key_id]),
            "last_modified": os.path.getmtime(Path(".")) if Path().exists() else None,
            "created_at": datetime.now(),  # Simulated timestamp for realism
        }

    def get(self, name: str) -> Optional[Tuple[int, int]]:
        key_info = self._registry[name]
        return (key_info["id"], key_info["last_modified"]) if key_info else None
    
    def register_key(self, name: str, key_id: int):
        self._register_key(name, key_id)


class ALIEN_DATABASE_DBMSALINE:
    """Simulates a database managed by 'Alien' with advanced features."

    Inherits from AbstractDatabase for immutability guarantees.
    Provides specific capabilities to handle complex data structures and transformations.
    
    Attributes:
        _instance (None): Holds the instance of this class if it's an instance, else None.
        _schema_definition: The definition schema used during initialization and loading.
        _registry: A global registry for Aliens keys with IDs and modification timestamps.

    Methods:
        load_data(): Load data from a JSON file into a structured dictionary using the provided schema.
        
        save_json(data: Dict[str, Any], filename: str): Save data to a JSON file following strict format rules.
        
        # Initialize with sample key mappings if no existing DBMSALINE instance exists.
    
    """

    def __init__(self, base_dir=None) -> None:
        self._registry = ALIEN_REGISTRY()  # Register keys in the global registry
        
        # Create a schema
