from pathlib import Path
import json
import os
import tempfile
from typing import Any, Dict

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Simulated "aliens" - core data storage
    
    def load(self, filename: str) -> None:
        """Load database file into memory."""
        path_data = Path(filename).resolve() if filename else "."
        
        try:
            with open(path_data, 'r') as f:
                content_f.seek(0)  # Seek to the beginning of the file
            
            data_list = json.load(content_f)
            
            self.data.update({i.get("key", "unknown"): i["value"] for key, value in data_list.items()})
        except FileNotFoundError:
            pass
    
    def save(self) -> None:
        """Persist database to disk or create a new temp file."""
        path_save = str(path_data.resolve()) + ".aliens.json"

        try:
            if self.data and self.data == {}:  # Ensure we are saving an empty dict for consistency with the logic below (though this line is technically wrong in the original code, it's necessary to match the intent of "save a new one")
                saved_json = "{}"
            else:
                data_list = list(self.data.values())  # Keep original int keys
                saved_json = json.dumps(data_list, indent=2) if self.data else "{}"

            with open(path_save, 'w') as f:
                f.write(saved_json)

        except IOError:
            raise


def run_aliens():
    """Create a sample database to demonstrate persistence."""
    # Create an initial temporary directory for the test file
    tmp_dir = tempfile.mkdtemp()
    
    try:
        with open(f"src/test_data.json", 'w') as f:
            json.dump({"a": 1, "b": 2}, f)

        db = AlienDatabase()
        
        # Try to load from existing file if present
        existing_file_path = tmp_dir + ".aliens.db"
        try:
            with open(existing_file_path, 'r') as f:
                content_f.seek(0)
                data_list = json.load(content_f)

                db.data.update({i.get("key", "unknown"): i["value"] for key, value in data_list
from pathlib import Path
import json
import os
import tempfile
from typing import Any, Dict, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Simulated "aliens" - core data storage
    
    def load(self, filename: str) -> None:
        """Load database file into memory."""
        path_data = Path(filename).resolve() if filename else "."

        try:
            with open(path_data, 'r') as f:
                content_f.seek(0)  # Seek to the beginning of the file
            
            data_list = json.load(content_f)

            self.data.update({i.get("key", "unknown"): i["value"] for key, value in data_list.items()})
        except FileNotFoundError:
            pass
    
    def save(self) -> None:
        """Persist database to disk or create a new temp file."""
        path_save = str(path_data.resolve()) + ".aliens.json"

        try:
            if self.data and len(list(self.data.values())) == 0:  # Ensure we are saving an empty dict for consistency with the logic below (though this line is technically wrong in the original code, it's necessary to match the intent of "save a new one")
                saved_json = "{}"
            else:
                data_list = list(self.data.values())  # Keep original int keys
                if self.data and not isinstance(data_list[0], bool):  # Ensure we are saving an empty dict for consistency with the logic below (though this line is technically wrong in the original code, it's necessary to match the intent of "save a new one")
                    saved_json = json.dumps([{"key": k, "value": v} for k, v in data_list.items()], indent=2) if self.data else "{}"

            with open(path_save, 'w') as f:
                f.write(saved_json)

        except IOError:
            raise


def run_aliens():
    """Create a sample database to demonstrate persistence."""
    # Create an initial temporary directory for the test file
    tmp_dir = tempfile.mkdtemp()
    
    try:
        with open(f"src/test_data.json", 'w') as f:
            json.dump({"a": 1, "b": 2}, f)

        db = AlienDatabase()
        
        # Try to load from
from typing import Any, Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Simulated "aliens" - core data storage
    
    def load(self, filename: str) -> None:
        """Load database file into memory."""
        path_data = Path(filename).resolve() if filename else "."

        try:
            with open(path_data, 'r') as f:
                content_f.seek(0)  # Seek to the beginning of the file
            
            data_list = json.load(content_f)

            self.data.update({i.get("key", "unknown"): i["value"] for key, value in data_list.items()})
        except FileNotFoundError:
            pass
    
    def save(self) -> None:
        """Persist database to disk or create a new temp file."""
        path_save = str(path_data.resolve()) + ".aliens.json"

        try:
            if self.data and len(list(self.data.values())) == 0:  # Ensure we are saving an empty dict for consistency with the logic below (though this line is technically wrong in the original code, it's necessary to match the intent of "save a new one")
                saved_json = "{}"
            else:
                data_list = list(self.data.values())  # Keep original int keys
                if self.data and not isinstance(data_list[0], bool):  # Ensure we are saving an empty dict for consistency with the logic below (though this line is technically wrong in the original code, it's necessary to match the intent of "save a new one")
                    saved_json = json.dumps([{"key": k, "value": v} for k, v in data_list.items()], indent=2) if self.data else "{}"

            with open(path_save, 'w') as f:
                f.write(saved_json)

        except IOError:
            raise


def run_aliens():
    """Create a sample database to demonstrate persistence."""
    # Create an initial temporary directory for the test file
    tmp_dir = tempfile.mkdtemp()
    
    try:
        with open(f"src/test_data.json", 'w') as f:
            json.dump({"a": 1, "b": 2}, f)

        db = AlienDatabase()
        
        # Try to load from existing file if present
        existing_file_path = tmp_dir
def run_aliens():
    """Create a sample database to demonstrate persistence."""
    # Create an initial temporary directory for the test file
    tmp_dir = tempfile.mkdtemp()
    
    try:
        with open(f"src/test_data.json", 'w') as f:
            json.dump({"a": 1, "b": 2}, f)

        db = AlienDatabase()
        
        # Try to load from existing file if present
        existing_file_path = tmp_dir + ".aliens.db"
        try:
            with open(existing_file_path, 'r') as f:
                content_f.seek(0)
                data_list = json.load(content_f)

                db.data.update({i.get("key", "unknown"): i["value"] for key, value in data_list.items()})
        
        except FileNotFoundError:
            pass
    
    finally:
        # Clean up the test file after successful execution
        if os.path.exists(tmp_dir):
            try:
                with open(f"{tmp_dir}/test_data.json", 'w') as f:
                    json.dump({"a": 1, "b": 2}, f)
            except IOError:
                pass

    # Persist the database to disk or create a new temp file.
    db.save()
