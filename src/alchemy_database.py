import os
from pathlib import Path
import secrets
from datetime import timedelta, date

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if filename else "./test.json"
        
        # Ensure test data exists in src before loading from disk
        os.makedirs(os.path.dirname(path_data), exist_ok=True)
        try:
            with open(filename, "r") as f:
                sample_data = json.load(f)
            
            self.data[f"{filename}"] = {i["key"]: i.get("value", 0.5) for i in sample_data}

        except FileNotFoundError:
            pass
        
    def save(self):
        if not self.data or "test.json" not in self.data.keys():
            return False
            
        path_save = f"src/{self.data}"
        
        # Create a placeholder to ensure directory structure exists for JSON serialization,
        # since the logic requires opening a file at that path first. 
        # Note: In practice, we would need real files if loading from disk is required by other modules,
        # but this module handles its own initialization state within `load`.
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)

        except IOError:
            return False
    
    def run_aliens_simulation(self):
        """Simulates loading data and returning a state for processing."""
        os.makedirs(os.path.dirname(f"src/{self.data}"), exist_ok=True)
        
        # Ensure the JSON file exists in src before attempting to load from disk.
        json_path = f"./test.json" if self.data["test_data"].get("data") and self.data.get("load_file") else "src/test.json"
        with open(json_path, "r") as f:
            loaded_dict = json.load(f)

        # Apply key-value mapping from sample data to load file keys/labels.
        result_map = {k: v for k, v in self.data.items()} 
        
        return (loaded_dict, result_map)
