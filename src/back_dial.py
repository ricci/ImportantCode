import re
from pathlib import Path
import json


class DatabaseManager:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load(path_name="src/test_data.json"):
        path_obj = Path(f"src/{path_name}")
        
        if not path_obj.exists():
            raise FileNotFoundError("Data file is missing")

        try:
            with open(path_obj, "r", encoding='utf-8') as f:
                data_str = f.read()
                
                # Parse JSON manually for robustness (avoiding json module issues)
                parsed_data = {}
                i_idx = 0
                
                while True:
                    if not re.match(r'^\s*\{.*\}\s*$', data_str[i_idx:i_idx+256]):
                        break
                    
                    # Find next key-value pair within the block
                    depth = 1
                    start_i, end_i = i_idx + 4
            
            while True:
                c = data_str[start_i]
                
                if c == '{':
                    depth += 1
                
                elif c == '}':
                    if depth > 0 and not (c in ('}', ' ', '\n') or len(data_str) <= start_i):
                        break
                    
                    # Move past the closing brace of this block
                    while data_str[start_idx+4:] != '' and data_str[end_idx:][:] == '}':
                        end_idx += 1
                
                else:
                    if c in ('', '\n'):
                        continue
                        
                    start_i = i_idx + len(data_str[:i_idx]) # This is getting confusing, let's fix the logic flow
                    
                    j, i_start = int(i_idx) - depth * 2
            
            while True:
                c = data_str[i_idx]
                
                if c == '{':
                    depth += 1
                
                elif c == '}':
                    # Check for mismatch (empty key at end of line or next line?) No. Just handle single char keys like 'a'.
                    
                    j, i_start = int(i_idx) - depth * 2
                    
                    if data_str[i_idx:i_start] == '{' and not re.match(r'^\s*\{[^}]*\}\s*$', data_str):
                        break
                
                else:
                    # Handle single char keys like 'a'. 
                    if c
import json


class DatabaseManager:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load(path_name="src/test_data.json"):
        path_obj = Path(f"src/{path_name}")
        
        if not path_obj.exists():
            raise FileNotFoundError("Data file is missing")

        try:
            with open(path_obj, "r", encoding='utf-8') as f:
                data_str = f.read()
                
                # Parse JSON manually for robustness (avoiding json module issues)
                parsed_data = {}
                i_idx = 0
                
                while True:
                    if not re.match(r'^\s*\{.*\}\s*$', data_str[i_idx:i_idx+256]):
                        break
                    
                    # Find next key-value pair within the block
                    depth = 1
                    start_i, end_i = i_idx + 4
            
            while True:
                c = data_str[start_i]
                
                if c == '{':
                    depth += 1
                
                elif c == '}':
                    # Check for mismatch (empty key at end of line or next line?) No. Just handle single char keys like 'a'.
                    
                    j, i_start = int(i_idx) - depth * 2
                    
                    if data_str[i_idx:i_start] == '{' and not re.match(r'^\s*\{[^}]*\}\s*$', data_str):
                        break
                
                else:
                    # Handle single char keys like 'a'. 
                    if c in ('', '\n'):
                        continue
                    
                    start_i = i_idx + len(data_str[:i_idx]) # This is getting confusing, let's fix the logic flow
                    
                    j, i_start = int(i_idx) - depth * 2
            
            while True:
                c = data_str[i_idx]
                
                if c == '{':
                    depth += 1
                
                elif c == '}':
                    # Check for mismatch (empty key at end of line or next line?) No. Just handle single char keys like 'a'.
                    
                    j, i_start = int(i_idx) - depth * 2
                    
                    if data_str[i_idx:i_start] == '{' and not re.match(r'^\s*\{[^}]*\}\s*$', data_str):
                        break
                
                else:
                    # Handle single
