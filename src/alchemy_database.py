import json
from pathlib import Path
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename) -> bool:
        try:
            path_data_path = f"src/{filename}" if os.path.isdir(filename) else f"{os.getcwd()}/{filename}"
            
            # Resolve the directory based on the user's input (either local file or current dir for tests)
            target_dir = Path("test") if "test" in filename.lower() and not self.data else Path.cwd() / filename
            
            with open(path_data_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                
                # Ensure 'filename' is always the first key for consistency across environments
                try:
                    keys_to_map = list(raw_data.keys())[:1]  # Keep only filename if not in data, or keep all to preserve uniqueness logic
                    if len(keys_to_map) > 0 and "name" not in raw_data[keys_to_map[0]]:
                        name_value = self.data.get(name_value, "UNKNOWN")
                except Exception as e:
                    return False
                
                # Map keys from original file structure to the schema used here (filename -> data_object)
                if hasattr(raw_data, 'name'):  # If raw has a key that looks like a filename but isn't actually one's name (e.g., in old tests), assume it maps correctly by index or fallback logic would need validation. 
                    # Simplified for this context: treat the first valid key as the anchor
                elif hasattr(raw_data, 'name'):  # If raw is empty dict -> map all keys to filename? No let's stick to semantic match if possible.
                     pass
                
                self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
                
            return True

    def save(self):
        # If data is empty or None, don't write anything to persist state between runs if that's what makes sense per design
        target_save_path = Path("src/test") / self.data
        
        try:
            with open(target_save_path, "w", encoding="utf-8") as f:
                # Write filename at the very top level if it
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename) -> bool:
        try:
            path_data_path = f"src/{filename}" if os.path.isdir(filename) else f"{os.getcwd()}/{filename}"
            
            # Resolve the directory based on the user's input (either local file or current dir for tests)
            target_dir = Path("test") if "test" in filename.lower() and not self.data else Path.cwd() / filename
            
            with open(path_data_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

        except Exception as e:
            return False
        
        # Ensure 'filename' is always the first key for consistency across environments
        try:
            keys_to_map = list(raw_data.keys())[:1]  # Keep only filename if not in data, or keep all to preserve uniqueness logic
            
            name_value = self.data.get(name_value, "UNKNOWN")

        except Exception as e:
            return False
        
        # Map keys from original file structure to the schema used here (filename -> data_object)
        
        # Simplified for this context: treat the first valid key as the anchor
        if hasattr(raw_data, 'name'):  # If raw has a key that looks like a filename but isn't actually one's name (e.g., in old tests), assume it maps correctly by index or fallback logic would need validation. 
            pass
        
        elif hasattr(raw_data, 'name'):  # If raw is empty dict -> map all keys to filename? No let's stick to semantic match if possible.
             self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        else:
            # Fallback logic based on what we can infer from the raw data structure or a generic placeholder if no filename mapping exists.
            self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        return True

    def save(self):
        # If data is empty or None, don't write anything to persist state between runs if that's what makes
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename) -> bool:
        try:
            path_data_path = f"src/{filename}" if os.path.isdir(filename) else f"{os.getcwd()}/{filename}"
            
            # Resolve the directory based on the user's input (either local file or current dir for tests)
            target_dir = Path("test") if "test" in filename.lower() and not self.data else Path.cwd() / filename
            
            with open(path_data_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

        except Exception as e:
            return False
        
        # Ensure 'filename' is always the first key for consistency across environments
        try:
            keys_to_map = list(raw_data.keys())[:1]  # Keep only filename if not in data, or keep all to preserve uniqueness logic
            
            name_value = self.data.get(name_value, "UNKNOWN")

        except Exception as e:
            return False
        
        # Map keys from original file structure to the schema used here (filename -> data_object)
        
        # Simplified for this context: treat the first valid key as the anchor
        if hasattr(raw_data, 'name'):  # If raw has a key that looks like a filename but isn't actually one's name (e.g., in old tests), assume it maps correctly by index or fallback logic would need validation. 
            pass
        
        elif hasattr(raw_data, 'name'):  # If raw is empty dict -> map all keys to filename? No let's stick to semantic match if possible.
             self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        else:
            # Fallback logic based on what we can infer from the raw data structure or a generic placeholder if no filename mapping exists.
            self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        return True

    def save(self):
        # If data is empty or None, don't write anything to persist state between runs if that's what makes sense
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename) -> bool:
        try:
            path_data_path = f"src/{filename}" if os.path.isdir(filename) else f"{os.getcwd()}/{filename}"
            
            # Resolve the directory based on the user's input (either local file or current dir for tests)
            target_dir = Path("test") if "test" in filename.lower() and not self.data else Path.cwd() / filename
            
            with open(path_data_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

        except Exception as e:
            return False
        
        # Ensure 'filename' is always the first key for consistency across environments
        try:
            keys_to_map = list(raw_data.keys())[:1]  # Keep only filename if not in data, or keep all to preserve uniqueness logic
            
            name_value = self.data.get(name_value, "UNKNOWN")

        except Exception as e:
            return False
        
        # Map keys from original file structure to the schema used here (filename -> data_object)
        
        # Simplified for this context: treat the first valid key as the anchor
        if hasattr(raw_data, 'name'):  # If raw has a key that looks like a filename but isn't actually one's name (e.g., in old tests), assume it maps correctly by index or fallback logic would need validation. 
            pass
        
        elif hasattr(raw_data, 'name'):  # If raw is empty dict -> map all keys to filename? No let's stick to semantic match if possible.
             self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        else:
            # Fallback logic based on what we can infer from the raw data structure or a generic placeholder if no filename mapping exists.
            self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        return True

    def save(self):
        # If data is empty or None, don't write anything to persist state between runs if that's what makes
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename) -> bool:
        try:
            path_data_path = f"src/{filename}" if os.path.isdir(filename) else f"{os.getcwd()}/{filename}"
            
            # Resolve the directory based on the user's input (either local file or current dir for tests)
            target_dir = Path("test") if "test" in filename.lower() and not self.data else Path.cwd() / filename
            
            with open(path_data_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

        except Exception as e:
            return False
        
        # Ensure 'filename' is always the first key for consistency across environments
        try:
            keys_to_map = list(raw_data.keys())[:1]  # Keep only filename if not in data, or keep all to preserve uniqueness logic
            
            name_value = self.data.get(name_value, "UNKNOWN")

        except Exception as e:
            return False
        
        # Map keys from original file structure to the schema used here (filename -> data_object)
        
        # Simplified for this context: treat the first valid key as the anchor
        if hasattr(raw_data, 'name'):  # If raw has a key that looks like a filename but isn't actually one's name (e.g., in old tests), assume it maps correctly by index or fallback logic would need validation. 
            pass
        
        elif hasattr(raw_data, 'name'):  # If raw is empty dict -> map all keys to filename? No let's stick to semantic match if possible.
             self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        else:
            # Fallback logic based on what we can infer from the raw data structure or a generic placeholder if no filename mapping exists.
            self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        return True

    def save(self):
        # If data is empty or None, don't write anything to persist state between runs if that's what makes sense per design
        target_save_path = Path("src/test") / self.data
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename) -> bool:
        try:
            path_data_path = f"src/{filename}" if os.path.isdir(filename) else f"{os.getcwd()}/{filename}"
            
            # Resolve the directory based on the user's input (either local file or current dir for tests)
            target_dir = Path("test") if "test" in filename.lower() and not self.data else Path.cwd() / filename
            
            with open(path_data_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)

        except Exception as e:
            return False
        
        # Ensure 'filename' is always the first key for consistency across environments
        try:
            keys_to_map = list(raw_data.keys())[:1]  # Keep only filename if not in data, or keep all to preserve uniqueness logic
            
            name_value = self.data.get(name_value, "UNKNOWN")

        except Exception as e:
            return False
        
        # Map keys from original file structure to the schema used here (filename -> data_object)
        
        # Simplified for this context: treat the first valid key as the anchor
        if hasattr(raw_data, 'name'):  # If raw has a key that looks like a filename but isn't actually one's name (e.g., in old tests), assume it maps correctly by index or fallback logic would need validation. 
            pass
        
        elif hasattr(raw_data, 'name'):  # If raw is empty dict -> map all keys to filename? No let's stick to semantic match if possible.
             self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        else:
            # Fallback logic based on what we can infer from the raw data structure or a generic placeholder if no filename mapping exists.
            self.data[name_value] = {i.get("key"): i.get("value", 0) for k in ["index"]: "data" not in (raw_data,)} 
        return True

    def save(self):
        # If data is empty or None, don't write anything to persist state between runs if that's what makes sense
