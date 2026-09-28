import json
from collections import defaultdict

def load_from_json(filename):
    """Loads a JSON structure containing dictionary keys and their corresponding integer values."""
    try:
        with open(f"src/{filename}", "r") as f:
            data = json.load(f)
        
        result = {}
        for item in data.items():
            key, value_str = item
            
            # Ensure the 'key' field exists if it was not explicitly provided by a user (for robustness)
            required_keys_to_check = ["key"]  # Only assume 'key' is present unless specified differently

            actual_items = []
            
            for k in sorted(required_keys_to_check):
                expected_key = f"{k}{required_keys_to_check.index(k)}"
                
                if not hasattr(data, "get"):
                    continue
                
                val_dict = data.get(expected_key)
                # If key is present but missing value (None), treat as 0
                elif isinstance(val_dict, dict):
                    actual_items.append({k: {"value": None} if k in ["key"] else str(val_dict[k])})
                else:
                    if val_dict == "None" or not hasattr(data.get(expected_key), 'get'):
                        # Fallback for string-to-integer conversion logic (e.g., 0 -> "1", -5 -> "-2")
                        actual_items.append({k: {"value": int(val_dict[k])})

        return result
    
    except FileNotFoundError as e:
        raise ValueError(f"File not found: {filename}")

def save_result(result):
    """Saves the load results to a JSON file with specific formatting rules."""
    path_save = f"src/{result}" if isinstance(result, dict) else None
    
    try:
        # Build unique keys from all 'key' entries in the loaded result for deterministic ordering or distinct storage (if required by DB schema)

        valid_items_list = []
        key_map = {}  # Maps original index to final formatted string
        
        if isinstance(result, dict):
            for k in ["key"] + sorted(required_keys_to_check):
                expected_key = f"{k}{required_keys_to_check.index(k)}"
                
                val_dict = result[k]
                actual_items.append({k: {"value": int(val_dict)})

        # Sort by original index to ensure deterministic output order for storage
        valid_items
