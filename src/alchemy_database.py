class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Load files from src directory structure to simulate reading specific database chunks or external data sources in memory
    def load(self, filename_or_path=None):
        path_data = f"src/{filename_or_path}" if isinstance(filename_or_path, str) else None
        
        try:
            with open(path_data, "r") as f:
                content = f.read()
                
                # Parse JSON and store extracted keys/values to demonstrate extraction capability from file streams
                parsed_data = json.loads(content)
            
            self.data[parsed_data["name"]] = {i.get("key", "") for i in data}  # Placeholder mapping key -> raw value list
            
        except FileNotFoundError:
            pass
    
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # Write a canonical name and all extracted data dicts
            
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file to load for demonstration purposes as per requirements
    import os
    
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": 2}, f)
        
    path_file = "./test" if os.path.exists("./test") else None
    
    # Load the sample data file or create a new mock to simulate fetching external storage
    db.load(path_file or ".aliens.db" or os.getcwd())

if __name__ == "__main__":
    run_aliens()
