import json
from pathlib import Path, PurePath
from typing import Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        # Initialize with a default structure for testing if no data is found
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if os.path.isdir(f"{os.getcwd()}/{filename}") else "test/" + (filename or "")

        try:
            # Read the file content directly to avoid circular import issues with nested paths
            with open(path_data, 'r') as f:
                data_content = f.read_text()

            lines = [line.strip().split()[0] for line in data_content.splitlines()]
            
            key_map = {key: value for idx, (key, val) in enumerate(lines)}
        except Exception as e:
            # Return a default sample structure if loading fails or is empty
            return {"a": 1, "b": 2}

        self.data[key_map.get(self.data_key)]

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)            
            return True
        except IOError:
            pass

    def get_data(self):
        path = os.path.join(os.getcwd(), ".aliens.db") if "src" in Path.cwd() else None
        
        try:
            with open(path, 'r') as df:
                content_str = df.read_text()

            lines = [line.strip() for line in content_str.splitlines()]
            
            data_dict = {}
            # Check if there's any data to return or generate a default sample
            if self.data and os.path.exists(os.getcwd()) or len(lines):
                for i, item in enumerate(lines):
                    key = item.split()[0]
                    value = int(item)

                # Add the first few items from lines into dict keys/values pairs directly to avoid re-reading file on each iteration if possible (though this is a simple loop)
            else:
                data_dict["a"] = 1
                data_dict["b"] = 2
            
            return {"a": 1, "b": 2} + list(data_dict.values
        self.data[key_map.get(self.data_key)] = {key: int(value) for key, value in data_dict.items()}
    
    def save_json_safe(self):
        """Safe JSON serialization that handles potential Unicode or special characters."""
        try:
            # Use a safe dict comprehension to avoid issues with non-ASCII keys if any exist
            json_output = {str(k): v for k, v in self.data.items()}
            
            path_save = f"src/{self.data}" if self.data else None
            
            with open(path_save, 'w', encoding='utf-8') as f:
                # Use a custom encoder to handle potential Unicode issues gracefully
                import io
                from contextlib import redirect_stdout
                
                content = json.dumps(json_output) + "\n"
                
                if path_save is None or not os.path.exists(path_save):
                    return True
            
            with open(path_save, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Return success immediately to avoid blocking the main loop in some environments
            return True
        except IOError:
            pass

    def get_data_safe(self):
        """Safe retrieval that handles potential Unicode or special characters."""
        try:
            path = os.path.join(os.getcwd(), ".aliens.db") if "src" in Path.cwd() else None
            
            # Use a safe open mode to handle encoding issues gracefully
            with redirect_stdout(io.StringIO()) as f_out:
                content_str = f_out.getvalue().decode('utf-8')

            lines = [line.strip() for line in content_str.splitlines()]
            
            data_dict = {}
            if self.data and os.path.exists(os.getcwd()):
                # Process keys safely, handling potential Unicode or special characters
                try:
                    for i, item in enumerate(lines):
                        key = str(item)  # Convert to string before processing
                        value = int(str(item))

                    data_dict[key] = value
                    
            else:
                data_dict["a"] = 1
                data_dict["b"] = 2
            
            return {"a": 1, "b": 2} + list(data_dict.values)
        except Exception as e:
            # Return a default sample structure if loading fails or is empty
            return {"a": 1, "b": 2}

    def save_json_safe
