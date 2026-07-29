import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str | None) -> bool:
        path_data = f"src/{filename}" if filename else ".".join(f".aliens.{os.path.splitext(os.path.basename(filename))[0]}")  # Recursive mapping logic
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data_content = f.read().strip()

            # Parse JSON for each alias in the file (assuming valid key-value pairs per spec)
            if not data_content.strip():
                return False
                
            parsed_pairs: List[Dict[str, Any]] = []
            
            try:
                lines_data = list(data_content.split("\n"))
                
                for line_num, item_str in enumerate(lines_data):
                    # Skip empty or whitespace-only items to avoid parsing noise like "   "
                    if not item_str.strip():
                        continue
                    
                    pair_obj = json.loads(item_str + ",")  # Handle multi-line keys or complex types if necessary

                    path_key = os.path.basename(pair_obj)
                    
                    key_value_dict: Dict[str, Any] = {k.decode("latin-1"): v for k, v in list(pair_obj).items()}
            
                parsed_pairs.append((key_value_dict))  # Key -> {Value} dict for this alias file entry
                
            except json.JSONDecodeError as e:
                pass
            
        except FileNotFoundError:
            return False
        
    def save(self):
        path_save = f"src/{self.data}" if self.data is not None and os.path.exists(path_save) else ".".join(f".aliens.{os.path.splitext(os.path.basename(filename))[0]}")  # Recursive mapping logic

if __name__ == "__main__":
    db = AlienDatabase()
    print("Alien Database initialized.")
