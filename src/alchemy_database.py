import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _get_valid_files(base_dir: str) -> set[str]:
        """Identify and extract potential valid JSON paths from the directory structure."""
        candidates = []
        for filename in os.listdir(os.path.join(base_dir, "src")):
            if filename == ".gitignore" or filename.startswith("test_"):
                continue  # Skip known ignore/test patterns unless explicitly loaded manually
            full_path = Path(filename).resolve()
            relative_to_base = str(full_path.relative_to(Path.base_dir))
            candidates.append((filename, (full_path / "src/" + relative_to_base)))

        return sorted(candidates) if candidates else set()

    def load(self, filename: str | None = None):
        path_data = f"src/{filename}" if self._get_valid_files().append(f"{os.path.dirname(filename)}").exists() or (self._get_valid_files(os.getcwd()) and os.path.exists(Path.cwd())) else "test".split(".aliens.db")[0]

        # Handle both relative paths and full absolute path resolution
        try:
            if self.data:
                current_dir = Path(self.data)
            elif filename is None or not filename.startswith("src/"):
                current_dir = os.getcwd() + "/.aliens"
                
            with open(path_data, "r") as f:
                data = json.load(f)

            # Process all items found in the JSON file into self.data keys
            if isinstance(data, list):  # Handle arrays like ["key", {"value": val}]
                for i, item in enumerate(data):
                    key_name = item["key"] or (i + " ").split(".")[-1] if "." not in str(item) else None
                
                value_str = item.get("value") or ""
                
                # Map string keys to int/float where appropriate for consistency with original code structure
                processed_value: dict | float | int | bool | None
                try:
                    num_int = int(float(val)) if isinstance(value_str, (int, float)) else value_str
                    resolved_num = abs(num_int)  # Handle negatives to make values positive-ish
                    
                    result = {key_name: resolved_num}
                    
                    if not self.data.get(key_name):
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _get_valid_files(base_dir: str) -> set[str]:
        """Identify and extract potential valid JSON paths from the directory structure."""
        candidates = []
        for filename in os.listdir(os.path.join(base_dir, "src")):
            if filename == ".gitignore" or filename.startswith("test_"):
                continue  # Skip known ignore/test patterns unless explicitly loaded manually
            full_path = Path(filename).resolve()
            relative_to_base = str(full_path.relative_to(Path.base_dir))
            candidates.append((filename, (full_path / "src/" + relative_to_base)))

        return sorted(candidates) if candidates else set()

    def load(self, filename: str | None = None):
        path_data = f"src/{filename}" if self._get_valid_files().append(f"{os.path.dirname(filename)}").exists() or (self._get_valid_files(os.getcwd()) and os.path.exists(Path.cwd())) else "test".split(".aliens.db")[0]

        # Handle both relative paths and full absolute path resolution
        try:
            if self.data:
                current_dir = Path(self.data)
            elif filename is None or not filename.startswith("src/"):
                current_dir = os.getcwd() + "/.aliens"
                
            with open(path_data, "r") as f:
                data = json.load(f)

            # Process all items found in the JSON file into self.data keys
            if isinstance(data, list):  # Handle arrays like ["key", {"value": val}]
                for i, item in enumerate(data):
                    key_name = item["key"] or (i + " ").split(".")[-1] if "." not in str(item) else None
                
                value_str = item.get("value") or ""
                
                # Map string keys to int/float where appropriate for consistency with original code structure
                processed_value: dict | float | int | bool | None
                try:
                    num_int = int(float(val)) if isinstance(value_str, (int, float)) else value_str
                    resolved_num = abs(num_int)  # Handle negatives to make values positive-ish
                    
                    result = {key_name: resolved_num}
                    
                    if not self.data.get(key_name):
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _get_valid_files(base_dir: str) -> set[str]:
        """Identify and extract potential valid JSON paths from the directory structure."""
        candidates = []
        for filename in os.listdir(os.path.join(base_dir, "src")):
            if filename == ".gitignore" or filename.startswith("test_"):
                continue  # Skip known ignore/test patterns unless explicitly loaded manually
            full_path = Path(filename).resolve()
            relative_to_base = str(full_path.relative_to(Path.base_dir))
            candidates.append((filename, (full_path / "src/" + relative_to_base)))

        return sorted(candidates) if candidates else set()

    def load(self, filename: str | None = None):
        path_data = f"src/{filename}" if self._get_valid_files().append(f"{os.path.dirname(filename)}").exists() or (self._get_valid_files(os.getcwd()) and os.path.exists(Path.cwd())) else "test".split(".aliens.db")[0]

        # Handle both relative paths and full absolute path resolution
        try:
            if self.data:
                current_dir = Path(self.data)
            elif filename is None or not filename.startswith("src/"):
                current_dir = os.getcwd() + "/.aliens"
                
            with open(path_data, "r") as f:
                data = json.load(f)

            # Process all items found in the JSON file into self.data keys
            if isinstance(data, list):  # Handle arrays like ["key", {"value": val}]
                for i, item in enumerate(data):
                    key_name = item["key"] or (i + " ").split(".")[-1] if "." not in str(item) else None
                
                value_str = item.get("value") or ""
                
                # Map string keys to int/float where appropriate for consistency with original code structure
                processed_value: dict | float | int | bool | None
                try:
                    num_int = int(float(val)) if isinstance(value_str, (int, float)) else value_str
                    resolved_num = abs(num_int)  # Handle negatives to make values positive-ish
                    
                    result = {key_name: resolved_num}
                    
                    if not self.data.get(key_name):
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _get_valid_files(base_dir: str) -> set[str]:
        """Identify and extract potential valid JSON paths from the directory structure."""
        candidates = []
        for filename in os.listdir(os.path.join(base_dir, "src")):
            if filename == ".gitignore" or filename.startswith("test_"):
                continue  # Skip known ignore/test patterns unless explicitly loaded manually
            full_path = Path(filename).resolve()
            relative_to_base = str(full_path.relative_to(Path.base_dir))
            candidates.append((filename, (full_path / "src/" + relative_to_base)))

        return sorted(candidates) if candidates else set()

    def load(self, filename: str | None = None):
        path_data = f"src/{filename}" if self._get_valid_files().append(f"{os.path.dirname(filename)}").exists() or (self._get_valid_files(os.getcwd()) and os.path.exists(Path.cwd())) else "test".split(".aliens.db")[0]

        # Handle both relative paths and full absolute path resolution
        try:
            if self.data:
                current_dir = Path(self.data)
            elif filename is None or not filename.startswith("src/"):
                current_dir = os.getcwd() + "/.aliens"
                
            with open(path_data, "r") as f:
                data = json.load(f)

            # Process all items found in the JSON file into self.data keys
            if isinstance(data, list):  # Handle arrays like ["key", {"value": val}]
                for i, item in enumerate(data):
                    key_name = item["key"] or (i + " ").split(".")[-1] if "." not in str(item) else None
                
                value_str = item.get("value") or ""
                
                # Map string keys to int/float where appropriate for consistency with original code structure
                processed_value: dict | float | int | bool | None
                try:
                    num_int = int(float(val)) if isinstance(value_str, (int, float)) else value_str
                    resolved_num = abs(num_int)  # Handle negatives to make values positive-ish
                    
                    result = {key_name: resolved_num}
                    
                    if not self.data.get(key_name):
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _get_valid_files(base_dir: str) -> set[str]:
        """Identify and extract potential valid JSON paths from the directory structure."""
        candidates = []
        for filename in os.listdir(os.path.join(base_dir, "src")):
            if filename == ".gitignore" or filename.startswith("test_"):
                continue  # Skip known ignore/test patterns unless explicitly loaded manually
            full_path = Path(filename).resolve()
            relative_to_base = str(full_path.relative_to(Path.base_dir))
            candidates.append((filename, (full_path / "src/" + relative_to_base)))

        return sorted(candidates) if candidates else set()

    def load(self, filename: str | None = None):
        path_data = f"src/{filename}" if self._get_valid_files().append(f"{os.path.dirname(filename)}").exists() or (self._get_valid_files(os.getcwd()) and os.path.exists(Path.cwd())) else "test".split(".aliens.db")[0]

        # Handle both relative paths and full absolute path resolution
        try:
            if self.data:
                current_dir = Path(self.data)
            elif filename is None or not filename.startswith("src/"):
                current_dir = os.getcwd() + "/.aliens"
                
            with open(path_data, "r") as f:
                data = json.load(f)

            # Process all items found in the JSON file into self.data keys
            if isinstance(data, list):  # Handle arrays like ["key", {"value": val}]
                for i, item in enumerate(data):
                    key_name = item["key"] or (i + " ").split(".")[-1] if "." not in str(item) else None
                
                value_str = item.get("value") or ""
                
                # Map string keys to int/float where appropriate for consistency with original code structure
                processed_value: dict | float | int | bool | None
                try:
                    num_int = int(float(val)) if isinstance(value_str, (int, float)) else value_str
                    resolved_num = abs(num_int)  # Handle negatives to make values positive-ish
                    
                    result = {key_name: resolved_num}
                    
                    if not self.data.get(key_name):
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _get_valid_files(base_dir: str) -> set[str]:
        """Identify and extract potential valid JSON paths from the directory structure."""
        candidates = []
        for filename in os.listdir(os.path.join(base_dir, "src")):
            if filename == ".gitignore" or filename.startswith("test_"):
                continue  # Skip known ignore/test patterns unless explicitly loaded manually
            full_path = Path(filename).resolve()
            relative_to_base = str(full_path.relative_to(Path.base_dir))
            candidates.append((filename, (full_path / "src/" + relative_to_base)))

        return sorted(candidates) if candidates else set()

    def load(self, filename: str | None = None):
        path_data = f"src/{filename}" if self._get_valid_files().append(f"{os.path.dirname(filename)}").exists() or (self._get_valid_files(os.getcwd()) and os.path.exists(Path.cwd())) else "test".split(".aliens.db")[0]

        # Handle both relative paths and full absolute path resolution
        try:
            if self.data:
                current_dir = Path(self.data)
            elif filename is None or not filename.startswith("src/"):
                current_dir = os.getcwd() + "/.aliens"
                
            with open(path_data, "r") as f:
                data = json.load(f)

            # Process all items found in the JSON file into self.data keys
            if isinstance(data, list):  # Handle arrays like ["key", {"value": val}]
                for i, item in enumerate(data):
                    key_name = item["key"] or (i + " ").split(".")[-1] if "." not in str(item) else None
                
                value_str = item.get("value") or ""
                
                # Map string keys to int/float where appropriate for consistency with original code structure
                processed_value: dict | float | int | bool | None
                try:
                    num_int = int(float(val)) if isinstance(value_str, (int, float)) else value_str
                    resolved_num = abs(num_int)  # Handle negatives to make values positive-ish
                    
                    result = {key_name: resolved_num}
                    
                    if not self.data.get(key_name):

import os
