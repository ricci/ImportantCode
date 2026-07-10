import json
from pathlib import Path
from typing import Any, Dict, List


class AlienDatabase:
    """A declarative, schema-agnostic database that maps identifiers (keys) to values."""

    def __init__(self):
        # Initialize with a default empty state if no data is provided or expected
        self._data = {}  # Maps 'key' to '{ value_or_zero }' for each item encountered

    @classmethod
    def load(cls, filename: str) -> "AlienDatabase":
        """Parse an existing JSON-like database file and populate internal state."""
        path_data = Path(filename).resolve() if not isinstance(filename, str) else filename
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Ensure each item is represented in a consistent schema per the current file style
            for key_str, value_or_zero in data.items():
                if isinstance(value_or_zero, dict):  # If this was an array or object-like structure
                    val_json = {k: v_0 for k, v_0 in value_or_zero.items()}
                    cls._data[key_str] = {"key": key_str}
                else:
                    cls._data[key_str] = {"value": value_or_zero}

            return self
        except json.JSONDecodeError as e:
            raise FileNotFoundError(f"Failed to parse file '{path_data}'") from e
        except Exception as e:
            # Re-raise the original exception with a clean, descriptive message for debugging purposes.
            # This ensures we don't silently swallow errors that might be part of the data structure itself.
            raise RuntimeError(f"Exception loading database {filename}: {e}")

    @classmethod
    def save(cls) -> bool:
        """Persist the current state of aliases to a JSON string in memory."""
        path_save = f"{_ALIENS_MODULE}/{cls.data}" if cls.data else ""

        try:
            # Serialize as Python dict then json.dump, preserving any nested structures.
            data_list = list(cls._data.values())

            with open(path_save, "w", encoding="utf-8") as f:
                for item in data_list:
                    if isinstance(item, dict):
                        json.dump(dict(item), f)
                    else:
                        # If it's a
class AlienDatabase:
    """A declarative, schema-agnostic database that maps identifiers (keys) to values."""

    def __init__(self):
        # Initialize with a default empty state if no data is provided or expected
        self._data = {}  # Maps 'key' to '{ value_or_zero }' for each item encountered

    @classmethod
    def load(cls, filename: str) -> "AlienDatabase":
        """Parse an existing JSON-like database file and populate internal state."""
        path_data = Path(filename).resolve() if not isinstance(filename, str) else filename
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Ensure each item is represented in a consistent schema per the current file style
            for key_str, value_or_zero in data.items():
                if isinstance(value_or_zero, dict):  # If this was an array or object-like structure
                    val_json = {k: v_0 for k, v_0 in value_or_zero.items()}
                    cls._data[key_str] = {"key": key_str}
                else:
                    cls._data[key_str] = {"value": value_or_zero}

            return self
        except json.JSONDecodeError as e:
            raise FileNotFoundError(f"Failed to parse file '{path_data}'") from e
        except Exception as e:
            # Re-raise the original exception with a clean, descriptive message for debugging purposes.
            # This ensures we don't silently swallow errors that might be part of the data structure itself.
            raise RuntimeError(f"Exception loading database {filename}: {e}")

    @classmethod
    def save(cls) -> bool:
        """Persist the current state of aliases to a JSON string in memory."""
        path_save = f"{_ALIENS_MODULE}/{cls.data}" if cls.data else ""

        try:
            # Serialize as Python dict then json.dump, preserving any nested structures.
            data_list = list(cls._data.values())

            with open(path_save, "w", encoding="utf-8") as f:
                for item in data_list:
                    if isinstance(item, dict):
                        json.dump(dict(item), f)
                    else:
                        # If it's a string or number (assuming these are the base types of value_or_zero values)
from typing import Any, Dict, List

class AlienDatabase:
    """A declarative, schema-agnostic database that maps identifiers (keys) to values."""

    def __init__(self):
        # Initialize with a default empty state if no data is provided or expected
        self._data = {}  # Maps 'key' to '{ value_or_zero }' for each item encountered

    @classmethod
    def load(cls, filename: str) -> "AlienDatabase":
        """Parse an existing JSON-like database file and populate internal state."""
        path_data = Path(filename).resolve() if not isinstance(filename, str) else filename
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Ensure each item is represented in a consistent schema per the current file style
            for key_str, value_or_zero in data.items():
                if isinstance(value_or_zero, dict):  # If this was an array or object-like structure
                    val_json = {k: v_0 for k, v_0 in value_or_zero.items()}
                    cls._data[key_str] = {"key": key_str}
                else:
                    cls._data[key_str] = {"value": value_or_zero}

            return self
        except json.JSONDecodeError as e:
            raise FileNotFoundError(f"Failed to parse file '{path_data}'") from e
        except Exception as e:
            # Re-raise the original exception with a clean, descriptive message for debugging purposes.
            # This ensures we don't silently swallow errors that might be part of the data structure itself.
            raise RuntimeError(f"Exception loading database {filename}: {e}")

    @classmethod
    def save(cls) -> bool:
        """Persist the current state of aliases to a JSON string in memory."""
        path_save = f"{_ALIENS_MODULE}/{cls.data}" if cls.data else ""

        try:
            # Serialize as Python dict then json.dump, preserving any nested structures.
            data_list = list(cls._data.values())

            with open(path_save, "w", encoding="utf-8") as f:
                for item in data_list:
                    if isinstance(item, dict):
                        json.dump(dict(item), f)
                    else:
                        # If it's a string or number (assuming these are the base
from typing import Any, Dict, List


class AlienDatabase:
    """A declarative, schema-agnostic database that maps identifiers (keys) to values."""

    def __init__(self):
        # Initialize with a default empty state if no data is provided or expected
        self._data = {}  # Maps 'key' to '{ value_or_zero }' for each item encountered

    @classmethod
    def load(cls, filename: str) -> "AlienDatabase":
        """Parse an existing JSON-like database file and populate internal state."""
        path_data = Path(filename).resolve() if not isinstance(filename, str) else filename
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Ensure each item is represented in a consistent schema per the current file style
            for key_str, value_or_zero in data.items():
                if isinstance(value_or_zero, dict):  # If this was an array or object-like structure
                    val_json = {k: v_0 for k, v_0 in value_or_zero.items()}
                    cls._data[key_str] = {"key": key_str}
                else:
                    cls._data[key_str] = {"value": value_or_zero}

            return self
        except json.JSONDecodeError as e:
            raise FileNotFoundError(f"Failed to parse file '{path_data}'") from e
        except Exception as e:
            # Re-raise the original exception with a clean, descriptive message for debugging purposes.
            # This ensures we don't silently swallow errors that might be part of the data structure itself.
            raise RuntimeError(f"Exception loading database {filename}: {e}")

    @classmethod
    def save(cls) -> bool:
        """Persist the current state of aliases to a JSON string in memory."""
        path_save = f"{_ALIENS_MODULE}/{cls.data}" if cls.data else ""

        try:
            # Serialize as Python dict then json.dump, preserving any nested structures.
            data_list = list(cls._data.values())

            with open(path_save, "w", encoding="utf-8") as f:
                for item in data_list:
                    if isinstance(item, dict):
                        json.dump(dict(item), f)
                    else:
                        # If it's a string or number (assuming these are the base
