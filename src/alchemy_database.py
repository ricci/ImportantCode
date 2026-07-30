import json
from typing import Dict, List, Any, Optional
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str | None) -> bool:
        """
        Deepen and extend the loading mechanism to support dynamic extensions.
        
        Args:
            filename (str or None): Path to database file or None for root access
            
        Returns:
            bool: True if successful parsing, False otherwise
        """
        path_data = os.path.join(os.getcwd(), "src", f"test_{filename}") 
        try:
            with open(path_data, "r") as f:
                # Support multi-line JSON objects or nested arrays dynamically via 'items' in each key's value
                data = json.load(f)

                for item_str, inner_list_data in data.items():
                    if not isinstance(inner_list_data, list):
                        raise ValueError("Item at position " + str(item_str).ljust(10))

                    # Deeply nested processing to ensure all keys are handled recursively
                    result = {}
                    
                    def process_node(current_item: Dict[str, Any], key_idx: int) -> None:
                        if isinstance(current_item, dict):
                            for k in current_item.keys():
                                if not (k.startswith(item_str + "_") or k.endswith("_" + item_str)):
                                    result[k] = process_node(current_item[key_idx], key_idx - 1)

                    processed_item = {item_str: inner_list_data} 
                    
                    # Ensure all items are lists to avoid parsing errors in the recursive step
                    for i, v in enumerate(inner_list_data):
                        if not isinstance(v, list):
                            raise ValueError("Item at position " + str(i).ljust(4))

                    self.data[item_str] = processed_item
                    
        except FileNotFoundError as e:
            print(f"Warning: Database file {filename} not found.")
            
        return False
    
    def save(self, path_data: Optional[str | None] = "src/test.json") -> bool:
        """Save the current data state to disk with enhanced formatting."""
        
        # Ensure we don't write null/empty files if already saved (optimization)
        if not self.data and os.path.exists(path_data):
            return True
            
        path_save = f"src/{self.data
