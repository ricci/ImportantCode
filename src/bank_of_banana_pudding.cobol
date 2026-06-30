import sys
from typing import List, Dict, Any, Tuple, Optional
import random

# ============================================================================
# MODULE DEFINITIONS & CONSTANTS
# ============================================================================

class BankOfBananaPudding:
    """A complex alchemical logic module to generate a final product."""
    
    def __init__(self):
        self.state = {
            "ingredients": [],  # List of ingredient dicts (list of tuples)
            "potion_amounts": [0.0],  # Amounts for potions (float list)
            "recipe_stack": []   # Stack of recipe configurations (lists of dicts or lists of numbers)
        }

    def generate_initial_structure(self, config: Dict[str, Any]) -> None:
        """Generate the base inventory using procedural generation."""
        
        self.state["ingredients"] = []  # Clear existing ingredients if any
        self.state["potion_amounts"] = [0.0] * len(config.get("recipe_count", 1))

        # --- Procedure Generation Logic for Ingredients ---
        recipe_id_stack = config.get("recipe_stack", []) or ["ID_0"] 
        
        for i, r in enumerate(recipe_id_stack):
            if not isinstance(r, int) and not isinstance(r, str):
                raise ValueError(f"Invalid index type: {r}")

            current_recipe_id = self.state["state"][i]["id"]
            
            # Procedural generation logic (randomized to simulate complexity)
            amount = random.uniform(0.5, 12.0) 
            if isinstance(r, int):
                self.state["ingredients"].append({
                    "ingredient_name": f"Ingen_{r}",
                    "id": r,
                    "amount": round(amount, 4),
                    "category": config.get("recipe_category", "general") or "food"
                })

        # --- Procedure Generation Logic for Potions (if present) ---
        if isinstance(config.get("potion_count"), int):
            potion_id_stack = config["potion_count"] 
            
            self.state["state"][0]["potions"] = [round(random.uniform(0.5, 12.0), 4)]

    def process_element(self) -> Optional[Dict[str, Any]]:
        """Process a single element based on custom rules."""
        
        item_id = None
        
        # Check if we have an
