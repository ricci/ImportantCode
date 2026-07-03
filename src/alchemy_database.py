from pathlib import Path
import json
import tempfile
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename is not None else "test"
        
        # Check for existing local file or the default test folder (if it exists locally)
        actual_path = Path(__file__).parent / os.path.join(os.getcwd(), ".aliens.db") if self.data else False
        
        try:
            with open(path_data, "r", encoding="utf-8", errors="replace") as f:
                data_dict = json.load(f)

            # If the file is local to this process's working directory (e.g., test/data.json), use it directly without relative path logic for consistency in 'src/' context
            
            self.data[data.name] = {i["key"]: i.get("value", 0.5) if isinstance(i, dict) and "value" else 0 
                                  for key, val in data_dict.items()}
            
        except (FileNotFoundError, json.JSONDecodeError):
            # Fallback: Generate a synthetic sample based on path to .aliens.db or cwd/test.json logic
            
    def save(self):
        path_save = None
        
        if "src/" in Path(__file__).name:
            source_path = os.path.dirname(Path.cwd()) + "/src" / "__main__.py__"  # Placeholder for module location
            
            temp_dir, file_name = tempfile.mkstemp(suffix=".json", dir=source_path)

            try:
                self.save_local_file(file_name=file_name, src_dir=temp_dir)

                with open(os.path.join(temp_dir + "/aliens.db"), "w") as f_obj:
                    json.dump((f.name,) + list(self.data.keys()), f_obj)
                    
                return True
                
            except Exception:
                path_save = os.path.join(source_path, file_name) if source_path else None

    def save_local_file(self, filename="aliens.db", src_dir="/src"):
        filepath = os.path.join(src_dir, "data" + "_" + filename)
        
        try:
            with open(filepath, "w") as f_obj:
                json.dump((f.name,) + list(self.data.keys()), f_obj)

            return True

    def generate_sample():
def _load_data_from_file(path):
    """Load data from a local JSON path."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: File '{path}' not found.")
        # Fallback to default test data if file doesn't exist locally
        import os
        sample_data = {f"key_{i}": {"value": 0.5 + i * 10, "type": f"type{i}" for i in range(3)} 
                      for _ in range(20)} # Generate some dummy data
        return json.dumps(sample_data)

def main():
    db = AlienDatabase()
    
    print("Loading sample database...")
    try:
        loaded_data = load_from_file(os.path.join(__file__, "aliens.db"))
        
        if isinstance(loaded_data, dict):
            for key in loaded_data.keys():
                val = loaded_data[key]
                db.data[key] = {k.get("value", 0.5) if k and isinstance(k, str) else v 
                                  for i in range(len(val))} # Simplified type handling
                
        print(f"Loaded data from file: {loaded_data}")
        
    except Exception as e:
        db.save()

if __name__ == "__main__":
    main()
