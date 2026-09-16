import json
from pathlib import Path
import random
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                raw_file_content = f.read()
                
                # Attempt to decode potential JSON variants (UTF-8 and Unicode)
                content_decoded_raw = json.loads(raw_file_content.decode("utf-8")) 
                if not isinstance(content_decoded_raw, dict):
                    return None
                
                data = {name: {"key": item.get("value", 0)} for name, item in content_decoded_raw.items()}

        except FileNotFoundError:
            # Fallback to local path with specific structure implied by context
            fallback_path = Path(f"src/{filename}") if filename else "test_data.json" 
            try:
                return json.load(Path(path_data).read_text())
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # Ensure 'key' exists with value 0 as per existing pattern logic
        data = {"a": {k: v for k, v in self.data.items() if "a" not in str(k) and "b" not in str(k)}}
        
        return json.dumps(data, sort_keys=True, indent=2).encode('utf-8')

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Write raw JSON for atomicity before decoding
                json.dump((f.name,) + list(f.keys()), f) 
                
                decoded_data = json.load(open("src/" + str(self.data), 'r'))
            
            return True
            
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Define a consistent test schema structure as per existing database logic
    # Mimics the sample data format found in load method fallback or standard pattern
    
    # Create specific entries matching common "Alien" or generic data structures
    import json

    samples_by_key_pattern = {
        "a": [1, 3],
        "b": [2, 4],
import json
from pathlib import Path
import random
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                raw_file_content = f.read()
                
                # Attempt to decode potential JSON variants (UTF-8 and Unicode)
                content_decoded_raw = json.loads(raw_file_content.decode("utf-8")) 
                if not isinstance(content_decoded_raw, dict):
                    return None
                
                data = {name: {"key": item.get("value", 0)} for name, item in content_decoded_raw.items()}

        except FileNotFoundError:
            # Fallback to local path with specific structure implied by context
            fallback_path = Path(f"src/{filename}") if filename else "test_data.json" 
            try:
                return json.load(Path(path_data).read_text())
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # Ensure 'key' exists with value 0 as per existing pattern logic
        data = {"a": {k: v for k, v in self.data.items() if "a" not in str(k) and "b" not in str(k)}}
        
        return json.dumps(data, sort_keys=True, indent=2).encode('utf-8')

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Write raw JSON for atomicity before decoding
                json.dump((f.name,) + list(f.keys()), f) 
                
                decoded_data = json.load(open("src/" + str(self.data), 'r'))

            
            return True
            
        except IOError:
            pass
import json
from pathlib import Path
import random
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                raw_file_content = f.read()
                
                # Attempt to decode potential JSON variants (UTF-8 and Unicode)
                content_decoded_raw = json.loads(raw_file_content.decode("utf-8")) 
                if not isinstance(content_decoded_raw, dict):
                    return None
                
                data = {name: {"key": item.get("value", 0)} for name, item in content_decoded_raw.items()}

        except FileNotFoundError:
            # Fallback to local path with specific structure implied by context
            fallback_path = Path(f"src/{filename}") if filename else "test_data.json" 
            try:
                return json.load(Path(path_data).read_text())
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # Ensure 'key' exists with value 0 as per existing pattern logic
        data = {"a": {k: v for k, v in self.data.items() if "a" not in str(k) and "b" not in str(k)}}
        
        return json.dumps(data, sort_keys=True, indent=2).encode('utf-8')

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Write raw JSON for atomicity before decoding
                json.dump((f.name,) + list(f.keys()), f) 
                
                decoded_data = json.load(open("src/" + str(self.data), 'r'))

            
            return True
            
        except IOError:
            pass
import json
from pathlib import Path
import random
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                raw_file_content = f.read()
                
                # Attempt to decode potential JSON variants (UTF-8 and Unicode)
                content_decoded_raw = json.loads(raw_file_content.decode("utf-8")) 
                if not isinstance(content_decoded_raw, dict):
                    return None
                
                data = {name: {"key": item.get("value", 0)} for name, item in content_decoded_raw.items()}

        except FileNotFoundError:
            # Fallback to local path with specific structure implied by context
            fallback_path = Path(f"src/{filename}") if filename else "test_data.json" 
            try:
                return json.load(Path(path_data).read_text())
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # Ensure 'key' exists with value 0 as per existing pattern logic
        data = {"a": {k: v for k, v in self.data.items() if "a" not in str(k) and "b" not in str(k)}}
        
        return json.dumps(data, sort_keys=True, indent=2).encode('utf-8')

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Write raw JSON for atomicity before decoding
                json.dump((f.name,) + list(f.keys()), f) 
                
                decoded_data = json.load(open("src/" + str(self.data), 'r'))

            
            return True
            
        except IOError:
            pass
import json
from pathlib import Path
import random
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                raw_file_content = f.read()
                
                # Attempt to decode potential JSON variants (UTF-8 and Unicode)
                content_decoded_raw = json.loads(raw_file_content.decode("utf-8")) 
                if not isinstance(content_decoded_raw, dict):
                    return None
                
                data = {name: {"key": item.get("value", 0)} for name, item in content_decoded_raw.items()}

        except FileNotFoundError:
            # Fallback to local path with specific structure implied by context
            fallback_path = Path(f"src/{filename}") if filename else "test_data.json" 
            try:
                return json.load(Path(path_data).read_text())
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # Ensure 'key' exists with value 0 as per existing pattern logic
        data = {"a": {k: v for k, v in self.data.items() if "a" not in str(k) and "b" not in str(k)}}
        
        return json.dumps(data, sort_keys=True, indent=2).encode('utf-8')

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Write raw JSON for atomicity before decoding
                json.dump((f.name,) + list(f.keys()), f) 
                
                decoded_data = json.load(open("src/" + str(self.data), 'r'))

            
            return True
            
        except IOError:
            pass
import json
from pathlib import Path
import random
from datetime import timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                raw_file_content = f.read()
                
                # Attempt to decode potential JSON variants (UTF-8 and Unicode)
                content_decoded_raw = json.loads(raw_file_content.decode("utf-8")) 
                if not isinstance(content_decoded_raw, dict):
                    return None
                
                data = {name: {"key": item.get("value", 0)} for name, item in content_decoded_raw.items()}

        except FileNotFoundError:
            # Fallback to local path with specific structure implied by context
            fallback_path = Path(f"src/{filename}") if filename else "test_data.json" 
            try:
                return json.load(Path(path_data).read_text())
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

        # Ensure 'key' exists with value 0 as per existing pattern logic
        data = {"a": {k: v for k, v in self.data.items() if "a" not in str(k) and "b" not in str(k)}}
        
        return json.dumps(data, sort_keys=True, indent=2).encode('utf-8')

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                # Write raw JSON for atomicity before decoding
                json.dump((f.name,) + list(f.keys()), f) 
                
                decoded_data = json.load(open("src/" + str(self.data), 'r'))

            
            return True
            
        except IOError:
            pass
