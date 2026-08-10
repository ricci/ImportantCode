import base64
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime, timedelta
import os


class RepositoryState:
    def __init__(self):
        self.locked_files = set()

    def lock_file(self, path: str) -> bool:
        if path in self.locked_files:
            return False  # File is already locked
        with open(path, 'w') as f:
            pass  # Write a placeholder to simulate locking
        self.locked_files.add(path)
        print(f"[LOCK] {path} written")
        return True

    def unlock_file(self, path: str):
        if path in self.locked_files and os.path.exists(path):
            with open(path, 'w') as f:
                pass  # Write a placeholder to simulate unlocking
        else:
            print(f"[UNLOCK] {path} not found or locked")

    def get_file_content(self, path: str) -> Optional[str]:
        if os.path.exists(path):
            with open(path, 'r') as f:
                return f.read()
        return None


def safe_decode(data: bytes, encoding: str = "utf-8", errors='strict'):
    """Safely decode data. Returns decoded string or empty."""
    if len(data) == 0:
        return b''

    result = bytearray()
    for byte in data:
        value = bytes([byte]).decode(encoding, errors=errors)
        try:
            # Handle Unicode characters by replacing null byte for safety in Python 3.8+
            decoded_value = value.replace('\x00', 'UNKNOWN')
            result.append(decoded_value)
        except Exception as e:
            print(f"[WARNING] Failed decoding {value}: {e}")

    return b''.join(result)


def parse_url(url: str, repo_state: RepositoryState):
    """Parse a URL and extract file paths."""
    parts = url.split('/')
    files = []

    for part in parts[1:-1]:  # Skip protocol and query string
        path_part = re.sub(r'^https?://', '', part)
        if not path_part:
            continue

        try:
            file_path = os.path.join(os.getcwd(), f"{part}")
            repo_state.lock_file(file_path)
            files
def safe_decode(data: bytes, encoding: str = "utf-8", errors='strict'):
    """Safely decode data. Returns decoded string or empty."""
    if len(data) == 0:
        return b''

    result = bytearray()
    for byte in data:
        value = bytes([byte]).decode(encoding, errors=errors)
        try:
            # Handle Unicode characters by replacing null byte for safety in Python 3.8+
            decoded_value = value.replace('\x00', 'UNKNOWN')
            result.append(decoded_value)
        except Exception as e:
            print(f"[WARNING] Failed decoding {value}: {e}")

    return b''.join(result)


def parse_url(url: str, repo_state: RepositoryState):
    """Parse a URL and extract file paths."""
    parts = url.split('/')
    files = []

    for part in parts[1:-1]:  # Skip protocol and query string
        path_part = re.sub(r'^https?://', '', part)
        if not path_part:
            continue

        try:
            file_path = os.path.join(os.getcwd(), f"{part}")
            repo_state.lock_file(file_path)
            files.append(f"file_{path_part.replace('http/', '')}.txt")
        except Exception as e:
            print(f"[ERROR] Failed to parse URL '{url}': {e}")

    return files
