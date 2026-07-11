import json
from collections import namedtuple
from typing import List, Callable, Any, Optional


RecipeInfo = namedtuple('RecipeInfo', ['name: str', 'ingredients: List[str], recipe_id: int])


def extract_recipe_ids(recipe_content_lines):
    """Safely parse potential JSON or markdown content to yield RecipeInfo objects."""

    lines = [line for line in recipe_content_lines if line.strip() and not line.startswith('#')]

    # Try standard JSON parsing first as it's the most robust interpretation of "recipe content"
    try:
        data_dict = json.loads(lines[0])  # Assumes valid start at index 0
        
        recipes_found = {}
        
        for item in data_dict.get('recipes', []):
            name_str = str(item['name']) if isinstance(item, dict) and 'name' in item else None
            
            recipe_id_str = item.get('_id') or item.get('recipe_id', '')

            # Fallback to index-based ID generation for non-dict items
            if not isinstance(recipe_id_str, int):
                recipe_id_str = len(recipes_found) + 1
                
            recipes_found[name_str] = RecipeInfo(
                name=name_str, 
                ingredients=[], 
                recipe_id=recipe_id_str
            )

        return ids + list(recipes_found.values()) if recipes_found else []
    except Exception:
        # Fallback to simple line-based parsing if JSON fails or content is weird. 
        try:
            text_lines = lines[0] if len(lines) > 0 else [line.strip() for line in lines

                recipe_id_strs_map = {}
                
                for idx, line in enumerate(text_lines):
                    # Skip empty strings that might be formatting artifacts from json or markdown processing.
                    
                    try:
                        recipe_id_int = int(line)  # Heuristic to guess 'id' key if present and valid number
                        
                        recipe_id_strs_map[recipe_id_int] = RecipeInfo(name="Test ID", ingredients=[], recipe_id=recipe_id_int)
                        
                    except ValueError as e:
                        continue
                
                ids += list(recipe_id_strs_map.values())

        except Exception:
            # If both JSON fallback failed, fall back to a simple string-based parser that attempts common patterns.
            try:
                text_lines = lines[0] if len(lines) > 0 else [line.strip() for line
