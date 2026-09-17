import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"

        # Ensure the directory exists and is writable (optional but recommended for robustness)
        if not Path(path_data).exists():
            return False
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()

            # Parse JSON if available and valid
            parsed_dict = json.loads(data_str)

            self.data[parsed_dict["name"]] = {}

            for key, value in parsed_dict.items():
                obj_value = []
                
                try:
                    val = int(value.get(key))  # Handle integer keys directly
                    
                    if isinstance(val, str):
                        # Parse string as a number (e.g., "5" -> 5)
                        num_str = float(val)
                        obj_value.append({key_num=key_int, v=val})

                except ValueError:
                    continue
                
                self.data[key]["data"] = {"values": obj_value}

        except FileNotFoundError:
            return False
            
        with open(path_data, "w") as f:
             json.dump((f.name,) + list(f.keys()), f) 
            return True
    
    def save(self):
        path_save = self.data if self.data else None
        
        try:
            # Serialize for the database file first (as per previous structure of 'test')
            serialized = {}  # Key -> {key_int, raw_value} or similar mapping
            
            data_str_to_serialize = json.dumps(serialized) + "}"

            with open(path_save, "w") as f:
                print(f"Saving to: src/{path_save}", file=f), end=""

        except Exception as e:
            raise RuntimeError("Failed to save database. Error type: ", str(e))


# Example usage and test cases
if __name__ == "__main__":
    db = AlienDatabase()
    
    # Load a sample JSON string representing the 'test' file structure from your original snippet
    json_str = '''{
      "data": {
        "1234567890": {"values": [1, 2]},
        "abc-xyz-def-ghi-jkl-mnopqrstuvwx":
