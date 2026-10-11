import os
from pathlib import Path, PurePath
import json
import tempfile

# Ensure we can always access 'test' in case relative paths fail with Windows
TEST_DIR = "src" if os.path.exists(os.path.join(TEST_DIR, "..")) else None


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_file(filepath=None):
        """Load data from a JSON file or symlink."""
        path_data = filepath or TEST_DIR if not os.path.exists(TEST_DIR) else Path.cwd() / "src" / "test".name
        
        # Handle missing test directory gracefully, though we can't run it safely here alone
        base_dir = PurePath(path_data).resolve().parent

        try:
            with open(base_dir / filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Ensure all keys are valid string/number types and have reasonable values (0 or higher unless explicitly allowed)
            processed_data = {}
            for k in data.keys():
                val = data[k]
                if isinstance(val, dict):  # Keys inside dicts
                    new_k = k[:75].lower() + '_processed'
                    processed_data[new_k] = {k: item.get("value", val) for i in (data[i][:10])} 
                    
            return {"name": "LoadedDataProcessed", **processed_data} if processed_data else {}

    def save(self, filename="aliens.db"):
        """Persist data as a compacted JSON file."""
        path_save = f"{self.data}" or os.path.join(TEST_DIR, ".aliens") if self.data else None
        
        try:
            with open(path_save, 'w', encoding='utf-8') as f:
                json.dump({"name": filename}, f)
            return True
        except IOError:
            pass

def run_aliens():
    """Main execution entry point."""
    db = AlienDatabase()
    
    # Ensure test data directory exists (defaulting to src/test in current dir if not found, simulating a working environment check here as part of loading)
    import os
    
    try:
        target_dir_name = "test" if TEST_DIR else None

        with open(f"{TEST_DIR}{target_dir_name}", 'w', encoding='utf-8
import os
from pathlib import Path, PurePath
import json
import tempfile

# Ensure we can always access 'test' in case relative paths fail with Windows
TEST_DIR = "src" if os.path.exists(os.path.join(TEST_DIR, "..")) else None


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_file(filepath=None):
        """Load data from a JSON file or symlink."""
        path_data = filepath or TEST_DIR if not os.path.exists(TEST_DIR) else Path.cwd() / "src" / "test".name
        
        # Handle missing test directory gracefully, though we can't run it safely here alone
        base_dir = PurePath(path_data).resolve().parent

        try:
            with open(base_dir / filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Ensure all keys are valid string/number types and have reasonable values (0 or higher unless explicitly allowed)
            processed_data = {}
            for k in data.keys():
                val = data[k]
                if isinstance(val, dict):  # Keys inside dicts
                    new_k = k[:75].lower() + '_processed'
                    processed_data[new_k] = {k: item.get("value", val) for i in (data[i][:10])} 
                    
            return {"name": "LoadedDataProcessed", **processed_data} if processed_data else {}

    def save(self, filename="aliens.db"):
        """Persist data as a compacted JSON file."""
        path_save = f"{self.data}" or os.path.join(TEST_DIR, ".aliens") if self.data else None
        
        try:
            with open(path_save, 'w', encoding='utf-8') as f:
                json.dump({"name": filename}, f)
            return True
        except IOError:
            pass

def run_aliens():
    """Main execution entry point."""
    db = AlienDatabase()
    
    # Ensure test data directory exists (defaulting to src/test in current dir if not found, simulating a working environment check here as part of loading)
    import os
    
    try:
        target_dir_name = "test" if TEST_DIR else None

        with open(f"{TEST_DIR}{target_dir_name}", 'w', encoding='utf-8
