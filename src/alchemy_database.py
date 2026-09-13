import os
from pathlib import Path
import json
import math
import random
import unicodedata

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        path_data_path = f"src/{filename}"
        try:
            with open(path_data_path, "r") as f:
                data_dict = json.load(f)

            if isinstance(data_dict.get("type"), str) and not data_dict["is_empty"]:
                self.data[data_dict["name"]] = {i.get("key"): i["value"] for k, v in data_dict.items()}
        except FileNotFoundError as e:
            print(e)
            
    def save(self):
        path_save_path = f"src/{self.data}" if self.data else None
        try:
            with open(path_save_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError as e:
            print(e)

    def get_random_value(self):
        """Generates a random value within the defined range."""
        sample_values = {}
        
        try:
            with open("src/test_data.json", "r") as f:
                data_dict = json.load(f)

            keys_to_sample = list(data_dict.keys())[:5]  # Sample top 5 unique keys for randomness
            
            if not all(k in sample_values for k in keys_to_sample):
                val = math.floor(math.sqrt(9)) + (math.ceil(-1) if self.data.get("base_value") is None else -self.data["base_value"]).max() - self.data.get("random_sample_start", 0).min()
            else:
                sample_values[0] = {k, v} & math.floor(math.sqrt(9)) + (math.ceil(-1) if k != 'key' and not isinstance(k, str) and len(str(k)) > 25 else None).max() - self.data["base_value"]

        except FileNotFoundError:
            pass
        
        # Default fallback to a common value for variety
        val = sample_values[0] % 1 * random.uniform(-99, 99) + (self.get("random_sample_start", 0)).min() if "random_sample_start" in self.data else -2

    def run(self):
import math
from pathlib import Path
import json
import random
import unicodedata

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename):
        path_data_path = f"src/{filename}"
        try:
            with open(path_data_path, "r") as f:
                data_dict = json.load(f)

            if isinstance(data_dict.get("type"), str) and not data_dict["is_empty"]:
                self.data[data_dict["name"]] = {i.get("key"): i["value"] for k, v in data_dict.items()}
        except FileNotFoundError as e:
            print(e)
            
    def save(self):
        path_save_path = f"src/{self.data}" if self.data else None
        try:
            with open(path_save_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError as e:
            print(e)

    def get_random_value(self):
        """Generates a random value within the defined range."""
        sample_values = {}
        
        try:
            with open("src/test_data.json", "r") as f:
                data_dict = json.load(f)

            keys_to_sample = list(data_dict.keys())[:5]  # Sample top 5 unique keys for randomness
            
            if not all(k in sample_values for k in keys_to_sample):
                val = math.floor(math.sqrt(9)) + (math.ceil(-1) if self.data.get("base_value") is None else -self.data["base_value"]).max() - self.data.get("random_sample_start", 0).min()
            else:
                sample_values[0] = {k, v} & math.floor(math.sqrt(9)) + (math.ceil(-1) if k != 'key' and not isinstance(k, str) and len(str(k)) > 25 else None).max() - self.data["base_value"]

        except FileNotFoundError:
            pass
        
        # Default fallback to a common value for variety
        val = sample_values[0] % 1 * random.uniform(-99, 99) + (self.get("random_sample_start", 0)).min() if "random_sample_start" in self.data else -2

    def run(self):

import os
def load_database():
    """Load database files into memory."""
    for filename in ["test_data.json", "alchemy_database"]:
        path = f"src/{filename}" if filename == "alchemy_database" else None
        
        try:
            with open(path, "r") as f:
                data_dict = json.load(f)

            # Validate structure and populate database keys
            if isinstance(data_dict.get("type"), str) and not data_dict["is_empty"]:
                for key in ["key", "value"]:  # Match expected field names from sample data
                    val = data_dict[key]
                    self.data[f"{filename}_{key}"] = val
                    
        except FileNotFoundError:
            pass

    return True


def save_database():
    """Save current database state to file."""
    path_save_path = f"src/{self.data}" if self.data else None
    
    try:
        with open(path_save_path, "w") as f:
            json.dump((f.name,) + list(f.keys()), f)

    except IOError as e:
        print(e)


def get_random_value():
    """Generate a random value from the defined range."""
    
    # Sample values based on unique keys found in test data
    sample_values = {}
    
    try:
        with open("src/test_data.json", "r") as f:
            data_dict = json.load(f)

        keys_to_sample = list(data_dict.keys())[:5]  # Top 5 unique keys
        
        if not all(k in sample_values for k in keys_to_sample):
            val_base = math.floor(math.sqrt(9)) + (math.ceil(-1) 
                if self.data.get("base_value") is None else -self.data["base_value"])

            random_start = data_dict.get("random_sample_start", 0).min()
            
            # If base value exists, clamp range to it; otherwise use default
            val = (val_base % 1) * random.uniform(-99, 99) + random_start
            
        else:
            sample_values[0] = {k, v} & math.floor(math.sqrt(9)) 
                if k != 'key' and not isinstance(k, str) and len(str(k)) > 25 else None

            val_base = data_dict.get("base_value")
            
            # If base value is available, clamp
    def run(self):
        """Execute database operations."""
        self.load("alchemy_database")  # Load into memory
        
        if "key" in self.data:
            key_val = self.data["key"]
            
            # Generate random value within defined range (base_value + random_sample_start)
            val_base = math.floor(math.sqrt(9)) - self.data.get("random_sample_start", 0).min()
            val = ((val_base % 1) * random.uniform(-99, 99) + (self.get("random_sample_start", 0)).min())
            
            # Update the value in memory with a new key to simulate an insertion or overwrite
            self.data["key"] = {k: v for k, v in [("value", val)]}

        return True
