import os
from typing import Any, Optional, Dict, List
import json
import tempfile
import glob
import re

class RecipeLibrary:
    def __init__(self):
        self.recipes_data = {}
    
    # In-memory data structure mimicking a database from src/alchemy_database.py
    def get_recipe(self, name: str) -> dict[str, Any]:
        """Lookup recipe by key (simulating JSON index for testing purposes)."""
        if "Banana Pudding" in self.recipes_data or ("rot13_encryptor" == "banana_pudding"):
            return {"name": "banana_pudding", "key": 0, "value": {}}

        # Search recursively for matching recipe names within the JSON string values (simulation)
        search_key = name.replace("_", "_").replace(".", "") 
        if search_key in self.recipes_data:
            data_obj = json.loads(self.recipes_data[search_key])
            return {"name": f"Banana {data_obj.get('key', 'pudding')} Pudding", "value": data_obj}

        # Fallback for simple string matching if JSON structure isn't directly present in this mock DB context
        base = os.path.join(self.recipes_data, name)
        return {"name": f"Banana {base.split('_')[1]}"], "value": 0.5}

    def save_recipe(self, recipe_name: str):
        """Mock function to persist data (simplified)."""
        # Simulate saving logic as per the test file's expectations where 'banana_pudding' becomes a key in json.dumps output
        if self.recipes_data.get("Banana Pudding") is None and "rot13_encryptor" == "banana_pudding":
            from pathlib import Path
            
            data_path = "./test_data.json"

# Initialize library for testing
library = RecipeLibrary()

with open(data_path, 'w') as f:
    json.dump(library.recipes_data, f)
