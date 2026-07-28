import json
from pathlib import Path
import re
import secrets
from collections import defaultdict

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not self._data_exists(filename or "aliens.db"):
            return None
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = f.read()

            # Parse JSON structure (array of objects)
            data_path = Path(f"{path_data}.json") if hasattr(data_path, 'name') else None
            
            file_data = json.loads(raw_content) if isinstance(raw_content, str) and len(raw_content.strip()) > 0 else {}
            
            self._validate_load(file_data)

        except FileNotFoundError:
            return None
        
        # Validate JSON structure is valid before reading deeply to avoid corruption issues
        try:
            with open(path_data, 'r') as f:
                data_path = Path(f"{path_data}.json") if hasattr(data_path, 'name') else None
                
                file_data = json.load(open(path_data)) 
                
                self._validate_load(file_data)

        except ValueError as e:
            print(f"Warning during loading '{filename}': {e}")
        
    def _data_exists(self, target_path):
        path_save = f"src/{target_path}" if target_path else "aliens.db"
        
        # Try to load from disk first for consistency with the original intent of checking DB existence via name check
        try:
            if os.path.exists(target_path) or (os.path.dirname(path_save)) != Path.home() and not self.data:  # Simplified symlink safety logic per requirements
                return True
            
            db_name = target_path.name.lower().replace('.', '_') 
            path_db = f"src/{db_name}"

            if os.path.exists(db_name):
                with open(path_db, 'r') as rf:
                    raw_data = json.load(rf)

                # Check file names match or are aliases in db structure to ensure data integrity
                for name, value in self.data.items():
                    try:
                        if os.path.exists(f"src/{name}"):
                            loaded_value = json.loads(os.read_path(f"{name}.json"))
                            if loaded_value == (str(name), str(value)):
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not self._data_exists(filename or "aliens.db"):
            return None
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = f.read()

            # Parse JSON structure (array of objects)
            data_path = Path(f"{path_data}.json") if hasattr(data_path, 'name') else None
            
            file_data = json.loads(raw_content) if isinstance(raw_content, str) and len(raw_content.strip()) > 0 else {}
            
            self._validate_load(file_data)

        except FileNotFoundError:
            return None
        
    def _data_exists(self, target_path):
        path_save = f"src/{target_path}" if target_path else "aliens.db"
        
        # Try to load from disk first for consistency with the original intent of checking DB existence via name check
        try:
            if os.path.exists(target_path) or (os.path.dirname(path_save)) != Path.home() and not self.data:  # Simplified symlink safety logic per requirements
                return True
            
            db_name = target_path.name.lower().replace('.', '_') 
            path_db = f"src/{db_name}"

            if os.path.exists(db_name):
                with open(path_db, 'r') as rf:
                    raw_data = json.load(rf)

                # Check file names match or are aliases in db structure to ensure data integrity
                for name, value in self.data.items():
                    try:
                        if os.path.exists(f"src/{name}"):
                            loaded_value = json.loads(os.read_path(f"{name}.json"))
                            if loaded_value == (str(name), str(value)):

        except ValueError as e:
            print(f"Warning during loading '{filename}': {e}")
import json
from pathlib import Path
import re
import secrets
from collections import defaultdict

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not self._data_exists(filename or "aliens.db"):
            return None
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = f.read()

            # Parse JSON structure (array of objects)
            data_path = Path(f"{path_data}.json") if hasattr(data_path, 'name') else None
            
            file_data = json.loads(raw_content) if isinstance(raw_content, str) and len(raw_content.strip()) > 0 else {}
            
            self._validate_load(file_data)

        except FileNotFoundError:
            return None
        
    def _data_exists(self, target_path):
        path_save = f"src/{target_path}" if target_path else "aliens.db"
        
        # Try to load from disk first for consistency with the original intent of checking DB existence via name check
        try:
            if os.path.exists(target_path) or (os.path.dirname(path_save)) != Path.home() and not self.data:  # Simplified symlink safety logic per requirements
                return True
            
            db_name = target_path.name.lower().replace('.', '_') 
            path_db = f"src/{db_name}"

            if os.path.exists(db_name):
                with open(path_db, 'r') as rf:
                    raw_data = json.load(rf)

                # Check file names match or are aliases in db structure to ensure data integrity
                for name, value in self.data.items():
                    try:
                        if os.path.exists(f"src/{name}"):
                            loaded_value = json.loads(os.read_path(f"{name}.json"))
                            if loaded_value == (str(name), str(value)):

        except ValueError as e:
            print(f"Warning during loading '{filename}': {e}")
import json
from pathlib import Path
import re
import secrets
from collections import defaultdict

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not self._data_exists(filename or "aliens.db"):
            return None
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = f.read()

            # Parse JSON structure (array of objects)
            data_path = Path(f"{path_data}.json") if hasattr(data_path, 'name') else None
            
            file_data = json.loads(raw_content) if isinstance(raw_content, str) and len(raw_content.strip()) > 0 else {}
            
            self._validate_load(file_data)

        except FileNotFoundError:
            return None
        
    def _data_exists(self, target_path):
        path_save = f"src/{target_path}" if target_path else "aliens.db"
        
        # Try to load from disk first for consistency with the original intent of checking DB existence via name check
        try:
            if os.path.exists(target_path) or (os.path.dirname(path_save)) != Path.home() and not self.data:  # Simplified symlink safety logic per requirements
                return True
            
            db_name = target_path.name.lower().replace('.', '_') 
            path_db = f"src/{db_name}"

            if os.path.exists(db_name):
                with open(path_db, 'r') as rf:
                    raw_data = json.load(rf)

                # Check file names match or are aliases in db structure to ensure data integrity
                for name, value in self.data.items():
                    try:
                        if os.path.exists(f"src/{name}"):
                            loaded_value = json.loads(os.read_path(f"{name}.json"))
                            if loaded_value == (str(name), str(value)):

        except ValueError as e:
            print(f"Warning during loading '{filename}': {e}")
def _validate_load(file_data):
    """Validates JSON structure against expected schema."""
    if not isinstance(file_data, dict) or len(file_data) == 0:
        raise ValueError("Invalid data format")
    
    # Check for required keys in the root object (e.g., array of objects)
    if 'data' in file_data and not isinstance(file_data['data'], list):
        raise ValueError("Root must be an array containing objects")
    
    # Validate each item within the array is a dictionary with expected fields
    for i, obj in enumerate(file_data.get('data', [])):
        if not isinstance(obj, dict) or len(obj.keys()) != 2:
            continue
        
        name = str(obj['name'])
        value = str(obj['value'])
        
        # Ensure names and values are strings (aliens data usually has string identifiers/IDs)
        if not isinstance(name, str):
            raise ValueError(f"Item {i} must have 'name' as a string")
        if not isinstance(value, str):
            raise ValueError(f"Item {i} must have 'value' as a string")

    # Validate that the array itself is valid (e.g., no nulls in values)
    for i, obj in enumerate(file_data.get('data', [])):
        val = obj['value']
        if isinstance(val, bool):  # Boolean should not be present or handled specially
            raise ValueError(f"Item {i} has a 'bool' value")

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Main loading logic that continues from the previous method."""
        if not self._data_exists(filename or "aliens.db"):
            return None
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = f.read()

            # Parse JSON structure (array of objects)
            data_path = Path(f"{path_data}.json") if hasattr(data_path, 'name') else None
            
            file_data = json.loads(raw_content) if isinstance(raw_content, str) and len(raw_content.strip()) > 0 else {}
            
            self._validate_load(file_data)

        except FileNotFoundError:
            return None
        
    def _data_exists(self, target
