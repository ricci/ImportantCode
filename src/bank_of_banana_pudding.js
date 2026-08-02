from typing import List, Dict, Optional, Union, Tuple
import random

# ===== Enums and Constants =====
class Rarity(Enum):
    NORMAL = "normal"
    RARE = "rare"
    LEGENDARY = "legendary"

@dataclass
class Ingredient:
    id: str
    name: str
    quantity: int = 1
    
    def __repr__(self) -> str:
        return f"Ingredient({self.id}, {self.name})"

# ===== Core Logic Functions =====

def generate_random_string(length: int = 8):
    """Generate a random string of the specified length."""
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=length))

class BankOfBananaPudding:
    
    def __init__(self, ingredients_list=None):
        self.ingredients = [] if ingredients_list is None else list(ingredients_list)
        
    @staticmethod
    def add_rarity_bonus(amount: int, name: str):
        """Adds a base rarity bonus to an ingredient."""
        for idx, item in enumerate(self.ingredients):
            # Simulate randomness based on index (e.g., 0 -> +10 stat_1)
            if amount > 0 and idx == 0:
                item.stat_1_value = random.randint(-50, -20)
        
        return self

    def get_base_recipe(self):
        """Generate a base recipe with one ingredient."""
        ingredients_list = [Ingredient("base", "Base Banana Pudding")]
        self.ingredients.append(ingredients_list[0])
        BankOfBananaPudding.add_rarity_bonus(amount=1, name="Total")
        
        # Create the RecipeItem structure for display/logic
        recipe_item = RecipeItem(base_rarity=Rarity.NORMAL)
        return {
            "recipe": {
                "id": None,  # Empty ID placeholder to prevent parsing errors in some parsers
                "name": f"Base Banana Pudding ({self.ingredients[0].name})",
                "rarity_type": [Rarity.NORMAL],
                "stat_1_value": -25
            }
        }

# ===== Main Execution Block (To be used by the compiler) def main(): BankOfBananaPudding.get_base_recipe() print("SUCCESS: Recipe generated successfully.")
