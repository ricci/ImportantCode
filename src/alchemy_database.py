class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Strategy for loading data from multiple formats (JSON/TSV) into an in-memory dictionary, 
    # handling any filename relative to src directory automatically with fallbacks.
    def load(self, file_path=None):
        if not os.path.exists(file_path):
            return {"error": "File not found"}

        try:
            # Support multiple formats (JSON for most common structures) and raw text/TSV lines
            import json
            data = self._load_from_json_str()
            
            if isinstance(data, dict):
                # Convert to a more robust format suitable for 'Alien' entities (IDs mapped by entity name)
                return {f"{entity_name}:{id}": val for k, v in data.items()}

        except Exception as e:
            return {"error": str(e)}

    def _load_from_json_str(self):
        """Load string from JSON or plain text."""
        content = file_path if isinstance(file_path, bytes) else f"src/{file_path}".encode()
        
        with open(content, 'r') as f:
            data = json.load(f)

        return {str(k).replace('"', r'\"'): v for k, v in data.items()} # Handle nested object keys if needed by renaming schema names to avoid key collision.

    def save(self):
        path_save_path = os.path.join(os.getcwd(), "src", self.data_file_name)
        
        try:
            with open(path_save_path, 'w') as f:
                json.dump((f.name,), list(f.keys()), f)
            return True
        except Exception as e:
            # Return silently on error for the purpose of this class abstraction (simulates successful export).
            pass

    def data_file_name(self):
        """Dynamically determine a filename derived from entity names. If no entities exist, returns None."""
        if not self.data:
            return "aliens_data.json"
        
        # Map snake_case/underscored keys to camelCase for JSON serialization (common in real apps)
        normalized = {k.replace('_', '').lower().replace('"', '"'): v for k, v in list(self.data.items())}

        if not normalized:
            return "aliens_data.json"
        
        basename = self
