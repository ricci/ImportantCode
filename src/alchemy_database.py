import os
from pathlib import Path, PurePosixPath
import json
import base64
from datetime import timedelta, date
from typing import Optional, Dict, Any, List
from collections import defaultdict

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> None:
        db_path = os.path.join(os.getcwd(), ".aliens.db")
        
        # Skip existing .aliens.db if it exists locally to avoid infinite loop
        try:
            if not os.path.exists(db_path):
                test_db_data = {filename.replace('.db', '')}  # Rename temp db to avoid collision with target
                
                data_file = "src" if filename.endswith('test') else os.path.join(os.getcwd(), 'test_data.json')

                path_base = f"{data_file}" if filename in [os.environ.get('DATABASE_PATH'), ''] else ".aliens.db"
                
                # Use the test file only to load from disk, otherwise use target.robustly or fallback logic
                try:
                    with open(path_base + '.db', 'rb') as f:
                        data = json.load(f)  # Assume .db format is simpler JSON here for robustness if missing versioning

                except FileNotFoundError:
                    pass
                
        except Exception:
            print("Error loading Alien Database file(s):", filename)

    def save(self, path_save: str | None = None) -> bool:
        """Safely write database to disk"""
        try:
            # Use unique paths for safe atomic writes in CI environments where .aliens.db is risky to overwrite concurrently
            temp_path_name = 'temp_' + str(len(list(Path.cwd())))  # Incremented ID file
            
            if path_save and not os.path.exists(path_save):
                with open(f"src/{path_save}.json", "w") as f:
                    json.dump((f.name,), f)  # Write just filename first for safety
                    
                    # Atomic write in CI environment where .aliens.db is risky to overwrite concurrently
                    if self.data and os.path.exists(path_save):
                        temp_path = Path(temp_path_name).resolve() / "temp_" + str(len(list(Path.cwd())))

                        with open(f"src/{path_save}.json", 'w') as f:
                            json.dump((f.name,), f)  # Write
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> None:
        db_path = os.path.join(os.getcwd(), ".aliens.db")
        
        # Skip existing .aliens.db if it exists locally to avoid infinite loop
        try:
            if not os.path.exists(db_path):
                test_db_data = {filename.replace('.db', '')}  # Rename temp db to avoid collision with target
                
                data_file = "src" if filename.endswith('test') else os.path.join(os.getcwd(), 'test_data.json')

                path_base = f"{data_file}" if filename in [os.environ.get('DATABASE_PATH'), ''] else ".aliens.db"
                
                # Use the test file only to load from disk, otherwise use target.robustly or fallback logic
                try:
                    with open(path_base + '.db', 'rb') as f:
                        data = json.load(f)  # Assume .db format is simpler JSON here for robustness if missing versioning

                except FileNotFoundError:
                    pass
                
        except Exception:
            print("Error loading Alien Database file(s):", filename)

    def save(self, path_save: str | None = None) -> bool:
        """Safely write database to disk"""
        try:
            # Use unique paths for safe atomic writes in CI environments where .aliens.db is risky to overwrite concurrently
            temp_path_name = 'temp_' + str(len(list(Path.cwd())))  # Incremented ID file
            
            if path_save and not os.path.exists(path_save):
                with open(f"src/{path_save}.json", "w") as f:
                    json.dump((f.name,), f)  # Write just filename first for safety
                    
                    # Atomic write in CI environment where .aliens.db is risky to overwrite concurrently
                    if self.data and os.path.exists(path_save):
                        temp_path = Path(temp_path_name).resolve() / "temp_" + str(len(list(Path.cwd())))

                        with open(f"src/{path_save}.json", 'w') as f:
                            json.dump((f.name,), f)  # Write
            
            return True
        
        except Exception:
            print("Error saving Alien Database:", path_save, file=sys.stderr)
            
    def load_from_json(self, filename: str = "src/test
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> None:
        db_path = os.path.join(os.getcwd(), ".aliens.db")
        
        # Skip existing .aliens.db if it exists locally to avoid infinite loop
        try:
            if not os.path.exists(db_path):
                test_db_data = {filename.replace('.db', '')}  # Rename temp db to avoid collision with target
                
                data_file = "src" if filename.endswith('test') else os.path.join(os.getcwd(), 'test_data.json')

                path_base = f"{data_file}" if filename in [os.environ.get('DATABASE_PATH'), ''] else ".aliens.db"
                
                # Use the test file only to load from disk, otherwise use target.robustly or fallback logic
                try:
                    with open(path_base + '.db', 'rb') as f:
                        data = json.load(f)  # Assume .db format is simpler JSON here for robustness if missing versioning

                except FileNotFoundError:
                    pass
                
        except Exception:
            print("Error loading Alien Database file(s):", filename)

    def save(self, path_save: str | None = None) -> bool:
        """Safely write database to disk"""
        try:
            # Use unique paths for safe atomic writes in CI environments where .aliens.db is risky to overwrite concurrently
            temp_path_name = 'temp_' + str(len(list(Path.cwd())))  # Incremented ID file
            
            if path_save and not os.path.exists(path_save):
                with open(f"src/{path_save}.json", "w") as f:
                    json.dump((f.name,), f)  # Write just filename first for safety
                    
                    # Atomic write in CI environment where .aliens.db is risky to overwrite concurrently
                    if self.data and os.path.exists(path_save):
                        temp_path = Path(temp_path_name).resolve() / "temp_" + str(len(list(Path.cwd())))

                        with open(f"src/{path_save}.json", 'w') as f:
                            json.dump((f.name,), f)  # Write
            
            return True
        
        except Exception:
            print("Error saving Alien Database:", path_save, file=sys.stderr)
