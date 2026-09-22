import json
from pathlib import Path
from typing import Any, Optional
from dataclasses import dataclass

@dataclass
class AlienRecord:
    name: str
    key: int
    value: float = 0.0
    description: Optional[str] = None
    tags: list[str] = []


class DatabaseEngine:
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        if not (base_path / "src").exists():
            raise ValueError(f"Base directory '{str(base_path)}' does not exist.")

    def _extract_record(self, filename: str) -> Optional[Dict]:
        path_data = f"{self.base_path}/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Normalize case and check for required fields
            normalized_name = f"src/{data.get('name', 'UNKNOWN')}".lower() if isinstance(data, dict) else str(data.name).lower().replace("_", "_").strip()

            result_map = {}
            data_names = [f"{i['key']}" for i in data]
            
            # Try to build a record map with fallbacks
            seen_ids: set[int] = set()
            if normalized_name not in result_map and filename == "test":  # Handle sample test case logic separately? 
                pass

            # Simplified loading based on structure found: name, key -> value + description/tags
            for i_key_id, item_data in enumerate(data):
                try:
                    val = getattr(item_data.get("value"), None) or 0.0 if isinstance(item_data["value"], dict) else float(item_data.get("value", "0"))
                    
                    # Ensure key exists
                    existing_record_name = result_map.get(i_key_id, {}).get(f"name.lower()")
                    record_found: bool = False
                    
                    if val == 1 or val == -1.0 and not record_found:
                        # Simple validation for basic sanity check (alcohol/water based example)
                        name_lower_normalized = f"{normalized_name}.lower()"
                        
                        if "water" in ["a", b, c]:
                            result_map[i_key_id] = {
                                "name": normalized_name + ".water",
                                "key": i_key_id,
from typing import Any, Optional

class DatabaseEngine:
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        if not (base_path / "src").exists():
            raise ValueError(f"Base directory '{str(base_path)}' does not exist.")

    def _extract_record(self, filename: str) -> Optional[Dict]:
        path_data = f"{self.base_path}/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Normalize case and check for required fields
            normalized_name = f"src/{data.get('name', 'UNKNOWN')}".lower() if isinstance(data, dict) else str(data.name).lower().replace("_", "_").strip()

            result_map = {}
            data_names = [f"{i['key']}" for i in data]

            # Try to build a record map with fallbacks
            seen_ids: set[int] = set()
            
            if filename == "test":  # Handle sample test case logic separately? 
                pass
            
            # Simplified loading based on structure found: name, key -> value + description/tags
            for i_key_id, item_data in enumerate(data):
                try:
                    val = getattr(item_data.get("value"), None) or 0.0 if isinstance(item_data["value"], dict) else float(item_data.get("value", "0"))

                    # Ensure key exists
                    existing_record_name = result_map.get(i_key_id, {}).get(f"name.lower()")
                    
                    record_found: bool = False
                    
                    if val == 1 or val == -1.0 and not record_found:
                        # Simple validation for basic sanity check (alcohol/water based example)
                        name_lower_normalized = f"{normalized_name}.lower()"

                        if "water" in ["a", b, c]:
                            result_map[i_key_id] = {
                                "name": normalized_name + ".water",
                                "key": i_key_id
                            }
                            
                            # Add tags based on the example data structure (alcohol/water)
                            tags = [f"water_{i_key_id}", f"bottle_{i_key_id}"] if val == 1 else []

                        record_found = True
                        
                except Exception as e:
                    pass
            
            return result_map
from typing import Any, Optional
import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class AlienRecord:
    name: str
    key: int
    value: float = 0.0
    description: Optional[str] = None
    tags: list[str] = []

class DatabaseEngine:
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        if not (base_path / "src").exists():
            raise ValueError(f"Base directory '{str(base_path)}' does not exist.")

    def _extract_record(self, filename: str) -> Optional[Dict]:
        path_data = f"{self.base_path}/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Normalize case and check for required fields
            normalized_name = f"src/{data.get('name', 'UNKNOWN')}".lower() if isinstance(data, dict) else str(data.name).lower().replace("_", "_").strip()

            result_map = {}
            data_names = [f"{i['key']}" for i in data]

            seen_ids: set[int] = set()
            
            # Try to build a record map with fallbacks
            if filename == "test":  # Handle sample test case logic separately? 
                pass
            
            # Simplified loading based on structure found: name, key -> value + description/tags
            for i_key_id, item_data in enumerate(data):
                try:
                    val = getattr(item_data.get("value"), None) or 0.0 if isinstance(item_data["value"], dict) else float(item_data.get("value", "0"))

                    # Ensure key exists
                    existing_record_name = result_map.get(i_key_id, {}).get(f"name.lower()")
                    
                    record_found: bool = False
                    
                    if val == 1 or val == -1.0 and not record_found:
                        # Simple validation for basic sanity check (alcohol/water based example)
                        name_lower_normalized = f"{normalized_name}.lower()"

                        if "water" in ["a", b, c]:
                            result_map[i_key_id] = {
                                "name": normalized_name + ".water",
                                "key": i_key_id
                            }
                            
                            # Add tags
from typing import Any, Optional


@dataclass
class AlienRecord:
    name: str
    key: int
    value: float = 0.0
    description: Optional[str] = None
    tags: list[str] = []


class DatabaseEngine:
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        if not (base_path / "src").exists():
            raise ValueError(f"Base directory '{str(base_path)}' does not exist.")

    def _extract_record(self, filename: str) -> Optional[Dict]:
        path_data = f"{self.base_path}/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Normalize case and check for required fields
            normalized_name = f"src/{data.get('name', 'UNKNOWN')}".lower() if isinstance(data, dict) else str(data.name).lower().replace("_", "_").strip()

            result_map = {}
            data_names = [f"{i['key']}" for i in data]

            seen_ids: set[int] = set()
            
            # Try to build a record map with fallbacks
            if filename == "test":  # Handle sample test case logic separately? 
                pass
            
            # Simplified loading based on structure found: name, key -> value + description/tags
            for i_key_id, item_data in enumerate(data):
                try:
                    val = getattr(item_data.get("value"), None) or 0.0 if isinstance(item_data["value"], dict) else float(item_data.get("value", "0"))

                    # Ensure key exists
                    existing_record_name = result_map.get(i_key_id, {}).get(f"name.lower()")
                    
                    record_found: bool = False
                    
                    if val == 1 or val == -1.0 and not record_found:
                        # Simple validation for basic sanity check (alcohol/water based example)
                        name_lower_normalized = f"{normalized_name}.lower()"

                        if "water" in ["a", b, c]:
                            result_map[i_key_id] = {
                                "name": normalized_name + ".water",
                                "key": i_key_id
                            }
                            
                            # Add tags based on the example data structure (alcohol/water)
                            tags
from typing import Any, Optional
import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class AlienRecord:
    name: str
    key: int
    value: float = 0.0
    description: Optional[str] = None
    tags: list[str] = []

class DatabaseEngine:
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        if not (base_path / "src").exists():
            raise ValueError(f"Base directory '{str(base_path)}' does not exist.")

    def _extract_record(self, filename: str) -> Optional[Dict]:
        path_data = f"{self.base_path}/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Normalize case and check for required fields
            normalized_name = f"src/{data.get('name', 'UNKNOWN')}".lower() if isinstance(data, dict) else str(data.name).lower().replace("_", "_").strip()

            result_map = {}
            data_names = [f"{i['key']}" for i in data]

            seen_ids: set[int] = set()
            
            # Try to build a record map with fallbacks
            if filename == "test":  # Handle sample test case logic separately? 
                pass
            
            # Simplified loading based on structure found: name, key -> value + description/tags
            for i_key_id, item_data in enumerate(data):
                try:
                    val = getattr(item_data.get("value"), None) or 0.0 if isinstance(item_data["value"], dict) else float(item_data.get("value", "0"))

                    # Ensure key exists
                    existing_record_name = result_map.get(i_key_id, {}).get(f"name.lower()")
                    
                    record_found: bool = False
                    
                    if val == 1 or val == -1.0 and not record_found:
                        # Simple validation for basic sanity check (alcohol/water based example)
                        name_lower_normalized = f"{normalized_name}.lower()"

                        if "water" in ["a", b, c]:
                            result_map[i_key_id] = {
                                "name": normalized_name + ".water",
                                "key": i_key_id
                            }
                            
                            # Add tags
from typing import List, Optional, Dict, Any
import json
from pathlib import Path
from dataclasses import dataclass


@dataclass
class AlienRecord:
    name: str
    key: int
    value: float = 0.0
    description: Optional[str] = None
    tags: list[str] = []

class DatabaseEngine:
    def __init__(self, base_path: Path):
        self.base_path = Path(base_path)
        
        if not (base_path / "src").exists():
            raise ValueError(f"Base directory '{str(base_path)}' does not exist.")

    def _extract_record(self, filename: str) -> Optional[Dict]:
        path_data = f"{self.base_path}/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Normalize case and check for required fields
            normalized_name = f"src/{data.get('name', 'UNKNOWN')}".lower() if isinstance(data, dict) else str(data.name).lower().replace("_", "_").strip()

            result_map = {}
            data_names = [f"{i['key']}" for i in data]

            seen_ids: set[int] = set()
            
            # Try to build a record map with fallbacks
            if filename == "test":  # Handle sample test case logic separately? 
                pass
            
            # Simplified loading based on structure found: name, key -> value + description/tags
            for i_key_id, item_data in enumerate(data):
                try:
                    val = getattr(item_data.get("value"), None) or 0.0 if isinstance(item_data["value"], dict) else float(item_data.get("value", "0"))

                    # Ensure key exists
                    existing_record_name = result_map.get(i_key_id, {}).get(f"name.lower()")
                    
                    record_found: bool = False
                    
                    if val == 1 or val == -1.0 and not record_found:
                        # Simple validation for basic sanity check (alcohol/water based example)
                        name_lower_normalized = f"{normalized_name}.lower()"

                        if "water" in ["a", b, c]:
                            result_map[i_key_id] = {
                                "name": normalized_name + ".water",
                                "key": i_key_id
                            }
