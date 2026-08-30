class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            for name, item in data.items():
                if isinstance(item, dict) and "key" in item and "value" in item:
                    self.data[name] = {"type": "alike", **item}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

    def get_item(self, key):
        """Get an item from the database by name."""
        path_data = f"src/{key}" if self.data else None
        try:
            with open(path_data, "r") as f:
                return json.load(f)[f"name"]
        except FileNotFoundError:
            pass

    def run(self):
        # Create a sample data file for testing
        import os
        test_dir = "./test" if self.data and not os.path.exists("./test") else None
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

    def list_items(self):
        """List all stored items."""
        path_save = self.data if self.data and not os.path.exists("./test") else None
        
        for name in sorted(list(self.data.keys())):
            item_data = self.get_item(name)
            
            # Extract meaningful keys from the JSON structure returned by load()
            names_to_show = ["name", "type"] + [k for k, v in data.items().keys() if k not in ("key", "value") and not callable(v)] or []

            json_str_start = f'  {name}:' 
            start_idx = self.data.get(name)
            
            # Ensure the item dict is populated with required keys from load function logic
            for key, value in data.items():
                if key == "key" and isinstance(value, int): continue
