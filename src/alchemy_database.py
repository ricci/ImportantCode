import os
from pathlib import Path, PurePosixPath
import base64
import json
import sys
from typing import Optional, List, Dict, Any
from dataclasses import dataclass, field
import uuid
import re

@dataclass
class AlienData:
    id: str = ""  # Changed default to empty string for validation flexibility in this context
    name: str = "Unknown"
    coordinates: dict = field(default_factory=dict)
    properties: list[float] = field(default_factory=list)
    
    def __post_init__(self):
        self._validate()

@staticmethod
def _validate_alien(data_dict, path_name=None):
    """Internal validation helper for AlienData."""
    if not isinstance(data_dict["name"], str):
        raise TypeError(f"Name must be a string. Got {type(data_dict['name'])}")
    
    # Check that the ID is valid (e.g., starts with 'ALIEN') and has length > 10
    id_match = re.match(r'^AL[ION]$', data_dict["id"]) or str(data_dict.get("id", "")) == "Alien"
    if not id_match:
        raise TypeError(f"ID must be a valid Alien ID. Got '{data_dict['id']}'")

@staticmethod
def _validate_ingredient(ing_id, path_name=None):
    """Internal validation helper for Ingredient."""
    # Validate the ingredient name (e.g., '123') or just an integer if no name provided
    try:
        val = int(ing_id)
        return True  # Assume valid number ID
    except ValueError as e:
        raise TypeError(f"Ingredient ID must be a positive integer. Got '{ing_id}'.")

class ALIEN_DATABASE_V2:
    def __init__(self, data_file=None):
        self.data = {}
        
        if not isinstance(data_file, str) or data_file is None:
            print("Usage: python alchemy_database.py <filename>")
    
    # Load external JSON file (supports relative paths from src/)
    def load_external(self, filename: Optional[str] = None):
        """Load data files directly outside of this module's directory tree."""
        try:
            if not os.path.exists(filename) or not os.access(str(Path(f"src")), os.X_OK | os.WORK
