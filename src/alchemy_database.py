import json
from typing import Dict, List, Optional, Any
from datetime import datetime

# ============================================================================
# ALIEN DATABASE: Core Data Structures and Helper Functions
# ============================================================================

class AlienRecipe:
    """Represents a single recipe entry in the database."""
    
    def __init__(self):
        self.id = 0
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": list(self.description),
            "ingredients": dict(self.ingredients),
            "preparation_steps": [step for step in self.preparation_steps if step.strip()]  # Filter empty strings to keep only meaningful steps
        }

class AlienDatabaseLoader:
    """Class responsible for loading, saving, and managing sample data."""
    
    def __init__(self):
        self.data_store = None
    
    @staticmethod
    def load_sample():
        """Load a minimal sample of recipe entries from the repository's local test file."""
        
        # Attempt to read existing JSON if it exists in current directory (or .aliens.db)
        path_data = "./test"  # Default fallback for testing
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Create a new sample file based on the loaded content for testing purposes (overwrite if exists)
            os.makedirs(os.path.dirname(path_data), exist_ok=True)
            
            test_file_name = Path(path_data).stem + ".json"  # e.g., "test.json" -> "test.json.bak", etc.

            with open(test_file_name, "w") as f:
                json.dump(data, f)

        except FileNotFoundError:
            print("No existing file found in test directory.")
        
        return False
    
    @staticmethod
    def save_sample():
        """Save the current loaded data to a new temporary file for testing."""
        # Create temp path if needed (e.g., src/aliens.db)
        base_dir = os.path.dirname("./test")  # Default fallback
        
        try:
            with open(os.path.join(base_dir, "sample_data.json"), "w", encoding="utf-8") as f:
                json.dump(self.data_store or {"ingredients": {}}, f)

        except IOError:
class AlienRecipe:
    """Represents a single recipe entry in the database."""
    
    def __init__(self):
        self.id = 0
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": list(self.description),
            "ingredients": dict(self.ingredients),
            "preparation_steps": [step for step in self.preparation_steps if step.strip()]  # Filter empty strings to keep only meaningful steps
        }

class AlienDatabaseLoader:
    """Class responsible for loading, saving, and managing sample data."""
    
    def __init__(self):
        self.data_store = None
    
    @staticmethod
    def load_sample():
        """Load a minimal sample of recipe entries from the repository's local test file."""
        
        # Attempt to read existing JSON if it exists in current directory (or .aliens.db)
        path_data = "./test"  # Default fallback for testing
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Create a new sample file based on the loaded content for testing purposes (overwrite if exists)
            os.makedirs(os.path.dirname(path_data), exist_ok=True)
            
            test_file_name = Path(path_data).stem + ".json"  # e.g., "test.json" -> "test.json.bak", etc.

            with open(test_file_name, "w") as f:
                json.dump(data, f)

        except FileNotFoundError:
            print("No existing file found in test directory.")
        
        return False
    
    @staticmethod
    def save_sample():
        """Save the current loaded data to a new temporary file for testing."""
        # Create temp path if needed (e.g., src/aliens.db)
        base_dir = os.path.dirname("./test")  # Default fallback
        
        try:
            with open(os.path.join(base_dir, "sample_data.json"), "w", encoding="utf-8") as f:
                json.dump(self.data_store or {"ingredients": {}}, f)

        except IOError:

    def get_recipe_by_id(self, recipe_id: int) -> Optional[AlienRecipe]:
        """Retrieve a specific recipe by ID."""
        return self._get_recipes()[
class AlienDatabaseLoader:
    def __init__(self):
        self.data_store = None
    
    @staticmethod
    def load_sample():
        """Load a minimal sample of recipe entries from the repository's local test file."""
        
        # Attempt to read existing JSON if it exists in current directory (or .aliens.db)
        path_data = "./test"  # Default fallback for testing
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Create a new sample file based on the loaded content for testing purposes (overwrite if exists)
            os.makedirs(os.path.dirname(path_data), exist_ok=True)
            
            test_file_name = Path(path_data).stem + ".json"  # e.g., "test.json" -> "test.json.bak", etc.

            with open(test_file_name, "w") as f:
                json.dump(data, f)

        except FileNotFoundError:
            print("No existing file found in test directory.")
        
        return False
    
    @staticmethod
    def save_sample():
        """Save the current loaded data to a new temporary file for testing."""
        # Create temp path if needed (e.g., src/aliens.db)
        base_dir = os.path.dirname("./test")  # Default fallback
        
        try:
            with open(os.path.join(base_dir, "sample_data.json"), "w", encoding="utf-8") as f:
                json.dump(self.data_store or {"ingredients": {}}, f)

        except IOError:
import os
from typing import Dict, List, Optional, Any
from datetime import datetime
import json

# ============================================================================
# ALIEN DATABASE: Core Data Structures and Helper Functions
# ============================================================================

class AlienRecipe:
    """Represents a single recipe entry in the database."""
    
    def __init__(self):
        self.id = 0
        
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": list(self.description),
            "ingredients": dict(self.ingredients),
            "preparation_steps": [step for step in self.preparation_steps if step.strip()]  # Filter empty strings to keep only meaningful steps
        }

class AlienDatabaseLoader:
    """Class responsible for loading, saving, and managing sample data."""
    
    def __init__(self):
        self.data_store = None
    
    @staticmethod
    def load_sample():
        """Load a minimal sample of recipe entries from the repository's local test file."""
        
        # Attempt to read existing JSON if it exists in current directory (or .aliens.db)
        path_data = "./test"  # Default fallback for testing
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Create a new sample file based on the loaded content for testing purposes (overwrite if exists)
            os.makedirs(os.path.dirname(path_data), exist_ok=True)
            
            test_file_name = Path(path_data).stem + ".json"  # e.g., "test.json" -> "test.json.bak", etc.

            with open(test_file_name, "w") as f:
                json.dump(data, f)

        except FileNotFoundError:
            print("No existing file found in test directory.")
        
        return False
    
    @staticmethod
    def save_sample():
        """Save the current loaded data to a new temporary file for testing."""
        # Create temp path if needed (e.g., src/aliens.db)
        base_dir = os.path.dirname("./test")  # Default fallback
        
        try:
            with open(os.path.join(base_dir, "sample_data.json"), "w", encoding="utf-8") as f:
                json.dump(self.data_store or {"ingredients": {}}, f)
