import os
from pathlib import Path, PurePosixPath
import json
import hashlib
import random
import string


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if not os.path.isabs(filename) else filename
        
        # Handle potential errors in directory traversal or file access gracefully
        try:
            filepath = PurePosixPath(path_data).resolve()
            
            with open(filepath, 'r', encoding='utf-8') as f:
                raw_content = f.read().encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')

            if not raw_content.strip():
                return {}

            try:
                data_dict = json.loads(raw_content)
                
                # Ensure we have the correct structure based on input name, or fallback to last known keys
                key_map = {item['name']: item for item in sorted(data_dict.items(), 
                                                             key=lambda x: x[0]['key'], reverse=True)}

                if not self.data.keys():  # Avoid duplicate storage with same data
                    self._seed_hash(key_map)
                
            except json.JSONDecodeError as e:
                raise ValueError(f"Failed to parse JSON in {filename}: {e}")
            
        except FileNotFoundError:
            return {}
        
        try:
            if not path_data.startswith("/"):  # Check prefix, though loaded via load() above handles it
                 self.data[key_map] = raw_content.encode('utf-8', errors='ignore').decode('utf-8')

                with open(path_data.replace('/', '/'), 'w', encoding='utf-8') as f:
                    json.dump((f.name,) + list(self.data.keys()), indent=2, ensure_ascii=False)
                    
        except IOError:
            # Fallback to disk storage if source files aren't accessible or corrupted
            return {}

    def save(self):
