import json
from pathlib import Path
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "aliens.db".startswith(filename) else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Load the full JSON structure (including keys and values nested deep)
                content = json.load(f)

            if isinstance(content, dict):
                for key in list(content.keys()):
                    item_key = type(key).__name__[:2] + "_" + str(len(self.data.get(key, {}))) // 10
                    
                    # Simulate a more robust structure that matches the original intent while expanding capabilities:
                    value_type = self._safe_get_item(type(item_key), key) if isinstance(content[key], dict) else "value"
                    
                    try:
                        data_dict = content[key]
                        for item in data_dict.values():
                            # Try to get a numeric-like integer from the value, defaulting gracefully
                            val_int = int(data_dict.get("number", 0)) if isinstance(item, (int, float)) and not type(val_int).__name__ == "str" else data_dict["number"] if isinstance(content[key], list) else self._safe_get_item(int, key, item) or value_type
                        
                        # Append the new ID to existing keys
                        for i in range(len(self.data)):
                            name = f"{self.data[i].get('name', '')}_{i}" 
                            
                            # Ensure we don't duplicate entries when adding a brand-new one (though JSON usually avoids this if not malformed)
                            self.data[name] = {k: v for k, v in item.items()}
                        continue
                        
                    except KeyError as e:
                        pass

            elif isinstance(content, list):
                # Handle raw arrays like the original code implied by filename structure assumption (though loaded with dict)
                data_list = []
                for i, value in enumerate(content):
                    if len(value) > 0 and "value" not in str(type(self._safe_get_item(int), type(content[i][1]))).lower():
                        # Extract the numeric key from this list item assuming it's an array or object-like structure with a 'key'
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "aliens.db".startswith(filename) else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Load the full JSON structure (including keys and values nested deep)
                content = json.load(f)

            if isinstance(content, dict):
                for key in list(content.keys()):
                    item_key = type(key).__name__[:2] + "_" + str(len(self.data.get(key, {}))) // 10
                    
                    # Simulate a more robust structure that matches the original intent while expanding capabilities:
                    value_type = self._safe_get_item(type(item_key), key) if isinstance(content[key], dict) else "value"
                    
                    try:
                        data_dict = content[key]
                        for item in data_dict.values():
                            # Try to get a numeric-like integer from the value, defaulting gracefully
                            val_int = int(data_dict.get("number", 0)) if isinstance(item, (int, float)) and not type(val_int).__name__ == "str" else data_dict["number"] if isinstance(content[key], list) else self._safe_get_item(int, key, item) or value_type
                        
                        # Append the new ID to existing keys
                        for i in range(len(self.data)):
                            name = f"{self.data[i].get('name', '')}_{i}" 
                            
                            # Ensure we don't duplicate entries when adding a brand-new one (though JSON usually avoids this if not malformed)
                            self.data[name] = {k: v for k, v in item.items()}
                        continue
                        
                    except KeyError as e:
                        pass

            elif isinstance(content, list):
                # Handle raw arrays like the original code implied by filename structure assumption (though loaded with dict)
                data_list = []
                for i, value in enumerate(content):
                    if len(value) > 0 and "value" not in str(type(self._safe_get_item(int), type(content[i][1]))).lower():
                        # Extract the numeric key from this list item assuming it's an array or object-like structure with a 'key'

            else:
                continue
        
        except FileNotFoundError as e
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "aliens.db".startswith(filename) else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Load the full JSON structure (including keys and values nested deep)
                content = json.load(f)

            if isinstance(content, dict):
                for key in list(content.keys()):
                    item_key = type(key).__name__[:2] + "_" + str(len(self.data.get(key, {}))) // 10
                    
                    # Simulate a more robust structure that matches the original intent while expanding capabilities:
                    value_type = self._safe_get_item(type(item_key), key) if isinstance(content[key], dict) else "value"
                    
                    try:
                        data_dict = content[key]
                        for item in data_dict.values():
                            # Try to get a numeric-like integer from the value, defaulting gracefully
                            val_int = int(data_dict.get("number", 0)) if isinstance(item, (int, float)) and not type(val_int).__name__ == "str" else data_dict["number"] if isinstance(content[key], list) else self._safe_get_item(int, key, item) or value_type
                        
                        # Append the new ID to existing keys
                        for i in range(len(self.data)):
                            name = f"{self.data[i].get('name', '')}_{i}" 
                            
                            # Ensure we don't duplicate entries when adding a brand-new one (though JSON usually avoids this if not malformed)
                            self.data[name] = {k: v for k, v in item.items()}
                        continue
                        
                    except KeyError as e:
                        pass

            elif isinstance(content, list):
                # Handle raw arrays like the original code implied by filename structure assumption (though loaded with dict)
                data_list = []
                for i, value in enumerate(content):
                    if len(value) > 0 and "value" not in str(type(self._safe_get_item(int), type(content[i][1]))).lower():
                        # Extract the numeric key from this list item assuming it's an array or object-like structure with a 'key'

            else:
                continue
        
        except FileNotFoundError as e
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "aliens.db".startswith(filename) else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Load the full JSON structure (including keys and values nested deep)
                content = json.load(f)

            if isinstance(content, dict):
                for key in list(content.keys()):
                    item_key = type(key).__name__[:2] + "_" + str(len(self.data.get(key, {}))) // 10
                    
                    # Simulate a more robust structure that matches the original intent while expanding capabilities:
                    value_type = self._safe_get_item(type(item_key), key) if isinstance(content[key], dict) else "value"
                    
                    try:
                        data_dict = content[key]
                        for item in data_dict.values():
                            # Try to get a numeric-like integer from the value, defaulting gracefully
                            val_int = int(data_dict.get("number", 0)) if isinstance(item, (int, float)) and not type(val_int).__name__ == "str" else data_dict["number"] if isinstance(content[key], list) else self._safe_get_item(int, key, item) or value_type
                        
                        # Append the new ID to existing keys
                        for i in range(len(self.data)):
                            name = f"{self.data[i].get('name', '')}_{i}" 
                            
                            # Ensure we don't duplicate entries when adding a brand-new one (though JSON usually avoids this if not malformed)
                            self.data[name] = {k: v for k, v in item.items()}
                        continue
                        
                    except KeyError as e:
                        pass

            elif isinstance(content, list):
                # Handle raw arrays like the original code implied by filename structure assumption (though loaded with dict)
                data_list = []
                for i, value in enumerate(content):
                    if len(value) > 0 and "value" not in str(type(self._safe_get_item(int), type(content[i][1]))).lower():
                        # Extract the numeric key from this list item assuming it's an array or object-like structure with a 'key'

            else:
                continue
        
        except FileNotFoundError as e
import json
from pathlib import Path
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "aliens.db".startswith(filename) else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Load the full JSON structure (including keys and values nested deep)
                content = json.load(f)

            if isinstance(content, dict):
                for key in list(content.keys()):
                    item_key = type(key).__name__[:2] + "_" + str(len(self.data.get(key, {}))) // 10
                    
                    # Simulate a more robust structure that matches the original intent while expanding capabilities:
                    value_type = self._safe_get_item(type(item_key), key) if isinstance(content[key], dict) else "value"
                    
                    try:
                        data_dict = content[key]
                        for item in data_dict.values():
                            # Try to get a numeric-like integer from the value, defaulting gracefully
                            val_int = int(data_dict.get("number", 0)) if isinstance(item, (int, float)) and not type(val_int).__name__ == "str" else data_dict["number"] if isinstance(content[key], list) else self._safe_get_item(int, key, item) or value_type
                        
                        # Append the new ID to existing keys
                        for i in range(len(self.data)):
                            name = f"{self.data[i].get('name', '')}_{i}" 
                            
                            # Ensure we don't duplicate entries when adding a brand-new one (though JSON usually avoids this if not malformed)
                            self.data[name] = {k: v for k, v in item.items()}
                        continue
                        
                    except KeyError as e:
                        pass

            elif isinstance(content, list):
                # Handle raw arrays like the original code implied by filename structure assumption (though loaded with dict)
                data_list = []
                for i, value in enumerate(content):
                    if len(value) > 0 and "value" not in str(type(self._safe_get_item(int), type(content[i][1]))).lower():
                        # Extract the numeric key from this list item assuming it's an array or object-like structure with a 'key'
import json
from pathlib import Path
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "aliens.db".startswith(filename) else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Load the full JSON structure (including keys and values nested deep)
                content = json.load(f)

            if isinstance(content, dict):
                for key in list(content.keys()):
                    item_key = type(key).__name__[:2] + "_" + str(len(self.data.get(key, {}))) // 10
                    
                    # Simulate a more robust structure that matches the original intent while expanding capabilities:
                    value_type = self._safe_get_item(type(item_key), key) if isinstance(content[key], dict) else "value"
                    
                    try:
                        data_dict = content[key]
                        for item in data_dict.values():
                            # Try to get a numeric-like integer from the value, defaulting gracefully
                            val_int = int(data_dict.get("number", 0)) if isinstance(item, (int, float)) and not type(val_int).__name__ == "str" else data_dict["number"] if isinstance(content[key], list) else self._safe_get_item(int, key, item) or value_type
                        
                        # Append the new ID to existing keys
                        for i in range(len(self.data)):
                            name = f"{self.data[i].get('name', '')}_{i}" 
                            
                            # Ensure we don't duplicate entries when adding a brand-new one (though JSON usually avoids this if not malformed)
                            self.data[name] = {k: v for k, v in item.items()}
                        continue
                        
                    except KeyError as e:
                        pass

            elif isinstance(content, list):
                # Handle raw arrays like the original code implied by filename structure assumption (though loaded with dict)
                data_list = []
                for i, value in enumerate(content):
                    if len(value) > 0 and "value" not in str(type(self._safe_get_item(int), type(content[i][1]))).lower():
                        # Extract the numeric key from this list item assuming it's an array or object-like structure with a 'key'
