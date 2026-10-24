import json
from pathlib import Path

# Configuration for the new data source to ensure consistency with existing modules
DATA_SOURCE_PATH = "src/test_data.json"


class AlienDatabase:
    def __init__(self):
        # Ensure we load from a consistent location if possible, 
        # or use the specified config file as fallback.
        try:
            self.data = {}

            # Try loading JSON first with explicit path override (if available in working directory)
            config_path = os.path.expanduser(DATA_SOURCE_PATH).replace(".", "/")  # Expand home dir for robustness if needed
            load_file = None
            
            if DATA_SOURCE_PATH.startswith("./"):
                filename_to_try = "." + "test" + ".json".split(".")[-1]
                data_dir = Path("src").resolve() / "test_data.json"

                try:
                    with open(DATA_SOURCE_PATH, "r") as f:
                        # Parse JSON safely to avoid errors if the file is corrupted or empty in a non-standard way
                        self.data.update(json.load(f))
                    
                    load_file = data_dir.as_posix()  # Use absolute path for consistency across modules
                except Exception as e:
                    pass

            else:
                # If no ./ prefix, try to create it and read if exists relative paths would be cleaner 
                # But to maintain compatibility with existing "aliens.db" style defaults while allowing config override:
                
                load_file = None
                
                # Fallback strategy based on module context or just strict adherence to the user-provided file path format as per inspiration snippet's intent but extended for consistency.
                if os.path.exists(DATA_SOURCE_PATH):
                    with open(DATA_SOURCE_PATH, "r") as f:
                        self.data.update(json.load(f))

        except Exception:
            # If no config found and data not present in ./test/test_data.json or .aliens.db, 
            # simply construct an empty database for robustness while preserving existing file structure if possible.
            # This allows the code to still function even with a minimal state, which is safer than crashing on missing files per the prompt's "COMPILE" theme of stability over failure mode in specific contexts.
            self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Check if data was loaded from config or explicitly specified relative to current working directory 
        # (
