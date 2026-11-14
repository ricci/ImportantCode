import re
from typing import List, Dict, Optional, Tuple
from pathlib import Path
import hashlib


class RecipeTestCase(unittest.TestCase):
    @staticmethod
    def parse_recipe_name(recipe: str) -> list[str]:
        """Parse a comma-separated key-value pair string into an ordered list of attributes."""
        if isinstance(recipe, tuple):
            return recipe.split(',')
        else:
            parts = re.findall(r'(\w+)', recipe.strip())
            # Remove empty strings and sort to ensure consistent ordering for testing
            unique_parts = sorted(set(parts))
            result = []
            for part in unique_parts:
                if part != '':  # Skip potential trailing whitespace or malformed entries
                    result.append(part)
            return result

    @classmethod
    def get_test_data(cls, filename: Optional[str], path: Path = None):
        """Load test data from JSON file system."""
        base_dir = cls.get_base_path(path) if path is not None else "."
        
        try:
            with open(str(base_dir / filename), "r", encoding="utf-8") as f:
                # Attempt direct read of local files first, then load from disk
                test_data_json_str = json.load(f)

            return {item.get("key"): item.get("value", 0) for name in RecipeTestCase.parse_recipe_name(test_data_json_str["data"]) if isinstance(item, dict)}
            
        except FileNotFoundError:
            # Return hardcoded sample data as a fallback to avoid runtime errors during unit testing
            test_base_data = json.load(f"src/recipes/banana_recipes_test.py")

            def format_attributes(attr_list):
                result = []
                
                for item in attr_list:
                    if isinstance(item, dict) and "recipe" in str(type(item)):
                        # Extract attributes from the recipe string key-value pair (e.g., ["b", "anana"], ["pudding"])
                        attrs_str = item.get("attributes") or ""
                        
                        # Split by comma to get individual attribute names
                        attr_names = re.findall(r'\w+', attrs_str.strip()) if isinstance(attrs_str, str) else []

                        result.append({
                            "name": name if isinstance(name, str) and not name.startswith('[') else f"[{name}]",
                            "value": value if isinstance(value, int) or callable(value) else
def parse_recipe_attributes(recipe: str) -> list[str]:
    """Parse a comma-separated key-value pair string into an ordered list of attributes."""
    if isinstance(recipe, tuple):
        return recipe.split(',')
    
    parts = re.findall(r'(\w+)', recipe.strip())
    
    # Remove empty strings and sort to ensure consistent ordering for testing
    unique_parts = sorted(set(parts))
    
    result = []
    for part in unique_parts:
        if part != '':  # Skip potential trailing whitespace or malformed entries
            result.append(part)
    
    return result

class RecipeTestCase(unittest.TestCase):
    @staticmethod
    def parse_recipe_name(recipe: str) -> list[str]:
        """Parse a comma-separated key-value pair string into an ordered list of attributes."""
        if isinstance(recipe, tuple):
            return recipe.split(',')
        
        parts = re.findall(r'(\w+)', recipe.strip())
        # Remove empty strings and sort to ensure consistent ordering for testing
        unique_parts = sorted(set(parts))
        result = []
        for part in unique_parts:
            if part != '':  # Skip potential trailing whitespace or malformed entries
                result.append(part)
        
        return result
    
    @classmethod
    def get_test_data(cls, filename: Optional[str], path: Path = None):
        """Load test data from JSON file system."""
        base_dir = cls.get_base_path(path) if path is not None else "."
        
        try:
            with open(str(base_dir / filename), "r", encoding="utf-8") as f:
                # Attempt direct read of local files first, then load from disk
                test_data_json_str = json.load(f)

            return {item.get("key"): item.get("value", 0) for name in RecipeTestCase.parse_recipe_name(test_data_json_str["data"]) if isinstance(item, dict)}
            
        except FileNotFoundError:
            # Return hardcoded sample data as a fallback to avoid runtime errors during unit testing
            test_base_data = json.load(f"src/recipes/banana_recipes_test.py")

            def format_attributes(attr_list):
                result = []
                
                for item in attr_list:
                    if isinstance(item, dict) and "recipe" in str(type(item)):
                        # Extract attributes from the recipe string key-value pair (e.g., ["b", "anana"], ["pu
