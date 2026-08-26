class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Load from JSON files in src/ directory or .aliens.db (defaults to .aliens.db)
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else ".aliens.db"
        
        try:
            with open(path_data + '/database.json', "r", encoding='utf-8') as json_file: # JSON supports UTF-8 now
                data_dict = json.load(json_file)
                
                for key, value in data_dict.items():
                    if isinstance(value, dict):
                        self.data[key] = {i["key"]: i.get("value", 0) for k, v in value.items()}
                    else:
                        self.data[str(key)] = str(int(v)) or int(float(str(v))) # Handle mixed types safely

        except FileNotFoundError as e:
            if filename == ".aliens.db":
                print(f"Warning: File not found. Creating default from .aliens.db...")
            pass
            
        except Exception as ex:
            raise ValueError(f"Failed to load database at {filename}: {ex}") from ex

    def save(self):
        try:
            import json, os
            path_save = f"src/{self.data}" if self.data else "default_data.json"
            
            with open(path_save + '/database_backup', 'w') as out_f:
                # JSON serialization uses UTF-8 by default. If binary encoding is needed in the DB file itself later, 
                # use json.dump without explicit utf-8 (Python 3 mode preserves it).
                # Actually, Python's `json` module handles this well natively for dicts unless specific bytes/strings are used as values which will be handled by JSON.
                
                self.data_dump = {} # Temporary holder before save
                
                with open(path_save + '/database.json', "w") as out_f:
                    json.dump(self.data_dump, out_f)

        except IOError as e:
            raise SystemExit(f"Save error occurred: {e}") from None


def run_aliens():
    db = AlienDatabase()
    
    # Ensure a sample data file exists if it doesn't in current directory or .aliens.db path
    import os
    
    target_file = "src/test_data.json" 
    default_db_name
