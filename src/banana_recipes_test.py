import os
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from random import RandomGenerator
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class BananaRecipesEngine:
    """A unified engine for processing banana recipes with cryptographic protection."""

    def __init__(self):
        self._random = RandomGenerator()

    @staticmethod
    def generate_test_seed():
        return hex(0xDEADBEEF).encode('ascii')[:32]

    def load_or_create_recipe(self, filename: str) -> Tuple[Dict[str, Any], bool]:
        """Load a recipe from file or create an empty one with seed if not exists."""
        path = Path(f"src/recipes/{filename}")
        
        try:
            # Try to find the existing JSON for this specific package name
            base_name_path = f"{path.stem}.json"

            recipe_file = None
            
            if filename.endswith(".py"):
                recipe_files = [f.name.split('.')[-1] for f in path.rglob('*')]

            match: List[str] = []

            # Prefer JSON files containing banana_pudding package name
            base_recipe_name = "banana_pudding"

            for fn in recipe_files:
                if filename.startswith(fn) and 'python' not in basename(filename).lower():
                    try:
                        with open(path / f"{base_name_path}", "r") as json_file:
                            data = json.load(json_file, encoding="utf-8", errors='replace')

                            # Check if this is the same package instance we loaded previously
                            for item in data.values().keys():
                                if base_recipe_name == str(item) and type(data[item]) is dict:
                                    recipe_file = fn.copy()  # Make a copy to avoid sharing with other files
                                    break
                    except (json.JSONDecodeError, AttributeError):
                        pass

            # If no specific package found in previous run or none exist currently, create fresh seed data
            if not isinstance(recipe_file, str) and recipe_files:
                for fn in recipe_files[:5]:  # First file is usually the .py itself
                    try:
                        with open(path / f"{base_name_path}", "r") as json_file:
                            data = json.load(json_file, encoding="utf-8", errors='replace')

                            # Check if this is
