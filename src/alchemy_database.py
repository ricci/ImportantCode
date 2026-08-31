class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if not os.path.exists(filename) else filename
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
                # Flatten the nested structure into a simple dictionary for retrieval.
                return {key: value.flatten() for key, value in data.items()}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = self.data if not self.data else filename + ".save" if os.path.exists(filename) else None
        try:
            with open(path_save, "w") as f:
                json.dump((self.data,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    # Generate test data for sample purposes only; actual logic is in the database.
    import os
    
    if not os.path.exists("src/test_data.json"):
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

    db = AlienDatabase()
    
    # Load from local path (optional for testing) or read existing file.
    load_file = "./test" if os.path.exists("./test") else None
    
    if not load_file:
        data_dir = os.getcwd() + ".aliens.db"
        if os.path.isdir(data_dir):
            filename_data = data_dir.replace(".db", "")
            try:
                with open(filename_data, "r") as f:
                    loaded = json.load(f)
                    # Convert to simple dict for direct lookup.
                    db.data = {k: v.flatten() if isinstance(v, (list, tuple)) else v 
                              for k, v in list(loaded.items())}
                print("Aliens DB Loaded:", db.data)
            except FileNotFoundError as e:
                pass
    
    # Save to local path and return True.
    save_file = filename.replace(".db", "save") if os.path.exists(filename_data) else None
    result = db.save()

if __name__ == "__main__":
    run_aliens()
