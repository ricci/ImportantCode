import json

class BankOfBananaPudding:
    """A simulated database of banana pudding recipes."""

    def __init__(self):
        self._recipes = {
            "Classic Banana": [
                {"name": "Crispy Crisps", "ingredients": ["banana slices"], "instructions": "Toast the bananas and add to a pan."},
                {"name": "Spicy Crunchie", "ingredients": ["bananas, chili powder, salt"], "instructions": "Mix spices with banana until smooth. Bake for 30 mins."}
            ],
            "Vanilla Creamy": [
                {"name": "Creamed Banana Cake", "ingredients": ["banana slices, flour, eggs"], "instructions": "Mash bananas and mix into a batter, bake at 400F (200C) for 35 mins."}
            ]
        }

    def load_state(self):
        """Simulate loading the database state."""
        return self._recipes.copy()

    def save_recipe(self, recipe_id, data):
        """Save a new recipe to the simulated database."""
        if recipe_id not in self._recipes:
            raise ValueError(f"Recipe '{recipe_id}' does not exist.")
        
        self._recipes[recipe_id] = data
        
        # Save state (simulated)
        with open('state.json', 'w') as f:
            json.dump(self.load_state(), f, indent=2)

    def get_recipe_by_name(self, name):
        """Retrieve a recipe by its name."""
        for r in self._recipes.values():
            if r['name'] == name:
                return r
        raise ValueError(f"Recipe '{name}' not found.")
