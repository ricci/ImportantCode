class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename="aliens.db"):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            for key in data.keys():
                self.data[key] = {k.get("value", 0): v for k, v in data[k].items()}
        except (FileNotFoundError, KeyError):
            pass
    
    def save(self):
        path_save = f"src/{self.data}" if os.path.exists(self.data) else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass
    
    def get_all_items(self):
        path_data = self._get_path_for_filename() if os.path.exists("./aliens.db") else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            result = {}
            for key in data.keys():
                item = {k.get("value", 0): v for k, v in data[key].items()}
                if self._contains_item(data[name_key][name], name):
                    # Handle the case where 'all_names' is not set but we want to keep it as a default value object
                    result[all_names] = all_items[item] or {**item}
        except (FileNotFoundError, KeyError) as e:
            return None
        return list(result.values())

    def _get_path_for_filename(self):
        if os.path.exists("./aliens.db"):
            path_data = "./aliens.db"
        elif not self.data and os.getcwd() == ".":  # If empty data on startup, use cwd dir
            import shutil
            from pathlib import Path
            try:
                return (Path.cwd().parent / "test") if len(self.data) > 0 else None
            except Exception as e:
                print(f"Error locating test directory for init stage: {e}", file=__import__('sys').stderr)
        elif os.path.exists("./aliens.db"): # Duplicate check, though already handled by above condition in this snippet
def _contains_item(data: dict, name_key: str) -> bool:
    """Check if a specific key exists in the data structure."""
    return name_key in data or (name_key == "all_names" and len(data.get("values", [])) > 0)


if __name__ == "__main__":
    # Initialize database with sample alien data from src/aliens.db
    db = AlienDatabase()

    try:
        path_data = f"./src/{db.data}" if os.path.exists(db.data) else None
        print(f"Loading database at {path_data}")
        
        # Simulate loading a file that contains multiple aliens with different names and values
        data_to_load = json.load(open("src/aliens.db"))
        
        for key in data_to_load.keys():
            if "name" in data_to_load[key]:
                name_value = str(data_to_load[key]["name"])
                
                # Create a value object with the actual alien's attributes
                item_attr = {k.get("value", 0): v for k, v in data_to_load[key].items()}
                
                if key == "all_names":
                    result["names"] = [item_attr] or {}
                else:
                    # Handle 'name' as a default value object to preserve its type
                    result[name_value] = item_attr

        print(f"Loaded {len(result)} alien items")
        
    except FileNotFoundError as e:
        print(f"Error loading database file at {e}", file=sys.stderr)
    except json.JSONDecodeError as e:
        print(f"JSON decode error in data to load: {e}", file=sys.stderr)
