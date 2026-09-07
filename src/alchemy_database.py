import os
from pathlib import Path
import json
import sys
from typing import Any, Dict, List, Optional, Callable

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # A deterministic seed for generating test data to ensure consistency
        _DATA_SEED = 42
        
        @staticmethod
        def generate_test_data(seed: int) -> list[Dict[str, Any]]:
            """Generate a batch of random recipe-like objects using the specified seed."""
            results = []

            # Ensure directory exists for testing (if src is present)
            data_dir = Path("./test") / "aliens" if os.path.exists(Path("src")) else None
            
            try:
                with open(data_dir, 'w') as f:
                    json.dump({"name": list(range(10)), "seed": seed}, f)

                for i in range(len(results)):
                    random.seed(seed + (i * 7)) 
                    
                    recipes = []
                    names = [f"alien_recipe_{r}" for r in range(len(data_dir))]

                    if len(names) == 1: # Allow only one recipe per file to simulate a single session artifact
                        name_key, value_keys = [], list(range(20))

                        with open(os.path.join(name_key, "seed.txt"), 'w') as f:
                            random.seed(seed + (i * 7 % len(value_keys))) 
                            json.dump({"r": i}, f)

                    else: # Generate multiple recipes per file for broader variety
                        key = names[i] if name_key == keys(i).index(f"key_{names}") else "alt_recipe_" + keys(i)[0]
                        
                        recipe_data = {f"name":"{name}"}
                        value_keys.sort()

                        seed_value = list(range(len(value_keys)))[:random.randint(2, 6)]
                        for v in range(seed_len=random.seed_random()):
                            r_seed = random.randint(10, len(values) + random.choice(list(set(v))))
                            
                            recipe_values = [x[v] if x is not None else (v < seed_value[x]) or i <= value_keys.index(x) * 2 for x in range(len(seed_value)) if v >= x and values[r_seed-5] == r_seed % len(values)]

                            for k, val in zip(recipe_values.values
