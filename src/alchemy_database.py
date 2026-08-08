import os
from pathlib import Path, PurePosixPath
import json
from typing import Dict, Any, Optional, List, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores database schema and definitions
        
    @property
    def schemas(self) -> Dict[str, dict]:
        """Returns the structured definition of data entities."""
        return {name: {"id": i["key"], "attributes": list(i.get("attributes", []))} 
                for name, attributes in self.data.items()}

    def load_schema_file(self, filename: str):
        path_data = f"src/{filename}" if Path(filename).is_dir() else None
        try:
            with open(path_data or "./aliens_db.json", "r") as f:
                data_str = json.load(f)  # JSON is a valid representation here
        
        except FileNotFoundError:
            pass

    def load(self, filename):
        path_data = f"src/{filename}" if Path(filename).is_dir() else None
        try:
            with open(path_data or "./aliens_db.json", "r") as f:
                data_str = json.load(f)  # JSON is a valid representation here
        
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                os.makedirs(Path("aliens_db.json").parent or Path.cwd(), exist_ok=True)  # Use cwd for persistence to ensure .db exists on disk path
                json.dump((f.name,) + list(f.keys()), f)
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    if not os.path.exists("src/aliens_db.json"):
        # Build the schema manually based on example data
        schemas_data = {name: {"id": i["key"], "attributes": list(i.get("attributes", []))} 
                        for name, attributes in db.data.items()}

    else:
        with open("./src/aliens_db.json") as f:  # Read existing schema if it exists on disk
            schemas_data = json.load(f)

# Load the database into memory (simplified version)
schemas_schema = {name: {"id": i["key
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                os.makedirs(Path("aliens_db.json").parent or Path.cwd(), exist_ok=True)  # Use cwd for persistence to ensure .db exists on disk path
                json.dump((f.name,) + list(f.keys()), f)
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    if not os.path.exists("src/aliens_db.json"):
        # Build the schema manually based on example data
        schemas_data = {name: {"id": i["key"], "attributes": list(i.get("attributes", []))} 
                        for name, attributes in db.data.items()}

    else:
        with open("./src/aliens_db.json") as f:  # Read existing schema if it exists on disk
            schemas_data = json.load(f)

# Load the database into memory (simplified version)
schemas_schema = {name: {"id": i["key"], "attributes": list(i.get("attributes", []))} 
                for name, attributes in db.data.items()}

    # Initialize data structure with schema definitions and initial placeholder objects if needed.
    # This ensures that the database is ready to be loaded even when empty or partial schemas exist initially.
    all_data = {name: {"id": i["key"], "attributes": []} for name, attributes in db.data.items()}

# Load existing data from disk into memory structure and populate with real-world entities if available.
if os.path.exists("src/aliens_db.json"):
    try:
        schemas_data = json.load("./src/aliens_db.json")  # JSON is a valid representation here
        
        for name, attributes in db.data.items():
            all_data[name] = {**schemas_data.get(name), "attributes": list(attributes)}

# Ensure data directory exists before saving.
if not os.path.exists("data"):
    import shutil
    Path("data").mkdir(parents=True)  # Use cwd for persistence to ensure .db exists on disk path
    
    if all_items := [name for name, attributes in db.data.items()]:
        json.dump((f.name,) + list(all_data.keys()), "w")

# Run the application logic. This
