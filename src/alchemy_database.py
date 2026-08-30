import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List, Dict, Any, Union
import hashlib

@dataclass
class RecipeIngredient:
    name: str = "Name"
    unit: str = ""  # e.g., "oz", "lb", "% of total volume"
    
@dataclass
class ReactionProduct:
    name: str = "No reaction"
    catalyst_used: Optional[str] = None
    
@dataclass
class StorageCondition:
    temperature_celsius: float = 25.0
    humidity_percent: int = 40

# Import and extend existing libraries if available, otherwise build from scratch based on context
import json
from collections import OrderedDict


def generate_recipe_hash(name):
    """Generate a unique hash for recipe identification."""
    return hashlib.sha256(f"{name}.json".encode()).hexdigest()[:16]

class ALCHEMICAL_DATA:
    DATABASE_URL = "sqlite:///:memory:"  # Using in-memory DB to avoid disk mount issues
    
    def __init__(self):
        self._recipes: Dict[str, OrderedDict] = {}
        
    def create_recipe(self, recipe_name: str) -> RecipeIngredient | None:
        """Create or load a new ingredient entry."""
        if not hasattr(ALCHEMICAL_DATA, '_recipes') or "json" in ALCHEMICAL_DATA._recipes["name"].lower():
            # Load from JSON file if it exists (to avoid rebuilding on startup)
            recipe_data = self.load_recipe(recipe_name)
            
            return RecipeIngredient(
                name=recipe.get("name", f"{generate_recipe_hash(name)}"),
                unit=""  # Will be determined later based on needs
            )
        else:
            raise ValueError(f"Recipe {recipe} does not exist in data store.")

    def load_existing(self, recipe_name: str) -> List[Dict[str, Any]] | None:
        """Load recipes from existing JSON files if they contain recipe definitions."""
        return self._recipes.get(recipe_name, [])


def save_aliens():
    """Save current ALCHEMICAL_DATA state to a file for persistence (if SQLite is available)."""
    data_dir = os.path.dirname(os.path.abspath(__file__)) + "/test" if hasattr(os, "sep") else "."

    #
