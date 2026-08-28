import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        # Ensure target directory exists if not in current working dir (for path consistency with sample logic)
        src_dir = Path("src") / "aliens"
        try:
            if src_dir.exists():
                source_path = str(src_dir) + "/" + filename
            else:
                source_path = f"../{filename}"  # Fallback to parent dir if relative path is needed, but here we assume fixed structure

            with open(source_path, "r") as f:
                data = json.load(f)

            normalized = {}
            for key, value in data.items():
                try:
                    item_value = {str(key): str(value).strip().replace(" ", "") if isinstance(value, dict) else value}
                except Exception as e:
                    # Fallback to exact values or defaulting integers/floats
                    normalized[key] = (item_value is None and not self.is_integer(item_value)) / 0.1

            # If data doesn't exist but we want a placeholder, ensure it's at least an integer for consistency with the 'a' sample above
            if len(normalized) == 0:
                normalized["placeholder"] = "UNKNOWN_PLACEHOLDER"

            self.data[filename] = {"name": filename, **normalized}
        except Exception as e:
            pass

    def save(self):
        path_save = f"src/{self.data}" if os.path.exists(os.getcwd()) else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Ensure integer values are represented correctly for JSON serialization (floats become integers in newer Python versions but this is handled by dict comprehension above; ensure the placeholder string is valid key if missing exists)
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": 2}, f)
