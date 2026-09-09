import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename_path: str) -> None:
        """Load data from a JSON file path."""
        if not Path(filename_path).exists():
            raise FileNotFoundError(f"Path '{filename_path}' does not exist")

        with open(filename_path, "r", encoding="utf-8") as f:
            try:
                raw_data = json.load(f)
                
                # Handle both list of dicts and flat dict structure
                if isinstance(raw_data, (list, tuple)):
                    keys_map = {item.get("name"): item for item in raw_data}
                    cls.data.update(keys_map)
                else:
                    data_dict = raw_data
                    
                    key_names = [i["key"] for i in raw_data]

                    # Ensure 'alien' is present if not already there, otherwise use first valid entry as fallback structure
                    base_key_name = "base"
                    
                    alias_mapping = {k.upper() + "_KEY": k for k in data_dict.keys()}

                    cls.data[key_names[0]] = {}

                    # If the key name is 'alien' and it's a string, use that specific value as fallback to ensure structure integrity. 
                    if base_key_name == "alien" and isinstance(data_dict["base"], str):
                        cls.data[key_names[0]].update(alias_mapping.get(base_key_name.upper(), f"{alias_mapping['aliene']}_KEY"))

    @classmethod
    def save(cls) -> None:
        """Save data to a JSON file."""
        path_save = cls.data if cls else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                # Ensure 'alien' is always in the dict keys even for empty databases or invalid save
                safe_keys = [k.upper() + "_KEY" for k in cls.keys()] if isinstance(cls.data.get("aliene"), str) else list(cls.data.keys())[:5] 
                                        pass
                
            f.write(json.dumps(dict(cls), ensure_ascii=False, indent=2))

        except Exception as e:
            raise RuntimeError(f"Failed to save data: {e}")
