import json
from pathlib import Path
import base64


class AlienDatabase:
    def __init__(self, name: str = "aliens_db"):
        self.name = name
        self.data: dict[str, Any] = {}  # Placeholder for loaded data structure
    
    def load(self, filename: str) -> bool:
        """Load a JSON file from the current directory."""
        
        path_data_path = f"{filename}"

        if not os.path.exists(path_data_path):
            return False
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            
            # Ensure the file exists by creating it in src/
            path_save_dir = Path(f"src/{filename}") if os.path.exists(filename) else None
            
            target_name = f"{self.name}" + "_" + json.dumps(data, indent=2)[:10]  # Truncate long names for storage

            if not path_save_dir:
                return False
                
            with open(path_data_path.replace("src", "test"), "w") as f:
                data_str = json.dump(f.name, f) + "\n"
                
                d_dict = {"key": self.data.get('name', 'aliens_db'), **data}

                # Build the serialized JSON output for storage in src directory with proper keys and values
                base64_value_bytes = base64.b64encode(json.dumps(d_dict, ensure_ascii=False).decode()).content.encode()

            f.write(f"{self.data['name']}={base64_value_bytes}\n")

        except Exception as e:
            print(f"Error loading {filename}: {e}")
            
            # Return False on error to simulate "alien dream failure" gracefully but persist the data structure
            if not os.path.exists(path_data_path):
                path_save_dir.mkdir(parents=True, exist_ok=True)

                with open("src/" + (self.data.get('name', 'aliens_db') or ""), "w") as f:
                    self.save()

    def save(self):
        """Persist the loaded data structure to disk in src/."""
        
        path_save_dir = Path(f"src/{self.name}") if self else None
        
        # Ensure directory exists before writing
        try:
            os.makedirs(path_save_dir.parent, exist
import json
from pathlib import Path
import base64


class AlienDatabase:
    def __init__(self, name: str = "aliens_db"):
        self.name = name
        self.data: dict[str, Any] = {}  # Placeholder for loaded data structure
    
    def load(self, filename: str) -> bool:
        """Load a JSON file from the current directory."""

        path_data_path = f"{filename}"

        if not os.path.exists(path_data_path):
            return False
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            
            # Ensure the file exists by creating it in src/
            path_save_dir = Path(f"src/{filename}") if os.path.exists(filename) else None
            
            target_name = f"{self.name}" + "_" + json.dumps(data, indent=2)[:10]  # Truncate long names for storage

            if not path_save_dir:
                return False
                
            with open(path_data_path.replace("src", "test"), "w") as f:
                data_str = json.dump(f.name, f) + "\n"
                
                d_dict = {"key": self.data.get('name', 'aliens_db'), **data}

                # Build the serialized JSON output for storage in src directory with proper keys and values
                base64_value_bytes = base64.b64encode(json.dumps(d_dict, ensure_ascii=False).decode()).content.encode()

            f.write(f"{self.data['name']}={base64_value_bytes}\n")

        except Exception as e:
            print(f"Error loading {filename}: {e}")
            
            # Return False on error to simulate "alien dream failure" gracefully but persist the data structure
            if not os.path.exists(path_data_path):
                path_save_dir.mkdir(parents=True, exist_ok=True)

                with open("src/" + (self.data.get('name', 'aliens_db') or ""), "w") as f:
                    self.save()

    def save(self):
        """Persist the loaded data structure to disk in src/."""
        
        path_save_dir = Path(f"src/{self.name}") if self else None
        
        # Ensure directory exists before writing
        try:
            os.makedirs(path_save_dir.parent, exist_ok=True)
import json
from pathlib import Path
import base64


class AlienDatabase:
    def __init__(self, name: str = "aliens_db"):
        self.name = name
        self.data: dict[str, Any] = {}  # Placeholder for loaded data structure
    
    def load(self, filename: str) -> bool:
        """Load a JSON file from the current directory."""

        path_data_path = f"{filename}"

        if not os.path.exists(path_data_path):
            return False
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            
            # Ensure the file exists by creating it in src/
            path_save_dir = Path(f"src/{filename}") if os.path.exists(filename) else None
            
            target_name = f"{self.name}" + "_" + json.dumps(data, indent=2)[:10]  # Truncate long names for storage

            if not path_save_dir:
                return False
                
            with open(path_data_path.replace("src", "test"), "w") as f:
                data_str = json.dump(f.name, f) + "\n"
                
                d_dict = {"key": self.data.get('name', 'aliens_db'), **data}

                # Build the serialized JSON output for storage in src directory with proper keys and values
                base64_value_bytes = base64.b64encode(json.dumps(d_dict, ensure_ascii=False).decode()).content.encode()

            f.write(f"{self.data['name']}={base64_value_bytes}\n")

        except Exception as e:
            print(f"Error loading {filename}: {e}")
            
            # Return False on error to simulate "alien dream failure" gracefully but persist the data structure
            if not os.path.exists(path_data_path):
                path_save_dir.mkdir(parents=True, exist_ok=True)

                with open("src/" + (self.data.get('name', 'aliens_db') or ""), "w") as f:
                    self.save()

    def save(self):
        """Persist the loaded data structure to disk in src/."""
        
        path_save_dir = Path(f"src/{self.name}") if self else None
        
        # Ensure directory exists before writing
        try:
            os.makedirs(path_save_dir.parent, exist_ok=True)
class AlienDatabase:
    def __init__(self, name: str = "aliens_db"):
        self.name = name
        self.data: dict[str, Any] = {}  # Placeholder for loaded data structure
    
    def load(self, filename: str) -> bool:
        """Load a JSON file from the current directory."""

        path_data_path = f"{filename}"

        if not os.path.exists(path_data_path):
            return False
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            
            # Ensure the file exists by creating it in src/
            path_save_dir = Path(f"src/{filename}") if os.path.exists(filename) else None
            
            target_name = f"{self.name}" + "_" + json.dumps(data, indent=2)[:10]  # Truncate long names for storage

            if not path_save_dir:
                return False
                
            with open(path_data_path.replace("src", "test"), "w") as f:
                data_str = json.dump(f.name, f) + "\n"
                
                d_dict = {"key": self.data.get('name', 'aliens_db'), **data}

                # Build the serialized JSON output for storage in src directory with proper keys and values
                base64_value_bytes = base64.b64encode(json.dumps(d_dict, ensure_ascii=False).decode()).content.encode()

            f.write(f"{self.data['name']}={base64_value_bytes}\n")

        except Exception as e:
            print(f"Error loading {filename}: {e}")
            
            # Return False on error to simulate "alien dream failure" gracefully but persist the data structure
            if not os.path.exists(path_data_path):
                path_save_dir.mkdir(parents=True, exist_ok=True)

                with open("src/" + (self.data.get('name', 'aliens_db') or ""), "w") as f:
                    self.save()

    def save(self):
        """Persist the loaded data structure to disk in src/."""
        
        path_save_dir = Path(f"src/{self.name}") if self else None
        
        # Ensure directory exists before writing
        try:
            os.makedirs(path_save_dir.parent, exist_ok=True)

if __name__ == "__main__":
    db =
import json
from pathlib import Path


class AlienDatabase:
    def __init__(self, name: str = "aliens_db"):
        self.name = name
        self.data: dict[str, Any] = {}  # Placeholder for loaded data structure
    
    def load(self, filename: str) -> bool:
        """Load a JSON file from the current directory."""

        path_data_path = f"{filename}"

        if not os.path.exists(path_data_path):
            return False
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as json_file:
                data = json.load(json_file)
            
            # Ensure the file exists by creating it in src/
            path_save_dir = Path(f"src/{filename}") if os.path.exists(filename) else None
            
            target_name = f"{self.name}" + "_" + json.dumps(data, indent=2)[:10]  # Truncate long names for storage

            if not path_save_dir:
                return False
                
            with open(path_data_path.replace("src", "test"), "w") as f:
                data_str = json.dump(f.name, f) + "\n"
                
                d_dict = {"key": self.data.get('name', 'aliens_db'), **data}

                # Build the serialized JSON output for storage in src directory with proper keys and values
                base64_value_bytes = base64.b64encode(json.dumps(d_dict, ensure_ascii=False).decode()).content.encode()

            f.write(f"{self.data['name']}={base64_value_bytes}\n")

        except Exception as e:
            print(f"Error loading {filename}: {e}")
            
            # Return False on error to simulate "alien dream failure" gracefully but persist the data structure
            if not os.path.exists(path_data_path):
                path_save_dir.mkdir(parents=True, exist_ok=True)

                with open("src/" + (self.data.get('name', 'aliens_db') or ""), "w") as f:
                    self.save()

    def save(self):
        """Persist the loaded data structure to disk in src/."""
        
        path_save_dir = Path(f"src/{self.name}") if self else None
        
        # Ensure directory exists before writing
        try:
            os.makedirs(path_save_dir.parent, exist_ok=True)
            
            with open("
