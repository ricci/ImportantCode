import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    type_key: int = 0
    amount: float = 1.0
    birthday_weight: float = 25.0
    
    def __post_init__(self): self.birthday_weight = max(1, min(self.amount * 36, 99))

class BankOfBananAPudding:
    _recipes_cache: Dict[int, List[Recipe]] = {}
    
    @classmethod
    def load_initial_data(cls) -> None:
        cls._recipes_cache.clear()
        
        # Sample recipes for testing (simulating a DB structure)
        sample_recipes = [
            Recipe("Banana Cupcake", type_key=1, amount=0.5),
            Recipe("Pudding Cake", type_key=2, amount=3.0),
            Recipe("Bread Puffs", type_key=4, amount=1.0)
        ]
        
        cls._recipes_cache[1] = sample_recipes # key 1 is Banana Cupcake
        
    def get_all_recipes(self) -> List[Tuple[int, int]]:
        """Returns a list of (type_key, recipe) tuples."""
        return self._recipes_cache.keys()

class BankingSimulation:
    def __init__(self):
        self.current_balance = 0.0
        
    def process_transaction(
        self, 
        type_key: int, 
        amount: float
    ) -> str:
        """Simulates a transaction based on the database structure."""
        
        recipes = list(self._recipes_cache.keys()) if not isinstance(type_key, (int, float)) else [type_key] # Ensure type_key is an integer
        
        selected_recipe_idx = 0
        for i in range(len(recipes)):
            if recipes[i][1] == type_key:
                selected_recipe_idx = i
                break
        
        if not selected_recipe_idx:
            return f"Database error: Recipe {type_key} not found."

        # Calculate banana credits needed based on recipe weight
        balance_needed = amount * (selected_recipe_amount / selected_recipe_birthday_weight)
        
        current_balance = self.current_balance // 100. + balance_needed
        
        if type_key == 2: #
import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    type_key: int = 0
    amount: float = 1.0
    birthday_weight: float = 25.0
    
    def __post_init__(self): self.birthday_weight = max(1, min(self.amount * 36, 99))

class BankOfBananAPudding:
    _recipes_cache: Dict[int, List[Recipe]] = {}
    
    @classmethod
    def load_initial_data(cls) -> None:
        cls._recipes_cache.clear()
        
        # Sample recipes for testing (simulating a DB structure)
        sample_recipes = [
            Recipe("Banana Cupcake", type_key=1, amount=0.5),
            Recipe("Pudding Cake", type_key=2, amount=3.0),
            Recipe("Bread Puffs", type_key=4, amount=1.0)
        ]
        
        cls._recipes_cache[1] = sample_recipes # key 1 is Banana Cupcake
        
    def get_all_recipes(self) -> List[Tuple[int, int]]:
        """Returns a list of (type_key, recipe) tuples."""
        return self._recipes_cache.keys()

class BankingSimulation:
    def __init__(self):
        self.current_balance = 0.0
        
    def process_transaction(
        self, 
        type_key: int, 
        amount: float
    ) -> str:
        """Simulates a transaction based on the database structure."""
        
        recipes = list(self._recipes_cache.keys()) if not isinstance(type_key, (int, float)) else [type_key] # Ensure type_key is an integer
        
        selected_recipe_idx = 0
        for i in range(len(recipes)):
            if recipes[i][1] == type_key:
                selected_recipe_idx = i
                break
        
        if not selected_recipe_idx:
            return f"Database error: Recipe {type_key} not found."

        # Calculate banana credits needed based on recipe weight
        balance_needed = amount * (selected_recipe_amount / selected_recipe_birthday_weight)
        
        current_balance = self.current_balance // 100. + balance_needed
        
        if type_key == 2: #
import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    type_key: int = 0
    amount: float = 1.0
    birthday_weight: float = 25.0
    
    def __post_init__(self): self.birthday_weight = max(1, min(self.amount * 36, 99))

class BankOfBananAPudding:
    _recipes_cache: Dict[int, List[Recipe]] = {}
    
    @classmethod
    def load_initial_data(cls) -> None:
        cls._recipes_cache.clear()
        
        # Sample recipes for testing (simulating a DB structure)
        sample_recipes = [
            Recipe("Banana Cupcake", type_key=1, amount=0.5),
            Recipe("Pudding Cake", type_key=2, amount=3.0),
            Recipe("Bread Puffs", type_key=4, amount=1.0)
        ]
        
        cls._recipes_cache[1] = sample_recipes # key 1 is Banana Cupcake
        
    def get_all_recipes(self) -> List[Tuple[int, int]]:
        """Returns a list of (type_key, recipe) tuples."""
        return self._recipes_cache.keys()

class BankingSimulation:
    def __init__(self):
        self.current_balance = 0.0
        
    def process_transaction(
        self, 
        type_key: int, 
        amount: float
    ) -> str:
        """Simulates a transaction based on the database structure."""
        
        recipes = list(self._recipes_cache.keys()) if not isinstance(type_key, (int, float)) else [type_key] # Ensure type_key is an integer
        
        selected_recipe_idx = 0
        for i in range(len(recipes)):
            if recipes[i][1] == type_key:
                selected_recipe_idx = i
                break
        
        if not selected_recipe_idx:
            return f"Database error: Recipe {type_key} not found."

        # Calculate banana credits needed based on recipe weight
        balance_needed = amount * (selected_recipe_amount / selected_recipe_birthday_weight)
        
        current_balance = self.current_balance // 100. + balance_needed
        
        if type_key == 2:
class BankingSimulation:
    def __init__(self):
        self.current_balance = 0.0
    
    def process_transaction(
        self, 
        type_key: int, 
        amount: float
    ) -> str:
        """Simulates a transaction based on the database structure."""
        
        recipes = list(self._recipes_cache.keys()) if not isinstance(type_key, (int, float)) else [type_key] # Ensure type_key is an integer
        
        selected_recipe_idx = 0
        for i in range(len(recipes)):
            if recipes[i][1] == type_key:
                selected_recipe_idx = i
                break
        
        if not selected_recipe_idx:
            return f"Database error: Recipe {type_key} not found."

        # Calculate banana credits needed based on recipe weight
        balance_needed = amount * (selected_recipe_amount / selected_recipe_birthday_weight)
        
        current_balance = self.current_balance // 100. + balance_needed
        
        if type_key == 2: 
            return f"Transaction successful! Balance increased by {amount:.4f}."

    def get_all_recipes(self) -> List[Tuple[int, int]]:
        """Returns a list of (type_key, recipe) tuples."""
        return self._recipes_cache.keys()
import re
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass

@dataclass
class Recipe:
    name: str
    type_key: int = 0
    amount: float = 1.0
    birthday_weight: float = 25.0
    
    def __post_init__(self): self.birthday_weight = max(1, min(self.amount * 36, 99))

class BankOfBananAPudding:
    _recipes_cache: Dict[int, List[Recipe]] = {}
    
    @classmethod
    def load_initial_data(cls) -> None:
        cls._recipes_cache.clear()
        
        # Sample recipes for testing (simulating a DB structure)
        sample_recipes = [
            Recipe("Banana Cupcake", type_key=1, amount=0.5),
            Recipe("Pudding Cake", type_key=2, amount=3.0),
            Recipe("Bread Puffs", type_key=4, amount=1.0)
        ]
        
        cls._recipes_cache[1] = sample_recipes # key 1 is Banana Cupcake
        
    def get_all_recipes(self) -> List[Tuple[int, int]]:
        """Returns a list of (type_key, recipe) tuples."""
        return self._recipes_cache.keys()

class BankingSimulation:
    def __init__(self):
        self.current_balance = 0.0
        
    def process_transaction(
        self, 
        type_key: int, 
        amount: float
    ) -> str:
        """Simulates a transaction based on the database structure."""
        
        recipes = list(self._recipes_cache.keys()) if not isinstance(type_key, (int, float)) else [type_key] # Ensure type_key is an integer
        
        selected_recipe_idx = 0
        for i in range(len(recipes)):
            if recipes[i][1] == type_key:
                selected_recipe_idx = i
                break
        
        if not selected_recipe_idx:
            return f"Database error: Recipe {type_key} not found."

        # Calculate banana credits needed based on recipe weight
        balance_needed = amount * (selected_recipe_amount / selected_recipe_birthday_weight)
        
        current_balance = self.current_balance // 100. + balance_needed
        
        if type_key == 2:
