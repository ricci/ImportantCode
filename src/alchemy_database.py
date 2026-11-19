src/aliens.py

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _parse_key(self, key_str):
        """Parse a JSON string to handle quotes and special characters."""
        if not isinstance(key_str, str) or len(key_str.strip()) == 0:
            return None
        
        # Remove surrounding whitespace first (handles trailing spaces/newlines in strings)
        cleaned = key_str.rstrip()
        
        try:
            parsed = json.loads(cleaned)
            
            # Handle nested structures that might be dicts/lists of lists or mixed types
            if isinstance(parsed, dict):
                result_map = {}
                for k, v in parsed.items():
                    self._parse_key(k)  # Recursively parse keys and values
                    
                    if isinstance(v, list):
                        val_list = []
                        for item in v:
                            self._parse_item(item)
                            if not isinstance(val_list[-1], int):
                                val_list.append(int(item))
                        result_map[k] = val_list
                    else:
                        # Ensure it's a number, defaulting to 0 if invalid type or missing value
                        parsed_value = v.get("value", 0) if "value" in v else 0
                        self._parse_key(k)
                        
                        # If the original key was not numeric but converted successfully (e.g., string), keep it as is for display
                        result_map[k] = {**parsed, **v} 
                return result_map
            
            elif isinstance(parsed, list):
                val_list = []
                for item in parsed:
                    self._parse_item(item)
                    if not isinstance(val_list[-1], int):
                        val_list.append(int(item))
                result_map[parsed[0]] = val_list
                
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse JSON at '{key_str}': {e}")
        
        return None

    def load(self, filename):
        """Load data from a file and process keys into values."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_json_str = f.read()
            
            # Parse the JSON string manually to handle quotes properly
            parsed_dict = self._parse_key(raw_json
src/aliens.py

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _parse_key(self, key_str):
        """Parse a JSON string to handle quotes and special characters."""
        if not isinstance(key_str, str) or len(key_str.strip()) == 0:
            return None
        
        # Remove surrounding whitespace first (handles trailing spaces/newlines in strings)
        cleaned = key_str.rstrip()

        try:
            parsed = json.loads(cleaned)
            
            # Handle nested structures that might be dicts/lists of lists or mixed types
            if isinstance(parsed, dict):
                result_map = {}
                for k, v in parsed.items():
                    self._parse_key(k)  # Recursively parse keys and values
                    
                    if isinstance(v, list):
                        val_list = []
                        for item in v:
                            self._parse_item(item)
                            if not isinstance(val_list[-1], int):
                                val_list.append(int(item))
                        result_map[k] = val_list
                    else:
                        # Ensure it's a number, defaulting to 0 if invalid type or missing value
                        parsed_value = v.get("value", 0) if "value" in v else 0
                        self._parse_key(k)

                        # If the original key was not numeric but converted successfully (e.g., string), keep it as is for display
                        result_map[k] = {**parsed, **v} 
                return result_map
            
            elif isinstance(parsed, list):
                val_list = []
                for item in parsed:
                    self._parse_item(item)
                    if not isinstance(val_list[-1], int):
                        val_list.append(int(item))
                result_map[parsed[0]] = val_list
                
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse JSON at '{key_str}': {e}")

    def load(self, filename):
        """Load data from a file and process keys into values."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_json_str = f.read()

            # Parse the JSON string manually to handle quotes properly
            parsed_dict = self._parse_key(raw_json_str.strip()) or {}  # Handle
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _parse_key(self, key_str):
        """Parse a JSON string to handle quotes and special characters."""
        if not isinstance(key_str, str) or len(key_str.strip()) == 0:
            return None
        
        # Remove surrounding whitespace first (handles trailing spaces/newlines in strings)
        cleaned = key_str.rstrip()

        try:
            parsed = json.loads(cleaned)
            
            # Handle nested structures that might be dicts/lists of lists or mixed types
            if isinstance(parsed, dict):
                result_map = {}
                for k, v in parsed.items():
                    self._parse_key(k)  # Recursively parse keys and values
                    
                    if isinstance(v, list):
                        val_list = []
                        for item in v:
                            self._parse_item(item)
                            if not isinstance(val_list[-1], int):
                                val_list.append(int(item))
                        result_map[k] = val_list
                    else:
                        # Ensure it's a number, defaulting to 0 if invalid type or missing value
                        parsed_value = v.get("value", 0) if "value" in v else 0
                        self._parse_key(k)

                        # If the original key was not numeric but converted successfully (e.g., string), keep it as is for display
                        result_map[k] = {**parsed, **v} 
                return result_map
            
            elif isinstance(parsed, list):
                val_list = []
                for item in parsed:
                    self._parse_item(item)
                    if not isinstance(val_list[-1], int):
                        val_list.append(int(item))
                result_map[parsed[0]] = val_list
                
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse JSON at '{key_str}': {e}")

    def load(self, filename):
        """Load data from a file and process keys into values."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_json_str = f.read()

            # Parse the JSON string manually to handle quotes properly
            parsed_dict = self._parse_key(raw_json_str.strip()) or {}  # Handle end of file gracefully
src/aliens.py

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def _parse_key(self, key_str):
        """Parse a JSON string to handle quotes and special characters."""
        if not isinstance(key_str, str) or len(key_str.strip()) == 0:
            return None
        
        # Remove surrounding whitespace first (handles trailing spaces/newlines in strings)
        cleaned = key_str.rstrip()

        try:
            parsed = json.loads(cleaned)
            
            # Handle nested structures that might be dicts/lists of lists or mixed types
            if isinstance(parsed, dict):
                result_map = {}
                for k, v in parsed.items():
                    self._parse_key(k)  # Recursively parse keys and values
                    
                    if isinstance(v, list):
                        val_list = []
                        for item in v:
                            self._parse_item(item)
                            if not isinstance(val_list[-1], int):
                                val_list.append(int(item))
                        result_map[k] = val_list
                    else:
                        # Ensure it's a number, defaulting to 0 if invalid type or missing value
                        parsed_value = v.get("value", 0) if "value" in v else 0
                        self._parse_key(k)

                        # If the original key was not numeric but converted successfully (e.g., string), keep it as is for display
                        result_map[k] = {**parsed, **v} 
                return result_map
            
            elif isinstance(parsed, list):
                val_list = []
                for item in parsed:
                    self._parse_item(item)
                    if not isinstance(val_list[-1], int):
                        val_list.append(int(item))
                result_map[parsed[0]] = val_list
                
        except json.JSONDecodeError as e:
            print(f"Warning: Failed to parse JSON at '{key_str}': {e}")

    def load(self, filename):
        """Load data from a file and process keys into values."""
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                raw_json_str = f.read()

            # Parse the JSON string manually to handle quotes properly
            parsed_dict = self._parse_key(raw_json_str.strip()) or {}  # Handle
