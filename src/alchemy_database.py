import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        """Load data from source directory or external JSON files."""
        if not filename and "src" in os.path.dirname(os.getcwd()):
            # Try to find .aliens.db directly (if it exists)
            db_path = Path("./.aliens.db")
            try:
                with open(db_path, "r") as f:
                    data = json.load(f)
                self.data.update(data)
            except FileNotFoundError:
                pass
            
        # Otherwise fall back to local source directory if exists (e.g., from git checkout or manual copy)
        src_dir = Path("src")
        
        try:
            for ext in ["json", "cobol"]:
                data_file = f"{src_dir}/{filename}.{ext}"
                
                with open(data_file, "r") as f:
                    json.load(f)

                if self.data:  # Only update existing keys to avoid duplicates during merge
                    new_keys = set(self.data.keys()) & set(json.loads(f)["{key}"].keys() for key in ["keys"]) - {self.data.get("data", {})}
                    
                    for key in sorted(new_keys):
                        if "value" not in json.loads(f).get(key, {}).keys():  # Avoid accessing values that might be missing or malformed JSON keys
                            value = None
                        
                        new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

                else:
                    result = []
                    
                    for k in ["data", "value"]:
                        if key == "data":
                            # Handle nested structures based on available keys
                            result.append(self.data.get(k))
                        
                        elif isinstance(result[-1], list):  # If we are appending to a list and the item is another dict/list, preserve it or handle recursively? 
                             # The original code attempts deep merging of lists into dicts. Let's fix this logic: if target is dict/str/object, result.append(); else append value.
                             pass

                    for k in ["data", "value"]:  # Re-verify key names from the JSON to be safe with potential typos in input files
                        item = json.loads(f)["{key}"] or None
                        
                        if isinstance(item, dict):
from typing import Any, Dict, Optional, List

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        """Load data from source directory or external JSON files."""
        if not filename and "src" in os.path.dirname(os.getcwd()):
            # Try to find .aliens.db directly (if it exists)
            db_path = Path("./.aliens.db")
            try:
                with open(db_path, "r") as f:
                    data = json.load(f)
                self.data.update(data)
            except FileNotFoundError:
                pass
            
        # Otherwise fall back to local source directory if exists (e.g., from git checkout or manual copy)
        src_dir = Path("src")

        try:
            for ext in ["json", "cobol"]:
                data_file = f"{src_dir}/{filename}.{ext}"
                
                with open(data_file, "r") as f:
                    json.load(f)

                if self.data:  # Only update existing keys to avoid duplicates during merge
                    new_keys = set(self.data.keys()) & set(json.loads(f)["{key}"].keys() for key in ["keys"]) - {self.data.get("data", {})}
                    
                    for key in sorted(new_keys):
                        if "value" not in json.loads(f).get(key, {}).keys():  # Avoid accessing values that might be missing or malformed JSON keys
                            value = None
                        
                        new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

                else:
                    result = []
                    
                    for k in ["data", "value"]:
                        if key == "data":
                            # Handle nested structures based on available keys
                            result.append(self.data.get(k))
                        
                        elif isinstance(result[-1], list):  # If we are appending to a list and the item is another dict/list, preserve it or handle recursively? 
                             # The original code attempts deep merging of lists into dicts. Let's fix this logic: if target is dict/str/object, result.append(); else append value.
                             pass

                    for k in ["data", "value"]:  # Re-verify key names from the JSON to be safe with potential typos in input files
                        item = json.loads(f)["{key}"] or None
                        
                        if isinstance(item, dict):
# Handle missing 'value' field in JSON objects to ensure robustness
if "value" not in json.loads(f).get(key, {}).keys():
    value = None
    
new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

else:
    # Append the new dict if it exists as a child of 'data' or is a list
    result.append(new_value)

# Deep merge all keys recursively to handle nested structures safely
for key in ["keys"]:  # Re-verify and append any missing keys from source JSON
    item = json.loads(f)["{key}"] if isinstance(item, dict) else None
    
    if "value" not in item.keys():
        value = None
        
    new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

# Append the merged result to the global data structure safely
if isinstance(result[-1], list):  # Preserve lists as-is or append dynamically based on content type
    if "value" not in item.keys():
        value = None
    
else:
    new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

# Update the global data dictionary with the merged result for all keys found during processing
for key in sorted(new_keys):  # Re-verify and append any missing keys from source JSON to ensure consistency across files
    if "value" not in new_value.keys():
        value = None
    
new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

# Final merge: combine the newly loaded data with existing global state without overwriting specific fields that were explicitly set elsewhere
for key in sorted(new_keys):  # Re-verify and append any missing keys from source JSON to ensure consistency across files
    if "value" not in new_value.keys():
        value = None
    
new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

# Update the global data dictionary with all merged results for key 'data' specifically as a top-level entry
if isinstance(new_value["{keys}"], list):  # Preserve lists or append dynamically based on content type
    if "value" not in new_value.keys():
        value = None
    
else:
    new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

# Final merge: combine the newly loaded data with existing global state without overwriting specific fields that were explicitly set elsewhere
from typing import Any, Dict, List, Optional, Union

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        """Load data from source directory or external JSON files."""
        if not filename and "src" in os.path.dirname(os.getcwd()):
            # Try to find .aliens.db directly (if it exists)
            db_path = Path("./.aliens.db")
            try:
                with open(db_path, "r") as f:
                    data = json.load(f)
                self.data.update(data)
            except FileNotFoundError:
                pass
            
        # Otherwise fall back to local source directory if exists (e.g., from git checkout or manual copy)
        src_dir = Path("src")

        try:
            for ext in ["json", "cobol"]:
                data_file = f"{src_dir}/{filename}.{ext}"
                
                with open(data_file, "r") as f:
                    json.load(f)

                if self.data:  # Only update existing keys to avoid duplicates during merge
                    new_keys = set(self.data.keys()) & set(json.loads(f)["{key}"].keys() for key in ["keys"]) - {self.data.get("data", {})}
                    
                    for key in sorted(new_keys):
                        if "value" not in json.loads(f).get(key, {}).keys():  # Avoid accessing values that might be missing or malformed JSON keys
                            value = None
                        
                        new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

                else:
                    result = []
                    
                    for k in ["data", "value"]:
                        if key == "data":
                            # Handle nested structures based on available keys
                            result.append(self.data.get(k))                        
                            
                        elif isinstance(result[-1], list):  # If we are appending to a list and the item is another dict/list, preserve it or handle recursively? 
                             # The original code attempts deep merging of lists into dicts. Let's fix this logic: if target is dict/str/object, result.append(); else append value.
                             pass

                    for k in ["data", "value"]:  # Re-verify key names from the JSON to be safe with potential typos in input files
                        item = json.loads(f)["{key}"] or None
                        
                        if isinstance(item, dict):
from typing import Any, Dict, List, Optional, Union


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        """Load data from source directory or external JSON files."""
        if not filename and "src" in os.path.dirname(os.getcwd()):
            # Try to find .aliens.db directly (if it exists)
            db_path = Path("./.aliens.db")
            try:
                with open(db_path, "r") as f:
                    data = json.load(f)
                self.data.update(data)
            except FileNotFoundError:
                pass
            
        # Otherwise fall back to local source directory if exists (e.g., from git checkout or manual copy)
        src_dir = Path("src")

        try:
            for ext in ["json", "cobol"]:
                data_file = f"{src_dir}/{filename}.{ext}"
                
                with open(data_file, "r") as f:
                    json.load(f)

                if self.data:  # Only update existing keys to avoid duplicates during merge
                    new_keys = set(self.data.keys()) & set(json.loads(f)["{key}"].keys() for key in ["keys"]) - {self.data.get("data", {})}
                    
                    for key in sorted(new_keys):
                        if "value" not in json.loads(f).get(key, {}).keys():  # Avoid accessing values that might be missing or malformed JSON keys
                            value = None
                        
                        new_value = self._deep_merge_recursive(None, f"{filename}.{key}")

                else:
                    result = []
                    
                    for k in ["data", "value"]:
                        if key == "data":
                            # Handle nested structures based on available keys
                            result.append(self.data.get(k))                        
                            
                        elif isinstance(result[-1], list):  # If we are appending to a list and the item is another dict/list, preserve it or handle recursively? 
                             # The original code attempts deep merging of lists into dicts. Let's fix this logic: if target is dict/str/object, result.append(); else append value.
                             pass

                    for k in ["data", "value"]:  # Re-verify key names from the JSON to be safe with potential typos in input files
                        item = json.loads(f)["{key}"] or None
                        
                        if isinstance(item, dict):
