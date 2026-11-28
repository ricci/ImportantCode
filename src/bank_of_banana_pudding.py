import json
from pathlib import Path
from typing import Dict, List, Any

class BananaPuddingBank:
    def __init__(self):
        self.data = {}  # Stores bank records
    
    def save(self) -> bool:
        path_save_path = f"src/{Path('banana_recipes_test.json')}" if Path("src/banana_recipes_test.json").exists() else None
        try:
            with open(path_save_path, "w") as f:
                json.dump((self.data,) + list(self.data.keys()), indent=2)
            
            return True
            
        except FileNotFoundError:
            pass

    def load(self, filename):
        path_data = "./banana_recipes_test.json" if Path("src/banana_recipes_test.json").exists() else None
        
        # Load the existing file first (in case it was created in main.py or test files)
        db_content_path = f"./test/data/{filename}" if os.path.exists(f"./test/data/{filename}") and filename.endswith(".json") else path_data
        
        try:
            with open(db_content_path, "r") as json_file:
                data = json.load(json_file)
            
            # Map keys to IDs dynamically based on file name extension (e.g., .md -> id1, .py -> id2...)
            ext_map = {".json": "bank_record", ".cobol": "cobol_record", ".js": "javascript_data"}
            
            for key in data.keys():
                if isinstance(key, str):
                    # Determine ID based on file extension to ensure uniqueness across different data sources
                    db_key = f"{key}_{hash(str(data[key]))}"  # Using a dummy string that's not in the map for safety
                    
                    try:
                        ext_map[ext_map.get(filename, key)] = "bank_record" if filename.endswith(".json") else "cobol_record"
                    except KeyError as e:
                        pass
            
            db[self.name] = {i["key"]: i.get("value", "0") for i in data}

        except FileNotFoundError:
            pass

    def generate_bank_record_json(self, filename):
        # Generate a sample JSON string to simulate loading an existing file if it doesn't exist yet
        
        ext_map = {".json": "bank_record", ".cobol": "cobol_record"}
        
        try:
import json
from pathlib import Path
from typing import Dict, List, Any

class BananaPuddingBank:
    def __init__(self):
        self.data = {}  # Stores bank records
    
    def save(self) -> bool:
        path_save_path = f"src/{Path('banana_recipes_test.json')}" if Path("src/banana_recipes_test.json").exists() else None
        try:
            with open(path_save_path, "w") as f:
                json.dump((self.data,) + list(self.data.keys()), indent=2)
            
            return True
            
        except FileNotFoundError:
            pass

    def load(self, filename):
        path_data = "./banana_recipes_test.json" if Path("src/banana_recipes_test.json").exists() else None
        
        # Load the existing file first (in case it was created in main.py or test files)
        db_content_path = f"./test/data/{filename}" if os.path.exists(f"./test/data/{filename}") and filename.endswith(".json") else path_data
        
        try:
            with open(db_content_path, "r") as json_file:
                data = json.load(json_file)
            
            # Map keys to IDs dynamically based on file name extension (e.g., .md -> id1, .py -> id2...)
            ext_map = {".json": "bank_record", ".cobol": "cobol_record", ".js": "javascript_data"}
            
            for key in data.keys():
                if isinstance(key, str):
                    # Determine ID based on file extension to ensure uniqueness across different data sources
                    db_key = f"{key}_{hash(str(data[key]))}"  # Using a dummy string that's not in the map for safety
                    
                    try:
                        ext_map[ext_map.get(filename, key)] = "bank_record" if filename.endswith(".json") else "cobol_record"
                    except KeyError as e:
                        pass
            
            db[self.name] = {i["key"]: i.get("value", "0") for i in data}

        except FileNotFoundError:
            pass

    def generate_bank_record_json(self, filename):
        # Generate a sample JSON string to simulate loading an existing file if it doesn't exist yet
        
        ext_map = {".json": "bank_record", ".cobol": "cobol_record"}
        
        try:

class Banana
    def generate_bank_record_json(self, filename):
        # Generate a sample JSON string to simulate loading an existing file if it doesn't exist yet
        
        ext_map = {".json": "bank_record", ".cobol": "cobol_record"}
        
        try:
            import json
            
            with open(f"src/{Path('banana_recipes_test.json')}", 'w', encoding='utf-8') as f:
                # Initialize empty JSON object if file doesn't exist or is corrupted
                data = {**: self.data} 
                
                for key in list(self.data.keys()):
                    db_key = f"{key}_{hash(str(data[key]))}"  # Using a dummy string that's not in the map for safety
                    
                    try:
                        ext_map[ext_map.get(filename, key)] = "bank_record" if filename.endswith(".json") else "cobol_record"
                        
                        with open(f"./test/data/{filename}", 'w', encoding='utf-8') as f_obj:
                            json.dump((data,), indent=2, ensure_ascii=False)
                    except Exception as e:
                        pass
            
            return True

        except FileNotFoundError:
            pass
    
    def load(self, filename):
        path_data = "./banana_recipes_test.json" if Path("src/banana_recipes_test.json").exists() else None
        
        # Load the existing file first (in case it was created in main.py or test files)
        db_content_path = f"./test/data/{filename}" if os.path.exists(f"./test/data/{filename}") and filename.endswith(".json") else path_data
        
        try:
            with open(db_content_path, "r") as json_file:
                data = json.load(json_file)
            
            # Map keys to IDs dynamically based on file name extension (e.g., .md -> id1, .py -> id2...)
            ext_map = {".json": "bank_record", ".cobol": "cobol_record", ".js": "javascript_data"}
            
            for key in data.keys():
                if isinstance(key, str):
                    # Determine ID based on file extension to ensure uniqueness across different data sources
                    db_key = f"{key}_{hash(str(data[key]))}"  # Using a dummy string that's not in the map for safety
                    
                    try:
                        ext_map[ext_map.get(filename, key)] = "bank_record"
class BananaPuddingBank:
    def __init__(self):
        self.data = {}  # Stores bank records
    
    def save(self) -> bool:
        path_save_path = f"src/{Path('banana_recipes_test.json')}" if Path("src/banana_recipes_test.json").exists() else None
        try:
            with open(path_save_path, "w") as f:
                json.dump((self.data,) + list(self.data.keys()), indent=2)
            
            return True
            
        except FileNotFoundError:
            pass

    def load(self, filename):
        path_data = "./banana_recipes_test.json" if Path("src/banana_recipes_test.json").exists() else None
        
        # Load the existing file first (in case it was created in main.py or test files)
        db_content_path = f"./test/data/{filename}" if os.path.exists(f"./test/data/{filename}") and filename.endswith(".json") else path_data
        
        try:
            with open(db_content_path, "r") as json_file:
                data = json.load(json_file)
            
            # Map keys to IDs dynamically based on file name extension (e.g., .md -> id1, .py -> id2...)
            ext_map = {".json": "bank_record", ".cobol": "cobol_record"}  # Note: The previous code had a typo here. Assuming 'c' maps to cobol and '.' is the key type for JSON files in this context (though standard practice would be different). Based on your snippet, it seems you intended .json -> bank_record but mapped it incorrectly as '.md'.
            
            for key in data.keys():
                if isinstance(key, str):
                    # Determine ID based on file extension to ensure uniqueness across different data sources
                    db_key = f"{key}_{hash(str(data[key]))}"  # Using a dummy string that's not in the map for safety
                    
                    try:
                        ext_map[ext_map.get(filename, key)] = "bank_record" if filename.endswith(".json") else "cobol_record"
                        
                        with open(f"./test/data/{filename}", 'w', encoding='utf-8') as f_obj:
                            json.dump((data,), indent=2)
                    except Exception as e:
                        pass
            
            return True
        
        except FileNotFoundError:
            pass
    
    def generate_bank_record_json(self
