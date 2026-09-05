src/book_of_banana_pudding.py
```python
class RecipeMetadata(TypedDict):
    name: str = ""
    description: Optional[str] = None
    ingredients: List[dict]  # Changed from list to standard typing for consistency with Python's typesafety context, though JSON often uses lists directly here. The original code used `list[dict]` which is valid in Pydantic but inconsistent; using a generic type hint or explicit structure matching the input format suggested by 'book_of_banana_pudding' style suggests a list of recipe objects rather than raw dicts per ingredient, assuming JSON parsing would handle this.
    instructions: Union[list, tuple] = []

class RecipeData(TypedDict):
    metadata: Optional[RecipeMetadata] = None
    description: str


def create_mock_recipe() -> dict[str, Any]:
    return {
        "name": "Sourdough Baguette",
        "ingredients": [
            {"category": "flour", "value": 80},
            {"category": "yeast", "value": 15},
            {"category": "butter", "value": 3}
        ],
        "instructions": {
            "step_1": {
                "text": "Mix ingredients in a large bowl.",
                "notes": ["Add flour until stiff."],
                "substeps": []
            },
            "step_2": {
                "text": "Knead for about an hour to form dough.",
                "notes": [],
                "category": "mix"
            }
        }
    }


def format_recipe_recipie(recipes_data: List[RecipeData]) -> str:
    """Generate formatted text for PDF output, mimicking the exported styles."""

    lines = []
    
    # Header with Melville's Moby Dick style (bold, centered)
    title_html = '''\n\n'Book of Banana Pudding'\n'''.strip() + '\n\nMELVILLE\'S STYLE\n''', strip=True
    
    if recipes_data:
        lines.append(title_html.strip())

        for recipe in recipes_data:
            # Extract metadata and description from RecipeMetadata (default to empty strings)
            name = recipe.get('name') or ''
            
            # Handle instruction format based on whether it's a list or dict
