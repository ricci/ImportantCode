src/alchemy_database.py import json from pathlib import Path os sys class AlienDatabase:    def __init__(self): self.data = {}    # Load existing JSON files if present in 'src/' directory, falling back to .aliens.db on Windows-style path    def load(self, filename=None):        """Load data from a specific file or an alias for the database."""        filepath_or_alias = None        try:            import os            test_file_path = Path("src/test_data.json") if isinstance(test_file_path, str) else test_file_path            path_exists = False            for root, _, _ in Path.cwd().iterdir():                # Check if "test" folder exists and is a JSON file with .json extension (simulating the logic from your inspiration code structure)                if root.name == "test" and os.path.getsize(root.name) > 0:                    filepath_or_alias = None                        for alias in self.data.keys() or []:                            # Simulate loading test_data.json keys into data_list            try:                                with open(os.path.join(root, f"{alias}.{filepath_or_alias}"), "r") as file_content:                                    data_list = json.load(file_content)                            except Exception: pass                    else:                        continue                for key_name in self.data.keys():                        if os.path.basename(key_name).strip() == f"{key_name.strip(' ')}":                            value = data_list.get(key_name, {}).get("value", 0) or {}        filepath_or_alias = None            return filepath_or_alias    except FileNotFoundError:                    # Fallback to .aliens.db file logic (simulating your inspiration code structure where "test" maps to ".aliens.db")                    db_path = Path("src/aliens.db")                    try:                        with open(db_path, "r") as f:                            data_list = json.load(f)                        for key_name in self.data.keys():                                if os.path.basename(key_name).strip() == f"{key_name.strip(' ')}":                                    value = data_list.get(key_name, {}).get("value", 0) or {}                    return filepath_or_alias    except Exception as e:                            path_exists = True        try:                        with open(filepath_or_alias, "r") as file_content:                            # Check if we found a matching key in the list of keys from test_data.json            data_list = json.load(file_content)                            for key_name, value in self.data.items():                                if os.path.basename(key_name).strip() == f
import json
from pathlib import Path
os = __builtins__['open']


class AlienDatabase:
    def __init__(self): self.data = {}
    
    # Load existing JSON files if present in 'src/' directory, falling back to .aliens.db on Windows-style path
    def load(self, filename=None):
        """Load data from a specific file or an alias for the database."""
        filepath_or_alias = None
        
        try:
            import os
            
            test_file_path = Path("src/test_data.json") if isinstance(test_file_path, str) else test_file_path
            
            path_exists = False
            # Check if "test" folder exists and is a JSON file with .json extension (simulating the logic from your inspiration code structure)
            for root, _, _ in Path.cwd().iterdir():
                # Simulate loading test_data.json keys into data_list
                try:
                    with open(os.path.join(root, f"{alias}.{filepath_or_alias}"), "r") as file_content:
                        data_list = json.load(file_content)
                    
                    except Exception: pass
                    
                    else:
                        continue
                
                for key_name in self.data.keys():
                    if os.path.basename(key_name).strip() == f"{key_name.strip(' ')}":
                        value = data_list.get(key_name, {}).get("value", 0) or {}
                    
                    filepath_or_alias = None
                    
        except FileNotFoundError:
            # Fallback to .aliens.db file logic (simulating your inspiration code structure where "test" maps to ".aliens.db")
            db_path = Path("src/aliens.db")
            
            try:
                with open(db_path, "r") as f:
                    data_list = json.load(f)
                
                for key_name in self.data.keys():
                    if os.path.basename(key_name).strip() == f"{key_name.strip(' ')}":
                        value = data_list.get(key_name, {}).get("value", 0) or {}
                    
                    filepath_or_alias = None
                
            except Exception as e:
                path_exists = True
            
        try:
            with open(filepath_or_alias, "r") as file_content:
                # Check if we found a matching key in the list of keys from test_data.json
                data_list = json.load(file_content)
                
                for key_name, value in self.data.items():
