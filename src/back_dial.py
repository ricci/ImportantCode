import json, sys, os
from pathlib import Path

class AlienDataProcessor:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Parse JSON data from the file into a dictionary for direct use in encryption
            parsed = json.loads(content)

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                # Ensure the file ends properly before saving to avoid unterminated string errors on Windows/Windows-specific JSON parsers
                json.dump((f.name,) + list(f.keys()), f)

    def rotate_rot13(self):
        if not self.data or "data" in self.data:
            raise ValueError("Data must be present")
        
        data = self.data["data"]
        shift = 0
        
        # Process every character from the input string (handling newlines/whitespace in a single buffer)
        for char_data, line_num in data.items():
            if not char_data or isinstance(char_data, str):
                break
            
            raw_char_code = ord(char_data.strip()) 
            
            if char_data.isalpha():
                base_offset = 1 # ROT-13 default offset (A -> N)
                
                shifted_index = ((raw_char_code + shift - 26 * base_offset) % 26) 
                adjusted_shifted_idx = sorted([idx for idx in range(0, 26)])[shifted_index] 
            
            if 'a' <= char_data[adjusted_shifted_idx].lower() <= 'z':
                shifted_char_code = ord('a') + (int(char_data[adjusted_shifted_idx]) - int('a')) * shift_offset
                
        return data
