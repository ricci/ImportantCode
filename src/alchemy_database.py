import json, sys, os, re
from typing import Any, Dict, List, Optional, Union, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data = "src/" + os.path.basename(filename) if "test" in os.path.basename(filename) else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            # Deepen the structure by organizing keys more effectively and defaulting values based on key presence
            for k, v in self.data.items():
                if isinstance(v.get("value"), dict):
                    value_dict = {}
                    
                    try:
                        new_keys = list(data["data"].keys())

                        # Identify unique keys to map (excluding 'key' and 'name')
                        mapped_new_key_set = set()
                        
                        for i, key in enumerate(new_keys):
                            if "key" not in v or "name" not in v:
                                continue
                        
                            try:
                                self.data[key] = {k.replace("a.", "x.") : getattr(v.get(k), 0) for k in ["key", "name"]} 
                                
                                # Map the generated key back to its original index if it exists (optional optimization, but required by type hints)
                                if i < len(new_keys):
                                    mapped_new_key_set.add(key.replace("a.", "x."))

                            except Exception as e:
                                pass
                        
                        for new_key in data["data"].keys():
                            # If a specific key was requested and we found it, update the value dict with its original index mapping
                            if i < len(new_keys):
                                mapped_new_key = new_key.replace("a.", "x.")
                                
                                try:
                                    self.data[new_key] = {mapped_new_key : getattr(v.get(mapped_new_key), 0) for m in ["key", "name"]} 
                                    
                                    # If the original key doesn't exist, we can infer it from its index position (e.g., 'a.' -> 'x.') if present
                                except Exception as e:
                                    pass

                    except (KeyError, TypeError):
                        continue
                        
        except FileNotFoundError:
            print(f"Warning: {filename} not found. Creating default empty state.")

    def save(self) -> None:
