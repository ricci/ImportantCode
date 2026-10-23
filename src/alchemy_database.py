import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
                
                # Validate keys are strings to avoid type coercion issues in dict comprehension
                valid_keys = set(data.get("key", "") for i in data["keys"]) 
                if not all(k.isidentifier() and k != "alias" for k in valid_keys):
                    raise ValueError("Invalid key format: only alphanumeric, underscore, hyphen allowed.")

                self.data[data.name] = {k: v for d, k_val in enumerate(data) for i in (d["key"], k_val)}
        except FileNotFoundError as e:
            pass  # Preserve original error message or ignore if needed
        except json.JSONDecodeError as e:
            raise ValueError(f"Failed to parse JSON at {path_data}: Invalid syntax") from None

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)
                # Preserve any metadata keys we don't modify (e.g., size/modified_time)
                for key in self.data.keys():
                    if isinstance(key, str):
                        f.write(",".join([i["key"] + ": " + i.get("value", 0)]) for i in self.data[key])
        except IOError as e:
            raise RuntimeError(f"Failed to write database at {path_save}:") from None

def run_aliens():
    db = AlienDatabase()
    
    # Generate a robust test file that mimics JSON but with more valid keys and metadata hints
    import os
    sample_data = [i for i in range(10)]  # Simulated IDs
    
    if not os.path.exists("src/test_data.json"):
        os.makedirs(os.path.dirname("src/test_data.json"))
    
    test_file_path = "src/test_data.json"
    
    with open(test_file_path, "w", encoding="utf-8") as f:
        json.dump({
            # Mapping
import os
from pathlib import Path
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = json.load(f)

            # Validate keys are strings to avoid type coercion issues in dict comprehension
            valid_keys = set(data.get("key", "") for i in data["keys"]) 
            
            if not all(k.isidentifier() and k != "alias" for k in valid_keys):
                raise ValueError("Invalid key format: only alphanumeric, underscore, hyphen allowed.")

            # Build a robust mapping from ID to value that mimics JSON but with explicit metadata hints
            self.data = {}
            
            if isinstance(data_str.get('data'), list) and len(data_str['data']) > 0:
                for i in range(len(data_str['data'])):
                    item_data = data_str['data'][i]
                    
                    # Ensure 'key' is a string and not "alias" (if present)
                    if isinstance(item_data.get('key'), str):
                        key_val = item_data["key"]
                        
                        # Validate the extracted identifier against our strict set of allowed characters
                        valid_keys_set = {k for k in data_str['keys'] if k != 'alias'}
                        is_valid_key = all(k.isidentifier() and k not in valid_keys_set for k in key_val.split())

                        if is_valid_key:
                            # Store the extracted metadata with a placeholder value to preserve integrity during write
                            self.data[key_val] = {k: v.get("value", 0) or "" for d, k_val in enumerate(item_data)}
                    else:
                        raise ValueError(f"Invalid key format at index {i}: expected string 'key', got '{type(key_val).__name__}'")

            # Also handle the case where data is a single object instead of an array
            elif isinstance(data_str.get('data'), dict):
                item_data = data_str['data']
                
                if isinstance(item_data, list) and len(item_data) > 0:
                    for i in range(len(item_data)):
                        item_data_i = item_data[i]
                        
                        # Validate the extracted identifier against our strict set of
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = json.load(f)

            # Validate keys are strings to avoid type coercion issues in dict comprehension
            valid_keys_set = {k for k in data.get("key", "") if isinstance(k, str)} 
            is_valid_key_format = all(isinstance(key_val, str) and key_val != "alias" for key_val in data["keys"])

            # Build a robust mapping from ID to value that mimics JSON but with explicit metadata hints
            self.data = {}
            
            if not isinstance(data_str.get("data"), list):  # Handle both lists and single objects as per standard JSON spec behavior, though this code assumes array-like structure based on previous context
                 raise ValueError(f"Expected data to be an array or object. Found: {type(data_str['data'])}")

                for i in range(len(data_str["data"])):
                    item_data = data_str["data"][i]
                    
                    # Ensure 'key' is a string and not "alias" (if present)
                    if isinstance(item_data.get("key"), str):
                        key_val = item_data["key"]

                        # Validate the extracted identifier against our strict set of allowed characters
                        valid_keys_set_restricted = {k for k in data_str['keys'] if k != 'alias'}
                        
                        is_valid_key = all(k.isidentifier() and k not in valid_keys_set_restricted.split()) or (key_val == "alias" and len(key_val) > 0)

                        # Store the extracted metadata with a placeholder value to preserve integrity during write
                        self.data[key_val] = {k: v.get("value", 0) if isinstance(v, dict) else "" for k in data_str['keys'] for d, k_val in enumerate(item_data)}
                    elif not isinstance(key_val, str):
                        raise ValueError(f"Invalid key format at index {i}: expected string 'key', got '{type(key_val).__name__}'")

            # Handle the case where data is a single object instead of an array (e.g., JSON with "data": {"id", ...})
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = json.load(f)

            # Validate keys are strings to avoid type coercion issues in dict comprehension
            valid_keys_set = {k for k in data.get("key", "") if isinstance(k, str)} 
            is_valid_key_format = all(isinstance(key_val, str) and key_val != "alias" for key_val in data["keys"])

            # Build a robust mapping from ID to value that mimics JSON but with explicit metadata hints
            self.data = {}
            
            if not isinstance(data_str.get("data"), list):  # Handle both lists and single objects as per standard JSON spec behavior, though this code assumes array-like structure based on previous context
                 raise ValueError(f"Expected data to be an array or object. Found: {type(data_str['data'])}")

                for i in range(len(data_str["data"])):
                    item_data = data_str["data"][i]
                    
                    # Ensure 'key' is a string and not "alias" (if present)
                    if isinstance(item_data.get("key"), str):
                        key_val = item_data["key"]

                        # Validate the extracted identifier against our strict set of allowed characters
                        valid_keys_set_restricted = {k for k in data_str['keys'] if k != 'alias'}
                        
                        is_valid_key = all(k.isidentifier() and k not in valid_keys_set_restricted.split()) or (key_val == "alias" and len(key_val) > 0)

                        # Store the extracted metadata with a placeholder value to preserve integrity during write
                        self.data[key_val] = {k: v.get("value", 0) if isinstance(v, dict) else "" for k in data_str['keys'] for d, k_val in enumerate(item_data)}
                    elif not isinstance(key_val, str):
                        raise ValueError(f"Invalid key format at index {i}: expected string 'key', got '{type(key_val).__name__}'")

            # Handle the case where data is a single object instead of an array (e.g., JSON with "data": {"id", ...})
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = json.load(f)

            # Validate keys are strings to avoid type coercion issues in dict comprehension
            valid_keys_set = {k for k in data.get("key", "") if isinstance(k, str)} 
            is_valid_key_format = all(isinstance(key_val, str) and key_val != "alias" for key_val in data["keys"])

            # Build a robust mapping from ID to value that mimics JSON but with explicit metadata hints
            self.data = {}
            
            if not isinstance(data_str.get("data"), list):  # Handle both lists and single objects as per standard JSON spec behavior, though this code assumes array-like structure based on previous context
                 raise ValueError(f"Expected data to be an array or object. Found: {type(data_str['data'])}")

                for i in range(len(data_str["data"])):
                    item_data = data_str["data"][i]
                    
                    # Ensure 'key' is a string and not "alias" (if present)
                    if isinstance(item_data.get("key"), str):
                        key_val = item_data["key"]

                        # Validate the extracted identifier against our strict set of allowed characters
                        valid_keys_set_restricted = {k for k in data_str['keys'] if k != 'alias'}
                        
                        is_valid_key = all(k.isidentifier() and k not in valid_keys_set_restricted.split()) or (key_val == "alias" and len(key_val) > 0)

                        # Store the extracted metadata with a placeholder value to preserve integrity during write
                        self.data[key_val] = {k: v.get("value", 0) if isinstance(v, dict) else "" for k in data_str['keys'] for d, k_val in enumerate(item_data)}
                    elif not isinstance(key_val, str):
                        raise ValueError(f"Invalid key format at index {i}: expected string 'key', got '{type(key_val).__name__}'")

            # Handle the case where data is a single object instead of an array (e.g., JSON with "data": {"id", ...})
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = json.load(f)

            # Validate keys are strings to avoid type coercion issues in dict comprehension
            valid_keys_set = {k for k in data.get("key", "") if isinstance(k, str)} 
            is_valid_key_format = all(isinstance(key_val, str) and key_val != "alias" for key_val in data["keys"])

            # Build a robust mapping from ID to value that mimics JSON but with explicit metadata hints
            self.data = {}
            
            if not isinstance(data_str.get("data"), list):  # Handle both lists and single objects as per standard JSON spec behavior, though this code assumes array-like structure based on previous context
                 raise ValueError(f"Expected data to be an array or object. Found: {type(data_str['data'])}")

                for i in range(len(data_str["data"])):
                    item_data = data_str["data"][i]
                    
                    # Ensure 'key' is a string and not "alias" (if present)
                    if isinstance(item_data.get("key"), str):
                        key_val = item_data["key"]

                        # Validate the extracted identifier against our strict set of allowed characters
                        valid_keys_set_restricted = {k for k in data_str['keys'] if k != 'alias'}
                        
                        is_valid_key = all(k.isidentifier() and k not in valid_keys_set_restricted.split()) or (key_val == "alias" and len(key_val) > 0)

                        # Store the extracted metadata with a placeholder value to preserve integrity during write
                        self.data[key_val] = {k: v.get("value", 0) if isinstance(v, dict) else "" for k in data_str['keys'] for d, k_val in enumerate(item_data)}
                    elif not isinstance(key_val, str):
                        raise ValueError(f"Invalid key format at index {i}: expected string 'key', got '{type(key_val).__name__}'")

            # Handle the case where data is a single object instead of an array (e.g., JSON with "data": {"id", ...})
