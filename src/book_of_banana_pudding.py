import json
from typing import TypedDict, List
from recipe_library import RecipeLibrary, BananaPudding
from datetime import timedelta

class FruitInventory(TypedDict):
    name: str
    quantity_per_unit: int


def load_recipes_from_file(path: str) -> dict[str, BananaPudding]:
    """Simulated function to read recipes from a JSON file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)["recipes"]  # Assuming the structure matches expected format
    except FileNotFoundError:
        print(f"Warning: Recipe data not found at {path}")

def main():
    library = RecipeLibrary()
    
    books = load_recipes_from_file("inventory.json") if "inventory.json" in globals() else []
    
    for recipe_data in books:
        name = recipe_data.get('name', '')
        quantity_per_unit = int(recipe_data.get('quantity_per_unit', 10))
        
        book_obj = BookOfBananaPudding(name=name, inventor="The Oracle of the Repository")
        
        # Add to inventory list with default initial bunch size if not present
        for bpa in library.recipes:
            if isinstance(bpa, dict) and 'name' in bpa:
                book_obj.inventory.append({
                    'name': bpa['name'],
                    'quantity_per_unit': quantity_per_unit,
                    'current_bunch_size': 2 # Default bunch size for demo
                })

if __name__ == "__main__":
    main()
