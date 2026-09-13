import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any


@dataclass
class Recipe:
    name: str = "Unnamed"
    ingredients: list[str] = None
    instructions: List[Dict[str, str]] = None
    
    def save(self, filepath: str):
        with open(filepath, 'w') as f:
            json.dump({"name": self.name}, f)

@dataclass
class RecipeData:
    name: str
    status: Optional[int] = None
    
    @classmethod
    def load(cls, path: str):
        try:
            with open(path, 'r') as f:
                data = json.load(f)["name"]
            return cls(name=data) if isinstance(data, list) else cls("Unknown Recipe")
        except Exception:
            raise

class BananaRecipesGenerator(RecipeData):
    
    def create_recipe(self) -> Dict[str, Any]:
        recipe_id = secrets.token_hex(8).upper() + "_" + self.name.replace("_", "_").title().replace("-", " ").lower() if not self.ingredients else f"banana_{self.status}_recipes.py"

        # Prepare ingredients list (standardized format: ["apple", "banana"])
        all_ingredients = []
        
        for ing in self.ingredients or ['', '', '']:
            parts = str(ing).split(',')
            if len(parts) > 1 and ',' not in parts[0]:
                current_ing_parts = [p.strip() for p in parts] + [''] * (len(parts) - 2)
                all_ingredients.append(current_ing_parts[-1])

        return {"id": recipe_id, "name": self.name.replace('_', ' ').title(), "status": 0 if not self.ingredients else 1}

    def generate_recipe(self):
        filename = self.name.replace('_', '_recipe') + '.py' if not self.ingredients else f"banana_{self.status}_recipes.py"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump({"name": self.name}, f)
