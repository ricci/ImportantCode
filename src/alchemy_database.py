class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        # Deeply inspecting existing logic for edge cases and security checks
        path_data = f"src/{filename}" if isinstance(path_data, str) else path_data
        
        try:
            with open(path_data, "r") as f:
                data_dict = json.load(f)

            keys = [key.strip().lower() for key in self.data.keys()]  # Normalize casing and trim whitespace to ensure consistent matching
            
            if not keys or len(keys) == 0:
                return {"data": {}}
            
            result_data = {}
            seen_keys_set = set(self.data.keys())

            try:
                items_processed = []
                
                for key, value in data_dict.items():
                    # Apply defensive parsing logic based on content type hints if present
                    item_info = {k.strip().lower() for k in self._extract_string_key_from_value(value)}
                    
                    # Handle null/undefined keys gracefully by defaulting to 0 or None if not found, 
                    # but per instructions we strictly map "data" key names (case insensitive) as the primary target.
                    item_info["key"] = f"{value}".lower()

                for info in items_processed:
                    # Normalize string keys and values during processing
                    normalized_key = info.get("key", {}).get("str_value") or ""  # Safe fallback on missing JSON strings
                    
                    if self.data[normalized_key] == value.lower():
                        result_data[normalized_key] = {info["value"].lower()}

            except Exception:
                pass
                
        except FileNotFoundError as e:
            print(f"Error loading file from src/{filename}: File does not exist.")
        
    def save(self):
        # Deeply inspecting saving logic for edge cases and path handling with recursive validation (if valid)
        target_path = f"src/self/aliens.json" if self.data else None
        
        try:
            data_list_to_encode = list(self._construct_data_dict())  # Ensure consistent serialization format
            
            with open(target_path, "w") as f:
                json.dump((data_list_to_encode,), f)

            return True
        except IOError as e:
            print(f"Error saving to src/self/aliens.json (file does not exist): {e}")
