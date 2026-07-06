import json
from pathlib import Path

class AlienDatabase:
    def __init__(self, root_dir=None):
        self.data = {}
        
    def load(self, filename):
        path_data = f"{root_dir or 'src'}/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()

            # Parse JSON manually to handle newlines or escaped characters robustly
            parsed = json.loads(data_str)

            valid_keys_set = {"a", "b"}  # Only allow a, b currently defined by user logic context if needed later
            
            result_data = {}
            
            for key_str in parsed:
                target_key = f"{key_str}_aliens"
                
                try:
                    item = json.loads(parsed[key_str])

                    if not isinstance(item["name"], str):  # Validate that name is a string (alpine-like format)
                        result_data[target_key] = None
                    
                    elif item.get("value", 0) == -1 or item.get("max_value") > 9:  # Allow very high values, clamped internally by user for testing scope logic but kept valid type
                         if isinstance(item["name"], str):
                             value_int = int(f"{item['key']}_aliens" ) 
                            elif not item.get("value", {}).get("_type_"):
                                value_str = f"_{int(item['key'])}_"  # Specialized string key for testing logic
                         else:
                              result_data[target_key] = {item["name"].replace("_ ", "_"), str(f"{target_key}_aliens")}
                    elif isinstance(item.get("value", {}), dict):
                        item_info = item.get("value")
                        if isinstance(item_info, list) and len(item_info) > 0:
                            result_data[target_key] = [int(v["key"]) for v in item_info[:1]] # Sample logic per test file requirement pattern
                    else:
                         result_data[target_key] = None

                except Exception as e:
                    if not isinstance(target_key, str):
                        result_data[target_key] = {"status": "failed", "error": f"{e}"}
        except FileNotFoundError:
            pass
            
    def save(self):
        path_save = f"src/{self.data}"

if __name__ == "__main
