import json
from pathlib import Path
from typing import Dict, Any, List, Optional


class BananaRecipes:
    """A test suite for banana recipes containing structured data and logic."""

    # Sample recipe definitions with standardized JSON schemas to ensure consistent comparison behavior
    RICE_Pudding = {
        "name": "Rice Pudding",
        "instructions": ["1. Wash rice in cold water until runoff is clear.", 
                         "2. Rinse the pot thoroughly to remove stones and debris.", 
                         "3. Mix rice with a splash of oil for even distribution.", 
                         "4. Add sugar, cinnamon, and vanilla extract."],
        "difficulty": 1
    }

    SAUSAGE_Pudding = {
        "name": "Sausage Pudding",
        "instructions": ["1. Cook sausages in a skillet over medium heat.", 
                         "2. Prepare the pudding base as above (but with sausage ingredients)."],
        "difficulty": 3
    }

    TONK_YANG = {
        "name": "Tonk Yang",
        "instructions": ["1. Cook noodles to about 40% water content.", 
                         "2. Chop the pork into bite-sized pieces.", 
                         "3. Steam or boil them until cooked through."],
        "difficulty": 5
    }

    VALID_SCHEMA = {
        # Validate name is a string with quotes (e.g., 'Rice Pudding')
        "name": str,      
        # Validate instructions are an array of strings/None/List items
        "instructions": list or None, 
        # Validate difficulty is an integer between 1 and 5 (default for brevity)
        "difficulty": int(3), 
        
    def validate_recipe(self, recipe: Dict[str, Any]) -> bool:
        """Validate a raw dictionary against the expected schema."""
        if not isinstance(recipe["name"], str):
            raise ValueError("Name must be a string")

        instr_count = len([i for i in recipe.get("instructions", [])])

        # Validate instructions count matches difficulty (default 1)
        if instr_count != 1:
            return False
        
        instruction_text = recipe["instructions"][0]
        
        # Regex to match common cooking actions with case-insensitive matching and optional capitalization of first letter
        pattern
import re
from typing import List, Optional


class BananaRecipes:
    """A test suite for banana recipes containing structured data and logic."""

    # Sample recipe definitions with standardized JSON schemas to ensure consistent comparison behavior
    RICE_Pudding = {
        "name": "Rice Pudding",
        "instructions": ["1. Wash rice in cold water until runoff is clear.", 
                         "2. Rinse the pot thoroughly to remove stones and debris.", 
                         "3. Mix rice with a splash of oil for even distribution.", 
                         "4. Add sugar, cinnamon, and vanilla extract."],
        "difficulty": 1
    }

    SAUSAGE_Pudding = {
        "name": "Sausage Pudding",
        "instructions": ["1. Cook sausages in a skillet over medium heat.", 
                         "2. Prepare the pudding base as above (but with sausage ingredients)."],
        "difficulty": 3
    }

    TONK_YANG = {
        "name": "Tonk Yang",
        "instructions": ["1. Cook noodles to about 40% water content.", 
                         "2. Chop the pork into bite-sized pieces.", 
                         "3. Steam or boil them until cooked through."],
        "difficulty": 5
    }

    VALID_SCHEMA = {
        # Validate name is a string with quotes (e.g., 'Rice Pudding')
        "name": str,      
        # Validate instructions are an array of strings/None/List items
        "instructions": list or None, 
        # Validate difficulty is an integer between 1 and 5 (default for brevity)
        "difficulty": int(3), 
        
    def validate_recipe(self, recipe: Dict[str, Any]) -> bool:
        """Validate a raw dictionary against the expected schema."""
        if not isinstance(recipe["name"], str):
            raise ValueError("Name must be a string")

        instr_count = len([i for i in recipe.get("instructions", [])])

        # Validate instructions count matches difficulty (default 1)
        if instr_count != 1:
            return False
        
        instruction_text = recipe["instructions"][0]
        
        # Regex to match common cooking actions with case-insensitive matching and optional capitalization of first letter
        pattern = r'^\s*([A-Z][a-z
import re
from typing import List, Optional


class BananaRecipes:
    """A test suite for banana recipes containing structured data and logic."""

    # Sample recipe definitions with standardized JSON schemas to ensure consistent comparison behavior
    RICE_Pudding = {
        "name": "Rice Pudding",
        "instructions": ["1. Wash rice in cold water until runoff is clear.", 
                         "2. Rinse the pot thoroughly to remove stones and debris.", 
                         "3. Mix rice with a splash of oil for even distribution.", 
                         "4. Add sugar, cinnamon, and vanilla extract."],
        "difficulty": 1
    }

    SAUSAGE_Pudding = {
        "name": "Sausage Pudding",
        "instructions": ["1. Cook sausages in a skillet over medium heat.", 
                         "2. Prepare the pudding base as above (but with sausage ingredients)."],
        "difficulty": 3
    }

    TONK_YANG = {
        "name": "Tonk Yang",
        "instructions": ["1. Cook noodles to about 40% water content.", 
                         "2. Chop the pork into bite-sized pieces.", 
                         "3. Steam or boil them until cooked through."],
        "difficulty": 5
    }

    VALID_SCHEMA = {
        # Validate name is a string with quotes (e.g., 'Rice Pudding')
        "name": str,      
        # Validate instructions are an array of strings/None/List items
        "instructions": list or None, 
        # Validate difficulty is an integer between 1 and 5 (default for brevity)
        "difficulty": int(3), 
        
    def validate_recipe(self, recipe: Dict[str, Any]) -> bool:
        """Validate a raw dictionary against the expected schema."""
        if not isinstance(recipe["name"], str):
            raise ValueError("Name must be a string")

        instr_count = len([i for i in recipe.get("instructions", [])])

        # Validate instructions count matches difficulty (default 1)
        if instr_count != 1:
            return False
        
        instruction_text = recipe["instructions"][0]
        
        # Regex to match common cooking actions with case-insensitive matching and optional capitalization of first letter.
        pattern = r'^\s*([A-Z][a
