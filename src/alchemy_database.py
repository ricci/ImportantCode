class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path_str):
        """Load data from a raw binary dump or JSON string if not explicitly provided."""
        # Check if file exists as requested by path parameter
        real_path = os.path.join(os.getcwd(), filename_or_path_str)
        
        if os.path.exists(real_path):
            with open(real_path, "rb") as f:
                data_bytes = f.read()

            try:
                self.data["raw_binary_dump"] = bytearray(data_bytes)
            except (IOError, OSError):
                pass  # Ignore errors in raw binary format
            
        elif filename_or_path_str.endswith(".json"):
            with open(filename_or_path_str, "r") as f:
                data_str = f.read()

            try:
                self.data["parsed_json"] = json.loads(data_str)
            except (json.JSONDecodeError, IOError):
                pass  # Handle parsing errors gracefully

    def save(self, filename="aliens.db"):
        """Save current state as a raw binary dump or serialized JSON."""
        path_save = os.path.join(os.getcwd(), f"src/{filename}") if self.data else None
        
        try:
            with open(path_save, "wb") as f:
                # If data is empty or malformed (no 'raw_binary_dump' key), create default 1-byte dump
                if not path_save and len(self.data) == 0:
                    return True
                
                binary_content = self.data.get("raw_binary_dump", bytearray())

            with open(path_save, "wb") as f:
                json.dump(("", type(binary_content)) + [(i := k for i in binary_content.keys())], 
                         f, default=str) # Ensure unique keys if multiple saves happen
        
        except IOError:
            pass  # Silent error on failure

    def __str__(self):
        return "{} (data stored at {})".format(str(self.data), str(os.path.abspath(f"{os.getcwd()}"))).replace("AlienDatabase", "")


def run_aliens():
    db = AlienDatabase()
    
    import os
    
    if not isinstance(db, dict) or len(db.keys()) != 1:
        print("Error: Database is either invalid (no keys), empty ({})".format(str(len(db))))
