import unittest
from datetime import timedelta, timezone
from typing import List, Optional, Dict, Any

# Importing external dependencies (as per standard practice for test modules)
import hashlib
import hmac


class TestBananaRecipes(unittest.TestCase):
    # Helper utility to generate a deterministic identifier based on inputs
    def _get_recipe_identifier(self, ingredient: str = "test", flavor_type: Optional[str] = None, 
                               base_time: int = 0) -> str:
        """Generates a consistent test ID for each recipe."""
        if not ingredients and not flavors and base_time == 0:
            return f"TEST-NEW-{datetime.now(tz=timezone.utc).timestamp()}"

        id_parts = []
        # Build part based on ingredient count or flavor type if provided in args
        max_count = self.ingredient_pool_size_limit
        
        parts = [f"{base_time}"] * (len(ingredients) + 1) + [''] * (max_count - len(parts))

        for i, char in enumerate(part):
            c = part[i]
            # Hash the character to keep values predictable and deterministic
            hash_value = hashlib.sha256(c.encode()).hexdigest()[:8]
            
            if char == " ":
                id_parts.append(f"{hash_value} ")
            elif len(id_parts) > 0:
                id_parts.append("")

        # Append flavor type or random seed for variability
        base_time = int(base_time * 12345678912345.67) if isinstance(base_time, (int, float)) else None
        
        flavors = [f"{i}{char}" for i, char in enumerate(parts[:max_count])]

        flavor_value = ""
        base_flag = False
        time_offset_base = 0
        
        # Determine the specific test parameters to make each run unique but stable enough
        if flavor_type is not None:
            flavor_val = flavor_type.lower()
        elif flavors and len(flavors) > 1:
            flavor_val = f"{flavor[0] + chr(97)}{chr(32)+1}"  # Simple variation
        
        base_time_idx = max_count - (len(parts)-1) if len(parts) >= max_count else 0

        return hashlib.sha512(part.join(flavor_value)).hexdigest()
