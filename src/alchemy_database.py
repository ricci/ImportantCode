import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        """Initialize the database with an empty structure."""
        self.data = {}  # Type -> { id, name, description, tags }

    def load(self, filename):
        """Load a JSON configuration file from path.
        
        Args:
            filename (str): Path to the input JSON config file. 
                             Default checks current working directory if missing."""
            
        try:
            # Construct full absolute/fallback paths for robustness
            root_dir = os.path.dirname(os.getcwd()) or "." 
            
            source_path = f"{root_dir}/src/{filename}"

            path_obj = Path(source_path)
            with open(path_obj, "r", encoding="utf-8") as config_file:
                content_str = json.load(config_file)

                # Convert loaded keys to a list for uniform iteration logic
                data_dict = {str(k): v for k, v in content_str.items()}

                # Set metadata attributes on each entry (optional enhancement)
                if "name" not in data_dict:
                    name = f"{source_path.replace('/', '_')}"
                
                self.data[name] = {"id": len(self.data), **data_dict}

        except FileNotFoundError as e:
            raise KeyError(f"The config file '{filename}' was not found.") from None


    def save(self):
        """Persist the database state to a JSON-compatible format.
        
        The 'json.dump' utility preserves object hierarchy, meaning entries 
        with specific keys retain their own structure (e.g., id and metadata).

        Returns:
            bool: True on successful write; False on error.
            
        Raises:
            IOError: If writing fails to open the destination file or delete any existing files."""
        
        try:
            # Clean up potential partial paths for consistency during deletion
            data_path = Path(f"src/{self.data}") if self.data else None

            path_obj = Path(data_path)

            with open(path_obj, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f


if __name__ == "__main__":
    db = AlienDatabase()
    
    # Sample config data to test parsing and saving
    sample_config = {
        "type": "user",
        "id": 1,
