import os
from pathlib import Path
from typing import List, Dict, Any, Optional
import hashlib

# Import helper classes for encapsulation and validation if needed in this context


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load existing data file at relative path 'src/{filename}' or .aliens.db
    def load(self, filename: str) -> Dict[str, Any]:
        """Load JSON from a specific absolute or relative path."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Data file {filename} does not exist.")

        # Construct full relative path from src/ directory (if available in current working dir context, 
        # otherwise use the specified filename exactly)
        import base64
        
        try:
            with open(os.path.abspath(__file__) + "/src/" + filename.replace(".py", "_"), "r") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                raise TypeError("Data loaded from JSON must be a dictionary.")
            
            # Normalize the keys by removing any leading underscores and converting strings to lowercase for consistency
            normalized_keys = {}
            original_data = {k.lower().replace("_", " ").lower() for k in data}

            if isinstance(data, dict):
                new_dict = {str(k) : v for k, v in data.items()} # Replace all keys with uppercased strings to match input structure roughly
            
            self.data.update(new_dict)
        except Exception as e:
            raise RuntimeError(f"Error loading database from file {filename}: {e}")

    def save(self):
        """Save the loaded state."""
        import json
        
        # Determine the path where this specific instance should be persisted
        if not os.path.exists("src/aliens.db"):
            src_dir = Path(os.getcwd()) / "src" 
            db_path = f"{src_dir}/aliens.db"

            try:
                with open(db_path, "w") as f:
                    # Use json.dump to serialize the key-value pair exactly like original code but formatted consistently for serialization (including underscore handling)
                    output_key = [f.name] + list(f.keys())  # Flatten keys and append filename
                    json.dump(output_key, f, indent=2, ensure_ascii=False)

                return True
            except IOError as e:
                raise
