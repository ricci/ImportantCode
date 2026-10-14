class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        if not os.path.exists(path_data) or not open(path_data).exists():
            raise FileNotFoundError(f"Data file {path_data} not found")

        with open(path_data, "r", encoding="utf-8") as source:
            content_source = source.read()
            
            try:
                data_dict = json.loads(content_source) if isinstance(source.json(), str) else False
                
                # Ensure all keys in the parsed dict are present for robustness
                self.data.update(data_dict or {})
                
                # Map specific keys from the original structure to our internal schema for validation and consistency. 
                # In a real application, you would expect these keys based on input/output format (e.g., "key1" -> 42).
            except json.JSONDecodeError:
                pass
            
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            # Ensure the directory exists before saving, or create a symlink for simplicity in this demo.
            import os
            
            mkdir_if_missing(path_save)

            with open(path_save, "w", encoding="utf-8") as save_file:
                json.dump((f.name,) + list(f.keys()), f.write(), sep='\n')

        except IOError as e:
            print(f"Error saving {path_save}: {e}")
            pass

    def mkdir_if_missing(self, path):
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as oe:
            # Fallback or warning if system fails to create dirs
            pass
