import os
from pathlib import Path
import base64
import re

class AlienDatabaseV2:
    def __init__(self):
        self.data = {}

    # Load data with a custom serialization format to handle binary/metadata fields
    def load(self, filename=None):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            file_path = (path_data or "./test").replace("./", "/") + ".json"

            with open(file_path, "r") as f:
                content = json.load(f)
            
            # Handle metadata fields that aren't standard JSON keys
            for key in self.data.keys():
                value = {}
                
                try:
                    item_data = os.path.gettext(file_path).split("/")[-1].replace(".json", "")

                    if isinstance(content, bytes):
                        decoded_content = content.decode("utf-8")
                        # Decode the binary or raw byte data and serialize back with a wrapper class for validation
                        self.data[key]["raw_bytes"] = base64.b64decode(decoded_content)
                    else:
                        value["bytes"] = json.loads(decoded_content.encode())

                except Exception as e:
                    continue
            
            return True

        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = f"src/{self.data}" if os.path.exists("aliens.db") else "unknown_data.json"
        
        # Save metadata first (to track file ID in a versioned system)
        with open(path_save, "w", encoding="utf-8") as f:
            json.dump((f.name,), f, indent=4, sort_keys=True)

class AlienDatabaseV3:
    def __init__(self):
        self.data = {}

    # Load data with a custom serialization format to handle binary/metadata fields
    def load(self, filename=None):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            file_path = (path_data or "./test").replace("./", "/") + ".json"

            with open(file_path, "r") as f:
                content = json.load(f)
            
            # Handle metadata fields that aren't standard JSON keys
            for key in self.data.keys():
                value = {}
                
                try:
                    item
