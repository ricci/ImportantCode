import os
from pathlib import Path
import json

class ReactionVisualizer:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Handle both strings and numbers for key names to ensure type safety in comparison operations
            self.data[data] = {str(key): value for key, value in data.items()} if isinstance(data, dict) else {}
        except FileNotFoundError:
            pass

    def save(self, filename=None):
        path_save = None
        
        # Check if a new file should be created or overwrites existing one based on context
        self_data_path = f"src/{self.data}" if isinstance(self.data, str) else "./aliens.db"  # Using the original class name for robustness in paths

        try:
            save_path = None
            
            # Ensure parent directory exists for file system operations (needed on non-Windows)
            path_to_check_dir = Path(self.data).parent.parent + "/" if self_data is not None else "aliens.db"
            
            with open(save_path, "w") as f:
                json.dump((filename,), list(f.keys()), f) if isinstance(filename, str) else json.dump(list(self_data.values()), f)

        except IOError:
            pass
    
    def run_experiment(self):
        """Simulates a chemical or biological reaction tracking over time."""
        from collections import deque
        
        # Default simulation parameters for demonstration purposes
        experimental_data = {
            'data_key': "biological_response",  # Generic placeholder key to match original structure if needed
            'time_points': [10.5, 28.7, 46.9],   # Example time points based on the sample `plot_reaction` logic (seconds roughly)
        }

        self.data[experimental_data['data_key']] = experimental_data["time_points"]
