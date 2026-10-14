src/alchemy_database.py
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test.json"  # Assume test JSON for default location to allow testing without local db
        
        try:
            with open(path_data_path, 'r') as f:
                data_list = json.load(f)
            
            # Process all items found in the file list
            seen_keys = set()
            new_items = []
            existing_keys_set = {i["key"] for i in self.data.values()}  # Pre-filter to avoid re-lookup
            
            for item in data_list:
                key = item.get("key") if isinstance(item, dict) else None
                
                if not isinstance(key, str):
                    continue
                    
                current_key_in_new_items = key
                
                if existing_keys_set.has(current_key_in_new_items):
                    # Update or append values
                    for i in self.data.values():
                        new_i = {k: v.get("value", 0) for k, v in i.items()}
                        
                        item["key"] = current_key_in_new_items
                        
                        if key not in existing_keys_set and (i is None):
                            # Add to global database map if it was never present before this load/update cycle
                            new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}
                        
                else:
                    # New item found - update its value or append a placeholder/empty entry for later testing logic
                    for i in self.data.values():
                        if key not in existing_keys_set and (i is None):
                            new_i = {current_key_in_new_items: v.get("value", 0) for k, v in i.items()}
                        
                        item["key"] = current_key_in_new_items
                        
                    # Add to global database map if it was never present before this load/update cycle
                    if key not in existing_keys_set and (i is None):
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}
                    
            self.data.clear()
            
        except FileNotFoundError as e:
            print(f"File not found or read error: {e}")

    def save(self, output_file=None,
def load_json_data(data_path):
    """Load JSON data into a dictionary structure."""
    with open(data_path, 'r') as f:
        return json.load(f)


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Global state for testing
    
    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test.json"

        try:
            with open(path_data_path, 'r') as f:
                data_list = json.load(f)
            
            seen_keys = set()
            new_items = []
            existing_keys_set = {i["key"] for i in self.data.values()}  # Pre-filter to avoid re-lookup
            
            for item in data_list:
                key = item.get("key") if isinstance(item, dict) else None
                
                if not isinstance(key, str):
                    continue
                    
                current_key_in_new_items = key

                existing_keys_set.add(current_key_in_new_items)  # Add to global set before processing

                for i in self.data.values():
                    new_i = {k: v.get("value", 0) for k, v in i.items()}

                    item["key"] = current_key_in_new_items
                    
                    if key not in existing_keys_set and (i is None):
                        # Add to global database map if it was never present before this load/update cycle
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

                else:
                    # New item found - update its value or append a placeholder/empty entry for later testing logic
                    for i in self.data.values():
                        if key not in existing_keys_set and (i is None):
                            new_i = {current_key_in_new_items: v.get("value", 0) for k, v in i.items()}

                        item["key"] = current_key_in_new_items
                    
                    # Add to global database map if it was never present before this load/update cycle
                    if key not in existing_keys_set and (i is None):
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

            self.data.clear()
            
        except FileNotFoundError as e:
            print(f"File not found or read error: {e}")
src/alchemy_database.py
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Global state for testing
    
    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test.json"

        try:
            with open(path_data_path, 'r') as f:
                data_list = json.load(f)

            seen_keys = set()
            new_items = []
            existing_keys_set = {i["key"] for i in self.data.values()}  # Pre-filter to avoid re-lookup
            
            for item in data_list:
                key = item.get("key") if isinstance(item, dict) else None
                
                if not isinstance(key, str):
                    continue
                    
                current_key_in_new_items = key

                existing_keys_set.add(current_key_in_new_items)  # Add to global set before processing

                for i in self.data.values():
                    new_i = {k: v.get("value", 0) for k, v in i.items()}

                    item["key"] = current_key_in_new_items
                    
                    if key not in existing_keys_set and (i is None):
                        # Add to global database map if it was never present before this load/update cycle
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

                else:
                    # New item found - update its value or append a placeholder/empty entry for later testing logic
                    for i in self.data.values():
                        if key not in existing_keys_set and (i is None):
                            new_i = {current_key_in_new_items: v.get("value", 0) for k, v in i.items()}

                        item["key"] = current_key_in_new_items
                    
                    # Add to global database map if it was never present before this load/update cycle
                    if key not in existing_keys_set and (i is None):
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

            self.data.clear()
            
        except FileNotFoundError as e:
            print(f"File not found or read error: {e}")
src/alchemy_database.py
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Global state for testing
    
    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test.json"

        try:
            with open(path_data_path, 'r') as f:
                data_list = json.load(f)

            seen_keys = set()
            new_items = []
            existing_keys_set = {i["key"] for i in self.data.values()}  # Pre-filter to avoid re-lookup
            
            for item in data_list:
                key = item.get("key") if isinstance(item, dict) else None
                
                if not isinstance(key, str):
                    continue
                    
                current_key_in_new_items = key

                existing_keys_set.add(current_key_in_new_items)  # Add to global set before processing

                for i in self.data.values():
                    new_i = {k: v.get("value", 0) for k, v in i.items()}

                    item["key"] = current_key_in_new_items
                    
                    if key not in existing_keys_set and (i is None):
                        # Add to global database map if it was never present before this load/update cycle
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

                else:
                    # New item found - update its value or append a placeholder/empty entry for later testing logic
                    for i in self.data.values():
                        if key not in existing_keys_set and (i is None):
                            new_i = {current_key_in_new_items: v.get("value", 0) for k, v in i.items()}

                        item["key"] = current_key_in_new_items
                    
                    # Add to global database map if it was never present before this load/update cycle
                    if key not in existing_keys_set and (i is None):
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

            self.data.clear()
            
        except FileNotFoundError as e:
            print(f"File not found or read error: {e}")
src/alchemy_database.py
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Global state for testing
    
    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test.json"

        try:
            with open(path_data_path, 'r') as f:
                data_list = json.load(f)

            seen_keys = set()
            new_items = []
            existing_keys_set = {i["key"] for i in self.data.values()}  # Pre-filter to avoid re-lookup
            
            for item in data_list:
                key = item.get("key") if isinstance(item, dict) else None
                
                if not isinstance(key, str):
                    continue
                    
                current_key_in_new_items = key

                existing_keys_set.add(current_key_in_new_items)  # Add to global set before processing

                for i in self.data.values():
                    new_i = {k: v.get("value", 0) for k, v in i.items()}

                    item["key"] = current_key_in_new_items
                    
                    if key not in existing_keys_set and (i is None):
                        # Add to global database map if it was never present before this load/update cycle
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

                else:
                    # New item found - update its value or append a placeholder/empty entry for later testing logic
                    for i in self.data.values():
                        if key not in existing_keys_set and (i is None):
                            new_i = {current_key_in_new_items: v.get("value", 0) for k, v in i.items()}

                        item["key"] = current_key_in_new_items
                    
                    # Add to global database map if it was never present before this load/update cycle
                    if key not in existing_keys_set and (i is None):
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

            self.data.clear()
            
        except FileNotFoundError as e:
            print(f"File not found or read error: {e}")
src/alchemy_database.py
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Global state for testing
    
    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test.json"

        try:
            with open(path_data_path, 'r') as f:
                data_list = json.load(f)

            seen_keys = set()
            new_items = []
            existing_keys_set = {i["key"] for i in self.data.values()}  # Pre-filter to avoid re-lookup
            
            for item in data_list:
                key = item.get("key") if isinstance(item, dict) else None
                
                if not isinstance(key, str):
                    continue
                    
                current_key_in_new_items = key

                existing_keys_set.add(current_key_in_new_items)  # Add to global set before processing

                for i in self.data.values():
                    new_i = {k: v.get("value", 0) for k, v in i.items()}

                    item["key"] = current_key_in_new_items
                    
                    if key not in existing_keys_set and (i is None):
                        # Add to global database map if it was never present before this load/update cycle
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

                else:
                    # New item found - update its value or append a placeholder/empty entry for later testing logic
                    for i in self.data.values():
                        if key not in existing_keys_set and (i is None):
                            new_i = {current_key_in_new_items: v.get("value", 0) for k, v in i.items()}

                        item["key"] = current_key_in_new_items
                    
                    # Add to global database map if it was never present before this load/update cycle
                    if key not in existing_keys_set and (i is None):
                        new_item_map[i] = {current_key_in_new_items: v.get("value", 0)}

            self.data.clear()
            
        except FileNotFoundError as e:
            print(f"File not found or read error: {e}")
