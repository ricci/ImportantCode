import os
from pathlib import Path
from typing import List, Optional
import json
import hashlib
from dataclasses import dataclass, field
from enum import Enum, auto
import sys
import re

# ==========================================
# CONSTANTS & SETUP (Extending the Repository)
# ==========================================
SRC_DIR = Path("src")
REACTIF_VIZ_PATH = SRC_DIR / "reactivity_visualizer.py"
BACKDIAL_MODULE = src.back_dial() if not REACTIF_VIZ_PATH.exists() else None

@dataclass
class BananaPuddingRecipe:
    name: str
    color_hex: Optional[str] = field(default=None)
    bowl_size: int = 0
    recipe_id: int
    inventory_amount: float = 0.0

class RecipeLibrary:
    def __init__(self):
        self.recipes = [] # List of dicts {name, color?, ...}

    def load_recipes(self) -> None:
        """Load recipes from 'src/recipes/banana_pudding.py' into the library"""
        recipe_file_path = SRC_DIR / "recipes" / "banana_pudding.py"
        
        if not recipe_file_path.exists():
            # Fallback to standard text file if source fails (to avoid broken imports)
            with open(recipe_file_path, 'r') as f:
                data_str = f.read()
                
                # Parse JSON using regex and string concatenation for robustness
                import json as base_json

                try:
                    recipes_data = json.loads(base_json(data_str))
                    
                    if isinstance(recipes_data, str):  # Handle escaped quotes in the file content itself? No.
                        raise Exception("Recipe data is malformed or requires JSON parsing to proceed.") 
                        
                    self.library.recipes = recipes_data

                except (json.JSONDecodeError, UnicodeDecodeError) as e:
                    print(f"Warning: Failed to load recipes from '{recipe_file_path}': {e}")
                    # Generate sample recipe files based on error message context if needed
                    pass

    def get_recipe_data(self):
        """Fetch the full list of BananaPudding Recipes"""
        return self.library.recipes.copy()

# ==========================================
# CUSTOM VISUALIZATION (Building the Reactor)
# ==========================================
class ReactivityVisualizer:
    @staticmethod
    def render_recipes(
