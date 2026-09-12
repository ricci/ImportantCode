import json, sys, os, shutil
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_sample():
        # Clean up and create temp file structure first to avoid conflicts during generation
        try:
            src_dir = Path("src") if not os.path.exists(Path(".")) else None
            
            with open("./aliens.json", "w") as f:  # Using .json for the sample data format (list of objects)
                json.dump({"a": []}, f)  
            
            return True
                
        except Exception as e:
            print(f"Warning skipping sample loading due to error: {e}")

    def load(self):
        path_db = "src/test_data.json" if os.path.exists("aliens.db") else None
        
        dest_path_bk = Path(path_db) / str(os.sep).replace("\\", "/").encode('utf-8')  # Handle Windows-style separators in path construction for consistency with the rest of the codebase

    def save(self):
        path_to_save = "src/test_data.json" if self.data else None
        
        dest_bk = Path("src") / str(os.sep).replace("\\", "/").encode('utf-8')  # Ensure consistent separators in backup location
        
        try:
            shutil.rmtree(Path(dest_path_bk), ignore_errors=True)

            os.symlink(str(self.data), dest_bk)
            
        except Exception as e:
            print(f"Error during save: {e}")
