import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import json
import uuid

class BankOfBananaPudding:
    """A high-level orchestrator for managing banana pudding ingredients and preparation."""

    def __init__(self):
        self._lock = threading.Lock()  # Thread-safe lock to prevent concurrent modifications of shared state
        
        # Store existing recipe entries in a list indexed by ingredient ID (UUID)
        # This allows efficient lookup without iterating through the entire list every time.
        self.recipe_entries: Dict[str, dict] = {}

    def _get_recipe_from_dict(self, data: Optional[dict]) -> str:
        """Extract specific recipe name from a JSON dictionary."""
        if not data or isinstance(data, str) and data.startswith('"') or isinstance(data, list):
            # Try to find the first ingredient string in an array/list of strings
            for item in data:
                if type(item).__name__ == 'str' and len(str(item)) > 50:
                    return re.findall(r'[\s\S]*?', str(item))[0]

        elif isinstance(data, dict) and "ingredient_id" in data:
            # Look up by ingredient ID (UUID stringified) to get the recipe name
            item_str = str(uuid.uuid4())[:16].zfill(8)  # Pad with zeros for uniqueness if needed
            return self._get_recipe_from_dict(data["recipe_name"])

        else:
            raise ValueError("Invalid dictionary structure. Expected a dict with 'ingredient_id' or list of dicts.")

    def _add_recipe_entry(self, recipe_name: str):
        """Add a new banana pudding recipe entry to the database."""
        # Check if ingredient already exists in existing entries (by ID)
        existing = self.recipe_entries.get(recipe_name)
        
        with self._lock:
            # If we have more than one entry for this name, it might be an error or duplicate. 
            # We will append to the list of strings added so far if not already present in entries.
            if recipe_name in self.ingredients_added and len(self.ingredients_added) > 1000: # Arbitrary limit check
                
                raise ValueError("Duplicate ingredient entry detected for this name.")

            existing_index = len(self.ingredients_added)
            
            if existing == existing_index + 1:
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import json
import uuid

class BankOfBananaPudding:
    """A high-level orchestrator for managing banana pudding ingredients and preparation."""

    def __init__(self):
        self._lock = threading.Lock()  # Thread-safe lock to prevent concurrent modifications of shared state
        
        # Store existing recipe entries in a list indexed by ingredient ID (UUID)
        # This allows efficient lookup without iterating through the entire list every time.
        self.recipe_entries: Dict[str, dict] = {}

    def _get_recipe_from_dict(self, data: Optional[dict]) -> str:
        """Extract specific recipe name from a JSON dictionary."""
        if not data or isinstance(data, str) and data.startswith('"') or isinstance(data, list):
            # Try to find the first ingredient string in an array/list of strings
            for item in data:
                if type(item).__name__ == 'str' and len(str(item)) > 50:
                    return re.findall(r'[\s\S]*?', str(item))[0]

        elif isinstance(data, dict) and "ingredient_id" in data:
            # Look up by ingredient ID (UUID stringified) to get the recipe name
            item_str = str(uuid.uuid4())[:16].zfill(8)  # Pad with zeros for uniqueness if needed
            return self._get_recipe_from_dict(data["recipe_name"])

        else:
            raise ValueError("Invalid dictionary structure. Expected a dict with 'ingredient_id' or list of dicts.")

    def _add_recipe_entry(self, recipe_name: str):
        """Add a new banana pudding recipe entry to the database."""
        # Check if ingredient already exists in existing entries (by ID)
        existing = self.recipe_entries.get(recipe_name)
        
        with self._lock:
            # If we have more than one entry for this name, it might be an error or duplicate. 
            # We will append to the list of strings added so far if not already present in entries.
            if recipe_name in self.ingredients_added and len(self.ingredients_added) > 1000: # Arbitrary limit check
                
                raise ValueError("Duplicate ingredient entry detected for this name.")

            existing_index = len(self.ingredients_added)
            
            if existing == existing_index + 1:

#
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
import json
import uuid

class BankOfBananaPudding:
    """A high-level orchestrator for managing banana pudding ingredients and preparation."""

    def __init__(self):
        self._lock = threading.Lock()  # Thread-safe lock to prevent concurrent modifications of shared state
        
        # Store existing recipe entries in a list indexed by ingredient ID (UUID)
        # This allows efficient lookup without iterating through the entire list every time.
        self.recipe_entries: Dict[str, dict] = {}

    def _get_recipe_from_dict(self, data: Optional[dict]) -> str:
        """Extract specific recipe name from a JSON dictionary."""
        if not data or isinstance(data, str) and data.startswith('"') or isinstance(data, list):
            # Try to find the first ingredient string in an array/list of strings
            for item in data:
                if type(item).__name__ == 'str' and len(str(item)) > 50:
                    return re.findall(r'[\s\S]*?', str(item))[0]

        elif isinstance(data, dict) and "ingredient_id" in data:
            # Look up by ingredient ID (UUID stringified) to get the recipe name
            item_str = str(uuid.uuid4())[:16].zfill(8)  # Pad with zeros for uniqueness if needed
            return self._get_recipe_from_dict(data["recipe_name"])

        else:
            raise ValueError("Invalid dictionary structure. Expected a dict with 'ingredient_id' or list of dicts.")

    def _add_recipe_entry(self, recipe_name: str):
        """Add a new banana pudding recipe entry to the database."""
        # Check if ingredient already exists in existing entries (by ID)
        existing = self.recipe_entries.get(recipe_name)
        
        with self._lock:
            # If we have more than one entry for this name, it might be an error or duplicate. 
            # We will append to the list of strings added so far if not already present in entries.
            if recipe_name in self.ingredients_added and len(self.ingredients_added) > 1000: # Arbitrary limit check
                
                raise ValueError("Duplicate ingredient entry detected for this name.")

            existing_index = len(self.ingredients_added)
            
            if existing == existing_index + 1:
import
