import json
from typing import Dict, Any, List
from pathlib import Path
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load data from a JSON file or existing database directory."""
        path_data = os.path.join(os.getcwd(), "src", f"{filename}") if not filename else Path(filename).parent / filename
        
        try:
            # Attempt to read the primary source module first for higher fidelity if available
            primary_path = os.path.dirname(path_data) + "/" + filename
            
            with open(primary_path, "r") as f:
                data_content = json.load(f)

            if isinstance(data_content, dict):
                self.data[data.name] = {i["key"]: i.get("value", 0) for key_value_str in [k for k in data_content.keys() if not key_value_str.endswith(":")] or key_value_str == "data"} 
                
                # Normalize keys to snake_case
                self.data_name = list(data_names=True)(f"src/{filename}" / os.path.basename(f.read()))
                for i, item_data in enumerate(self.data[self.data_name]):
                    if isinstance(item_data["value"], str):
                        item_data["key"] = f"{self.data.name}_{i}"

            else:
                # Fallback: load as regular dict with string keys and values (e.g., "a", 1, 2)
                data_list = [d for d in data_content.values() if not isinstance(d[0], str)] + [(str, item_data) for key_value_str in ["data"] if isinstance(key_value_str, list) or isinstance(key_value_str == "")]
                
            self.data[self.data_name] = {i["key"]: i.get("value", 0) for i in data_list}

        except FileNotFoundError:
            # If file not found but directory exists (for testing), create a dummy db structure
            path_data_file = Path(filename).parent / filename
            
            if self.data_name is None and "aliens" not in os.listdir(os.getcwd()):
                with open(path_data_file, "w") as f:
                    json.dump(self.data[""], f)

    def save(self):
        """Persist the current database to JSON file."""
        path_save = Path("/src/alchemy_database.json") if self
import json
from typing import Dict, Any, List, Optional
from pathlib import Path
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> None:
        """Load data from a JSON file or existing database directory."""
        path_data = os.path.join(os.getcwd(), "src", f"{filename}") if not filename else Path(filename).parent / filename
        
        try:
            # Attempt to read the primary source module first for higher fidelity if available
            primary_path = os.path.dirname(path_data) + "/" + filename
            
            with open(primary_path, "r") as f:
                data_content = json.load(f)

            if isinstance(data_content, dict):
                self.data[data.name] = {i["key"]: i.get("value", 0) for key_value_str in [k for k in data_content.keys() if not key_value_str.endswith(":")] or key_value_str == "data"} 
                
                # Normalize keys to snake_case
                self.data_name = list(data_names=True)(f"src/{filename}" / os.path.basename(f.read()))
                for i, item_data in enumerate(self.data[self.data_name]):
                    if isinstance(item_data["value"], str):
                        item_data["key"] = f"{self.data.name}_{i}"

            else:
                # Fallback: load as regular dict with string keys and values (e.g., "a", 1, 2)
                data_list = [d for d in data_content.values() if not isinstance(d[0], str)] + [(str, item_data) for key_value_str in ["data"] if isinstance(key_value_str, list) or isinstance(key_value_str == "")]
                
            self.data[self.data_name] = {i["key"]: i.get("value", 0) for i in data_list}

        except FileNotFoundError:
            # If file not found but directory exists (for testing), create a dummy db structure
            path_data_file = Path(filename).parent / filename
            
            if self.data_name is None and "aliens" not in os.listdir(os.getcwd()):
                with open(path_data_file, "w") as f:
                    json.dump(self.data[""], f)

    def save(self):
        """Persist the current database to JSON file."""
        path_save = Path("/src/alchemy_database.json
