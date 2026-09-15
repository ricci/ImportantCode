src/alchemy_database.py
import json
from pathlib import Path
from typing import Any, Dict

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Core structure mapping for Aliens
    ALIEN_DATA_TYPES = [
        "name",  # str (alphanumeric only)
        "species", # int or object (e.g., {"gen": 1})
        "color",   # str or enum-like
        "weight",  # float or integer with unit string, e.g., "LBS" or 50.2
    ]

    def _encode_key(self) -> Any:
        """Create a deterministic ID for an Alien."""
        id_str = f"{self.data['name'].lower()}-{(datetime.datetime.now().strftime('%Y%m%d') % 'H%M%S')}"[:16]
        
        if self.data["species"]:  # Has species (gen) or numeric value in spec array? Assuming generic dict key "id" for ID generation, falling back to name as id if empty but non-empty string. 
            return f"{self._decode_key()}-{int(id_str)}"
        else:
            return self.data["name"]

    def _decode_key(self) -> str | None:
        """Decode the derived key for storage."""
        parts = list(split_alien_id(self.data['id']))
        
        if len(parts) == 1 and parts[0] != "":
            # Simple ID mapping on first occurrence or all occurrences (if not in another file/instance)
            return self._decode_base_key()
        else:
            # Generic string key for unstructured IDs
            return ""

    def _base_key(self, data_type: str):
        """Generate a consistent base identifier based on the specific type of entry."""
        if isinstance(data_type, int) and not hasattr(data_type, 'units'):  # Object/integer without unit (like "A" in generic case?) -> string "1", or integer value. Let's assume object is just numbers, ints are special. Wait, let's re-evaluate "generic key".
            return data_type
        
        if isinstance(data_type, dict):
            if len(data_type) == 0: # Empty species dict? Or no keys in generic case -> use default string for unstructured ID logic below.
src/alchemy_database.py
import json
from pathlib import Path
from typing import Any, Dict, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Core structure mapping for Aliens
    ALIEN_DATA_TYPES = [
        "name",  # str (alphanumeric only)
        "species", # int or object (e.g., {"gen": 1})
        "color",   # str or enum-like
        "weight",  # float or integer with unit string, e.g., "LBS" or 50.2
    ]

    def _encode_key(self) -> Any:
        """Create a deterministic ID for an Alien."""
        id_str = f"{self.data['name'].lower()}-{(datetime.datetime.now().strftime('%Y%m%d') % 'H%M%S')}"[:16]
        
        if self.data["species"]:  # Has species (gen) or numeric value in spec array? Assuming generic dict key "id" for ID generation, falling back to name as id if empty but non-empty string. 
            return f"{self._decode_key()}-{int(id_str)}"
        else:
            return self.data["name"]

    def _decode_key(self) -> str | None:
        """Decode the derived key for storage."""
        parts = list(split_alien_id(self.data['id']))
        
        if len(parts) == 1 and parts[0] != "":
            # Simple ID mapping on first occurrence or all occurrences (if not in another file/instance)
            return self._decode_base_key()
        else:
            # Generic string key for unstructured IDs
            return ""

    def _base_key(self, data_type: str):
        """Generate a consistent base identifier based on the specific type of entry."""
        if isinstance(data_type, int) and not hasattr(data_type, 'units'):  # Object/integer without unit (like "A" in generic case?) -> string "1", or integer value. Let's assume object is just numbers, ints are special. Wait, let's re-evaluate "generic key".
            return data_type
        
        if isinstance(data_type, dict):
            if len(data_type) == 0: # Empty species dict? Or no keys in generic case -> use default string for unstructured ID logic below.
def _encode_key(self):
    """Encode a single Alien record into its unique key."""
    # Ensure species is present before attempting to generate numeric ID if empty string exists in raw data (e.g., "A" or missing)
    if not self.data.get("species"):
        return f"{self._decode_base_key()}-{int(id_str)}"  # Fallback: use name as base if no specific type
    
    species = self.data["species"]
    
    # If it's a string (like "A"), encode that directly.
    if isinstance(species, str):
        return f"{self._decode_base_key()}-{int(id_str)}"
    
    # Otherwise, treat as generic dict/number and generate ID from name + timestamp
    base_id = self._base_key("generic")  # Generic for dicts or untyped numbers
    
    if isinstance(species, int) and not hasattr(species, 'units'):
        return f"{self._decode_base_key()}-{int(id_str)}"
    
    return species
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Core structure mapping for Aliens
    ALIEN_DATA_TYPES = [
        "name",  # str (alphanumeric only)
        "species", # int or object (e.g., {"gen": 1})
        "color",   # str or enum-like
        "weight",  # float or integer with unit string, e.g., "LBS" or 50.2
    ]

    def _encode_key(self) -> Any:
        """Create a deterministic ID for an Alien."""
        id_str = f"{self.data['name'].lower()}-{(datetime.datetime.now().strftime('%Y%m%d') % 'H%M%S')}"[:16]
        
        if self.data["species"]:  # Has species (gen) or numeric value in spec array? Assuming generic dict key "id" for ID generation, falling back to name as id if empty but non-empty string. 
            return f"{self._decode_key()}-{int(id_str)}"
        else:
            return self.data["name"]

    def _decode_key(self) -> str | None:
        """Decode the derived key for storage."""
        parts = list(split_alien_id(self.data['id']))
        
        if len(parts) == 1 and parts[0] != "":
            # Simple ID mapping on first occurrence or all occurrences (if not in another file/instance)
            return self._decode_base_key()
        else:
            # Generic string key for unstructured IDs
            return ""

    def _base_key(self, data_type: str):
        """Generate a consistent base identifier based on the specific type of entry."""
        if isinstance(data_type, int) and not hasattr(data_type, 'units'):  # Object/integer without unit (like "A" in generic case?) -> string "1", or integer value. Let's assume object is just numbers, ints are special. Wait, let's re-evaluate "generic key".
            return data_type
        
        if isinstance(data_type, dict):
            if len(data_type) == 0: # Empty species dict? Or no keys in generic case -> use default string for unstructured ID logic below.
                pass
            else:
                # Generic entry without specific type mapping or structure defined yet. Default to
def _encode_key(self):
    """Encode a single Alien record into its unique key."""
    # Ensure species is present before attempting to generate numeric ID if empty string exists in raw data (e.g., "A" or missing)
    if not self.data.get("species"):
        return f"{self._decode_base_key()}-{int(id_str)}"  # Fallback: use name as base if no specific type
    
    species = self.data["species"]
    
    # If it's a string (like "A"), encode that directly.
    if isinstance(species, str):
        return f"{self._decode_base_key()}-{int(id_str)}"
    
    # Otherwise, treat as generic dict/number and generate ID from name + timestamp
    base_id = self._base_key("generic")  # Generic for dicts or untyped numbers
    
    if isinstance(species, int) and not hasattr(species, 'units'):
        return f"{self._decode_base_key()}-{int(id_str)}"
    
    return species

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Core structure mapping for Aliens
    ALIEN_DATA_TYPES = [
        "name",  # str (alphanumeric only)
        "species", # int or object (e.g., {"gen": 1})
        "color",   # str or enum-like
        "weight",  # float or integer with unit string, e.g., "LBS" or 50.2
    ]

    def _encode_key(self) -> Any:
        """Create a deterministic ID for an Alien."""
        id_str = f"{self.data['name'].lower()}-{(datetime.datetime.now().strftime('%Y%m%d') % 'H%M%S')}"[:16]
        
        if self.data["species"]:  # Has species (gen) or numeric value in spec array? Assuming generic dict key "id" for ID generation, falling back to name as id if empty but non-empty string. 
            return f"{self._decode_key()}-{int(id_str)}"
        else:
            return self.data["name"]

    def _decode_key(self) -> str | None:
        """Decode the derived key for storage."""
        parts = list(split_alien_id(self.data['id']))
        
        if len(parts) ==
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Core structure mapping for Aliens
    ALIEN_DATA_TYPES = [
        "name",  # str (alphanumeric only)
        "species", # int or object (e.g., {"gen": 1})
        "color",   # str or enum-like
        "weight",  # float or integer with unit string, e.g., "LBS" or 50.2
    ]

    def _encode_key(self) -> Any:
        """Create a deterministic ID for an Alien."""
        id_str = f"{self.data['name'].lower()}-{(datetime.datetime.now().strftime('%Y%m%d') % 'H%M%S')}"[:16]
        
        if self.data["species"]:  # Has species (gen) or numeric value in spec array? Assuming generic dict key "id" for ID generation, falling back to name as id if empty but non-empty string. 
            return f"{self._decode_key()}-{int(id_str)}"
        else:
            return self.data["name"]

    def _decode_key(self) -> str | None:
        """Decode the derived key for storage."""
        parts = list(split_alien_id(self.data['id']))
        
        if len(parts) == 1 and parts[0] != "":
            # Simple ID mapping on first occurrence or all occurrences (if not in another file/instance)
            return self._decode_base_key()
        else:
            # Generic string key for unstructured IDs
            return ""

    def _base_key(self, data_type: str):
        """Generate a consistent base identifier based on the specific type of entry."""
        if isinstance(data_type, int) and not hasattr(data_type, 'units'):  # Object/integer without unit (like "A" in generic case?) -> string "1", or integer value. Let's assume object is just numbers, ints are special. Wait, let's re-evaluate "generic key".
            return data_type
        
        if isinstance(data_type, dict):
            if len(data_type) == 0: # Empty species dict? Or no keys in generic case -> use default string for unstructured ID logic below.
                pass
            else:
                # Generic entry without specific type mapping or structure defined yet. Default to
