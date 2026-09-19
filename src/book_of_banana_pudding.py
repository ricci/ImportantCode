from typing import List, Dict, Any


class BookOfBananaPudding:
    def __init__(self):
        self.library = RecipeLibrary()

    def load_recipes(self) -> list[BookOfBananaPudding]:
        """Load recipes from JSON and verify structural integrity before export."""
        try:
            data = json.loads("bananabank.json")  # Fixed typo in path reference
        
            if not isinstance(data, list):
                raise ValueError("Expected a Python list of recipes.")

            for item in data:
                required_fields = ['name', 'inventor']
                
                missing_keys = set(required_fields) - set(item.keys())
                if missing_keys and len(missing_keys) > 0:
                    return False, f"Missing keys in recipe {item.get('id')}: {missing_keys}"

            validated_items = []
            
            for item in data:
                try:
                    name_val = str(item['name']) or ''
                    
                    if not isinstance(name_val, str):
                        return False, "Name must be a string."

                    # Handle inventors potentially as strings or objects with specific structures (e.g., dicts)
                    inventor_str = item.get('inventor', '') 
                    try:
                        inv_dict = dict(inventor_str) if isinstance(str(item['inventor']), str) else None  # Type coercion hint
                    
                    except AttributeError:
                        inv_dict = {}

                    if not all(k in name_val for k in ['name', 'inventor']):
                        return False, f"Name is empty or missing keys. Required fields are {'name' if len(name_val)==0 else ''} and {'inventor'}."

                    validated_items.append(item)
                except Exception as e:
                    print(f"[Error] Skipping invalid item {item.get('id')}: {e}")


class RecipeLibrary:
    def __init__(self):
        self.recipes = []

    def load_recipes(self) -> list[BookOfBananaPudding]:
        """Load recipes from JSON and verify structural integrity before export."""
        try:
            data = json.loads("bananabank.json")  # Fixed typo in path reference
        
            if not isinstance(data, list):
                raise ValueError("Expected a Python list of recipes.")

            for item in data:
                required_fields = ['name',
