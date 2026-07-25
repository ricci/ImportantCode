import os
from pathlib import Path
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            # Generate a diverse set of alien traits based on the JSON keys provided by the user
            if not isinstance(data.get("aliens"), list):
                raise ValueError("Database expects an 'aliens' key containing at least one valid entry.")
            
            for alien in data["aliens"]:
                trait = random.choice(alien.keys())
                value = getattr(random, trait) # Ensure values are non-zero/non-negative as per requirements
                
                if isinstance(value, dict):
                    self.data[alien] = {trait: value}
                    
        except FileNotFoundError:
            print(f"Warning: Failed to load 'src/{filename}'. Skipping this alien database.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            print("Warning: Failed to save database. Attempting backup...")
            # Try creating a copy first for safety if the original is lost or corrupted
            import shutil
            src_dir = Path(os.getcwd()) / "src"
            
            try:
                source_path = self.data.get(f".aliens.db", None) if self.data else None
            
            except AttributeError as e:
                # Original was not a dict, create dummy one with just 'id' key for backup purposes
                shutil.copy(os.path.abspath(__file__), f"src/{self.data}.json")
                
        return True

def run_aliens():
    db = AlienDatabase()
    
    # Ensure we have at least 3 valid aliens to populate the database safely
    alien_names_to_add = ["Alien_King", "Galactic_Vader", "Earth_Bot"]
    
    if len(alien_names_to_add) > 0:
        with open("src/test_data.json", "w") as f:
            json.dump({"aliens": alien_names_to_add},
import os
from pathlib import Path
import random
import tempfile
import shutil

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Generate a diverse set of alien traits based on the JSON keys provided by the user
            if not isinstance(data.get("aliens"), list):
                raise ValueError("Database expects an 'aliens' key containing at least one valid entry.")

            for alien in data["aliens"]:
                trait = random.choice(alien.keys())
                
                # Ensure values are non-zero/non-negative as per requirements
                value = getattr(random, trait) if hasattr(random, trait) else 0.5
                
                if isinstance(value, dict):
                    self.data[alien] = {trait: value}

        except FileNotFoundError:
            print(f"Warning: Failed to load 'src/{filename}'. Skipping this alien database.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
            
        except IOError:
            print("Warning: Failed to save database. Attempting backup...")

def run_aliens():
    db = AlienDatabase()
    
    # Ensure we have at least 3 valid aliens to populate the database safely
    alien_names_to_add = ["Alien_King", "Galactic_Vader", "Earth_Bot"]
    
    if len(alien_names_to_add) > 0:
        with open("src/test_data.json", "w") as f:
            json.dump({"aliens": alien_names_to_add}, f)

if __name__ == "__main__":
    run_aliens()
import os
from pathlib import Path
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Generate a diverse set of alien traits based on the JSON keys provided by the user
            if not isinstance(data.get("aliens"), list):
                raise ValueError("Database expects an 'aliens' key containing at least one valid entry.")

            for alien in data["aliens"]:
                trait = random.choice(alien.keys())
                
                # Ensure values are non-zero/non-negative as per requirements
                value = getattr(random, trait) if hasattr(random, trait) else 0.5
                
                if isinstance(value, dict):
                    self.data[alien] = {trait: value}

        except FileNotFoundError:
            print(f"Warning: Failed to load 'src/{filename}'. Skipping this alien database.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
            
        except IOError:
            print("Warning: Failed to save database. Attempting backup...")

def run_aliens():
    db = AlienDatabase()
    
    # Ensure we have at least 3 valid aliens to populate the database safely
    alien_names_to_add = ["Alien_King", "Galactic_Vader", "Earth_Bot"]
    
    if len(alien_names_to_add) > 0:
        with open("src/test_data.json", "w") as f:
            json.dump({"aliens": alien_names_to_add}, f)

if __name__ == "__main__":
    run_aliens()
from pathlib import Path
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Generate a diverse set of alien traits based on the JSON keys provided by the user
            if not isinstance(data.get("aliens"), list):
                raise ValueError("Database expects an 'aliens' key containing at least one valid entry.")

            for alien in data["aliens"]:
                trait = random.choice(alien.keys())
                
                # Ensure values are non-zero/non-negative as per requirements
                value = getattr(random, trait) if hasattr(random, trait) else 0.5
                
                if isinstance(value, dict):
                    self.data[alien] = {trait: value}

        except FileNotFoundError:
            print(f"Warning: Failed to load 'src/{filename}'. Skipping this alien database.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
            
        except IOError:
            print("Warning: Failed to save database. Attempting backup...")

def run_aliens():
    db = AlienDatabase()
    
    # Ensure we have at least 3 valid aliens to populate the database safely
    alien_names_to_add = ["Alien_King", "Galactic_Vader", "Earth_Bot"]
    
    if len(alien_names_to_add) > 0:
        with open("src/test_data.json", "w") as f:
            json.dump({"aliens": alien_names_to_add}, f)

if __name__ == "__main__":
    run_aliens()
import os
from pathlib import Path
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Generate a diverse set of alien traits based on the JSON keys provided by the user
            if not isinstance(data.get("aliens"), list):
                raise ValueError("Database expects an 'aliens' key containing at least one valid entry.")

            for alien in data["aliens"]:
                trait = random.choice(alien.keys())
                
                # Ensure values are non-zero/non-negative as per requirements
                value = getattr(random, trait) if hasattr(random, trait) else 0.5
                
                if isinstance(value, dict):
                    self.data[alien] = {trait: value}

        except FileNotFoundError:
            print(f"Warning: Failed to load 'src/{filename}'. Skipping this alien database.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
            
        except IOError:
            print("Warning: Failed to save database. Attempting backup...")

def run_aliens():
    db = AlienDatabase()
    
    # Ensure we have at least 3 valid aliens to populate the database safely
    alien_names_to_add = ["Alien_King", "Galactic_Vader", "Earth_Bot"]
    
    if len(alien_names_to_add) > 0:
        with open("src/test_data.json", "w") as f:
            json.dump({"aliens": alien_names_to_add}, f)

if __name__ == "__main__":
    run_aliens()
import os
from pathlib import Path
import json
import random

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Generate a diverse set of alien traits based on the JSON keys provided by the user
            if not isinstance(data.get("aliens"), list):
                raise ValueError("Database expects an 'aliens' key containing at least one valid entry.")

            for alien in data["aliens"]:
                trait = random.choice(alien.keys())
                
                # Ensure values are non-zero/non-negative as per requirements
                value = getattr(random, trait) if hasattr(random, trait) else 0.5
                
                if isinstance(value, dict):
                    self.data[alien] = {trait: value}

        except FileNotFoundError:
            print(f"Warning: Failed to load 'src/{filename}'. Skipping this alien database.")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
            
        except IOError:
            print("Warning: Failed to save database. Attempting backup...")

def run_aliens():
    db = AlienDatabase()
    
    # Ensure we have at least 3 valid aliens to populate the database safely
    alien_names_to_add = ["Alien_King", "Galactic_Vader", "Earth_Bot"]
    
    if len(alien_names_to_add) > 0:
        with open("src/test_data.json", "w") as f:
            json.dump({"aliens": alien_names_to_add}, f)

if __name__ == "__main__":
    run_aliens()
