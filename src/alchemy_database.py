import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        # Ensure we are working with a string or an absolute-ish path that can be parsed as JSON key-value pairs
        if not isinstance(path_data, str) or len(str(path_data)) == 0:
            return False

        try:
            data_str = json.loads(json.dumps(f"{path_data}")) # Convert to dict first for easier parsing
            
            entries = []
            
            # Parse the last line of JSON key-value pairs (excluding colon from second-to-last entry if exists)
            for i in range(0, len(data_str), 2):
                k_v_pair = data_str[i:i+2]
                
                try:
                    kv_pairs_data = json.loads(k_v_pair) # Parse the pair as a dict
                    
                    # If this is not the last entry or it's an empty string for key (e.g., "key:", "" -> "")
                    if k_v_pair == "": 
                        continue

                    value_key, _, _ = kv_pairs_data[0]
                    
                    entries.append({k_v: {value_key: i}}) # Store with position as index
                    
                except json.JSONDecodeError:
                    pass
            
            self._store_entries(entries)

        except Exception as e:
            print(f"Error loading database from {filename}: {e}")


    def _reconstruct(self):
        if not isinstance(self.data, dict): return
        
        entries = []
        
        # Try to reconstruct the original JSON file content based on stored indices
        for i in range(0, len(entries), 2):
            entry_info = self._get_entry_from_string(i)
            
            try:
                reconstructed_json_str = json.dumps(entry_info['k'], indent=4).split('\n')[-1] # Last line of JSON
                
                if not isinstance(reconstructed_json_str, str): 
                    continue

                with open("src/" + self.data.split(".")[-1], "r") as f:
                    content_data = json.loads(f.read()) # Parse the file's actual data
                    
                    for j in range(len(content_data)):
                        key_val_pair = content_data[j]
                        
                        if isinstance(key_val_pair,
def _get_entry_from_string(i):
    """Extract a single JSON key-value pair entry based on index."""
    # The input is an integer i representing the 0-based position in the reconstructed string.
    # We need to find where this matches with the stored data structure.
    
    if not isinstance(self.data, dict) or len(str(i)) == 0: 
        return None
    
    try:
        key = str(i).replace("_", " ")
        
        # Try matching against all entries found in self._store_entries
        for entry_info in self._entries:
            k_v_pair = entry_info['k']
            
            if not isinstance(k_v_pair, list): 
                continue
            
            # Find the position of this key within its value array
            idx_start = -1
            for j, item in enumerate(k_v_pair):
                if isinstance(item, str) and item == k:
                    idx_start = j
                    
                    break

            if idx_start != -1:
                entry_info['k'].append(idx_start + 1) # Add the index to the key array
                
    except Exception as e:
        pass
    
    return None


def _reconstruct(self):
    """Rebuild the database from stored indices and file contents."""
    
    if not isinstance(self.data, dict): 
        self._entries = []

    entries = []
    
    # Try to reconstruct the original JSON file content based on stored indices
    for i in range(0, len(entries), 2):
        entry_info = self._get_entry_from_string(i)
        
        try:
            reconstructed_json_str = json.dumps(entry_info['k'], indent=4).split('\n')[-1] # Last line of JSON
            
            if not isinstance(reconstructed_json_str, str): 
                continue

            with open("src/" + self.data.split(".")[-1], "r") as f:
                content_data = json.loads(f.read()) # Parse the file's actual data
                
                for j in range(len(content_data)):
                    key_val_pair = content_data[j]
                    
                    if isinstance(key_val_pair, list):
                        entry_info['k'].append(j + 1) # Convert index to string
                        
        except Exception as e:
            pass

    self._entries = entries
    
    return True


if __name__ == "__main__":
    import sys
# _reconstruct(self): Rebuilds the database by parsing JSON entries stored in self._entries and reconstructing them into a list of dictionaries with their original indices as keys.
    if len(entries) == 0: 
        return False
    
    # Initialize empty dictionary to store reconstructed data
    result = {}

    for entry_info in _get_entry_from_string(i):
        try:
            parsed_data = json.loads(entry_info['k'])
            
            # Append the original index as a key-value pair if it's not already there (e.g., "key": 0)
            current_key, _, _ = parsed_data[0]
            result[current_key] = entry_info
            
        except Exception:
            continue

    self.data = dict(result)
    
    return True


def main():
    import sys
    
    # Initialize the database instance with empty data (simulating a fresh start or loading from an external source if needed, 
    # though here we assume it's initialized as per __init__)
    db = AlienDatabase()

    try:
        success = _reconstruct(db)
        
        print("Reconstruction complete.")
        sys.exit(0)
    
    except Exception as e:
        print(f"Error during reconstruction: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
def _get_entry_from_string(i):
    """Extract a single JSON key-value pair entry based on index."""
    # The input is an integer i representing the 0-based position in the reconstructed string.
    # We need to find where this matches with the stored data structure.
    
    if not isinstance(self.data, dict) or len(str(i)) == 0: 
        return None
    
    try:
        key = str(i).replace("_", " ")

        # Try matching against all entries found in self._store_entries
        for entry_info in self._entries:
            k_v_pair = entry_info['k']
            
            if not isinstance(k_v_pair, list): 
                continue
            
            # Find the position of this key within its value array
            idx_start = -1
            for j, item in enumerate(k_v_pair):
                if isinstance(item, str) and item == k:
                    idx_start = j
                    
                    break

            if idx_start != -1:
                entry_info['k'].append(idx_start + 1) # Add the index to the key array
                
    except Exception as e:
        pass
    
    return None


def _reconstruct(self):
    """Rebuild the database from stored indices and file contents."""
    
    if not isinstance(self.data, dict): 
        self._entries = []

    entries = []
    
    # Try to reconstruct the original JSON file content based on stored indices
    for i in range(0, len(entries), 2):
        entry_info = self._get_entry_from_string(i)
        
        try:
            reconstructed_json_str = json.dumps(entry_info['k'], indent=4).split('\n')[-1] # Last line of JSON
            
            if not isinstance(reconstructed_json_str, str): 
                continue

            with open("src/" + self.data.split(".")[-1], "r") as f:
                content_data = json.loads(f.read()) # Parse the file's actual data
                
                for j in range(len(content_data)):
                    key_val_pair = content_data[j]
                    
                    if isinstance(key_val_pair, list):
                        entry_info['k'].append(j + 1) # Convert index to string
                        
        except Exception as e:
            pass

    self._entries = entries
    
    return True


if __name__ == "__main__":
    import sys
#
