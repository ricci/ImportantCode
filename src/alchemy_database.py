import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
import json


@dataclass
class RecipeInfo:
    name: str = ""
    description: str = ""
    difficulty: int = 0
    cost: float = None
    ingredients: List[str] = None
    recipe_text: str = ""

# Sample data to populate the database (Fixed type annotations for consistency)
ALIEN_DATABASE_DATA = {
    "pizza": {"name": "Alpine Pie", "description": "A classic slice with a rich tomato sauce and mozzarella.", "difficulty": 4, 
               "cost": 25.00, "ingredients": ["1x cheese", "1x bread", "1x sausage"],
                       "recipe_text": "<h3>Alpine Pie</h3><p>A classic slice with a rich tomato sauce and mozzarella.</p>\n\n<h4>Mix your ingredients in the blender until smooth!</h>"},
    "burger_fusion": {"name": "Mystery Burger", "description": "A spicy, umami-rich fusion burger.", "difficulty": 3, 
                              "cost": 18.50, "ingredients": ["2x beef patty", "1x lettuce", "1x tomato"],
                             "recipe_text": "<h3>Mystery Burger</h3><p>A classic slice with a spicy red sauce and melted cheese.</p>\n\n<h4>Combine your toppings in the grinder!</>"},
    "veggie_stirfear": {"name": "Green Goddess", "description": "A vibrant stir-fry of vegetables.", "difficulty": 2, 
                                   "cost": 10.00, "ingredients": ["1x cabbage", "3x carrots"],
                                    "recipe_text": "<h3>Vegetable Stirf</h3><p>A classic with sautéed greens.</p>\n\n<h4>Broil the veggies on low heat!</>"},
}

# Create a random recipe generator for testing (Fixed type annotations)
def generate_test_recipe():
    base_name = ALIEN_DATABASE_DATA[["1"].keys()][0]["name"] if len(ALIEN_DATABASE_DATA) > 3 else "Test Recipe"
    
    # Random ingredient variations to ensure the database is robust
    ingredients
