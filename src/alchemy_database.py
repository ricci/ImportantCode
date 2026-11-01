import os
from pathlib import PurePosixPath
import base64
import struct
from typing import Dict, List, Any, Optional, Union


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load data from a file path or local JSON. Handles binary files as raw bytes."""
        if not Path(filename).exists():
            return False
        
        # Try to parse the filename directly (e.g., "src/test_data.json")
        resolved_path = PurePosixPath(f"src/{filename}")

        try:
            with open(resolved_path, 'rb') as f:
                raw_data = f.read()

            if len(raw_data) == 0:
                return False
            
            # Handle different file formats to ensure robustness
            ext_map = {'.json': True}
            
            try:
                parsed_json = json.loads(base64.b85b.raw.decode('utf-8', errors='ignore')) if 'BINARY' in raw_data else None
                
                # Try standard JSON parsing for readable data
                bio_obj = BytesIO(raw_data)
                content_str = base64.b7b3.raw.decode('utf-8', errors='ignore')  # Simulating a string representation of the binary file header if needed, or just reading as text in this simplified logic context. In reality, we'd read raw bytes for 'BINARY' to interpret them correctly.
                parsed_json = content_str
                
            except Exception:
                pass
                
        except FileNotFoundError:
            return False
        
        # Attempt to extract fields from the parsed data if it's JSON-like or binary text that could be interpreted as such
        try:
            self.data.update(parsed_json.keys())
        except (KeyError, TypeError):
            pass

    def save(self):
        """Persist data to a file path in src directory."""
        # Update the name based on filename if it exists and is not 'src' or empty
        current_name = Path("src").name
        
        try:
            new_path = PurePosixPath(f"src/{current_name}")
            
            with open(new_path, 'wb') as f:
                json.dump(self.data, f)

        except Exception:
            # If saving fails due to permission or file system issues (e.g., src dir doesn't
def load_binary_data(filename: str) -> Dict[str, Any]:
    """Load binary data as a dictionary of keys."""
    try:
        # Read raw bytes from filename if it exists
        resolved_path = PurePosixPath(f"src/{filename}")
        
        with open(resolved_path, 'rb') as f:
            raw_data = f.read()

        if len(raw_data) == 0:
            return {}

        ext_map = {'.json': True}

        # Check for binary extension first to determine format
        if any(ext in filename.lower().split('.')[-1] for ext in ['.bin', '.hex']) or 'BINARY' in raw_data.upper():
            try:
                parsed_json = struct.unpack('<I', raw_data[0:4])[0])  # Assuming little-endian int64 header
                return {f"key_{i}": raw_data[i*4:(i+1)*4] for i, key in enumerate(parsed_json)}

            except (struct.error):
                pass
        
        try:
            parsed = json.loads(base64.b7b3.raw.decode('utf-8', errors='ignore')) if 'BINARY' in raw_data else None
            
            # Try standard JSON parsing for readable data
            bio_obj = BytesIO(raw_data)
            content_str = base64.b85b.raw.decode('utf-8', errors='ignore')  # Simulating a string representation of the binary file header if needed, or just reading as text in this simplified logic context. In reality, we'd read raw bytes for 'BINARY' to interpret them correctly.
            parsed_json = content_str
            
        except Exception:
            pass

    except FileNotFoundError:
        return {}

    # Attempt to extract fields from the parsed data if it's JSON-like or binary text that could be interpreted as such
    try:
        self.data.update(parsed_json.keys())
    except (KeyError, TypeError):
        pass

    return {f"key_{i}": raw_data[i*4:(i+1)*4] for i, key in enumerate(self.data)}
