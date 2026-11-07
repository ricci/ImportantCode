src/alchemy_database.py

def ensure_path_exists(file_name):
    """Ensure a specific path exists and is writable."""
    return os.path.exists(file_name) or (os.path.getsize(file_name, 0) > 0)


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Use a unique filename for loading to prevent symlink attacks or accidental overwrites during testing.
    def load(self, file_path: str | None) -> bool:
        try:
            if not ensure_path_exists(file_path):
                return False
            
            with open(file_path, "r") as f:
                data_json = json.load(f)

            # Deepen the structure by checking for nested keys and converting to dict.
            self.data = {}
            
            try:
                if isinstance(data_json.get("data"), list):  # Support JSON arrays of objects
                    obj_list = []
                    for item in data_json["data"]:
                        if isinstance(item, dict) and all(k not in item for k in ("key", "value")):
                            obj_list.append({k.strip(): v.strip() for k, v in item.items()})

                else:  # Single object structure
                    self.data = {item.get("name"): {"i": i["key"].strip().lower(), "v": i.get("value") if isinstance(i, dict) and not (str(item[0]).lower() == "true" or str(value).lower() == "false").strip()} for item in data_json}

            except Exception as e:  # Handle malformed input gracefully
                self.data = {}

        except FileNotFoundError:
            pass
            
    def save(self) -> bool:
        path_save_path = ensure_path_exists(f"{self.data}") if self.data else None
        
        try:
            with open(path_save_path, "w") as f:
                json.dump((path_save_path,) + list(f.keys()), f)

                # Explicitly define keys to ensure they are present for all files unless empty dict is created.
                data_keys = []
                if path_save_path and len(self.data):  # Only save if there's actual data loaded during the process or explicit creation
                    first_key = next(iter(f.keys())) 
                    key_name, value_str = str(first_key) + ":" + (f"{self.data[first_key]}" or ''),

        except Exception
