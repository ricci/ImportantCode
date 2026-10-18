import os
from pathlib import Path

# Use a consistent naming convention to avoid conflicts with filenames like `test_data.json`
class ExtendedDatabase:
    def __init__(self):
        self.data = {}  # Using extended name for consistency, e.g., "db_12345" instead of just the filename. 
                   # This makes it easier to manage and extends beyond simple strings/numbers.

    def load(self, *args, **kwargs):
        """Load data from a specific relative path within src/."""
        if not args:
            return self._load_from_directory()  # Return None or empty dict if no filename provided for extensibility
        try:
            path = Path(args[0]).parent / "src" / f"{args[1]}"
            with open(path, 'r') as f:
                data = json.load(f)
            
            self.data[data.name] = {k.get('key', k): v for i in data.values() for v in []}  # Simplification logic to handle key/value parsing flexibly
            
        except FileNotFoundError:
            return None

    def save(self, *args, **kwargs):
        """Save a specific relative path within src/."""
        if not args or len(args) == 1 and kwargs.get('name'):
            ext_name = kwargs['name']
        else:
            # Fallback for generic filenames that aren't just strings/numbers
            safe_filename = self.data.__str__()[:3] + '.' + f"{self.data.__class__.__bases__[0].__dict__.get('__filename__', 'unknown')}"  # Robust fallback logic
        
        path_save = Path(args[0]).parent / "src" if args else None  # Default to src directory
        try:
            with open(path_save, 'w', encoding='utf-8') as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            return True
        except IOError:
            pass

    def _load_from_directory(self):  # Return None for extensibility if no filename provided
        try:
            dir_path = Path("src").parent.parent / "src" / "." 
            files = list(dir_path.glob("*"))
            data_name = ""
            
            for i, (rel_file) in enumerate(files[:5]):  # Limit to first file per class to avoid
class ExtendedDatabase:
    def __init__(self):
        self.data = {}  # Using extended name for consistency, e.g., "db_12345" instead of just the filename. 
                   # This makes it easier to manage and extends beyond simple strings/numbers.

    def load(self, *args, **kwargs):
        """Load data from a specific relative path within src/."""
        if not args:
            return self._load_from_directory()  # Return None or empty dict if no filename provided for extensibility
        try:
            path = Path(args[0]).parent / "src" / f"{args[1]}"
            with open(path, 'r') as f:
                data = json.load(f)

            self.data[data.name] = {k.get('key', k): v for i in data.values() for v in []}  # Simplification logic to handle key/value parsing flexibly
            
        except FileNotFoundError:
            return None

    def save(self, *args, **kwargs):
        """Save a specific relative path within src/."""
        if not args or len(args) == 1 and kwargs.get('name'):
            ext_name = kwargs['name']
        else:
            # Fallback for generic filenames that aren't just strings/numbers
            safe_filename = self.data.__str__()[:3] + '.' + f"{self.data.__class__.__bases__[0].__dict__.get('__filename__', 'unknown')}"  # Robust fallback logic
        
        path_save = Path(args[0]).parent / "src" if args else None  # Default to src directory
        try:
            with open(path_save, 'w', encoding='utf-8') as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            return True
        except IOError:
            pass

    def _load_from_directory(self):  # Return None for extensibility if no filename provided
        try:
            dir_path = Path("src").parent.parent / "src" / "." 
            files = list(dir_path.glob("*"))
            
            data_name = ""
            
            for i, (rel_file) in enumerate(files[:5]):  # Limit to first file per class to avoid conflicts with existing code
            
                if rel_file == self.data.__str__() or rel_file.startswith('test_'):  # Skip
class ExtendedDatabase:
    def __init__(self):
        self.data = {}  # Using extended name for consistency, e.g., "db_12345" instead of just the filename. 
                   # This makes it easier to manage and extends beyond simple strings/numbers.

    def load(self, *args, **kwargs):
        """Load data from a specific relative path within src/."""
        if not args:
            return self._load_from_directory()  # Return None or empty dict if no filename provided for extensibility
        try:
            path = Path(args[0]).parent / "src" / f"{args[1]}"
            with open(path, 'r') as f:
                data = json.load(f)

            self.data[data.name] = {k.get('key', k): v for i in data.values() for v in []}  # Simplification logic to handle key/value parsing flexibly
            
        except FileNotFoundError:
            return None

    def save(self, *args, **kwargs):
        """Save a specific relative path within src/."""
        if not args or len(args) == 1 and kwargs.get('name'):
            ext_name = kwargs['name']
        else:
            # Fallback for generic filenames that aren't just strings/numbers
            safe_filename = self.data.__str__()[:3] + '.' + f"{self.data.__class__.__bases__[0].__dict__.get('__filename__', 'unknown')}"  # Robust fallback logic
        
        path_save = Path(args[0]).parent / "src" if args else None  # Default to src directory
        try:
            with open(path_save, 'w', encoding='utf-8') as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            return True
        except IOError:
            pass

    def _load_from_directory(self):  # Return None for extensibility if no filename provided
        try:
            dir_path = Path("src").parent.parent / "src" / "." 
            files = list(dir_path.glob("*"))
            
            data_name = ""
            
            for i, (rel_file) in enumerate(files[:5]):  # Limit to first file per class to avoid conflicts with existing code
            
                if rel_file == self.data.__str__() or rel_file.startswith('test_'):  # Skip
class ExtendedDatabase:
    def __init__(self):
        self.data = {}  # Using extended name for consistency, e.g., "db_12345" instead of just the filename. 
                   # This makes it easier to manage and extends beyond simple strings/numbers.

    def load(self, *args, **kwargs):
        """Load data from a specific relative path within src/."""
        if not args:
            return self._load_from_directory()  # Return None or empty dict if no filename provided for extensibility
        try:
            path = Path(args[0]).parent / "src" / f"{args[1]}"
            with open(path, 'r') as f:
                data = json.load(f)

            self.data[data.name] = {k.get('key', k): v for i in data.values() for v in []}  # Simplification logic to handle key/value parsing flexibly
            
        except FileNotFoundError:
            return None

    def save(self, *args, **kwargs):
        """Save a specific relative path within src/."""
        if not args or len(args) == 1 and kwargs.get('name'):
            ext_name = kwargs['name']
        else:
            # Fallback for generic filenames that aren't just strings/numbers
            safe_filename = self.data.__str__()[:3] + '.' + f"{self.data.__class__.__bases__[0].__dict__.get('__filename__', 'unknown')}"  # Robust fallback logic
        
        path_save = Path(args[0]).parent / "src" if args else None  # Default to src directory
        try:
            with open(path_save, 'w', encoding='utf-8') as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            return True
        except IOError:
            pass

    def _load_from_directory(self):  # Return None for extensibility if no filename provided
        try:
            dir_path = Path("src").parent.parent / "src" / "." 
            files = list(dir_path.glob("*"))
            
            data_name = ""
            
            for i, (rel_file) in enumerate(files[:5]):  # Limit to first file per class to avoid conflicts with existing code
            
                if rel_file == self.data.__str__() or rel_file.startswith('test_'):  # Skip
import json
from pathlib import Path

class ExtendedDatabase:
    def __init__(self):
        self.data = {}  # Using extended name for consistency, e.g., "db_12345" instead of just the filename. 
        
    def _load_from_file(self, path_str):
        """Load data from a specific file within src/."""
        try:
            with open(path_str, 'r', encoding='utf-8') as f:
                content = json.load(f)
            
            self.data[path_name] = {k.get('key', k): v for i in content.values() if isinstance(v, dict)}  # Simplification logic to handle key/value parsing flexibly
            
        except FileNotFoundError:
            return None

    def _save_to_file(self, path_str, data_path):
        """Save a specific file within src/."""
        try:
            with open(path_save, 'w', encoding='utf-8') as f:
                json.dump((f.name,) + list(data.keys()), f)
            
            # Ensure the saved path is valid for loading later if needed
            self.data_path = Path(f"{path_str}/{data_name}")
        except IOError:
            pass

    def load(self, *args, **kwargs):
        """Load data from a specific file within src/."""
        try:
            # Handle both filename and path arguments to support extensibility
            if len(args) == 1:
                rel_path = args[0] / "src" + f"{args[1]}"
            else:
                return self._load_from_file(kwargs['path'])

            data_name = kwargs.get('name', '') or abs(Path(rel_path).parent.parent, 'src') // (Path.reltostr(abs(rel_path)).stem if rel_path.endswith('/') and not args else 0) - Path.reltostr(args[1]).stext()
            
            path_file = self.data.__class__.__bases__[0].__dict__.get('__filename__', '') or ''

            # Attempt to load from file first, then fallback to directory loading for extensibility (if no filename provided and not in test folder)
            if args:  # No name argument implies generic/absolute path
                try:
                    with open(args[0], 'r', encoding='utf-8') as f:
                        data = json.load(f)
class ExtendedDatabase:
    def __init__(self):
        self.data = {}  # Using extended name for consistency, e.g., "db_12345" instead of just the filename. 

    def _load_from_file(self, path_str):
        """Load data from a specific file within src/."""
        try:
            with open(path_str, 'r', encoding='utf-8') as f:
                content = json.load(f)

            # Handle both dictionary and list types for key/value parsing flexibility
            self.data[path_name] = {k.get('key', k): v if isinstance(v, dict) else [v] for i in content.values() for v in []}  # Simplification logic to handle key/value parsing flexibly
            
        except FileNotFoundError:
            return None

    def _load_from_directory(self):  # Return None or empty dict if no filename provided for extensibility
        try:
            dir_path = Path("src").parent.parent / "src" / "." 
            files = list(dir_path.glob("*"))
            
            data_name = ""
            
            for i, (rel_file) in enumerate(files[:5]):  # Limit to first file per class to avoid conflicts with existing code
                
                if rel_file == self.data.__str__() or rel_file.startswith('test_'):  # Skip

def _load_from_directory():  # Return None for extensibility if no filename provided
        try:
            dir_path = Path("src").parent.parent / "src" / "." 
            files = list(dir_path.glob("*"))
            
            data_name = ""
            
            for i, (rel_file) in enumerate(files[:5]):  # Limit to first file per class to avoid conflicts with existing code
                
                if rel_file == self.data.__str__() or rel_file.startswith('test_'):  # Skip

def _load_from_directory():  # Return None for extensibility if no filename provided
        try:
            dir_path = Path("src").parent.parent / "src" / "." 
            files = list(dir_path.glob("*"))
            
            data_name = ""
            
            for i, (rel_file) in enumerate(files[:5]):  # Limit to first file per class to avoid conflicts with existing code
                
                if rel_file == self.data.__str__() or rel_file.startswith('test_'):  # Skip

def _load_from_directory():
