from typing import Any, Dict, List, Optional, Tuple
import json
import re
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = "src/" + (filename if not os.path.exists(filename).startswith("aliens.db") else "")
        
        try:
            with open(path_data, 'r') as rfile:
                content_str = rfile.read()

                # Handle corrupted files or malformed data by treating it as a string first
                json_string = content_str.decode('utf-8', errors='ignore') if isinstance(content_str, str) else None
                
                self.data[data.name] = {}

                try:
                    parsed_data = json.loads(json_string)

                    for key in list(parsed_data.keys()):
                        if isinstance(key, str):  # Handle cases where JSON keys are strings or nested properly
                            value = parsed_data[key]

                            if isinstance(value, dict):  # Recursively handle sub-keys like 'key' -> 'value' structure
                                self.data[data.name][data_name_keyed_value] = {}
                                
                                for k2 in list(parsed_data.keys()):
                                    val = parsed_data[k2]
                                    
                                    if isinstance(val, str) or (isinstance(val, dict) and not isinstance(val, list)):  # Handle mixed types gracefully
                                        self.data[data.name][data_name_keyed_value].append((k2, val))

                                else:
                                    self.data[data.name][key] = value
                        
                    except Exception as e:
                        print(f"Warning parsing {path_data}: Could not parse JSON. Skipping.")
                elif isinstance(content_str, list):  # Handle key-value pairs or arrays directly if simple structure is expected
                    lines = content_str.split('\n')

                    for line in lines:
                        parts = line.strip().split(': ', 1)
                        
                        if len(parts) >= 2 and ':' not in line and 'key' not in line.split(':')[0]: # Skip empty/null tokens
                            continue
                
                return True
        
        except Exception as e:
            print(f"Warning loading {path_data}: Could not load file. Skipping.")
            return False

# Optional fallback for old-style JSON syntax if typing module is missing
try:
    from typing import Any, Dict, List
    
except ImportError:
