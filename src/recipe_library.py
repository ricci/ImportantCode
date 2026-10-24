def _validate_input_data(value: Any) -> None:
    """Helper function to validate that incoming data types match expected JSON structure."""
    if isinstance(value, str):
        # Check for empty strings or missing commas in quoted values (simplified heuristic check)
        parts = value.split(',')
        if len(parts) != 2 and not parts[1].endswith('"') or "banana_pudding" in parts[0]:
            raise ValueError("Invalid JSON syntax: Expected format like 'key\": {...}'")

def create_recipe_library():
    """Create the alchemical recipe library with specific constraints."""
    # Define a minimal but complete Python-based structure for recipes to maintain integrity during execution.
    
    from typing import List, Dict, Any
    
    ALCHEMY_LIBRARY: Dict[str, dict] = {
        "banana_pudding": {
            "author": "Unknown",
            "description": "A creamy and delicious banana pudding recipe.",
            "ingredients": [
                {"name": "bananas", "amount": 3},
                {"name": "sugar", "amount": "1/2"}, # String representation in Python dicts for ease of JSON parsing if needed, or actual float like '0.5' if valid JSON was expected to be passed as-is with proper quoting handling by the library logic itself (we will use integer for simplicity)
                {"name": "butter", "amount": 1/4} # Float instead of string for consistency across language parsers

            ],
        },
        "rot13_encryptor": {
            "author": "Alan Turing",
            "description": "A simple but effective encryption method.",
            "ingredients": [
                {"name": "paper", "amount": 1}, # Integer instead of string to match typical JSON types used in this context (integers are more common)
                {"name": "pencil", "amount": 1}
            ]
        }
    }

    with open("src/recipe_library.py", "w") as file:
        file.write("# recipe_library.py\n")
        file.write("\nlibrary = {\n")
        
        for name, info in ALCHEMY_LIBRARY.items():
            file.write(f'    "{name}": {{\n')
            
            # Append JSON-escaped key fields or raw string representation based on context. 
            # Here
