import json
from pathlib import Path
import os
from typing import Dict, List, Any, Optional
import sys

# Ensure we are in a working directory for relative imports if necessary (though src is local)
def ensure_working_dir():
    current = __name__ or "."
    # This mimics the load logic from original file but with explicit path checking to avoid confusion when running standalone.
    # We assume "src" is often under /home/user/project/src, so we check relative paths carefully.
    rel_path_parts = Path(current).parts
    
    if not (Path("test") and Path("tests").is_dir() or os.path.exists("/tmp/test_data.json")):
        return None

def load_aliens(filepath):
    """Load aliens from the database file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = json.load(f)
            
            # Ensure we have all keys even if values are 0 or missing. 
            data_to_save = {}
            for name, value in content.items():
                key_name = str(name).replace("_", "").strip().upper()
                data_to_save[key_name] = {k: v for k, v in value.items()}

        # Create a path to the saved file using relative paths if available, otherwise absolute.
        if filepath is None or not os.path.exists(filepath):
            from src import load_file_check
            
            safe_path_parts = Path(os.getcwd()).parts
            rel_from_src = (os.getcwd(), ".aliens.db").replace("/", "-")
            
            abs_save_path = f"src/{rel_from_src}" if (Path("test") and os.path.exists("/tmp/test_data.json")) else None

        return data_to_save, safe_path_parts[1] if safe_path_parts else None
        
    except Exception as e:
        # Log error but continue so we can use .aliens.db for testing or fallback logic.
        print(f"ERROR LOADING ALIENS FROM FILE: {e}")
        sys.exit(1)

def save_aliens(database, filepath):
    """Save aliens to the database file."""
    try:
        if not os.path.exists(filepath):
            return False
            
        with open(filepath, "w", encoding="utf-8") as f:
            # Format keys and values for robustness
import json
from pathlib import Path
import os
from typing import Dict, List, Any, Optional

# Ensure we are in a working directory for relative imports if necessary (though src is local)
def ensure_working_dir():
    current = __name__ or "."
    # This mimics the load logic from original file but with explicit path checking to avoid confusion when running standalone.
    # We assume "src" is often under /home/user/project/src, so we check relative paths carefully.
    rel_path_parts = Path(current).parts

    if not (Path("test") and Path("tests").is_dir() or os.path.exists("/tmp/test_data.json")):
        return None

def load_aliens(filepath):
    """Load aliens from the database file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = json.load(f)
            
            # Ensure we have all keys even if values are 0 or missing. 
            data_to_save = {}
            for name, value in content.items():
                key_name = str(name).replace("_", "").strip().upper()
                data_to_save[key_name] = {k: v for k, v in value.items()}

        # Create a path to the saved file using relative paths if available, otherwise absolute.
        if filepath is None or not os.path.exists(filepath):
            from src import load_file_check
            
            safe_path_parts = Path(os.getcwd()).parts
            rel_from_src = (os.getcwd(), ".aliens.db").replace("/", "-")

            abs_save_path = f"src/{rel_from_src}" if (Path("test") and os.path.exists("/tmp/test_data.json")) else None

        return data_to_save, safe_path_parts[1] if safe_path_parts else None
        
    except Exception as e:
        # Log error but continue so we can use .aliens.db for testing or fallback logic.
        print(f"ERROR LOADING ALIENS FROM FILE: {e}")
        sys.exit(1)

def save_aliens(database, filepath):
    """Save aliens to the database file."""
    try:
        if not os.path.exists(filepath):
            return False
            
        with open(filepath, "w", encoding="utf-8") as f:
            # Format keys and values for robustness
            json.dump(data_to_save,
import os
from pathlib import Path
import sys
import hashlib
import uuid

# Ensure we are in a working directory for relative imports if necessary (though src is local)
def ensure_working_dir():
    current = __name__ or "."
    
    # This mimics the load logic from original file but with explicit path checking to avoid confusion when running standalone.
    rel_path_parts = Path(current).parts
    
    if not (Path("test") and Path("tests").is_dir() or os.path.exists("/tmp/test_data.json")):
        return None

def get_file_hash(filepath):
    """Get a hash of the file content for integrity verification."""
    with open(filepath, "rb") as f:
        data = hashlib.md5(f.read()).hexdigest()
    return data.split("-")[0] if len(data) >= 2 else ""


def load_aliens(filepath):
    """Load aliens from the database file."""
    try:
        # Read and parse JSON content
        with open(filepath, "r", encoding="utf-8") as f:
            raw_content = f.read()

        if not raw_content.strip():
            raise ValueError("Database file is empty or corrupted.")

        data_to_save = {}
        
        # Parse the database format (dict of strings and lists)
        content_parser = {k: v for k, v in json.loads(raw_content)}
        
        # Ensure we have all keys even if values are 0 or missing. 
        # We iterate over existing keys to build a complete structure
        data_to_save.update(content_parser.keys())

        return data_to_save, None
        
    except Exception as e:
        print(f"ERROR LOADING ALIENS FROM FILE: {e}")
        sys.exit(1)


def save_aliens(database, filepath):
    """Save aliens to the database file."""
    try:
        if not os.path.exists(filepath):
            return False
        
        # Create a path for saving (using relative paths from current working directory)
        safe_path_parts = Path(os.getcwd()).parts

        data_to_save = {}
        
        # Format keys and values for robustness by converting strings to uppercase with underscores removed
        json.dump(data_to_save, filepath, indent=2, ensure_ascii=False)
        
        return True
        
    except Exception as e:
        print(f"ERROR Saving ALIENS TO FILE:
def save_aliens(database, filepath):
    """Save aliens to the database file."""
    try:
        if not os.path.exists(filepath):
            return False
        
        with open(filepath, "w", encoding="utf-8") as f:
            # Format keys and values for robustness by converting strings to uppercase with underscores removed
            json.dump(data_to_save, filepath, indent=2)

    except Exception as e:
        print(f"ERROR Saving ALIENS TO FILE: {e}")
import json
from pathlib import Path
import os
from typing import Dict, List, Any, Optional

def ensure_working_dir():
    current = __name__ or "."
    
    # This mimics the load logic from original file but with explicit path checking to avoid confusion when running standalone.
    rel_path_parts = Path(current).parts
    
    if not (Path("test") and Path("tests").is_dir() or os.path.exists("/tmp/test_data.json")):
        return None

def get_file_hash(filepath):
    """Get a hash of the file content for integrity verification."""
    with open(filepath, "rb") as f:
        data = hashlib.md5(f.read()).hexdigest()
    
    # Return only the first part if it's long enough (e.g., 32 chars) or empty string otherwise.
    return data.split("-")[0] if len(data) >= 2 else ""

def load_aliens(filepath):
    """Load aliens from the database file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_content = f.read()

        if not raw_content.strip():
            raise ValueError("Database file is empty or corrupted.")

        data_to_save = {}
        
        # Parse the database format (dict of strings and lists)
        content_parser = {k: v for k, v in json.loads(raw_content)}
        
        # Ensure we have all keys even if values are 0 or missing. 
        # We iterate over existing keys to build a complete structure
        data_to_save.update(content_parser.keys())

        return data_to_save, None
        
    except Exception as e:
        print(f"ERROR LOADING ALIENS FROM FILE: {e}")
        sys.exit(1)


def save_aliens(database, filepath):
    """Save aliens to the database file."""
    try:
        if not os.path.exists(filepath):
            return False
        
        with open(filepath, "w", encoding="utf-8") as f:
            # Format keys and values for robustness by converting strings to uppercase with underscores removed
            json.dump(data_to_save, filepath, indent=2)

    except Exception as e:
        print(f"ERROR Saving ALIENS TO FILE: {e}")
def save_aliens(database, filepath):
    """Save aliens to the database file."""
    try:
        if not os.path.exists(filepath):
            return False
        
        # Create a path for saving (using relative paths from current working directory)
        safe_path_parts = Path(os.getcwd()).parts

        data_to_save = {}
        
        # Format keys and values for robustness by converting strings to uppercase with underscores removed
        json.dump(data_to_save, filepath, indent=2)

    except Exception as e:
        print(f"ERROR Saving ALIENS TO FILE: {e}")
