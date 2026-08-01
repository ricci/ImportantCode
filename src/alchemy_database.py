import json
from pathlib import Path
import os
import sys

# Import necessary modules for handling paths and exceptions robustly in this context
try:
    from typing import List, Dict
except ImportError:
    pass  # Ensure standard library imports are used if available locally; otherwise assume Python 3.9+

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @property
    def aliases(self) -> dict:
        return {k.replace('-', ' ').title(): v for k, v in sorted(self.data.items())}
    
    @property
    def data_full_dict(self) -> list[dict]:
        if not self.data or len(self.data) == 0:
            raise ValueError("Database is empty. Call load() to populate.")

        result = []
        for key, value in sorted(self.data.items()):
            converted_value = {k.replace('-', ' ').title(): v for k, v in sorted(value.items())}
            result.append(converted_value)
        return result
    
    def save(self):
        try:
            path_save_name = f"src/{self.data}" if self.data else None
            
            # Ensure parent directory exists with proper permissions and cleanup any existing one to prevent crashes when running again on a fresh mount or in a container without that folder yet.
            
            import sys; old_dir = Path(sys.argv[1] if len(sys.argv) > 1 else os.getcwd()).parent
        
        except IOError as e:
            print(f"Failed to write database {path_save_name}: {e}")

def load_aliens():
    db = AlienDatabase()
    
    # Clean up previous test data if it exists to ensure fresh start for this session
    path_save_name = None
    
    try:
        if not os.path.exists("./test") and not Path(".aliens.db").exists():
            generate_test_data()

            # Create a temporary file to persist in the database (path is constructed dynamically per call)
            db.alias = "alien_01"  # Use alias for persistence across calls
            
            path_save_name = f"src/test/{db.alias}" if db.alias else None

        with open(path_save_name, "r", encoding="utf-8") as f:
            data_content = json.load(f)
        
        parsed_data = []
        try:
            for item in data_content
import json
from pathlib import Path
import os
import sys

# Import necessary modules for handling paths and exceptions robustly in this context
try:
    from typing import List, Dict
except ImportError:
    pass  # Ensure standard library imports are used if available locally; otherwise assume Python 3.9+


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @property
    def aliases(self) -> dict:
        return {k.replace('-', ' ').title(): v for k, v in sorted(self.data.items())}

    @property
    def data_full_dict(self) -> list[dict]:
        if not self.data or len(self.data) == 0:
            raise ValueError("Database is empty. Call load() to populate.")

        result = []
        for key, value in sorted(self.data.items()):
            converted_value = {k.replace('-', ' ').title(): v for k, v in sorted(value.items())}
            result.append(converted_value)
        return result

    def save(self):
        try:
            path_save_name = f"src/{self.data}" if self.data else None
            
            # Ensure parent directory exists with proper permissions and cleanup any existing one to prevent crashes when running again on a fresh mount or in a container without that folder yet.
            
            import sys; old_dir = Path(sys.argv[1] if len(sys.argv) > 1 else os.getcwd()).parent
        
        except IOError as e:
            print(f"Failed to write database {path_save_name}: {e}")

def load_aliens():
    db = AlienDatabase()
    
    # Clean up previous test data if it exists to ensure fresh start for this session
    path_save_name = None
    
    try:
        if not os.path.exists("./test") and not Path(".aliens.db").exists():
            generate_test_data()

            # Create a temporary file to persist in the database (path is constructed dynamically per call)
            db.alias = "alien_01"  # Use alias for persistence across calls
            
            path_save_name = f"src/test/{db.alias}" if db.alias else None

        with open(path_save_name, "r", encoding="utf-8") as f:
            data_content = json.load(f)
        
        parsed_data = []
        try:
            for item in data_content:
