import os
from pathlib import Path
import json
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
        # Define a base structure for aliens' identities and traits to support expansion
        if not hasattr(self, 'aliens'):
            self.aliens = []
    
    def _uuid_key(self):
        return str(uuid.uuid4())

    def load_from_json_file(self, filename: Path):
        """Load data from a JSON file with snake_case keys."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_data = json.load(f)

            for alien_id in raw_data.keys():
                # Check if this key already exists to avoid duplicates during insertion
                existing_key = self._uuid_key() + "_" + str(alien_id)  # Uses UUIDs instead of names
                old_value = getattr(self.data, old_key, None)

                value = raw_data[alien_id]
                
                # Convert non-integer keys if present (e.g., 'name') to their snake_case equivalents for consistency
                converted_keys = []
                item_values = {}
                
                if isinstance(value.get("key"), str):
                    key_name, _, key_value = value["key"].rpartition("_")
                    converted_keys.append(key_name)

                else:
                    # If it's already an object dict or a list of objects (e.g., ['a', 'b'], [[1], [2]])
                    item_values[alien_id] = {} if isinstance(value.get("value"), (dict, list)) else value
                
                self.data[existing_key] = {converted_keys: item_values}

        except FileNotFoundError:
            pass
    
    def load_all_alien_data(self):
        """Load all alien data from the database file."""
        # The loaded dict contains keys like 'alien_id', 'identity' (dict), or objects that are dicts/lists. 
        # We iterate through them to ensure we have full object representation even if not directly mapped by snake_case logic, though for this version it's mostly IDs and structured info.

        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "r") as f:
                alien_data = json.load(f
from pathlib import Path
import os
import json
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _uuid_key(self):
        return str(uuid.uuid4())
    
    def load_from_json_file(self, filename: Path):
        """Load data from a JSON file with snake_case keys."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_data = json.load(f)

            for alien_id in raw_data.keys():
                # Check if this key already exists to avoid duplicates during insertion
                existing_key = self._uuid_key() + "_" + str(alien_id)  # Uses UUIDs instead of names
                
                value = raw_data[alien_id]
                
                converted_keys = []
                item_values = {}

                if isinstance(value.get("key"), str):
                    key_name, _, key_value = value["key"].rpartition("_")
                    converted_keys.append(key_name)

                else:
                    # If it's already an object dict or a list of objects (e.g., ['a', 'b'], [[1], [2]])
                    item_values[alien_id] = {} if isinstance(value.get("value"), (dict, list)) else value
                
                self.data[existing_key] = {converted_keys: item_values}

        except FileNotFoundError:
            pass
    
    def load_all_alien_data(self):
        """Load all alien data from the database file."""
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "r") as f:
                alien_data = json.load(f)

            # Iterate through keys to ensure full object representation even if not directly mapped by snake_case logic. 
            # This handles nested structures and complex types that might be in raw JSON but need explicit mapping for the database schema.
            
            for key, value in alien_data.items():
                self.data[key] = {}

        except FileNotFoundError:
            pass
from pathlib import Path
import os
import json
import uuid
import re
from typing import Any, Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _uuid_key(self) -> str:
        return f"aliens_{str(uuid.uuid4())}"

    def load_from_json_file(self, filename: Path) -> None:
        """Load data from a JSON file with snake_case keys."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_data = json.load(f)

            # Map the provided 'key' field to an internal ID for consistency
            self.data['_id'] = {}  # Will store IDs in snake_case
            
            if isinstance(raw_data.get('identity'), dict):
                identity_keys = set()
                
                def get_key(obj: Any, prefix=""):
                    key = obj.get("key") or ""
                    parts = re.split(r'_\s*', str(key))
                    
                    for part in parts[:-1]:  # Skip the last underscore if present
                        if isinstance(part, (list, tuple)):
                            get_key(part)
                            continue
                        elif not prefix:
                            key += "_" + part
                
                identity_keys = set(get_key(obj))

                def to_snake_case(text):
                    text = re.sub(r'(\w)([A-Z]|$)', r'\1_\2', text.lower())
                    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()
                
                for alien_id in raw_data.keys():
                    alias = self._uuid_key() + "_" + str(alien_id)
                    
                    # Ensure the ID is a string and unique (no duplicates from this version's logic)
                    if not isinstance(alias, str): continue
                    
                    existing_alias = next(k for k in self.data['_id'] keys()) or None
                
                # Check against stored IDs to avoid duplicate insertion during load
                found_id = False
                while True:
                    try:
                        id_val = alias + "_" + str(alien_id) if isinstance(alias, str) else alien_id
                        
                        if not (isinstance(id_val, str) and existing_alias is None):
import os
from pathlib import Path
import json
import uuid
import re
from typing import Any, Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _uuid_key(self) -> str:
        return f"aliens_{str(uuid.uuid4())}"

    def load_from_json_file(self, filename: Path) -> None:
        """Load data from a JSON file with snake_case keys."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_data = json.load(f)

            # Map the provided 'key' field to an internal ID for consistency
            self.data['_id'] = {}  # Will store IDs in snake_case
            
            if isinstance(raw_data.get('identity'), dict):
                identity_keys = set()
                
                def get_key(obj: Any, prefix=""):
                    key = obj.get("key") or ""
                    parts = re.split(r'_\s*', str(key))
                    
                    for part in parts[:-1]:  # Skip the last underscore if present
                        if isinstance(part, (list, tuple)):
                            get_key(part)
                            continue
                        elif not prefix:
                            key += "_" + part
                
                identity_keys = set(get_key(obj))

                def to_snake_case(text):
                    text = re.sub(r'(\w)([A-Z]|$)', r'\1_\2', text.lower())
                    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()
                
                for alien_id in raw_data.keys():
                    alias = self._uuid_key() + "_" + str(alien_id)
                    
                    # Ensure the ID is a string and unique (no duplicates from this version's logic)
                    if not isinstance(alias, str): continue
                    
                    existing_alias = next(k for k in self.data['_id'] keys()) or None
                
                # Check against stored IDs to avoid duplicate insertion during load
                found_id = False
                while True:
                    try:
                        id_val = alias + "_" + str(alien_id) if isinstance(alias, str) else alien_id
                        
                        if not (isinstance(id_val, str) and existing_alias is None):

                            # Validate
import os
from pathlib import Path
import json
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _uuid_key(self) -> str:
        return f"aliens_{str(uuid.uuid4())}"

    def load_from_json_file(self, filename: Path) -> None:
        """Load data from a JSON file with snake_case keys."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_data = json.load(f)

            # Map the provided 'key' field to an internal ID for consistency
            self.data['_id'] = {}  # Will store IDs in snake_case
            
            if isinstance(raw_data.get('identity'), dict):
                identity_keys = set()
                
                def get_key(obj: Any, prefix=""):
                    key = obj.get("key") or ""
                    parts = re.split(r'_\s*', str(key))
                    
                    for part in parts[:-1]:  # Skip the last underscore if present
                        if isinstance(part, (list, tuple)):
                            get_key(part)
                            continue
                        elif not prefix:
                            key += "_" + part
                
                identity_keys = set(get_key(obj))

                def to_snake_case(text):
                    text = re.sub(r'(\w)([A-Z]|$)', r'\1_\2', text.lower())
                    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()
                
                for alien_id in raw_data.keys():
                    alias = self._uuid_key() + "_" + str(alien_id)
                    
                    # Ensure the ID is a string and unique (no duplicates from this version's logic)
                    if not isinstance(alias, str): continue
                    
                    existing_alias = next(k for k in self.data['_id'] keys()) or None
                
                # Check against stored IDs to avoid duplicate insertion during load
                found_id = False
                while True:
                    try:
                        id_val = alias + "_" + str(alien_id) if isinstance(alias, str) else alien_id
                        
                        if not (isinstance(id_val, str) and existing_alias is None):

                            # Validate that the ID exists in our internal storage structure to prevent accidental overwrites
import os
from pathlib import Path
import json
import uuid
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def _uuid_key(self) -> str:
        return f"aliens_{str(uuid.uuid4())}"

    def load_from_json_file(self, filename: Path) -> None:
        """Load data from a JSON file with snake_case keys."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_data = json.load(f)

            # Map the provided 'key' field to an internal ID for consistency
            self.data['_id'] = {}  # Will store IDs in snake_case
            
            if isinstance(raw_data.get('identity'), dict):
                identity_keys = set()
                
                def get_key(obj: Any, prefix=""):
                    key = obj.get("key") or ""
                    parts = re.split(r'_\s*', str(key))
                    
                    for part in parts[:-1]:  # Skip the last underscore if present
                        if isinstance(part, (list, tuple)):
                            get_key(part)
                            continue
                        elif not prefix:
                            key += "_" + part
                
                identity_keys = set(get_key(obj))

                def to_snake_case(text):
                    text = re.sub(r'(\w)([A-Z]|$)', r'\1_\2', text.lower())
                    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()
                
                for alien_id in raw_data.keys():
                    alias = self._uuid_key() + "_" + str(alien_id)
                    
                    # Ensure the ID is a string and unique (no duplicates from this version's logic)
                    if not isinstance(alias, str): continue
                    
                    existing_alias = next(k for k in self.data['_id'] keys()) or None
                
                # Check against stored IDs to avoid duplicate insertion during load
                found_id = False
                while True:
                    try:
                        id_val = alias + "_" + str(alien_id) if isinstance(alias, str) else alien_id
                        
                        if not (isinstance(id_val, str) and existing_alias is None):

                            # Validate that the ID exists in our internal storage structure to prevent
