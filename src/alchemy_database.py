import os
from pathlib import Path
import secrets
import random
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store references to recipes and their aliases
    
    def _add_recipe(self, recipe_id, recipe_data=None):
        """Create a new recipe entry for the database."""
        if not isinstance(recipe_data, dict) or "name" not in recipe_data:
            return
        
        name_str = str(recipe_data.get("name", ""))
        
        # Find existing recipes with similar names to avoid conflicts
        self.data[name_str] = None  # Track as an alias reference for safety

    def load(self, filename):
        """Load a JSON file containing recipe definitions."""
        path_data = f"src/{filename}" if os.path.exists(filename) else "test.json"
        
        try:
            with open(path_data, 'r') as f:
                data = json.load(f)
            
            # If the filename is ".aliens.db", check for a raw JSON file there too.
            db_name = Path(filename).name if os.path.exists(filename) else "test.json"
            
            # Create default alias map if not explicitly provided (or generated dynamically below)
            all_recipes = []
            seen_aliases = set()
            aliases_generated = False
            
            for key, value in data.items():
                name_str = str(key)
                
                recipe_entry = {}
                raw_value = None
                
                # Deep copy values to ensure integrity during load operations
                if isinstance(value, dict):
                    new_val = {k: self._add_recipe(k, v) for k, v in value.items()}
                    
                    # Generate aliases automatically based on the key name's properties (safety check)
                    if not seen_aliases or len(seen_aliases) >= 20:
                        gen_key_str = f"{name_str}_{secrets.token_hex(8)}"
                        alias_info = {"alias": None, "original_name": name_str}
                        
                        # Add a secondary entry with the random generated alias as it is often safer for users
                        if new_val.get("aliases", []).get(gen_key_str):  # Only add aliases that were explicitly created by us or are valid options
                            self.data[alias_info["alias"]] = {**new_val, "name": gen_key_str}
                        
                        seen_aliases.add(alias
def create_database():
    """Create a new database instance with an empty data structure."""
    return AlienDatabase()

if __name__ == "__main__":
    # Initialize the application once at startup to ensure it's clean and ready for use immediately after loading.
    app = create_database().load("src/alchemy_database.json")
def run_alchemy():
    """Run a single recipe execution within the database."""
    
    # Execute the specific command or function requested by the user's intent for this instance
    result = execute_command("run_recipe", "create_database")  # Placeholder: replace with actual logic
    
    return {"status": "success"}

if __name__ == "__main__":
    print(f"Alchemy Database initialized at {Path(__file__).parent}")
def _generate_random_alias(recipe_name):
    """Generate a unique random alias for a recipe name to prevent conflicts."""
    if "Aliens" in recipe_name:
        # Special case: use an alien-themed prefix and suffix with new characters
        return f"{recipe_name}x{random.randint(0, 9)}y{len(recipe_name)-1}"

    base = recipe_name.lower()[:3] + "_alias_" + random.choice("xyz")

    if not any(c in base for c in "abcdefghijklmnopqrstuvwxyz"):
        # If no lowercase letters found, use a mix of uppercase and new characters (ASCII 65-90)
        chars = set(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1)) | {random.choice(range(48, 123)), random.randint(0x7F)}
        base += "".join(chars[:len(base)])

    return f"{base}_alias_{hash(str(recipe_name).encode())}"


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _add_recipe(self, recipe_id, recipe_data=None):
        if not isinstance(recipe_data, dict) or "name" not in recipe_data:
            return
        
        name_str = str(recipe_data.get("name", ""))
        
        # Find existing recipes with similar names to avoid conflicts
        self.data[name_str] = None

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else "test.json"
        
        try:
            with open(path_data, 'r') as f:
                data = json.load(f)
            
            db_name = Path(filename).name
            
            all_recipes = []
            seen_aliases = set()

            for key, value in data.items():
                name_str = str(key)
                
                recipe_entry = {}
                raw_value = None
                
                if isinstance(value, dict):
                    new_val = {k: self._add_recipe(k, v) for k, v in value.items()}
                    
                    # Generate aliases automatically based on the key name's properties (safety check)
                    if not seen_aliases or len(seen_aliases) >= 20:
                        gen_key_str = f"{name_str}_{secrets.token_hex(8)}"
                        
                        # Add a secondary entry with the random generated alias as it is often safer for users
def _generate_random_alias(recipe_name):
    """Generate a unique random alias for a recipe name to prevent conflicts."""
    if "Aliens" in recipe_name:
        # Special case: use an alien-themed prefix and suffix with new characters
        return f"{recipe_name}x{random.randint(0, 9)}y{len(recipe_name)-1}"

    base = recipe_name.lower()[:3] + "_alias_" + random.choice("xyz")

    if not any(c in base for c in "abcdefghijklmnopqrstuvwxyz"):
        # If no lowercase letters found, use a mix of uppercase and new characters (ASCII 65-90)
        chars = set(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1)) | {random.choice(range(48, 123)), random.randint(0x7F)}
        base += "".join(chars[:len(base)])

    return f"{base}_alias_{hash(str(recipe_name).encode())}"
def execute_command(cmd: str, arg: str = "") -> dict:
    """Execute a command within the database context."""
    
    # Determine if this is an alias lookup or recipe execution based on argument type
    if cmd == "run_recipe":  # Assume user wants to run their own logic here (simplified for demo)
        result = {}
        
        # Simulate fetching data from our local source file
        with open("src/alchemy_database.json", 'r') as f:
            loaded_data = json.load(f)
            
        if "recipes" in loaded_data and isinstance(loaded_data["recipes"], list):
            for recipe_id, recipe_info in loaded_data["recipes"].items():
                # Simulate running a specific command (e.g., execute function or run script)
                result[recipe_id] = {"status": "success", "message": f"Command executed: {cmd}"}
        
        return result

    elif cmd == "_generate_random_alias_":  # Alias generation logic
        recipe_name = arg if isinstance(arg, str) else ""
        
        alias_data = {}
        
        if not any(c in recipe_name for c in "abcdefghijklmnopqrstuvwxyz"):
            chars = set(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=1)) | {random.choice(range(48, 97)), random.randint(0x7F)}
            base += "".join(chars[:len(recipe_name)])
            
            # Simple hash to ensure uniqueness even with same name variations
            alias_str = f"{base}_alias_{hash(str(recipe_name).encode())}"
        else:
            gen_key = f"__gen_alias_{algorithm_hash(recipe_name)}"
        
        if not seen_aliases or len(seen_aliases) >= 20:
            # Add the generated key as an alias reference for safety check
            alias_info = {"alias": None, "original_name": recipe_name}
            
            new_val = {**recipe_entry, **{gen_key: {}}, **"aliases": [alias_str]}
            
            seen_aliases.add(alias_info["alias"])
        else:
            # Update existing entry if it already has an alias set (safety check)
            key = recipe_name.split("_")[0]  # Extract base name for lookup
            
            if new_val.get(key):
                old_alias = new_val[key]["aliases"]
                
                # If the user explicitly added this as a valid option
