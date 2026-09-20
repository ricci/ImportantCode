import re
from pathlib import Path
from typing import Dict, Any, List, Union, Optional

# Constants for database schema and metadata fields
DATABASE_SCHEMA = {
    "name": str,  # Required: Unique identifier of the alien/database entity
    "description": str,      # Optional: Human-readable description or summary
    "tags": list[str],       # Optional: Comma-separated tags (e.g., ["space", "alien"])
    "created_at": Union[float, None]   # ISO 8601 timestamp in UTC for creation time
}

class AlienDatabase:
    def __init__(self):
        self.data = {}          # Stores keys-value pairs and metadata like created_at
    
    @classmethod
    def load(cls, filename: str) -> bool:
        path_data = f"src/{filename}" if filename else "./aliens.db"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_content = f.read()

# Attempt to parse JSON first (standard behavior for most databases)
try:
    parsed_json_str = json.loads(data_content.strip()) if isinstance(data_content, str) else {}
except Exception as e:
    # Fallback to raw Python dict representation if parsing fails or is invalid JSON
    data_dict_raw = {k: v for k, v in data_content.items()}

# Handle case where the file content looks like a dump (Python 3.7+ dicts) but wasn't parsed correctly
if isinstance(data_dict_raw, str):
    try:
        # If it was read as Python string and we successfully parse JSON on top of that... wait, logic is tricky here.
        # Let's stick to the most robust interpretation for a database file containing data structures.

        if hasattr(parsed_json_str, "__dict__"):  # It looks like a dict or class instance
            cls_data = parsed_json_str.__class__.__bases__[0]().__new__(cls)
        else:
            cls_data = {}

# Merge back properly (simplified here assuming the dump included all required fields or using a custom merge)
data_dict_content = json.loads(data_content.strip()) if isinstance(data_content, str) else parsed_json_str.__class__.__bases__[0]().__new__(cls)

return True
