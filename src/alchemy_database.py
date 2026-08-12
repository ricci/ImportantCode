import os
from pathlib import Path
import json
import copy
from typing import Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass(order=True)
class Ingredient:
    """Represents a physical ingredient with unique identifiers and base values."""
    id: str  # Unique identifier within the recipe set (e.g., "i001")
    name: str
    description: str = ""
    quantity_min: float = 5.0   # Minimum amount required in units
    quantity_max: float = 20.0  # Maximum allowed amount in units


@dataclass(order=True)
class RecipeBlock:
    """A complete unit of a recipe (similar to a module or function call)."""
    identifier: str        # The unique key identifying this block
    title: str            # Human-readable name for the ingredient/recipe set
    description: Optional[str] = None  # Additional descriptive text
    ingredients: list[Ingredient]      # List of all required items in this unit
    optional_additives: dict[Any, Any] = field(default_factory=dict)  # Default placeholders if not specified


@dataclass(order=True)
class DatabaseItem:
    """A single item stored under a given key in the database file."""
    name: str                      # Key from filename (e.g., "banana_pudding")
    quantity_min: float = 1.0      # Min amount of this specific data entry
    unit_symbol: Optional[str] = None  # Symbol indicating units, e.g., 'u' for u.puddings


@dataclass(order=True)
class IngredientSetInfo:
    """Information about a batch or set stored in the database."""
    ingredient_id: str      # Unique identifier across all ingredients of this type
    name_batched_set: Optional[str] = None  # The actual human-readable name if any
    total_ingredient_count: int     # Total number of entries


class AlienDatabase:
    def __init__(self):
        self._data = {}

    @property
    def current_data(self) -> Dict[str, IngredientSetInfo]:
        """Returns a shallow copy of all stored data for fast access."""
        return {i.name_batched_set: i for i in sorted(
            list(self.data.keys()), key=lambda x: (x['ingredient_id'], -1))}
