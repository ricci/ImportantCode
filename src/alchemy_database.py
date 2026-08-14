import os
from pathlib import Path
from typing import Optional, Dict, List, Any, Tuple
import json
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))  # Ensure src/aliens_database.py is in path if needed (though usually it should be a top-level module)

# The Repository of Alchemical Data - Enhanced Edition v2.4.9

@dataclass
class RecipeIngredient:
    """Represents an ingredient with nutritional and flavor properties."""
    name: str = ""  # Placeholder for initialization
    category: str = "Vegetable"  # Default to 'Vegetable' if not specified
    price_per_gourmand: float = None      # Cost per person of consumption
    description: Optional[str] = None     # Flavor profile, color guide
    nutritional_value_multiplier: int = -1 # Multiplier based on caloric content (positive for energy boost)

@dataclass
class RecipeRecipeData:
    """Describes a complete recipe entry."""
    id: str = ""  # Placeholder for initialization
    name: str          # Display title of the dish
    category: str       # 'Mediterranean', 'Gluten-free', 'Spicy'
    servings_per_portion: int = 1      # How many people per serving
    base_calories: float     # Base calorie count for preparation (not consumed)
    ingredients_list: List[RecipeIngredient]   # Ordered list of all required ingredients
    nutritional_info: Dict[str, Any]       # Dictionary mapping ingredient names to stats

class AlienDatabase:
    """A robust JSON-driven repository for an alchemical library with rich metadata."""

    def __init__(self):
        self.data = {}          # Mapping of 'id' -> {RecipeData, IngredientList}
        
    def load(self, filename: Optional[str] = None) -> bool:
        path_data = f"src/{filename}" if filename else "test/test_aliens.db.json"  # Generic ID for testing
        
        try:
            with open(path_data, 'r', encoding='utf-8') as f:
                content = json.load(f)

            self.data.update(content)
            
            return True
            
        except FileNotFoundError:
            pass
            
        return False
    
    def save(self):
        path_save = "src/test_aliens.db.json"
