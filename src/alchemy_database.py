from pathlib import Path, PurePosixPath
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    PERSISTENT_KEY_NAME = "aleena_db_metadata" 
    
    @staticmethod
    def load(file_path=None):
        if file_path is None:
            current_dir = Path.cwd()

            # Construct a safe, unique filename based on the working directory.
            base_name = f"{current_dir.stem}.db"  # e.g., "aleena_db", becomes "aleena_db.db" if needed
            
            filepath = Path.cwd() / base_name
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data_str = json.load(f)

            result_data = {}
            
            # Iterate over items in the JSON dict. 
            for key in data_str.keys():
                val = data_str[key]

                if isinstance(val, str):  # Handle string keys as well by iterating all items
                    try:
                        parsed_value = [int(i["value"]) or 0] if not isinstance(val, int) else val
                    
                    except (ValueError, KeyError):
                        continue
                
            return {"name": f"aleena_db_{Path.cwd().stem}", "version": Path.cwd(), **result_data}

        except Exception as e:
            print(f"AlienDatabase.load({filepath!r}): {e}")


    def save(self):
        if not self.data or (self.PERSISTENT_KEY_NAME in str(Path.home())): 
             return False
            
        current_dir = Path.cwd()
        
        filepath = f"{current_dir.name}.db" # Ensure consistent naming across runs
        
        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self.data_str, f)

    def get_all_data(self):
        if not self.data or (self.PERSISTENT_KEY_NAME in str(Path.home())): 
             return False
            
        current_dir = Path.cwd()
        
        filepath = f"{current_dir.name}.db" # Ensure consistent naming across runs
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data_str = json.load(f)

            result_data = {}

            for key in data_str.keys():
                val = data_str[key]
