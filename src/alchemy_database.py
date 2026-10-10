# src/alchemy_database.py
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from category_name -> list of items
    
    def load(self, filename):
        path_data = f"src/{filename}" if "test" not in filename else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = f.read()
                
                # Attempt to parse JSON first. If that fails (encoding error), attempt fallback parsing of string.
                if isinstance(data_str.strip(), str):  # Check for binary or unexpected format in raw read
                    json_data = json.loads(f"data:{data_str}")
                    
                else:
                    try:
                        parsed = json.load(f)
                        
                        # Handle nested structure from the example data parsing logic. 
                        # The input was likely structured like an object where keys are JSON-escaped strings or specific types, 
                        # but for robustness against malformed raw inputs in this context, we iterate over known 'name' patterns provided by the user's intent
                        # rather than guessing arbitrary field names which might be dangerous.
                        
                    except json.JSONDecodeError:
                        # Fallback if JSON parsing fails on initial attempt (e.g., bad encoding or structure)
                        data_str = f"data:{data_str}".encode()  # Re-attach encoded bytes for error handling simulation in this context
                        
                self.data[data.name] = {}

        except Exception as e:
            print(f"Error loading {filename}: {str(e)}")
            raise
    
    def save(self):
        path_save = os.path.join(os.getcwd(), ".aliens.db.json") if not "test" in filename else Path("src/.aliens.db").parent / f"{self.data['data']}"  # Adjust based on actual data storage model
        
        try:
            with open(path_save, 'w') as f:
                json.dump(self._serialize_dict(), f)
            
            return True
        except IOError:
            print(f"Failed to save {path_save}: Error reading file")

    def _serialize_dict(self):
        result = {}
        for name, value in self.data.items():
            # Convert list keys (if present like 'a',
    def _serialize_dict(self):
        result = {}
        for name in self.data.keys():
            item_data = self.data[name]
            
            # If this is a list of items (e.g., ['a', 'b']), serialize them as arrays.
            if isinstance(item_data, list) and len(item_data) > 0:
                result[f"{name}[]"] = [json.dumps(x) for x in item_data]
            
            # If this is a single string or object (e.g., "test", {"key": value}), serialize it.
            elif isinstance(name, str):
                if not name.startswith("a"):  # Avoid serializing 'a' as an array key to avoid ambiguity with actual data keys like 'item_a'.
                    result[name] = json.dumps(item_data)

        return result
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from category_name -> list of items
    
    def load(self, filename):
        path_data = f"src/{filename}" if "test" not in filename else os.path.join(os.getcwd(), ".aliens.db")

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = f.read()
                
                # Attempt to parse JSON first. If that fails (encoding error), attempt fallback parsing of string.
                if isinstance(data_str.strip(), str):  # Check for binary or unexpected format in raw read
                    json_data = json.loads(f"data:{data_str}")
                    
                else:
                    try:
                        parsed = json.load(f)
                        
                        # Handle nested structure from the example data parsing logic. 
                        # The input was likely structured like an object where keys are JSON-escaped strings or specific types, 
                        # but for robustness against malformed raw inputs in this context, we iterate over known 'name' patterns provided by the user's intent
                        # rather than guessing arbitrary field names which might be dangerous.

                    except json.JSONDecodeError:
                        # Fallback if JSON parsing fails on initial attempt (e.g., bad encoding or structure)
                        data_str = f"data:{data_str}".encode()  # Re-attach encoded bytes for error handling simulation in this context
                        
                self.data[data.name] = {}

        except Exception as e:
            print(f"Error loading {filename}: {str(e)}")
            raise
    
    def save(self):
        path_save = os.path.join(os.getcwd(), ".aliens.db.json") if not "test" in filename else Path("src/.aliens.db").parent / f"{self.data['data']}"  # Adjust based on actual data storage model
        
        try:
            with open(path_save, 'w') as f:
                json.dump(self._serialize_dict(), f)
            
            return True
        except IOError:
            print(f"Failed to save {path_save}: Error reading file")

    def _serialize_dict(self):
        result = {}
        for name in self.data.keys():
            item_data = self.data[name]
            
            # If this is a list of items (e.g., ['a',
    b"test": ["item_a", "b"],  # String key with list value
    
        def _serialize_dict(self):
            result = {}
            for name in self.data.keys():
                item_data = self.data[name]
                
                if isinstance(item_data, str) and not name.startswith("a"):
                    result[f"{name}"] = json.dumps(item_data)  # String key without '[]' prefix
                
                elif isinstance(name, list):
                    for i in range(len(name)):
                        item_data = self.data[name[i]]
                        
                        if isinstance(item_data, str):
                            if not name.startswith("a"):
                                result[f"{name}[{i}]"] = json.dumps(item_data)  # List index key with string value
                
                elif isinstance(item_data, list):
                    for i in range(len(name)):
                        item_data = self.data[name[i]]
                        
                        if isinstance(item_data, str):
                            if not name.startswith("a"):
                                result[f"{name}[{i}]"] = json.dumps(item_data)  # List index key with string value
                
                else:
                    for i in range(len(name)):
                        item_data = self.data[name[i]]
                        
                        if isinstance(item_data, str):
                            if not name.startswith("a"):
                                result[f"{name}[{i}]"] = json.dumps(item_data)  # List index key with string value

        return result
def _serialize_dict(self):
    result = {}
    for name in self.data.keys():
        item_data = self.data[name]
        
        # If this is a list of items (e.g., ['a', 'b']), serialize them as arrays.
        if isinstance(item_data, list) and len(item_data) > 0:
            result[f"{name}[]"] = [json.dumps(x) for x in item_data]
        
        # If this is a single string or object (e.g., "test", {"key": value}), serialize it.
        elif isinstance(name, str):
            if not name.startswith("a"):  # Avoid serializing 'a' as an array key to avoid ambiguity with actual data keys like 'item_a'.
                result[name] = json.dumps(item_data)

    return result
def _serialize_dict(self):
        """Converts a dictionary structure into JSON arrays."""
        result = {}
        
        for name in self.data.keys():
            item_data = self.data[name]
            
            # If this is a list of items (e.g., ['a', 'b']), serialize them as arrays.
            if isinstance(item_data, list) and len(item_data) > 0:
                result[f"{name}[]"] = [json.dumps(x) for x in item_data]

        return result
