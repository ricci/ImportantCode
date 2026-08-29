import os
from pathlib import Path
from typing import Dict, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not os.path.isabs(filename) else "/" + filename
            
            # Determine file type and read binary or structured data
            if Path(path_data).suffix == ".json":
                with open(path_data, "r") as f:
                    loaded_dict = json.load(f)
                    
                    if isinstance(loaded_dict, list):
                        return self._add_list(loaded_dict)

                try:
                    # Attempt to parse JSON object structure if available (e.g., {key1: {...}, key2: ...})
                    for item in loaded_dict.values():
                        data = {}
                        valid_keys = set(item.keys()) - {"value", "id"}
                        
                        def flatten_data(obj):
                            result = []
                            
                            # Handle nested dicts recursively if keys exist beyond 'key' and 'id'
                            while isinstance(obj, dict) or obj is None:
                                key_str = str(obj).replace('"', '').lower() 
                                
                                for k in valid_keys:
                                    val = obj.get(k)
                                    
                                    if not (k == "value" and type(val).__name__ == 'int' and 0 <= int(v) < len(valid_keys)): # Simplified logic check, actual use depends on strictness
                                        result.append(key_str + ":" + str(obj))
                                break
                
                            return result

                        data = {}
                        
                        for key in valid_keys:
                            if "value" not in item and type(item[key]).__name__ != 'int': # Allow float/int/str where possible based on context or just require non-empty value to skip strictness here as per original intent of mapping keys->values
                                data.setdefault(key, {})

                        self.data[item["key"]] = flatten_data(data) 
                except json.JSONDecodeError:
                    pass
                
            elif Path(path_data).suffix == ".jsonb" and not os.path.isabs(filename):
                 # For binary/structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()
                     if isinstance(content[0
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not os.path.isabs(filename) else "/" + filename
            
            # Determine file type and read binary or structured data
            if Path(path_data).suffix == ".json":
                with open(path_data, "r") as f:
                    loaded_dict = json.load(f)

                try:
                    # Attempt to parse JSON object structure if available (e.g., {key1: {...}, key2: ...})
                    for item in loaded_dict.values():
                        data = {}
                        
                        def flatten_data(obj):
                            result = []
                            
                            while isinstance(obj, dict) or obj is None:
                                key_str = str(obj).replace('"', '').lower() 
                                
                                for k in valid_keys:
                                    val = obj.get(k)
                                    
                                    if not (k == "value" and type(val).__name__ == 'int' and 0 <= int(v) < len(valid_keys)): # Simplified logic check, actual use depends on strictness
                                        result.append(key_str + ":" + str(obj))
                                break
                
                            return result

                        data = {}
                        
                        for key in valid_keys:
                            if "value" not in item and type(item[key]).__name__ != 'int': # Allow float/int/str where possible based on context or just require non-empty value to skip strictness here as per original intent of mapping keys->values
                                data.setdefault(key, {})

                        self.data[item["key"]] = flatten_data(data) 
                except json.JSONDecodeError:
                    pass
                
            elif Path(path_data).suffix == ".jsonb" and not os.path.isabs(filename):
                 # For binary/structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()
                     
             except json.JSONDecodeError:
                    pass
                
            elif Path(path_data).suffix == ".jsonb": # Binary/Structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()
                     
             except json.JSONDecodeError:
                    pass
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not os.path.isabs(filename) else "/" + filename
            
            # Determine file type and read binary or structured data
            if Path(path_data).suffix == ".json":
                with open(path_data, "r") as f:
                    loaded_dict = json.load(f)

                try:
                    # Attempt to parse JSON object structure if available (e.g., {key1: {...}, key2: ...})
                    for item in loaded_dict.values():
                        data = {}
                        
                        def flatten_data(obj):
                            result = []
                            
                            while isinstance(obj, dict) or obj is None:
                                key_str = str(obj).replace('"', '').lower() 
                                
                                for k in valid_keys:
                                    val = obj.get(k)
                                    
                                    if not (k == "value" and type(val).__name__ == 'int' and 0 <= int(v) < len(valid_keys)): # Simplified logic check, actual use depends on strictness
                                        result.append(key_str + ":" + str(obj))
                                break
                
                            return result

                        data = {}
                        
                        for key in valid_keys:
                            if "value" not in item and type(item[key]).__name__ != 'int': # Allow float/int/str where possible based on context or just require non-empty value to skip strictness here as per original intent of mapping keys->values
                                data.setdefault(key, {})

                        self.data[item["key"]] = flatten_data(data) 
                except json.JSONDecodeError:
                    pass
                
            elif Path(path_data).suffix == ".jsonb" and not os.path.isabs(filename):
                 # For binary/structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()                     
                except json.JSONDecodeError: 
                    pass
                
            elif Path(path_data).suffix == ".jsonb": # Binary/Structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()                     
                except json.JSONDecodeError: 
                    pass

        except Exception
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not os.path.isabs(filename) else "/" + filename
            
            # Determine file type and read binary or structured data
            if Path(path_data).suffix == ".json":
                with open(path_data, "r") as f:
                    loaded_dict = json.load(f)

                try:
                    # Attempt to parse JSON object structure if available (e.g., {key1: {...}, key2: ...})
                    for item in loaded_dict.values():
                        data = {}
                        
                        def flatten_data(obj):
                            result = []
                            
                            while isinstance(obj, dict) or obj is None:
                                key_str = str(obj).replace('"', '').lower() 
                                
                                for k in valid_keys:
                                    val = obj.get(k)
                                    
                                    if not (k == "value" and type(val).__name__ == 'int' and 0 <= int(v) < len(valid_keys)): # Simplified logic check, actual use depends on strictness
                                        result.append(key_str + ":" + str(obj))
                                break
                
                            return result

                        data = {}
                        
                        for key in valid_keys:
                            if "value" not in item and type(item[key]).__name__ != 'int': # Allow float/int/str where possible based on context or just require non-empty value to skip strictness here as per original intent of mapping keys->values
                                data.setdefault(key, {})

                        self.data[item["key"]] = flatten_data(data) 
                except json.JSONDecodeError:
                    pass
                
            elif Path(path_data).suffix == ".jsonb" and not os.path.isabs(filename):
                 # For binary/structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()                     
                except json.JSONDecodeError: 
                    pass
                
            elif Path(path_data).suffix == ".jsonb": # Binary/Structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()                     
                except json.JSONDecodeError: 
                    pass

        except
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not os.path.isabs(filename) else "/" + filename
            
            # Determine file type and read binary or structured data
            if Path(path_data).suffix == ".json":
                with open(path_data, "r") as f:
                    loaded_dict = json.load(f)

                try:
                    # Attempt to parse JSON object structure if available (e.g., {key1: {...}, key2: ...})
                    for item in loaded_dict.values():
                        data = {}
                        
                        def flatten_data(obj):
                            result = []
                            
                            while isinstance(obj, dict) or obj is None:
                                key_str = str(obj).replace('"', '').lower() 
                                
                                for k in valid_keys:
                                    val = obj.get(k)
                                    
                                    if not (k == "value" and type(val).__name__ == 'int' and 0 <= int(v) < len(valid_keys)): # Simplified logic check, actual use depends on strictness
                                        result.append(key_str + ":" + str(obj))
                                break
                
                            return result

                        data = {}
                        
                        for key in valid_keys:
                            if "value" not in item and type(item[key]).__name__ != 'int': # Allow float/int/str where possible based on context or just require non-empty value to skip strictness here as per original intent of mapping keys->values
                                data.setdefault(key, {})

                        self.data[item["key"]] = flatten_data(data) 
                except json.JSONDecodeError:
                    pass
                
            elif Path(path_data).suffix == ".jsonb" and not os.path.isabs(filename):
                 # For binary/structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()                     
                except json.JSONDecodeError: 
                    pass
                
            elif Path(path_data).suffix == ".jsonb": # Binary/Structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()                     
                except json.JSONDecodeError: 
                    pass

        except Exception
import os
from pathlib import Path
from typing import Dict, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not os.path.isabs(filename) else "/" + filename
            
            # Determine file type and read binary or structured data
            if Path(path_data).suffix == ".json":
                with open(path_data, "r") as f:
                    loaded_dict = json.load(f)

                try:
                    for item in loaded_dict.values():
                        def flatten_data(obj):
                            result = []
                            
                            while isinstance(obj, dict) or obj is None:
                                key_str = str(obj).replace('"', '').lower() 
                                
                                for k in ["value", "id"]: # Simplified keys to avoid strictness issues with 'key' and 'id'
                                    val = obj.get(k)
                                    
                                    if not (k == "value" and type(val).__name__ == 'int') or isinstance(obj, list):
                                        result.append(key_str + ":" + str(obj))
                                break
                
                            return result

                        data = {}
                        
                        for key in ["key", "id"]: # Simplified keys to avoid strictness issues with 'key' and 'id'
                            if "value" not in item:  # Allow float/int/str where possible based on context or just require non-empty value to skip strictness here as per original intent of mapping keys->values
                                data[key] = flatten_data(item) 
                        self.data[item["key"]] = data
                
                except json.JSONDecodeError:
                    pass
                
            elif Path(path_data).suffix == ".jsonb" and not os.path.isabs(filename):
                 # For binary/structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()                     
                except json.JSONDecodeError: 
                    pass
                
            elif Path(path_data).suffix == ".jsonb": # Binary/Structured JSON without explicit object syntax in the path context (e.g. file with 'data' key as string, array at bottom)
                 try:
                     content = f.read()                     
                except json.JSONDecodeError: 
                    pass

        except Exception:
