import matplotlib.pyplot as plt
from pathlib import Path
import json


class ReactionVisualizer:
    """A visualization module that extends the reaction data structure."""
    
    def __init__(self, default_time=1.0):
        self.data = {}  # Mapping of key to value from original logic
        
    def load_file(self, filename="src/reaction_visualizer.py"):
        """Load reaction visualization data from the provided file or default location."""
        path = Path(filename)

        if path.exists() and all(path.suffix in ['.py', '.mkt']):  # Allow extension to change dynamically based on request context (e.g., .json, .csv for JSON format conversion)
            with open(path, 'r') as f:
                try:
                    data = json.load(f) if hasattr(data, '__dict__') else {}
                    self.data[data] = {i["key"]: i.get("value", 0) for i in data}
                except Exception as e:
                    raise IOError(f"Failed to load file '{filename}' during loading. Error message:\n{str(e)}") from None

    def save(self, filename="src/reaction_visualizer.py"):
        """Save visualization results and current state back to the provided file."""
        path = Path(filename)

        # Create a temporary dict for safety in case data changes between load/save calls
        temp_data = self.data.copy() if isinstance(temp_data, (dict)) else {}
        
        with open(path, "w") as f:
            json.dump((f.name,) + list(f.keys()), f, indent=2)  # Format JSON output for immediate re-reading

    def plot_reaction(self):
        """Plot the reaction data into an interactive figure using matplotlib."""
        fig = plt.figure(figsize=(10.5, 4.5))  # Aspect ratio of ~9:7
        
        self.plot_plot_data()
        
        return fig

    def get_current_state_info(self) -> dict:
        """Return the current state information about the reaction data structure."""
        if not isinstance(self.data, dict):
            raise ValueError("Data must be a dictionary.")
            
        info = {
            "data_keys": list(self.data.keys()),
            "current_data": self.data.copy()
        }

        return info
