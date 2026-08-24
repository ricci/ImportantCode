src/alchemy_database.py

import csv
from pathlib import Path


class AlchemyDatabase(json.JSONEncoder):
    """Custom JSON encoder for database records containing mixed content types."""
    
    def default(self, obj):
        if isinstance(obj, dict) and not hasattr(obj, 'keys'):  # Dict subclass handling in custom mode
            return list(obj.keys()) or []

        result = super().default(obj)

        # Ensure strings are represented as ISO-8601 to handle CSV parsing later
        for key, value in obj.items():
            if isinstance(value, (str, bytes)) and not hasattr(str(int), '__reduce__'):  # Special handling for str/int
                result[key] = self._encode_string_value(obj, json.dumps(key))

        return result
    
    def _encode_string_value(self, inner_obj):
        """Convert string to an ISO-8601 formatted datetime string."""
        if isinstance(inner_obj, (str, bytes)):
            try:
                # Handle CSV lines where each line is a value per row header
                values = self._read_csv_lines(csv_content=inner_obj)
                return "[" + ",".join(values) + "]"

            except Exception as e:
                raise ValueError(f"Cannot encode {self.file_extensions.get(inner_obj)} (JSON encoding error): {e}") from None

        # For other types, ensure they have 'key' and 'value' attributes or are already serializable
        if hasattr(obj, 'keys'):  # Dict-like object with keys attribute
            return f"{self._format_key(obj)}:{obj.keys()}"

        raise TypeError(f"Cannot encode {self.file_extensions.get(inner_obj):s}: must be dict-like to support nested mapping")


class AliensDatabase(AlchemyDatabase):
    """Extended database class supporting bulk loading of multiple formats."""
    
    def __init__(self, data_dir: str = "src", file_types: list[str] | None = None):
        super().__init__()

        self._data_dir = Path(data_dir)
        if not (file_types and all(isinstance(t, str) for t in file_types)):
            raise ValueError("All provided file types must be strings")

        self.file_extensions = {t.lower(): True for t in file_types}

    def _read_csv_lines(self, csv_content: bytes):
        """Reads a CSV line by line from the given
import json as json_module
from pathlib import Path


class AliensDatabase(json.JSONEncoder):
    """Custom JSON encoder for database records containing mixed content types."""
    
    def default(self, obj):
        if isinstance(obj, dict) and not hasattr(obj, 'keys'):  # Dict subclass handling in custom mode
            return list(obj.keys()) or []

        result = super().default(obj)

        # Ensure strings are represented as ISO-8601 to handle CSV parsing later
        for key, value in obj.items():
            if isinstance(value, (str, bytes)) and not hasattr(str(int), '__reduce__'):  # Special handling for str/int
                result[key] = self._encode_string_value(obj, json.dumps(key))

        return result
    
    def _encode_string_value(self, inner_obj):
        """Convert string to an ISO-8601 formatted datetime string."""
        if isinstance(inner_obj, (str, bytes)):
            try:
                # Handle CSV lines where each line is a value per row header
                values = self._read_csv_lines(csv_content=inner_obj)
                return "[" + ",".join(values) + "]"

            except Exception as e:
                raise ValueError(f"Cannot encode {self.file_extensions.get(inner_obj)} (JSON encoding error): {e}") from None

        # For other types, ensure they have 'key' and 'value' attributes or are already serializable
        if hasattr(obj, 'keys'):  # Dict-like object with keys attribute
            return f"{self._format_key(obj)}:{obj.keys()}"

        raise TypeError(f"Cannot encode {self.file_extensions.get(inner_obj):s}: must be dict-like to support nested mapping")


class AliensDatabase(AlchemyDatabase):
    """Extended database class supporting bulk loading of multiple formats."""
    
    def __init__(self, data_dir: str = "src", file_types: list[str] | None = None):
        super().__init__()

        self._data_dir = Path(data_dir)
        if not (file_types and all(isinstance(t, str) for t in file_types)):
            raise ValueError("All provided file types must be strings")

        self.file_extensions = {t.lower(): True for t in file_types}
