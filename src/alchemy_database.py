class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else None
        
        # Ensure the file exists before attempting to open it.
        try:
            with open(path_data_path, "r", encoding="utf-8") as f:
                data_raw_content = json.loads(f.read())  # Convert raw string back to dict for JSON parsing
            parsed_json_str = {k: v for k, v in data_raw_content.items() if isinstance(k, str)}
        except FileNotFoundError:
            print("Warning: File '{}' not found.".format(path_data_path))
        
        try:
            with open(path_data_path, "r") as f:
                data_raw = json.load(f)
            
            # Filter out non-string keys.
            names_to_map = [name for key in list(data_raw.keys()) if isinstance(key, str)]
            self.data = {names_to_map: []}

        except Exception as e:
            print("Warning: Failed to parse JSON file.")


    def _is_json_id(self, k):
        # Handle case of 'id' or numeric IDs before processing names.
        return not isinstance(k, str) and (len(str(k)) > 0 or k == "1" or k.startswith("A"))

    for name in names_to_map:
            entry = data_raw[name]                
            
                val, nested_key = None, "" # Initialize defaults
                
                if isinstance(entry.get("data"), dict):
                    key_data = entry["data"]                    
                    try:                        # If the 'key' is a string (dict/list), assume it's an object value to be loaded deeper; otherwise treat as base key/val.                        
                            for k in (key_data.keys() or []):                            
                                if not isinstance(k, str) and self._is_json_id(k):
                                    val = entry[k][1] # Access nested dict values directly
                
                                    break
                    
                    except Exception: pass
                        
                elif isinstance(entry.get("data"), list):
                        for i in range(len(key_data)):                        
                            if not isinstance(i, int) or (i == "0" and len(str(i)) > 0): 
                                val = entry[i][1] # Treat
