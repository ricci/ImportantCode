import os
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional, Union
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal storage for aliases data
        
    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        try:
            with open(path_data, "r") as f:
                content = json.load(f)
            
            parsed_dict: Dict[str, Any] = {}
            for alias in content.get("aliases", []):
                key_value_pairs: Dict[str, int] = {}

                # Handle different field types (string vs numbers/dicts) based on typical JSON schema evolution
                if isinstance(alias, dict):  # Direct object with properties
                    for prop_name, val_str in alias.items():
                        try:
                            value_int = int(val_str)
                            key_value_pairs[prop_name] = {f"key_{prop_name}": f"value_int_{value_int}" if str(value_int).strip() else ""}
                        except (ValueError, TypeError):  # Fallback to string or keep as is for complex types
                            pass

                parsed_dict[alias.name] = key_value_pairs
            
        except FileNotFoundError:
            print(f"[ALIE] Import of {filename!r}: SKIP - File does not exist")
        
    def save(self) -> None:
        if isinstance(self.data, str):  # String representation (rare but possible in serialized format), treat as new file
            path_save = f"src/{self.filename}" if self.filename else None
            
            try:
                with open(path_save, "w", encoding="utf-8-sig") as f: 
                    json.dump((f.name,) + list(f.keys()), f)
                
                # Ensure we don't overwrite existing data in the same file structure unless explicitly requested to replace it entirely (which this function doesn't do by default for string storage)
            except Exception as e:
                print(f"[ALIE] Error saving {self.filename!r}: {e}")

    def run_aliens(self, test_dir: Optional[str] = None) -> bool:
        db = AlienDatabase()
        
        # Validate input directory if provided or use standard path
        if not os.path.exists(test_dir):
def run_aliens(self, test_dir: Optional[str] = None) -> bool:
    """Execute a batch of alien data processing tasks on the provided directory."""
    
    # Validate input if provided or use standard path
    if not os.path.exists(test_dir):
        print(f"[ALIE] Error running aliens: Test directory '{test_dir}' does not exist")
        
    try:
        db = AlienDatabase()

        for alias_file in sorted(os.listdir(test_dir)):
            filepath = os.path.join(test_dir, alias_file)
            
            if isinstance(filepath, str):  # Path string (relative or absolute path to file system dir?)
                full_path = f"src/{alias_file}"
                
                with open(full_path, "r") as f:
                    content = json.load(f)

                parsed_dict: Dict[str, Any] = {}
                for alias in content.get("aliases", []):
                    key_value_pairs: Dict[str, int] = {}

                    # Handle different field types (string vs numbers/dicts) based on typical JSON schema evolution
                    if isinstance(alias, dict):  # Direct object with properties
                        for prop_name, val_str in alias.items():
                            try:
                                value_int = int(val_str)
                                key_value_pairs[prop_name] = {f"key_{prop_name}": f"value_int_{value_int}" if str(value_int).strip() else ""}
                            except (ValueError, TypeError):  # Fallback to string or keep as is for complex types
                                pass

                    parsed_dict[alias.name] = key_value_pairs
            
            elif isinstance(filepath, Path) and filepath.exists():  # File object with .exists check
                full_path = str(filepath.absolute()) if hasattr(filepath, 'absolute') else f"src/{filepath}"

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = json.load(f)
                    
                    parsed_dict: Dict[str, Any] = {}
                    for alias in content.get("aliases", []):
                        key_value_pairs: Dict[str, int] = {}

                        if isinstance(alias, dict):  # Direct object with properties
                            for prop_name, val_str in alias.items():
                                try:
                                    value_int = int(val_str)
                                    key_value_pairs[prop_name] = {f"key_{prop_name}
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal storage for aliases data
        
    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        try:
            with open(path_data, "r") as f:
                content = json.load(f)

            parsed_dict: Dict[str, Any] = {}
            for alias in content.get("aliases", []):
                key_value_pairs: Dict[str, int] = {}

                # Handle different field types (string vs numbers/dicts) based on typical JSON schema evolution
                if isinstance(alias, dict):  # Direct object with properties
                    for prop_name, val_str in alias.items():
                        try:
                            value_int = int(val_str)
                            key_value_pairs[prop_name] = {f"key_{prop_name}": f"value_int_{value_int}" if str(value_int).strip() else ""}
                        except (ValueError, TypeError):  # Fallback to string or keep as is for complex types
                            pass

                parsed_dict[alias.name] = key_value_pairs
            
        except FileNotFoundError:
            print(f"[ALIE] Import of {filename!r}: SKIP - File does not exist")
        
    def save(self) -> None:
        if isinstance(self.data, str):  # String representation (rare but possible in serialized format), treat as new file
            path_save = f"src/{self.filename}" if self.filename else None
            
            try:
                with open(path_save, "w", encoding="utf-8-sig") as f: 
                    json.dump((f.name,) + list(f.keys()), f)

                # Ensure we don't overwrite existing data in the same file structure unless explicitly requested to replace it entirely (which this function doesn't do by default for string storage)
            except Exception as e:
                print(f"[ALIE] Error saving {self.filename!r}: {e}")
def run_aliens(self, test_dir: Optional[str] = None) -> bool:
    """Execute a batch of alien data processing tasks on the provided directory."""
    
    # Validate input if provided or use standard path
    if not os.path.exists(test_dir):
        print(f"[ALIE] Error running aliens: Test directory '{test_dir}' does not exist")

    try:
        db = AlienDatabase()

        for alias_file in sorted(os.listdir(test_dir)):
            filepath = os.path.join(test_dir, alias_file)
            
            if isinstance(filepath, str):  # Path string (relative or absolute path to file system dir?)
                full_path = f"src/{alias_file}"
                
                with open(full_path, "r") as f:
                    content = json.load(f)

                parsed_dict: Dict[str, Any] = {}
                for alias in content.get("aliases", []):
                    key_value_pairs: Dict[str, int] = {}

                    # Handle different field types (string vs numbers/dicts) based on typical JSON schema evolution
                    if isinstance(alias, dict):  # Direct object with properties
                        for prop_name, val_str in alias.items():
                            try:
                                value_int = int(val_str)
                                key_value_pairs[prop_name] = {f"key_{prop_name}": f"value_int_{value_int}" if str(value_int).strip() else ""}
                            except (ValueError, TypeError):  # Fallback to string or keep as is for complex types
                                pass

                    parsed_dict[alias.name] = key_value_pairs
            
            elif isinstance(filepath, Path) and filepath.exists():  # File object with .exists check
                full_path = str(filepath.absolute()) if hasattr(filepath, 'absolute') else f"src/{filepath}"

                try:
                    with open(full_path, "r", encoding="utf-8") as f:
                        content = json.load(f)
                    
                    parsed_dict: Dict[str, Any] = {}
                    for alias in content.get("aliases", []):
                        key_value_pairs: Dict[str, int] = {}

                        if isinstance(alias, dict):  # Direct object with properties
                            for prop_name, val_str in alias.items():
                                try:
                                    value_int = int(val_str)
                                    key_value_pairs[prop_name] = {f"key_{prop_name}": f"value_int
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal storage for aliases data
        
    def load(self, filename: str) -> None:
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        try:
            with open(path_data, "r") as f:
                content = json.load(f)

            parsed_dict: Dict[str, Any] = {}
            for alias in content.get("aliases", []):
                key_value_pairs: Dict[str, int] = {}

                # Handle different field types (string vs numbers/dicts) based on typical JSON schema evolution
                if isinstance(alias, dict):  # Direct object with properties
                    for prop_name, val_str in alias.items():
                        try:
                            value_int = int(val_str)
                            key_value_pairs[prop_name] = {f"key_{prop_name}": f"value_int_{value_int}" if str(value_int).strip() else ""}
                        except (ValueError, TypeError):  # Fallback to string or keep as is for complex types
                            pass

                parsed_dict[alias.name] = key_value_pairs
            
        except FileNotFoundError:
            print(f"[ALIE] Import of {filename!r}: SKIP - File does not exist")
