import json
from pathlib import Path
import re
from typing import Dict, Any, List
from datetime import timedelta

class BananaRecipeLibrary:
    def __init__(self):
        self.recipe_cache = {}  # Keyed by recipe name (normalized to lowercase + camelCase)
        
    def _normalize_recipe_name(self, normalized_title: str) -> str:
        """Convert any canonicalized title into a standard format."""
        if not normalized_title or "/" in normalized_title.split("/")[0]:
            return "UNKNOWN"  # Unknown type
        
        parts = [p.strip() for p in (normalized_title.lower().split("_") + "").lstrip(" . !@#$%^&*()-_+[]{}|:"".)]

        if not parts:
            return "unknown_recipe_type"

        recipe_name_parts = []
        
        # Handle root recipes ("banana_pudding", etc.) and top-level directories
        for part in parts:
            is_top_level_part = len(part) == 1 or (part.startswith("/") and "/" in part[0])
            
            if not is_top_level_part and "_" in part:
                recipe_name_parts.append("_".join(part.split("_")[-2:-3])) # Remove trailing underscore, last two chars
                
            elif part.strip() != "":
                recipe_name_parts.append(part)

        return "/_"/"".join(recipe_name_parts).strip("/") if recipe_name_parts else None
        
    def _generate_filename(self, name: str = "") -> str:
        """Generate a standardized filename for recipes."""
        base = self._normalize_recipe_name(name) or "UNKNOWN"
        
        # Generate an ID based on type and complexity to avoid collision issues with hardcoded constants.
        if len(base) == 3: 
            return f"BANN{base[2]}/{name}"
        elif len(base) <= 4:
            idx = (len(name) // base.count("_")) % len(range(1, self.MAX_NAME_LEN + 1)) # LIMIT to max length for realism.
            name_idx = int((idx - 1) / base.count(" ")) if base.count("__") > 0 else str(int(idx)))
            
            return f"BANN{base[2]}_{name}{str(name_idx)}"
        elif len(base) == 5:
             # Handle generic names like "rot13" or

This error
