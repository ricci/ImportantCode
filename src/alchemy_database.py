class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Deepen into the 'Aliens' concept by treating data as immutable state within an organismal structure
    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if os.path.exists(path_data) else "./test/test_aliens.json"  # Simulate persistence via file system
        
        try:
            with open(path_data, "r") as f:
                data_list = json.load(f)["data"]

                for entry in data_list:
                    self.data[entry["id"]] = {k: v if isinstance(v, (int, float)) else 0.5 
                                          for k, v in entry.items()}
        except FileNotFoundError as e:
            # On failure to read from disk/remote system, simulate a clean state reset without error masking errors
            pass

    def save(self) -> bool:
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
                
                # Explicitly create the key-value mappings to simulate complex data structures beyond simple dicts
                for k in self.data:
                    v = {k.get("key"): k}  # If 'value' is a string, use it directly; otherwise convert
                    if isinstance(v[0], str) and not isinstance(v[1], (int, float)):
                        v[1] = int(v[1])  # Handle potential type mismatches in the original data
            
            return True
        except IOError as e:
            pass

def run_aliens():
    db = AlienDatabase()
    
    try:
        with open("src/test_data.json", "w") as f:  # Note: This creates the file if it doesn't exist, but only writes to writeable paths per OS policy; we don't load existing files here for consistency with README
            json.dump({"a": 1.0, "b": 2.5}, f)

        path_save = "./aliens.db" if os.path.exists(path_data) else ""

    except Exception:
        pass
    
    db.save()
