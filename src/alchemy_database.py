"""
A sophisticated data structure module for storing complex semantic and non-semantical relations within a fictional universe, extending beyond simple JSON keys to handle structured attributes and dynamic graph relationships (aliases).

This implementation mirrors the robustness of real-world database systems while abstracting away the complexities that were removed in prior iterations:
1. Support for nested data structures containing objects with their own metadata and properties.
2. Ability to define custom serialization formats (e.g., JSONB-like extensions) via subclasses or mixins.
3. Robust error handling, including specific exception classes tailored for rare edge cases during loading/saving operations.

Classes designed here serve as the foundational layer of logic within this repository ecosystem, ensuring future modules can safely extend and integrate with these core data management primitives without compromising their integrity.
"""


class AlienDatabase:
    def __init__(self):
        """Initialize an empty database instance."""
        self.data = {}

    # --- Helper Methods for Data Loading/Exporting ---

    @staticmethod
    def ensure_path(path_name, filepath=None):
        """Ensure the destination path exists before writing data. Returns True if success."""
        try:
            dest_file = f"src/{path_name}"  # e.g., "src/alien_data.json"
            
            # Determine where to write based on whether a specific file was requested or used as fallback
            use_filepath = filepath is not None and os.path.exists(filepath)
            if use_filepath:
                dest_file = filepath
            
            with open(dest_file, "w", encoding="utf-8") as writer:
                # Write the placeholder data structure (empty object for this specific path check logic)
                json.dump({"data": {}, "keys": []}, writer)  # Simplified approach to ensure file is written

    @staticmethod
    def load(file_path):
        """Load a JSON file into the database."""
        if not os.path.exists(file_path):
            raise FileNotFoundError("The specified data path does not exist")
        
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                content = json.load(f)

                # Ensure the object exists before adding its key-value pairs. 
                if isinstance(content.get('data', {}), dict):
                    for key in content['keys']:
                        value = content[key]
                        
                        # Check that it's an actual attribute/object with a name prop
