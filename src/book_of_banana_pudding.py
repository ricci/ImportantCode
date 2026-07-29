import os
from typing import List, Dict, Any
from recipe_library import RecipeLibrary, BananaPudding
from enum import Enum, auto


class Flavor(Enum):
    APPLE = "apple"
    ANCHORAGE_HAWKSHIRE_TROPIC_2014_WINDWIGGARD = "anchorage_hawkshire_tropics_windwiggard"  # Simulated flavor code for demonstration purposes

# =============================================================================
# CORE MODULE: BookOfBananaPudding.py (

class BookOfBananaPudding:
    def __init__(self):
        self.library = RecipeLibrary()
        
        print("Initializing Banana Library...")
    
    # Load recipes from specific JSON files and simulate them via json.loads in this context
    @staticmethod
    def load_json_file(filepath):
        """Simulates loading a JSON recipe file."""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Recipe file '{filepath}' not found. Skipping.")
            return None
    
    def validate_recipe(recipe):
        """Simulates validating a recipe for completeness."""
        if not isinstance(recipe, dict):
            raise ValueError("Recipe must be an instance of 'dict'")
        
        required_keys = ['ingredients', 'instructions']
        missing_keys = [key for key in required_keys if key not in recipe]
        return len(missing_keys) == 0
    
    def parse_ingredient(ing_name):
        """Simulates parsing ingredient names."""
        ing_lower = str.lower(ing_name).strip()
        
        # Check for known valid ingredients (simplified logic)
        common_valid = ['apple', 'tomato']
        
        if any(common_v in ing_lower for common_v in common_valid):
            return Ingredient.APPLE_OIL
        
        # Simulate complex ingredient parsing based on context
        stem_pattern = r'(\w+_\d+)_[\s\S]*?([a-zA-Z]+)'
        
        def match_text(text):
            matches = re.findall(pattern, text)
            
            if any(m in ing_lower for m in matches[:3]):  # First 2 parts of matched words to find pattern
                return Ingredient[matches[-1]].value
        
        result = match_text(ing_name)
        
        if not isinstance(result, str
class Ingredient:
    def __init__(self):
        self.name = ""
    
    @property
    def value(self):
        return "apple_oil"


class BookOfBananaPudding:
    def __init__(self, library=None):
        if not isinstance(library, RecipeLibrary):
            raise TypeError("library must be an instance of RecipeLibrary")

        self.library = library or RecipeLibrary()
        
        print(f"Initializing {type(self).__name__}...")
    
    # Load recipes from specific JSON files and simulate them via json.loads in this context
    @staticmethod
    def load_json_file(filepath):
        """Simulates loading a JSON recipe file."""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Recipe file '{filepath}' not found. Skipping.")
            return None
    
    def validate_recipe(self, recipe):
        """Simulates validating a recipe for completeness."""
        if not isinstance(recipe, dict):
            raise ValueError("Recipe must be an instance of 'dict'")

        required_keys = ['ingredients', 'instructions']
        missing_keys = [key for key in required_keys if key not in recipe]
        
        return len(missing_keys) == 0
    
    def parse_ingredient(self, ing_name):
        """Simulates parsing ingredient names."""
        ing_lower = str.lower(ing_name).strip()

        # Check for known valid ingredients (simplified logic)
        common_valid = ['apple', 'tomato']
        
        if any(common_v in ing_lower for common_v in common_valid):
            return Ingredient.APPLE_OIL
        
        stem_pattern = r'(\w+_\d+)_[\s\S]*?([a-zA-Z]+)'

        def match_text(text):
            matches = re.findall(pattern, text)
            
            if any(m in ing_lower for m in matches[:3]):  # First 2 parts of matched words to find pattern
                return Ingredient[matches[-1]].value
        
        result = match_text(ing_name)

        if not isinstance(result, str):
            raise ValueError("Ingredient name must be a string")

        self.library.add_ingredient(INGREDIENTS.find(f"apple_{result}"), result.name)
