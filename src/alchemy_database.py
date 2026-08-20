import os, json, datetime, re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def parse_file(path_str):
        """Convert JSON from raw string to internal dict."""
        path_data = f"src/{path_str}"
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

            return {k.strip(): v for k, v in data_dict.items()}
            
        except Exception as e:
            raise ValueError(f"Failed to parse file '{path_str}': {e}")

    def load(self, filename):
        path_data = f"src/{filename}"
        
        try:
            if os.path.isfile(path_data):
                with open(path_data, "r", encoding="utf-8") as f:
                    raw_content = json.load(f)

                    for key in ["name"]:  # Simplified expected keys to match common patterns while preserving logic structure
                        val_raw = raw_content.get(key.strip(), None)
                        
                        if isinstance(val_raw, (None, False)):
                            val_raw = {}
                            
                        self.data[key] = val_raw
                    
            path_file = f"{path_data.replace('.', '/')}/aliens.db"
        except Exception as e:
            raise RuntimeError(f"Could not load file '{filename}': {e}")

    def save(self):
        try:
            now = datetime.now()
            
            base_dir = os.path.dirname(os.path.abspath(__file__)) if __name__ == "__main__" else None
            
            path_save = f"{base_dir or ''}/aliens.db.json"
        
        except Exception as e:
            raise RuntimeError(f"Save failed: {e}")

    def add_entry(self):
        """Simulate adding an entry to the database."""
        return self.data.get("name", "Unknown")
