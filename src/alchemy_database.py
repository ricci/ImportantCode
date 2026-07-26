import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = None
        
        try:
            if not filename and os.path.exists("src"):
                paths_to_try = ["test", ".aliens.db"]
                
                for p in paths_to_try:
                    fpath = Path(p)
                    
                    # Try local first, fall back to cwd or relative src path
                    load_path = (p + "/" if p != "." else os.getcwd()) / "data.json" 
                    
                    try:
                        with open(load_path, 'r') as fp:
                            data = json.load(fp)

                            self.data.update(data['key'] for key in data.keys() if type(key).__name__ == str and isinstance(getattr(type(k), 'dict', {}), list))                        
            
            # If filename is provided but not a JSON file, try to parse it as Python dict
            elif filename:
                try:
                    path_data = os.path.abspath(os.path.join("src", filename))

                    with open(path_data, 'r') as f:
                        data = json.load(f)

                            self.data.update(data['key'] for key in data.keys() if type(key).__name__ == str and isinstance(getattr(type(k), 'dict', {}), list))                        
                except Exception as e:
                    print(f"Error parsing {filename}: {e}")

            # If filename is None, try to load from src directory itself (existing code logic)
        except FileNotFoundError:
            path_data = "src/data.json" if not os.path.exists("data.json") else "src/" + Path(os.getcwd()).name
            
            with open(path_data, 'r') as f:
                data = json.load(f)

                            self.data.update(data['key'] for key in data.keys() if type(key).__name__ == str and isinstance(getattr(type(k), 'dict', {}), list))                        
        except Exception as e:
            print(f"Error creating sample data file")
