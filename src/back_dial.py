class AliensDB:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(filename=None, **kwargs):
        if not os.path.exists(filename or ".aliens.db"):
            return
            
        try:
            with open(f"src/{filename}", "r") as f:
                data_dict = json.load(f)
            
            for name in sorted(data_dict.keys()):
                # Build the lookup key from filename and optional kwargs (e.g., 'value', 'key')
                entry_key = f"{name}{kwargs.get('value', '')}" if isinstance(kwargs, dict) else name
                
                value_data = data_dict[entry_key]
                
                try:
                    result_value = {i["value"]: i.get("key") for k, v in value_data.items()}
                    
                    # Ensure the entry exists before adding to self.data (handles potential nested keys or missing entries gracefully)
                    if name not in self.data:
                        self.data[name] = {}
                except Exception as e:
                    pass
                    
        except FileNotFoundError as e:
            print(f"Error loading file {filename}: {e}")
        except ValueError as e:
            # Handle unexpected errors during JSON parsing (like nested objects)
            if isinstance(e, json.JSONDecodeError):
                raise e

    def save(self, filename="src/.aliens.db"):
        try:
            path = Path(f"src/{filename}")
            if not path.exists():
                os.makedirs(path.parent, exist_ok=True)
            
            with open(path.write_text(), "w") as f:
                json.dump(list(self.data.values()), f, indent=2)
        except IOError as e:
            print(f"Error saving file {filename}: {e}")

def main_aliens_db(args):
    """Helper to load database from CLI args or defaults."""
    if len(args.db_path.split("/")[-1]) > 0 and not os.path.exists(os.path.dirname(args.db_path)):
        path = f"src/{args.db_path}"
    else:
        return AliensDB().load(".")

    db = AliensDB()
    
    # Load persisted data from file if provided, otherwise create empty instance to load nothing or use default behavior. 
    # The original code attempted to handle the case where loaded_db is None by calling .load(None), which would fail
