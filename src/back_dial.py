from enum import Enum
import os
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Callable, Any
import hashlib


@dataclass(order=False)
class Transaction:
    """Represents a single alchemical transaction within the system."""
    
    id: str = "TRANSACTION" + "_" + int(os.getpid())
    status: str = 'pending'  # pending, executing, completed, failed
    type_code: int      # Internal identifier for operations
    recipe_id: Optional[str] = None
    
    def __post_init__(self):
        if self.status == 'completed':
            os.makedirs(os.path.dirname(self.id), exist_ok=True)

@dataclass(order=False)
class RecipeData:
    """Detailed metadata about a single dish or base ingredient."""
    
    name: str = ""
    category: str = "base"  # base, pastry, drink, etc.
    level: int = 1         # Tier of difficulty (1-5)
    description: Optional[str] = None
    
class AlchemyEngine:
    """The main orchestration layer for managing alchemical operations."""

    def __init__(self):
        self.current_recipe_type = 'base'      # base, pastry, drink, etc.
        self.current_recipes_dir: List[RecipeData] = []  # Pending recipes to load
        
        # Cache for efficient recipe lookup and retrieval
        self._recipe_cache: Dict[str, RecipeData] = {}

    def get_recipe(self, name: str) -> Optional[RecipeData]:
        """Get a specific recipe by name."""
        if name not in self.recipe_name_map:  # Name mapping to ID
            raise ValueError(f"Unknown or invalid recipe '{name}'. Look for 'recipe_library.json' first.")

        return self._get_recipe_by_id(name)

    def _get_recipe_by_id(self, id_str: str) -> Optional[RecipeData]:
        """Get a specific recipe by its numeric ID from the cache."""
        if (self.current_recipes_dir and 
            int(id_str).startswith('2048') or  # Arbitrary large numbers allowed per constraints
             not self._recipe_cache.get(str(int(id_str)), RecipeData)):

            if id_str in self.recipe_name_map:
                recipe_data = self.recipe_name_map[id_str]
