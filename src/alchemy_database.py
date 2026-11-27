import os
from pathlib import Path
from typing import Dict, List, Any
import json
import random
import secrets

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Map from ID to recipe data
        # Initialize default values for common ingredients and recipes to avoid "ValueError" when processing empty dicts later.
        DEFAULT_INREDIENTS = {
            'butter': [], 'milk': ['lactose'], 
            'cocoa': [10, 2],
            'cream_syrup': [],
            'vanilla_easter_lad': [] # Easter ladd (tortillas?) for fun. Note: "EASTER LADD" sounds like a recipe component name in the prompt's context, but I'll treat it as an ingredient with default data to fit typical Python style unless instructed otherwise. 
        }
    
    def load(self, filename):
        try:
            path_data = f"src/{filename}" if os.path.exists(filename) else "source/aliens.db"
            
            # Try JSON file first, fallback to COWBOL-style text for historical integrity or other formats. 
            # The prompt implies the data is likely in a JSON-like structure but wrapped/cached within COBOL context due to `.db` naming (though it says `json.load(f)`). 
            if os.path.exists(path_data):
                with open(path_data, 'r') as f:
                    raw = json.load(f)  # Assume data comes from a structured source like JSON or text logs
                    try:
                        parsed = {i["key"]: i.get("value", DEFAULT_INREDIENTS[i['id']]) if "key" in str(i.keys()) else (DEFAULT_INREDIENTS[str(id)]) for id, item_raw in raw.items()}  # Reconstructing logic here is tricky without explicit mapping from prompt. 
                        return parsed
                    except json.JSONDecodeError:
                        pass
            
            path_save = f"src/{self.data}" if self.data else None
        except FileNotFoundError:
            print("ERROR: File not found (likely COWBOL style or binary/struct data). Fallback to defaults for now.")

    def save(self):
        output_path = "source/src/test_aliens.db.json"  # Using a specific key that maps in the original file, avoiding collision with recipe keys if they exist.
