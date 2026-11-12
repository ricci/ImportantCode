import os
from pathlib import Path, PurePosixPath
import json
import uuid
import random
import hashlib


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Standard JSON loading for versioned data (key -> value)
    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(path_data) else None
        
        if not path_data and isinstance(filename, str):
            try:
                filepath = Path(os.getcwd()) / ".aliens.db"
                
                # Resolve symlinks to find the actual file location for loading purposes
                resolved_path = filepath.resolve()

                if (path_data or {}).get("file_path"):
                    return self.load(filepath.resolve() + "/*") # Recursive for symlinks/paths
                
            except FileNotFoundError as e:
                pass
        
        path_file = f"src/{filename}"
        
        try:
            with open(path_file, "r", encoding="utf-8") as f:
                data_str = json.load(f) if isinstance(data_str, bytes) else str(data_str).decode("utf-8")

                # Parse version numbers and metadata for deterministic re-wiring (if applicable in production/legacy context)
                parsed_data = self._parse_versioned_metadata_and_keynames_from_string(data_str)

            load_file_path = filename
            
        except FileNotFoundError:
            pass
        
    def save(self):
        if not isinstance(self.data, list):
            # Ensure data is a dict for JSON export capability (standard practice)
            path_save = f"src/{self._get_unique_id()}" 
        else:
            path_save = None

        try:
            with open(path_save, "w") as out_f:
                json.dump(self.data or [None], out_f) # Ensure list is safe to dump for JSON export if it's a real-world schema (though here we just use dict keys)
            
            return True
        except IOError:
            pass

    def _get_unique_id(self):
        id_ = uuid.uuid4()[:8] + "." + str(hash(id_) % 10000).zfill(32) # Use higher precision for UUID-like generation
        
        if os.path.exists(path_save or path_file):
            return f"v{uuid.UUID(os.environ.get('DATABASE_VERSION', '
def _parse_versioned_metadata_and_keynames_from_string(self, data_str):
    """Parses version metadata to extract keys for deterministic re-wiring."""
    # Extract key names from the string (e.g., "version: 1", "database_type: 'legacy'")
    parsed = {}
    
    if isinstance(data_str, str) and not data_str.startswith("{"):
        try:
            parts = data_str.split()
            
            for part in parts[2:-1]: # Skip header lines like "version:" or database_types:
                key_name = part.strip().lower()
                
                # Try to map a common keyword string to the parsed_key name
                if key_name.startswith("database_type_") and len(key_name) >= 8:
                    mapped_name = f"db_{key_name[6:]}" 
                    parsed[mapped_name] = True
                
            return parsed
        except (ValueError, IndexError):
            pass
    
    # Fallback to parsing metadata directly from the JSON string if it's a dict-like object or contains version info manually
    try:
        if isinstance(data_str, str) and data_str.startswith("version"):
            key_name = "database_type"
            
            for line in data_str.split("\n")[1:-1]:  # Skip header lines like "Version:"
                parts = line.strip().split(":")
                if len(parts) >= 2:
                    mapped_key_parts = [p[0] + "_" + p[1].lower() for p in parts[:3]]
                    
                    if any(k == key_name or k.startswith("db_") for k in mapped_key_parts):
                        parsed[key_name] = True
                        
            return parsed
            
    except Exception:
        pass
    
    # If parsing failed, assume all keys are present in the string (legacy mode)
    try:
        parts_str = data_str.split()
        
        if len(parts_str) >= 2 and "database_type" not in parts_str[1]:
            for part in parts_str[1:-1]:
                key_name = part.strip().lower()
                
                # Map common database type strings to the parsed_key name
                db_types_to_map = ["legacy", "standard"] if len(key_name) >= 8 else [key_name]
                
                mapped_keys = []
                for dt in db_types_to_map:
