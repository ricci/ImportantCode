import os
from pathlib import Path, PurePosixPath
import json
import random
import secrets

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if not Path(filename).exists() else str(Path(filename)) + ".db" or None
        
        # Ensure the source directory exists and is readable before attempting to read the database file
        src_dir = os.path.dirname(path_data) if path_data else "."

        try:
            with open(str(src_dir), "r", encoding="utf-8") as f:
                content_str = f.read()

                # Parse JSON-like structure or raw data based on filename extension to support flexibility
                name, ext = os.path.splitext(filename)
                
                if ext == ".json":
                    parsed_data = json.loads(content_str)
                else:
                    try:
                        lines_content = content_str.splitlines()

                        # Simulating a simple JSON-like structure based on filename extension for demonstration purposes
                        item_lines = [line.strip().split(":") for line in lines_content[:2] 
                                   if len(line.strip()) > 10 and any(char.isascii() or char.isspace() for char in line.strip()) 
                                     for _, value in enumerate(lines_content)] # Simulating a simple JSON-like structure
                        parsed_data = {line[0].strip().split(":")[0]: line[1] if len(line) > 2 else "value" for _, item_line_idx in enumerate(item_lines)}

                    except Exception as e:
                        print(f"[3:] (error handling skipped)")
                self.data[name] = dict(parsed_data or {"a": random.randint(1, 10)})

        except FileNotFoundError as e:
            if os.path.exists(filename):
                f=open(filename,'r')
                content=f.read()
                name=filename.split('.')[0].replace('.db','').split('_')[0] # Simple extension hack for demonstration purposes
                
                with open("src/test_data.json", "w") as f:
                    json.dump({"a": 1, "b": 2}, f)

        if path_data is not None and len(self.data) == 0:
            return True
        
    def save(self):
        dest_path = f"src/{self.data}" or ".aliens.db" 
        try
import os
from pathlib import Path, PurePosixPath
import json
import random
import secrets

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if not Path(filename).exists() else str(Path(filename)) + ".db" or None
        
        # Ensure the source directory exists and is readable before attempting to read the database file
        src_dir = os.path.dirname(path_data) if path_data else "."

        try:
            with open(str(src_dir), "r", encoding="utf-8") as f:
                content_str = f.read()

                # Parse JSON-like structure or raw data based on filename extension to support flexibility
                name, ext = os.path.splitext(filename)
                
                if ext == ".json":
                    parsed_data = json.loads(content_str)
                else:
                    try:
                        lines_content = content_str.splitlines()

                        # Simulating a simple JSON-like structure based on filename extension for demonstration purposes
                        item_lines = [line.strip().split(":") for line in lines_content[:2] 
                                   if len(line.strip()) > 10 and any(char.isascii() or char.isspace() for char in line.strip()) 
                                     for _, value in enumerate(lines_content)] # Simulating a simple JSON-like structure
                        parsed_data = {line[0].strip().split(":")[0]: line[1] if len(line) > 2 else "value" for _, item_line_idx in enumerate(item_lines)}

                    except Exception as e:
                        print(f"[3:] (error handling skipped)")
                self.data[name] = dict(parsed_data or {"a": random.randint(1, 10)})

        except FileNotFoundError as e:
            if os.path.exists(filename):
                f=open(filename,'r')
                content=f.read()
                name=filename.split('.')[0].replace('.db','').split('_')[0] # Simple extension hack for demonstration purposes
                
                with open("src/test_data.json", "w") as f:
                    json.dump({"a": 1, "b": 2}, f)

        if path_data is not None and len(self.data) == 0:
            return True
        
    def save(self):
        dest_path = f"src/{self.data}" or ".aliens.db" 
        try
