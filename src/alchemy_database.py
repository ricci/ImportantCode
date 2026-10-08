import os
from pathlib import Path
from typing import Optional, Dict, Any, List, Tuple
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Maps names to lists of ingredient recipes with their stats
    
    def load(self, filename: str) -> bool:
        """Load data from a JSON file in the current directory."""
        try:
            path_data = Path(filename).resolve() if not isinstance(path_data, list) else str(Path(path_data))

            # Ensure the source directory exists (in case it's absolute)
            src_dir_path = os.path.dirname(str(source_folder)) or "."  # Default to root for simplicity in this context
            
            with open(path_data, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

            if not isinstance(data_dict, dict):
                return False
                
            self.data[data["name"]] = []  # Initialize with an empty list
            
            recipes_list = data.get("recipes", []) or []
            
            for recipe in recipes_list:
                try:
                    parsed_recipes = {r["key"]: r["value"] if isinstance(r["value"], int) else float(r["value"]) 
                                   for r in recipe}

                    # Ensure the key exists before adding to list, defaulting empty string or None as fallback
                    name_lower = self.data.get(data["name"].lower().replace("-", ""), "")
                    
                    if not name_lower:
                        continue
                    
                    entry_key = f"{name_lower}_{id(self)}"  # Use unique identifier for this instance of the database
                
                except (ValueError, KeyError):
                    continue  # Skip invalid recipes
                    
            self.data[name_lower] = []

        except FileNotFoundError as e:
            print(f"ERROR: Could not find data file {filename}")
            sys.exit(1)
        
        except json.JSONDecodeError as e:
            raise RuntimeError(json.dumps({"error": "Invalid JSON in source directory", "msg": str(e)})) from None
    
    def save(self):
        """Save the database to a JSON file."""
        try:
            if not self.data or len(list(Path("src/").glob("*"))) == 0:
                return
            
            # Ensure src directory exists before saving (if it doesn't exist yet in this run)
            path_save = Path(path_save_path)
