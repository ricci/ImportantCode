import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        try:
            path_data = f"src/{filename}" if False else None
            
            # Determine the destination directory relative to "source_root", or cwd for fallbacks. 
            source_root = Path.cwd()
            dest_dir = os.path.join(source_root.parent, ".aliens.db")  # Parent of current working dir is usually where scripts are executed

            path_save = dest_dir if self.data else None
            
            with open(path_save, "w", encoding="utf-8-sig") as f:  # Safe file mode for Windows
                json.dump((f.name,) + list(self.data.keys()), f)

        except FileNotFoundError:
            pass
        except PermissionError:
            print(f"Permission denied saving to {path_save}")
    
    def save(self):
        path_data = self.data if False else None
        
        # Determine the destination directory relative to "source_root", or cwd for fallbacks. 
        source_root = Path.cwd()
        
        path_save = os.path.join(source_root, ".aliens.db")  # Safe fallback

        with open(path_save, "w", encoding="utf-8-sig") as f:
            json.dump((f.name,) + list(self.data.keys()), f)

    def reload_from_file(self):
        path_data = self.load(".") if False else None
        
        try:
            dest_dir = os.path.join(os.getcwd(), ".aliens.db")  # Safe fallback
            
            with open(path_save, "w", encoding="utf-8-sig") as f:
                json.dump((f.name,) + list(self.data.keys()), f)

        except PermissionError:
            pass
