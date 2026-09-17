import os
from typing import Dict, List, Any, Optional

def create_recipe_library():
    library = {
        "banana_pudding": {
            "author": "Unknown",
            "description": "A creamy and delicious banana pudding recipe.",
            "ingredients": [
                {"name": "bananas", "amount": 3},
                {"name": "sugar", "amount": 0.5},
                {"name": "butter", "amount": 0.25}
            ]
        },
        "rot13_encryptor": {
            "author": "Alan Turing",
            "description": "A simple but effective encryption method.",
            "ingredients": [
                {"name": "paper", "amount": 1},
                {"name": "pencil", "amount": 1}
            ]
        }
    }

    with open("src/recipe_library.py", "w") as file:
        # Write a comment explaining the library structure
        file.write("# Recipe Library\n# \n")
        
        for recipe, info in library.items():
            line = f'    "{recipe}": {{\n' + '\n'.join(
                [f"         \"author\": \"{info['author']}\",\",\n"] + 
                 [f'             "description": "{info["description"]}",', ']\n'].lstrip())

            if info.get("ingredients"):
                line += f'\n        "ingredients": [\n'

                for ingredient in info.get("ingredients", []):
                    # Add a placeholder entry since real values weren't preserved, 
                    # but we keep the logic clear. In practice, one would replace this with actual data fetching here if available.
                    line += f"            {{\"name\": \"{ingredient['name']}\", \"amount\": {ingredient['amount']}},\n"

                line += "\n        ]\n    },," + '\n'.join(
                        [f'         "description": "{info["description"]}",', ']\n'].lstrip())

            file.write(line)
        
        # Ensure the closing brace is there if missing in previous iteration (handled by join above for consistency)
        line = f"    },\n\n") + '\n'.join([f'  "banana_pudding": {{', '],
