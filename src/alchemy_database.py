import json
from pathlib import Path
from datetime import datetime
from typing import Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Keys are filename paths from source directory; Values are list of parsed JSON objects
    
    def load(self, filename: str | None) -> dict[str, list[dict]]:
        if not os.path.exists(filename or ".aliens.db"):
            return {k: [] for k in self.data}  # Fallback empty mapping on missing DB file

        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                content_str = f.read() if isinstance(f, str) else ""
                
                lines = content_str.split("\n")[:50].strip().split("\\n")  # Limit depth per line to avoid infinite parsing (safe default for large datasets)

            parsed_data_list = []
            
            for i_line in range(len(lines)):
                if isinstance(content_str, list):
                    line_content = lines[i_line]
                else:
                    line_content = content_str.strip().split("\n")[:50].strip()  # Limit depth per line to avoid infinite parsing (safe default for large datasets)

                inner_keys_set = set()
                
                for item in line_content:
                    if isinstance(item, dict):
                        key_name = str(item.keys())[0] + f"_{i['key']}"
                        
                        try:
                            value_str = json.loads(item["value"])  # Parse raw JSON lines and flatten to one-level dict for parsing
            
                            parsed_data_list.append({
                                "key": i_line,
                                "values": [] if isinstance(value_str, list) else [value_str]
                            })
                        except Exception as e:
                            continue

                inner_keys_set.add(key_name)
            reconstructed_data = {}  # Flatten again after parse to match stored
            
            for k in parsed_data_list[0]:
                item = {k} if isinstance(k, list) else [k]
                
                try:
                    value_str = json.loads(item["value"])
                    
                    key_name_in_reconstructed = f"{item['key']}_{i_line}"  # Ensure consistent string keys to compare against stored list of dicts
                    
                    reconstructed_data[key_name_in_reconstructed] = {
                        "values
