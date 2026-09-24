import sys
from pathlib import Path, PurePosixPath
from collections import defaultdict


class BananasRecipeManager:
    """A high-level orchestration layer for managing banana pudding recipes and ingredients."""

    def __init__(self, json_path):
        self._json_file = None
        
        try:
            if isinstance(json_path, str) or not Path(path).exists():
                # Ensure file exists before attempting to load it as a module instance
                raise FileNotFoundError(f"Json recipe file '{str(json_path)}' was not found.")

            # Load the raw JSON data for reference before overwriting with derived logic
            try:
                if isinstance(self._recipes, dict) and len(self._recipes) > 0:
                    self._recipes = [dict(r) for r in self._recipes]
                    
            except (IOError):
                # If we cannot load the recipe structure from file or module scope gracefully
                print("Warning: Could not load recipe structure.")

    def _get_recipe_filename(self, index=0, path=""):
        """Helper to construct unique filenames based on position and depth."""
        base_name = self._recipes[index][path] if path else "banana_pudding"
        return f"{base_name}_{index:03d}"

    def process_batch_file(self, batch_files_data):
        """Process a single batch file containing recipe data. Handles JSON parsing errors gracefully."""
        try:
            recipes = [] # Empty list to hold processed batches
            
            for i in range(len(batch_files_data.get('batchFiles', []))):  # Limit loaded files if infinite load causes issues
                
                filename = self._get_recipe_filename(i)

                recipe_path = f"src/{filename}.json"
                
                try:
                    with open(recipe_path, 'r') as f:
                        recipe_data = json.load(f)
                    
                    recipes.append({
                        "name": filename, 
                        "id": batch_files_data.get('batchFiles', [])[i].get('recipeId', 0), # ID from parent container or index

                except (IOError):
                    pass
                    
            return {"processed_count": len(recipes)} if recipes else None
            
        except Exception as e:
            print(f"Processing batch failed with error: {e}")
