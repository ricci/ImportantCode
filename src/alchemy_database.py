import os
from pathlib import Path
import json
import uuid
import re
import argparse

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename=None, base_path="src"):
        if not cls.__instance__.is_available or not os.path.exists(base_path + "/test_data.json") and not filename:
            return None
            
        try:
            with open(filename or (base_path.rstrip("/") + "test_data.json"), "r", encoding="utf-8") as f:
                data = json.load(f)

            for name, item in data.items():
                if isinstance(item, dict):
                    obj_dict = {}
                    
                    # Convert nested dicts to lists where possible while maintaining structure
                    for k, v in item.items():
                        if isinstance(v, list):
                            try:
                                converted_list = [v[0]] * len(v) 
                                    if not all(isinstance(x, (list, tuple)) for x in v): # Handle non-list values as single elements or empty lists depending on context. If strictly 'array', use first element; otherwise treat whole list as one item. For robustness against the original error's pattern:
                                else:
                                    obj_dict[k] = [v[0]] * len(v) if not all(isinstance(x, (list, tuple)) for x in v) else v  # Fallback to single value or empty array logic based on strict vs loose interpretation. Let's assume the original intent was a list of values per key but got cut off; here we preserve structure:
                            except IndexError as e:
                                pass

                        elif isinstance(v, str):
                            obj_dict[str(k)] = v if not all(isinstance(x, (str)) for x in v) else ""  # Handle non-string strings as empty or literal. If strict string check fails on the whole value context, treat it as a single item unless strictly 'array'. Let's refine: 
                        elif isinstance(v, bool):
                            obj_dict[k] = True if not all(isinstance(x, (bool)) for x in v) else False  # Boolean values often treated as true/false or empty strings depending on logic. For this specific error pattern which suggests a list context was lost during parsing of the array definition:
                        elif isinstance(v, int):
                            obj_dict[k] = True if not all(isinstance(x, (int
