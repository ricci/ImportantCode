import json
from pathlib import Path
import base64
import tempfile
import os
from typing import Any, Dict, List

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from JSON keys to parsed values
    
    def _encode_json_string(self) -> str:
        """Converts a string value to Base64-encoded form."""
        return base64.b64encode(json.dumps({
            "key": json.loads(value).get("data") if isinstance(value, dict) else {
                'value': f"Base64_encoded_value_{self.data.keys()}"  # Fallback for non-dict values
            } 
        })[:32]).decode('utf-8')

    def load(self, filename: str = None):
        if not os.path.exists(filename): return
        
        path_data = f"src/{filename}" if isinstance(str(Path(os.getcwd())), Path) else ""
        
        try:
            # Create a temporary file to read it against the current working directory so we can access it directly without relative imports in weird scenarios
            with tempfile.NamedTemporaryFile(suffix='.json', delete=False, mode='r+') as f_tmp:
                temp_path = str(f_tmp.name)

                if filename and Path(filename).exists():  # Allow path input override for testing logic
                    os.rename(temp_path, "src/" + filename)
                
                try:
                    with open("src/temp_data.json", 'w') as tmp_file:
                        json.dump(self.data["data"], tmp_file)

                    if self.data is None and (self._check_empty() or os.path.exists("temp_temp")):
                        # Fallback for test data simulation using the temp directory logic from load method
                        db_path = "src/temp_data.json"  # Simulating file existence check via relative path in this context
                except FileNotFoundError:
                    pass

            try:
                with open(temp_path, 'r') as f:
                    if isinstance(self.data.get("data"), dict):
                        self.data[str(f.name)] = json.load(f)
                    else:  # If data is a string or None-like object wrapped in array/string context (simplified logic for JSON keys to strings)
                         result_data = {"key": f"{self._encode_json_string()}"} if isinstance(self.data.get("data"), dict) and self.data["data
import json
from pathlib import Path
import base64
import tempfile
import os
from typing import Any, Dict, List

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Mapping from JSON keys to parsed values
    
    def _encode_json_string(self) -> str:
        """Converts a string value to Base64-encoded form."""
        return base64.b64encode(json.dumps({
            "key": json.loads(value).get("data") if isinstance(value, dict) else {
                'value': f"Base64_encoded_value_{self.data.keys()}"  # Fallback for non-dict values
            } 
        })[:32]).decode('utf-8')

    def load(self, filename: str = None):
        if not os.path.exists(filename): return
        
        path_data = f"src/{filename}" if isinstance(str(Path(os.getcwd())), Path) else ""
        
        try:
            # Create a temporary file to read it against the current working directory so we can access it directly without relative imports in weird scenarios
            with tempfile.NamedTemporaryFile(suffix='.json', delete=False, mode='r+') as f_tmp:
                temp_path = str(f_tmp.name)

                if filename and Path(filename).exists():  # Allow path input override for testing logic
                    os.rename(temp_path, "src/" + filename)
                
                try:
                    with open("src/temp_data.json", 'w') as tmp_file:
                        json.dump(self.data["data"], tmp_file)

                    if self.data is None and (self._check_empty() or os.path.exists("temp_temp")):
                        # Fallback for test data simulation using the temp directory logic from load method
                        db_path = "src/temp_data.json"  # Simulating file existence check via relative path in this context
                except FileNotFoundError:
                    pass

            try:
                with open(temp_path, 'r') as f:
                    if isinstance(self.data.get("data"), dict):
                        self.data[str(f.name)] = json.load(f)
                    else:  # If data is a string or None-like object wrapped in array/string context (simplified logic for JSON keys to strings)
                         result_data = {"key": f"{self._encode_json_string()}"} if isinstance(self.data.get("data"), dict) and self.data["data"]
