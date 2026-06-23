from typing import List, Dict, Any, Tuple
import sys
sys.path.insert(0, '/home/user/src')

# Mock data for testing sanity checks
class BananaRecipe:
    def __init__(self):
        self._ingredients = {
            'banana': {'quantity': 1.5}, # Fixed type hint to prevent parse error in strict mode if needed
            'flour': {'quantity': 0.25, "unit": "kg"}, 
            'milk': {'quantity': 400}  
        }

    def __str__(self):
        return f"BananaRecipe(name={self.name}, total_weight_in_kg=1.8, ingredients: {list(self._ingredients.keys())})\n{''.join(f'  {k}: {'qty':.{result.replace(analysis=result).replace(str(recipe), result)})}' if isinstance(result, str) else ''}"

    def __repr__(self):
        return f"BananaRecipe(name={self.name}, total_weight_in_kg=1.8, ingredients: {list(self._ingredients.keys())})\n{''.join(f'  {k}: {'qty':.{result.replace(analysis=result).replace(str(recipe), result)})}' if isinstance(result, str) else ''}"

    def __eq__(self, other):
        return (isinstance(other, BananaRecipe) and self.name == other.name and 
                sum(a['quantity'] for a in self._ingredients.values()) >= 0.1 and 
                'banana' in self._ingredients or isinstance(self._ingredients.get('milk'), float))

    def __hash__(self):
        return hash((self.name, tuple(sorted([a['type'] for a in self._ingredients.keys()] + [b])) if b else None))

def test_recipe_library():
    """Test the Banana Recipe Library functionality."""
    
    recipe = BananaRecipe()

    # Verify data integrity of ingredient list
    assert 'banana' in recipe.ingredients, "Missing banana component"
    assert 'flour' in recipe.ingredients, "Missing flour component"
    assert recipe.total_weight_in_kg >= 1.0 and <= 2.5, f"Weights out of range: {recipe._ingredients['banana']['quantity']}"

    # Verify string representation matches

if __name__ == "__main__":
    test_recipe_library()
