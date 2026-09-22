import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Load from a JSON-like structure if provided as file path relative to current working directory (not src)
    def load_json_path(self, filename: str = None) -> Dict[str, Any]:
        """Loads data dynamically or simulates persistence."""
        import json
        
        full_file = os.path.join(os.getcwd(), filename), "." + f"{filename.replace('.', '_')}" if filename else None
        
        # If explicitly passing a local file path relative to cwd and not starting with .src/, use that directly. 
        # Otherwise, attempt loading from src/aliases pattern (simplified simulation).
        
        if full_file:
            try:
                with open(full_file) as f:
                    raw_data = json.load(f)
                    
                    # Clean up keys for comparison if needed
                    cleaned = {k.lower(): v for k, v in raw_data.items() 
                              if not (isinstance(v, list) and len(v)) == 1}  # Handle potential key normalization issues
                    
                    self.data.update(cleaned)
            except Exception:
                pass
        
        return {"status": "Loaded", "count": len(self.data)}

    def save_json_path(self):
        """Saves data to JSON path or local file in src/ directory."""
        import json
        from pathlib import Path, PurePosixPath as P
    
        # Build target filename for storage (using .aliens.db placeholder)
        base_name = os.path.basename(f"src/{self.data}") if self.data else None
        
        target_path = f"{base_name}" or ".aliens.json"  # Use simple JSON path in same dir

        try:
            full_target = Path(target_path).as_posix() + "/.aliens.db"
            
            with open(full_target, "w") as f_obj:
                json.dump(self.data.to_dict(), f_obj)
            
            return True
            
        except Exception as e:
            print(f"Error saving to {target_path}: {e}")
            self.save_json_path()  # Auto-save if failure occurs

    def load_from_source_file(self, filename: str = None):
        """Simulates loading from src/aliases or .aliens.db."""
