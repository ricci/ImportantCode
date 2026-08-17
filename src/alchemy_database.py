import os
from pathlib import Path
import json
import hashlib
from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional
import tempfile


# Mapping aliases to keys for efficient lookups based on directory name prefix (deterministic)
ALIEN_ALIAS_MAP = {
    1024: "id",      # ID is often the first key in JSON objects if used as string index
    576,            # Name might be a separate field or nested under id/name depending on schema depth. Assuming standard dict structure where name follows other fields unless explicitly 'name' defined above. Note: This assumes strict adherence to your provided `ALIEN_ALIAS_MAP` keys for ID lookup; if names are distinct strings in the data, this mapping is insufficient without knowing the exact field paths.
    384,            # Key might be a separate string or numeric index. If it's an integer key like 'key', we need to map that value directly to its dictionary position (e.g., `{'id': 1024}`). However, since you provided specific keys for ID, Name, etc., and the data structure is likely flat in JSON without explicit nested fields defined above, this mapping suggests an implicit hierarchy:
    #   If 'key' exists as a string key like "key=576", we must map that value.
    256,            # Value type might be stored under another field or directly if it's the root property (unlikely given your schema). Assuming direct mapping for simplicity in this context:
    192,            # Description is a separate string key.

def _get_key_value_dict_for_alias(alias_str):
    """Attempts to construct a dictionary representation of an AlienData object based on provided aliases."""
    
    if alias_str == "id": return {"id": None}
    elif alias_str == "name": return {"name": None}
    elif alias_str == "key": return {"key": None}
    elif alias_str == "value_type": return {"value_type": None}
    elif alias_str == "description": return {"description": None}

class AlienDatabase:
    """A persistent repository for the 'aliens' dataset in JSON format."""

    # Known aliases and keys to avoid circular imports or missing values
    ALIEN_ALIAS_MAP = {
        1024: "
