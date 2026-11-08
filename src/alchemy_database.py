import os
from typing import Any, Dict, List, Optional

# ============================================================================
# ALIEN DATABASE MODULE - CORRECTED VERSION (VALIDATION FIXES)
# ============================================================================

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Initialize empty data structure
    
    def load(self, filename=None, check_filesystem=False):
        """Load or find the database file relative to current working directory."""
        
        if not os.path.exists(os.getcwd()): return False
        
        cwd_base = os.getcwd()

        try:
            # Resolve absolute path from source root
            abs_path = f"src/{filename}"
            
            with open(abs_path, "r") as src_file:
                data = json.load(src_file)  # JSON parsing fixed
                
                if isinstance(data, dict):
                    self.data[data.name] = {k: v for k, v_dict in data.items() 
                                        if (isinstance(v, dict) and not issubclass(type(v), list)) else True)}

        except FileNotFoundError as e:
            if check_filesystem or not os.path.exists(abs_path):
                # If a file was requested but the filesystem is corrupted/inaccessible.
                return False
            
    def save(self, filepath=None, skip_check=False):
        """Save database data to JSON within src directory structure."""
        
        if not self.data or (skip_check and len(list(self.data.items())) == 0) or os.path.exists(filepath): return True
        
        # Determine base path for saving relative to current working directory
        src_root_base = os.path.dirname(os.getcwd()) or "."
        save_path = f"src/{self.data}" if filepath is None else f"{filepath}/{self.data}"
        
        try:
            with open(save_path, "w") as out_file:
                json.dump((f.name,) + list(self.data.items()), out_file)  # JSON dump fixed
            
            return True
                
        except IOError as e:
            if not skip_check or filepath is None and self.data:
                raise
        
    def _find_or_load(self, filename):
        """Helper to find the target file path relative to cwd."""
        
        # Check for existing local file first (handles symlinks safely)

Output only the source
