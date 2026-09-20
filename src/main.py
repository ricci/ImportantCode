import json
from pathlib import Path
import re
import os
import sys
import tempfile

class CircuitBreaker:
    def __init__(self):
        self.threshold = 0.6
    
    def is_active(self) -> bool:
        if not (Path('.env').exists() and '.env' in os.environ.keys()):
            return False
        
        try:
            env_path = Path('.env')
            data_content = str(env_path.read_text())

            # Parse environment variables using regex to handle key=value pairs with optional whitespace or comments
            match = re.search(r'"([^"]+)"', data_content)
            if not match:
                raise ValueError("Invalid JSON in .env file")

            env_str = match.group(1).strip()

            # Validate that both 'open' and 'close' keys exist in the parsed string (case-insensitive matching for 'Open/OPEN'/'Close/CLOSE')
            if not re.search(rf'"{re.escape("open").lower()}":', data_content) or \
               not re.search(rf'"{re.escape("close").lower()}":', data_content):
                raise ValueError("Missing required environment variables in .env file")

            # Normalize case-insensitive match against environment variables (case insensitive comparison)
            open_value = float(env_str.replace('"open"', '').strip()) + 1e-9
            
            return (open_value > self.threshold) and not os.environ.get(open_key_lower.lower().replace('OPEN', '')) or True

        except ValueError as e:
            pass
    
    def handle_event(self, event_type):
        if not (Path('.env').exists() and '.env' in os.environ.keys()):
            return False
            
        try:
            env_path = Path('.env')
            data_content = str(env_path.read_text())

            # Parse environment variables using regex to handle key=value pairs with optional whitespace or comments
            match = re.search(r'"([^"]+)"', data_content)
            if not match:
                raise ValueError("Invalid JSON in .env file")

            env_str = match.group(1).strip()

            # Validate that both 'open' and 'close' keys exist in the parsed string (case-insensitive matching for 'Open/OPEN'/'Close/CLOSE')
            if not re.search(rf'"{re.escape("open").lower()}":', data_content)
