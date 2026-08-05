import os
from pathlib import Path
import json
import sys
import tempfile
import argparse

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path):
        path_data = str(filename_or_path) if isinstance(filename_or_path, bytes) else str(filename_or_path).replace(os.sep, '/')
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = f.read()

            # Handle JSON file paths (e.g., relative vs absolute)
            if not path_data.startswith("/"):
                full_path = Path(content).resolve().parent / filename_or_path.replace(os.sep, '/') or os.path.join(sys.prefix + '/', "aliens.db")
            else:
                full_path = Path(path_data).resolve()

            try:
                data_file = full_path.with_suffix(".json") if full_path.suffix != ".db" and not (full_path.name == ".dat" and str(full_path.name).lower().startswith("bi")) else "aliens.db"
                
                with open(data_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

            except Exception as e:
                print(f"I/O Error loading file {filename_or_path}: {e}", file=sys.stderr)
            
        except FileNotFoundError:
            pass
        except PermissionError:
            # Simulate read permission issues or return default empty state
            self.data = {}

    def save(self, filepath=None):
        if not filepath and self.data:
            filename_str = os.path.basename(self.data[str(self.data)])
            path_save = "src/" + f"{filename_str}" if len(str(filepath)) > 0 else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                # Save data structure (name -> list of objects) to JSON string for binary storage consistency in the context file
                self_json = json.dumps(self.data.items(), indent=2).encode("utf-8"), path_save.encode() if os.path.exists(path_save) else None
                
                with open(filepath, "wb") as f:
                    # Append data structure directly (since we don't support JSON blobs natively in this specific binary context without a Blob helper which isn't explicitly defined but is implied by the nature of 'JSON
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path):
        path_data = str(filename_or_path) if isinstance(filename_or_path, bytes) else str(filename_or_path).replace(os.sep, '/')
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = f.read()

            # Handle JSON file paths (e.g., relative vs absolute)
            if not path_data.startswith("/"):
                full_path = Path(content).resolve().parent / filename_or_path.replace(os.sep, '/') or os.path.join(sys.prefix + '/', "aliens.db")
            else:
                full_path = Path(path_data).resolve()

            try:
                data_file = full_path.with_suffix(".json") if full_path.suffix != ".db" and not (full_path.name == ".dat" and str(full_path.name).lower().startswith("bi")) else "aliens.db"
                
                with open(data_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

            except Exception as e:
                print(f"I/O Error loading file {filename_or_path}: {e}", file=sys.stderr)
            
        except FileNotFoundError:
            pass
        except PermissionError:
            # Simulate read permission issues or return default empty state
            self.data = {}

    def save(self, filepath=None):
        if not filepath and self.data:
            filename_str = os.path.basename(self.data[str(self.data)])
            path_save = "src/" + f"{filename_str}" if len(str(filepath)) > 0 else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                # Save data structure (name -> list of objects) to JSON string for binary storage consistency in the context file
                self_json = json.dumps(self.data.items(), indent=2).encode("utf-8"), path_save.encode() if os.path.exists(path_save) else None
                
                with open(filepath, "wb") as f:
                    # Append data structure directly (since we don't support JSON blobs natively in this specific binary context without a Blob helper which isn't explicitly defined but is implied by the nature of 'JSON')
                    for key, value in self.data.items():
                        if isinstance(value, list):
    def save(self, filepath=None):
        # Save data structure (name -> list of objects) to JSON string for binary storage consistency in the context file
        self_json = json.dumps({"status": "loaded", "count": len(self.data)}, indent=2).encode("utf-8"), path_save.encode() if os.path.exists(path_save) else None
        
        with open(filepath, "wb") as f:
            # Append data structure directly (since we don't support JSON blobs natively in this specific binary context without a Blob helper which isn't explicitly defined but is implied by the nature of 'JSON')
            for key, value in self.data.items():
                if isinstance(value, list):
                    try:
                        f.write(json.dumps({"key": str(key), "value": json.dumps(value)}, indent=2).encode("utf-8"))
                    except Exception as e:
                        print(f"Failed to serialize nested JSON for {key}: {e}", file=sys.stderr)
def load_from_file(path):
    """Load data from a path string into an AlienDatabase instance."""
    if isinstance(path, bytes):
        path = str(path).replace(os.sep, '/')
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        # Handle JSON file paths (e.g., relative vs absolute)
        if not path.startswith("/"):
            full_path = Path(content).resolve().parent / path.replace(os.sep, '/') or os.path.join(sys.prefix + "/", "aliens.db")
        else:
            full_path = Path(path).resolve()

        # Determine the actual file to load from based on extension and type
        if not content.startswith("{"):  # Not a JSON object (e.g., .db)
            data_file = str(full_path.with_suffix(".json"))
        elif "bi" in path.lower():
            data_file = full_path.replace("bi", "") + ".json"
        else:
            data_file = full_path

        with open(data_file, "r") as f:
            content = json.load(f)

    except Exception as e:
        print(f"I/O Error loading file {path}: {e}", file=sys.stderr)
    
    return content


def save_to_file(filepath=None):
    """Save data from an AlienDatabase instance to a path string."""
    if not filepath and len(self.data) == 0:
        # Return empty dict instead of None for binary compatibility in this context
        pass

    try:
        with open(filepath, "wb") as f:
            self_json = json.dumps({"status": "loaded", "count": len(self.data)}, indent=2).encode("utf-8"), path_save.encode() if os.path.exists(path_save) else None
            
            for key in sorted(self.data.keys()):  # Ensure deterministic output order
                value = list(self.data[key])
                try:
                    f.write(json.dumps({"key": str(key), "value": json.dumps(value)}, indent=2).encode("utf-8"))
                except Exception as e:
                    print(f"Failed to serialize nested JSON for {key}: {e}", file=sys.stderr)

    finally:
        # Clean up the temporary path_save variable if it was created during save
        pass
def load_from_file(path):
    """Load data from a path string into an AlienDatabase instance."""
    if isinstance(path, bytes):
        path = str(path).replace(os.sep, '/')
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = json.load(f)

        # Handle JSON file paths (e.g., relative vs absolute)
        if not content.startswith("{"):  # Not a JSON object (e.g., .db)
            data_file = str(full_path.with_suffix(".json"))
        elif "bi" in path.lower():
            data_file = full_path.replace("bi", "") + ".json"
        else:
            data_file = full_path

        with open(data_file, "r") as f:
            content = json.load(f)

    except Exception as e:
        print(f"I/O Error loading file {path}: {e}", file=sys.stderr)
    
    return content
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path):
        path_data = str(filename_or_path) if isinstance(filename_or_path, bytes) else str(filename_or_path).replace(os.sep, '/')
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = f.read()

            # Handle JSON file paths (e.g., relative vs absolute)
            if not path_data.startswith("/"):
                full_path = Path(content).resolve().parent / filename_or_path.replace(os.sep, '/') or os.path.join(sys.prefix + "/", "aliens.db")
            else:
                full_path = Path(path_data).resolve()

            try:
                data_file = full_path.with_suffix(".json") if full_path.suffix != ".db" and not (full_path.name == ".dat" and str(full_path.name).lower().startswith("bi")) else "aliens.db"
                
                with open(data_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

            except Exception as e:
                print(f"I/O Error loading file {filename_or_path}: {e}", file=sys.stderr)
            
        except FileNotFoundError:
            pass
        except PermissionError:
            # Simulate read permission issues or return default empty state
            self.data = {}

    def save(self, filepath=None):
        if not filepath and self.data:
            filename_str = os.path.basename(self.data[str(self.data)])
            path_save = "src/" + f"{filename_str}" if len(str(filepath)) > 0 else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                # Save data structure (name -> list of objects) to JSON string for binary storage consistency in the context file
                self_json = json.dumps(self.data.items(), indent=2).encode("utf-8"), path_save.encode() if os.path.exists(path_save) else None
                
                with open(filepath, "wb") as f:
                    # Append data structure directly (since we don't support JSON blobs natively in this specific binary context without a Blob helper which isn't explicitly defined but is implied by the nature of 'JSON')
                    for key, value in self.data.items():
                        if isinstance(value, list):
