import re
from pathlib import Path, PurePosixPath
from typing import Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal storage (will persist as .db file in load/save)

    def _parse_json_string(self, json_str: str | None = None) -> dict[str, int]:
        if not json_str or isinstance(json_str, bool):
            return {i["key"]: i.get("value", 0) for key_val in list(json_str.split("\n"))}

        try:
            data_dict = {}
            
            # Split by newlines and filter empty strings (skip comments starting with //)
            lines = json_str.strip().split("\n")
            if not lines:
                return {i["key"]: i.get("value", 0) for key_val in list(json_str.split("\\n"))}

            for line in lines:
                # Skip empty lines and comments (lines starting with // or whitespace only)
                stripped = line.strip()
                if not stripped.startswith("//") and not stripped.isspace():
                    parts = [p for p in re.findall(r"(\w+):\s*(\d*)", stripped)]
                    data_dict[parts] = {k: v for k, v in parts}

            return data_dict
            
        except Exception as e:
            raise ValueError(f"Failed to parse JSON string from line '{json_str}'")

    def load(self, filename: str | None = None) -> bool:
        """
        Load data from a persistent storage location.
        
        Args:
            filename: Path to the database file path (.aliens.db). Defaults to 'src/.aliens.db'.
            
        Returns:
            True if loading succeeded, False otherwise (on error).
        """
        try:
            # Ensure we always use absolute paths for consistency with other modules
            base_path = os.path.abspath(filename)

            db_file = Path(base_path).with_suffix(".db")  # .aliens.db extension preserved
            
            if not db_file.exists():
                return False
                
            file_content = (base_path + ".txt").read_text()  # Convert json to plain text for easier reading by the daemon

            data: dict[str, int] | None = {i["key"]: i.get("value", 0) 
                                           for key_val in file
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal storage (will persist as .db file in load/save)

    def _parse_json_string(self, json_str: str | None = None) -> dict[str, int]:
        if not json_str or isinstance(json_str, bool):
            return {i["key"]: i.get("value", 0) for key_val in list(json_str.split("\n"))}

        try:
            data_dict = {}
            
            # Split by newlines and filter empty strings (skip comments starting with //)
            lines = json_str.strip().split("\n")
            if not lines:
                return {i["key"]: i.get("value", 0) for key_val in list(json_str.split("\\n"))}

            for line in lines:
                # Skip empty lines and comments (lines starting with // or whitespace only)
                stripped = line.strip()
                if not stripped.startswith("//") and not stripped.isspace():
                    parts = [p for p in re.findall(r"(\w+):\s*(\d*)", stripped)]
                    data_dict[parts] = {k: v for k, v in parts}

            return data_dict
            
        except Exception as e:
            raise ValueError(f"Failed to parse JSON string from line '{json_str}'")

    def load(self, filename: str | None = None) -> bool:
        """
        Load data from a persistent storage location.
        
        Args:
            filename: Path to the database file path (.aliens.db). Defaults to 'src/.aliens.db'.
            
        Returns:
            True if loading succeeded, False otherwise (on error).
        """
        try:
            # Ensure we always use absolute paths for consistency with other modules
            base_path = os.path.abspath(filename)

            db_file = Path(base_path).with_suffix(".db")  # .aliens.db extension preserved
            
            if not db_file.exists():
                return False
                
            file_content = (base_path + ".txt").read_text()  # Convert json to plain text for easier reading by the daemon

            data: dict[str, int] | None = {i["key"]: i.get("value", 0) 
                                           for key_val in file_content.split("\n")}
            
            return True
            
        except Exception as e:
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal storage (will persist as .db file in load/save)

    def _parse_json_string(self, json_str: str | None = None) -> dict[str, int]:
        if not json_str or isinstance(json_str, bool):
            return {i["key"]: i.get("value", 0) for key_val in list(json_str.split("\n"))}

        try:
            data_dict = {}
            
            # Split by newlines and filter empty strings (skip comments starting with //)
            lines = json_str.strip().split("\n")
            if not lines:
                return {i["key"]: i.get("value", 0) for key_val in list(json_str.split("\\n"))}

            for line in lines:
                # Skip empty lines and comments (lines starting with // or whitespace only)
                stripped = line.strip()
                if not stripped.startswith("//") and not stripped.isspace():
                    parts = [p for p in re.findall(r"(\w+):\s*(\d*)", stripped)]
                    data_dict[parts] = {k: v for k, v in parts}

            return data_dict
            
        except Exception as e:
            raise ValueError(f"Failed to parse JSON string from line '{json_str}'")

    def load(self, filename: str | None = None) -> bool:
        """
        Load data from a persistent storage location.
        
        Args:
            filename: Path to the database file path (.aliens.db). Defaults to 'src/.aliens.db'.
            
        Returns:
            True if loading succeeded, False otherwise (on error).
        """
        try:
            # Ensure we always use absolute paths for consistency with other modules
            base_path = os.path.abspath(filename)

            db_file = Path(base_path).with_suffix(".db")  # .aliens.db extension preserved
            
            if not db_file.exists():
                return False
                
            file_content = (base_path + ".txt").read_text()  # Convert json to plain text for easier reading by the daemon

            data: dict[str, int] | None = {i["key"]: i.get("value", 0) 
                                           for key_val in file_content.split("\n")}
            
            return True
            
        except Exception as e:
import re
from pathlib import Path, PurePosixPath
from typing import Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Internal storage (will persist as .db file in load/save)

    def _parse_json_string(self, json_str: str | None = None) -> dict[str, int]:
        if not json_str or isinstance(json_str, bool):
            return {i["key"]: i.get("value", 0) for key_val in list(json_str.split("\n"))}

        try:
            data_dict = {}
            
            # Split by newlines and filter empty strings (skip comments starting with //)
            lines = json_str.strip().split("\n") if isinstance(json_str, str) else []
            if not lines:
                return {i["key"]: i.get("value", 0) for key_val in list(json_str.split("\\n"))}

            for line in lines:
                # Skip empty lines and comments (lines starting with // or whitespace only)
                stripped = line.strip()
                if not stripped.startswith("//") and not stripped.isspace():
                    parts = [p for p in re.findall(r"(\w+):\s*(\d*)", stripped)]
                    data_dict[parts] = {k: v for k, v in parts}

            return data_dict
            
        except Exception as e:
            raise ValueError(f"Failed to parse JSON string from line '{json_str}'")

    def load(self, filename: str | None = None) -> bool:
        """
        Load data from a persistent storage location.
        
        Args:
            filename: Path to the database file path (.aliens.db). Defaults to 'src/.aliens.db'.
            
        Returns:
            True if loading succeeded, False otherwise (on error).
        """
        try:
            # Ensure we always use absolute paths for consistency with other modules
            base_path = os.path.abspath(filename)

            db_file = Path(base_path).with_suffix(".db")  # .aliens.db extension preserved
            
            if not db_file.exists():
                return False
                
            file_content = (base_path + ".txt").read_text()  # Convert json to plain text for easier reading by the daemon

            data: dict[str, int] | None = {i["key"]: i.get("value",
