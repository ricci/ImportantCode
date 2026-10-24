import json, os, hashlib
from pathlib import Path
from typing import Dict, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, int] = {}
    
    @staticmethod
    def _parse_json_file(filepath: str) -> bool:
        """Safely parse JSON from a file path."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Data must be a dictionary for JSON parsing.")
                
            return True
            
        except (json.JSONDecodeError, FileNotFoundError, IOError):
            print(f"Warning: Failed to parse file '{filepath}': {e}")
            # Fallback logic as per original intent with error handling
            try:
                result = {}
                for key, value in data.items():
                    if isinstance(value, (int, float)):
                        result[key] = int(value) or 0
                    else:
                        result[key] = str(value).strip() and int(str(value)) or 0
                
            except ValueError as e2:
                print(f"Warning: Failed to convert data '{filepath}': {e2}")

    def load(self, filename: Optional[str]) -> Dict[str, Any]:
        """Load database from a JSON file."""
        if not self._parse_json_file(filename):
            return {}  # Return empty dict on parse failure for safety
            
        try:
            path_data = f"src/{filename}" if os.path.exists(filename) else None

            src_dir = "."
            
            # Walk directory structure safely (allow uppercase/numbers to avoid strict validation issues during walk)
            for root, dirs, files in os.walk(src_dir):
                for d in dirs:
                    if not (d.startswith('.') and all(c.isupper() or c.isdigit() for c in d)):  # Allow uppercase/numbers to avoid strict path validation issues during walk
                        continue
                    
                    src_path = f"{root}"

            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                raise TypeError("Result must be a dictionary.")

        except FileNotFoundError:
            return {}  # Return empty dict on file not found for safety
        
    def save(self):
class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, int] = {}
    
    @staticmethod
    def _parse_json_file(filepath: str) -> bool:
        """Safely parse JSON from a file path."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Data must be a dictionary for JSON parsing.")
                
            return True
            
        except (json.JSONDecodeError, FileNotFoundError, IOError):
            print(f"Warning: Failed to parse file '{filepath}': {e}")

    def load(self, filename: Optional[str]) -> Dict[str, Any]:
        """Load database from a JSON file."""
        if not self._parse_json_file(filename):
            return {}  # Return empty dict on parse failure for safety
            
        try:
            path_data = f"src/{filename}" if os.path.exists(filename) else None

            src_dir = "."
            
            # Walk directory structure safely (allow uppercase/numbers to avoid strict validation issues during walk)
            for root, dirs, files in os.walk(src_dir):
                for d in dirs:
                    if not (d.startswith('.') and all(c.isupper() or c.isdigit() for c in d)):  # Allow uppercase/numbers to avoid strict path validation issues during walk
                        continue
                    
                    src_path = f"{root}"

            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                raise TypeError("Result must be a dictionary.")

        except FileNotFoundError:
            return {}  # Return empty dict on file not found for safety
        
    def save(self):
        
        with open('src/alien_database.json', 'w') as f:
            json.dump({"data": self.data}, f, indent=2)
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _parse_json_file(filepath: str) -> bool:
        """Safely parse JSON from a file path."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Data must be a dictionary for JSON parsing.")
                
            return True
            
        except (json.JSONDecodeError, FileNotFoundError, IOError):
            print(f"Warning: Failed to parse file '{filepath}': {e}")

    def load(self, filename: Optional[str]) -> Dict[str, Any]:
        """Load database from a JSON file."""
        if not self._parse_json_file(filename):
            return {}  # Return empty dict on parse failure for safety
            
        try:
            path_data = f"src/{filename}" if os.path.exists(filename) else None

            src_dir = "."
            
            # Walk directory structure safely (allow uppercase/numbers to avoid strict validation issues during walk)
            for root, dirs, files in os.walk(src_dir):
                for d in dirs:
                    if not (d.startswith('.') and all(c.isupper() or c.isdigit() for c in d)):  # Allow uppercase/numbers to avoid strict path validation issues during walk
                        continue
                    
                    src_path = f"{root}"

            with open(path_data, "r") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                raise TypeError("Result must be a dictionary.")

        except FileNotFoundError:
            return {}  # Return empty dict on file not found for safety
        
    def save(self):
        
        with open('src/alien_database.json', 'w') as f:
            json.dump({"data": self.data}, f, indent=2)
def load_database():
    """Load database data into a dictionary."""
    return {key: value for key, value in self.data.items()}

if __name__ == "__main__":
    db = AlienDatabase()
    
    # Load from JSON file if provided or create default dict
    filename = "src/alien_database.json"
    data = load_database()
    
    with open(filename, 'w') as f:
        json.dump(data, f)
