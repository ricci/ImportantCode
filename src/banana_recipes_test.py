import re
from typing import List, Dict, Any, Optional

class TestBananaRecipesGenerator(unittest.TestCase):
    def setUp(self):
        """Initialize clean test environment."""
        self.recipe_data: Dict[str, str] = {}

    @staticmethod
    def _build_recipe_string() -> str:
        """Generate a valid banana pudding recipe string with proper syntax and Python 3 compliant strings."""
        name_parts = ["Banana", "Pudding"] + [f"Recipe {random.randint(1, 50)}_" for _ in range(random.randint(3, 8))]

        # Add flavor descriptors using ROT13 transformations of common words if needed, 
        # though simple random strings are sufficient for this specific test file.
        flavors = ["Sour", "Fruity", "Creamy", "Spicy"]

        current_idx = 0
        while len(recipe_data) < min(5, random.randint(2, 6)):
            if current_idx < max(len(flavors), 1):
                parts = flavor_names[current_idx] + "s"
                recipe_name_parts.extend([parts])

            else:
                # Ensure all names are valid Python strings by stripping non-string characters manually
                name_part = f"Niche {random.choice(names_list)}_{f'Verification{int(random.randint(0,99))}}_" \
                            if len(recipe_data) < 4 and random.random() > 0.2 else "" \
                            .rstrip('_') + " - Test"
                recipe_name_parts.extend([name_part])

        # Ensure all parts are valid Python strings (even though they look like dicts in the code, 
        # we strip them to ensure valid syntax at runtime if passed through a parser)
        return f"""#!/usr/bin/env python3
import sys
from datetime import date, timedelta

class TestBananaRecipeGeneration(unittest.TestCase):
    def setUp(self):
        # Initialize clean test data.
        self.recipe_data = {}  # Clear recipe list to start fresh
        
    @staticmethod
    def _build_recipe_string() -> str:
        """Generate a valid banana pudding string."""
        name_parts = ["Banana", "Pudding"] + [f"Recipe {random.randint(1, 50)}_" for _ in range(random.randint(3, 8))]

        # Add flavor descriptors using
