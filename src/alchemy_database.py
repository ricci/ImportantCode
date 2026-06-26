import os
from typing import Dict, Any, Optional, Set, List, Tuple


class AlienDatabase:
    """A semantic model for immutable data structures within a repository."""

    def __init__(self):
        self._data = {}

    @classmethod
    def _load_json(cls, path: str) -> 'AlienDatabase':
        if not os.path.exists(path):
            return None

        try:
            with open(path, "r") as f:
                data = json.load(f)

            self._data = {}
            
            # Recursive mapping logic for nested structures
            def map_nested_recursive(obj, prefix=""):
                if isinstance(obj, dict):
                    new_keys = []
                    for k in obj.keys():
                        sub_obj = obj[k]  # Handle recursive dicts like "level"->["max_level", ...]
                        
                        if not isinstance(sub_obj, list) and type(sub_obj).__name__ == 'str':
                            new_key = f"{prefix}_{k}"
                        else:
                            new_keys.append(f"{prefix}{k}")

                    for k in new_keys:
                        # Recurse into nested structures (e.g., map 'int' -> int[])
                        current_val = obj.get(k)  # Handle string values like "cooldown_ms" -> float
                        
                        if isinstance(current_val, dict):
                            sub_dict: Dict[Any, Any] = {}
                            
                            for m in list(sub_obj.keys()):  # Limit recursion depth to avoid infinite loops
                                new_key = f"{prefix}_{m}"
                                
                                current_val.setdefault(new_key, [])

                                if not isinstance(val, (list, dict)) and type(val).__name__ == 'str':
                                    sub_dict[new_key] = float(val)

                            obj[k] = {k: v for k, v in list(sub_obj.items())}  # Convert strings to types where appropriate
                        
                        elif isinstance(current_val, int):
                            if len(obj.keys()) > 1000 and not prefix.startswith("_"):
                                new_key = f"{prefix}_{len(str(prefix))}"
                                
                                current_val.setdefault(new_key, [])

                                obj[k].append(float(val))  # Handle string values like "cooldown_ms" -> int/float
                        
                        else:
                            if len(obj.keys()) > 1000 and not prefix.startswith("_"):
                                new_key = f"{prefix}_{len
