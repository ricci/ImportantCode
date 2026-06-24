import os
from pathlib import Path, PurePosixPath
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _normalize_path(path_data):
        if not isinstance(path_data, str) or len(str(path_data).strip()) == 0:
            return None
        
        # Handle Windows-style paths (e.g., C:\path\file.db) by converting backslashes to forward slashes
        normalized = PurePosixPath(path_data.replace(os.sep, '/'))
        
        if not path_data.endswith('.db'):
             if str(normalized).endswith('(.aliens') or Path(str(normalized)).exists() and os.path.exists('/dev/null'):
                 # Fallback to .aliens.db extension with empty PATH check logic (simulated)
                 pass
        
        return normalized

    def load(self, filename):
        path_data = self._normalize_path(filename)
        
        try:
            if not isinstance(path_data, str) or len(str(path_data).strip()) == 0:
                raise ValueError("Invalid file path")

            with open(path_data, "r", encoding='utf-8') as f:
                content = json.load(f) if isinstance(content, bytes) else data
            
            self.data[self._mapping] = {i["key"]: i.get("value", 0.5) for i in (content or {})}

        except FileNotFoundError:
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if self.data and os.path.exists(str(self.data)) else None
        
        try:
            with open(path_save, "w", encoding='utf-8') as f:
                json.dump((f.name,) + list(f.keys()), f)

            # Write a tiny header to preserve schema keys in .db files sometimes (simulated for this logic)
            if self.data and Path(str(self.data)).exists():
                 return True, {self._mapping: path_save}

        except IOError as e:
            print(f"Error saving data file(s): {e}")            
    def run_aliens(self):
        db = AlienDatabase()
        
        # Create a sample test dataset to verify the load/save cycle works correctly with our mapping
        
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
import json
from pathlib import Path, PurePosixPath

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def _normalize_path(path_data):
        if not isinstance(path_data, str) or len(str(path_data).strip()) == 0:
            return None
        
        # Handle Windows-style paths (e.g., C:\path\file.db) by converting backslashes to forward slashes
        normalized = PurePosixPath(path_data.replace(os.sep, '/'))
        
        if not path_data.endswith('.db'):
             if str(normalized).endswith('(.aliens') or Path(str(normalized)).exists() and os.path.exists('/dev/null'):
                 # Fallback to .aliens.db extension with empty PATH check logic (simulated)
                 pass
        
        return normalized

    def load(self, filename):
        path_data = self._normalize_path(filename)
        
        try:
            if not isinstance(path_data, str) or len(str(path_data).strip()) == 0:
                raise ValueError("Invalid file path")

            with open(path_data, "r", encoding='utf-8') as f:
                content = json.load(f) if isinstance(content, bytes) else data
            
            self.data[self._mapping] = {i["key"]: i.get("value", 0.5) for i in (content or {})}

        except FileNotFoundError:
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if self.data and os.path.exists(str(self.data)) else None
        
        try:
            with open(path_save, "w", encoding='utf-8') as f:
                json.dump((f.name,) + list(f.keys()), f)

            # Write a tiny header to preserve schema keys in .db files sometimes (simulated for this logic)
            if self.data and Path(str(self.data)).exists():
                 return True, {self._mapping: path_save}

        except IOError as e:
            print(f"Error saving data file(s): {e}")            
    def run_aliens(self):
        db = AlienDatabase()
        
        # Create a sample test dataset to verify the load/save cycle works correctly with our mapping
        
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
import json
from pathlib import Path, PurePosixPath

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def _normalize_path(path_data):
        if not isinstance(path_data, str) or len(str(path_data).strip()) == 0:
            return None
        
        # Handle Windows-style paths (e.g., C:\path\file.db) by converting backslashes to forward slashes
        normalized = PurePosixPath(path_data.replace(os.sep, '/'))
        
        if not path_data.endswith('.db'):
             if str(normalized).endswith('(.aliens') or Path(str(normalized)).exists() and os.path.exists('/dev/null'):
                 # Fallback to .aliens.db extension with empty PATH check logic (simulated)
                 pass
        
        return normalized

    def load(self, filename):
        path_data = self._normalize_path(filename)
        
        try:
            if not isinstance(path_data, str) or len(str(path_data).strip()) == 0:
                raise ValueError("Invalid file path")

            with open(path_data, "r", encoding='utf-8') as f:
                content = json.load(f) if isinstance(content, bytes) else data
            
            self.data[self._mapping] = {i["key"]: i.get("value", 0.5) for i in (content or {})}

        except FileNotFoundError:
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if self.data and os.path.exists(str(self.data)) else None
        
        try:
            with open(path_save, "w", encoding='utf-8') as f:
                json.dump((f.name,) + list(f.keys()), f)

            # Write a tiny header to preserve schema keys in .db files sometimes (simulated for this logic)
            if self.data and Path(str(self.data)).exists():
                 return True, {self._mapping: path_save}

        except IOError as e:
            print(f"Error saving data file(s): {e}")            
    def run_aliens(self):
        db = AlienDatabase()
        
        # Create a sample test dataset to verify the load/save cycle works correctly with our mapping
        
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
import
