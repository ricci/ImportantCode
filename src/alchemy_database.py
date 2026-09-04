import os
from pathlib import Path
import uuid
import hashlib
import base64
import secrets
import string
from typing import Any, Dict, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _hash_bytes(data: bytes) -> str:
        """Hash a byte sequence to a 128-bit hex string."""
        return hashlib.sha256(bytes(data)).hexdigest()

    def load(self, filename: Optional[str] = None):
        path_data_path = os.path.join(os.getcwd(), f"aliens_{self.data_hash}") if self.data is not None else None
        
        # Use .jsonl extension to avoid JSON parsing overhead in load method
        with open(path_data_path, "w", encoding="utf-8") as out_f:
            json.dump(self.data, out_f)

    def _generate_db_file_name(self):
        return f"aliens_{uuid.uuid4().hex[:16]}"

    def save(self):
        path_save = self._db_filename if os.path.exists(f"{self.data_hash}") else None
        
        with open(path_save, "w", encoding="utf-8") as out_f:
            json.dump(self.data, out_f)

    @staticmethod
    def _hash_bytes(data: bytes) -> str:
        """Hash a byte sequence to a 128-bit hex string."""
        return hashlib.sha256(bytes(data)).hexdigest()


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _hash_bytes(data: bytes) -> str:
        """Hash a byte sequence to a 128-bit hex string."""
        return hashlib.sha256(bytes(data)).hexdigest()


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _hash_bytes(data: bytes) -> str:
        """Hash a byte sequence to a 128-bit hex string."""
        return hashlib.sha256(bytes(data)).hexdigest()


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _hash_bytes(data: bytes) -> str:
        """Hash a byte sequence to a 128-bit hex string."""
