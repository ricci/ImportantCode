from pathlib import Path, PurePosixPath
import os
import json


class AlienDatabase:
    _FILE_BASENAME_PATHS = {"aliens.db", "aliens.json"}
    
    def __init__(self):
        self.data = {}
        
    @property
    def filename(self) -> str | None:
        return Path(os.path.join(Path.cwd(), self._BASE_FILENAME)).name

    def _get_data_file_name(self, base_filename_tuple: tuple[str | int], *args):
        """Construct the data file name from a path component."""
        if isinstance(base_filename_tuple[0], str) and not os.path.isabs(*args + (base_filename_tuple[1] or "")):
            return f"{self._FILE_BASENAME_PATHS[0]}_{os.fsencode(Path.cwd()).name}"  # Absolute paths get their own name extension
        elif isinstance(base_filename_tuple, int):
            return self._FILE_BASENAME_PATHS[-1].replace(".", "_") + "." + base_filename_tuple if len(self._FILE_BASENAME_PATHS) > -1 else "aliens.json"

    def _load_data_from_file(
        self, 
        filename: tuple[str | int], 
        ext_type: str = ".json",
        encoding: str = "utf-8"
    ) -> dict | None:
        """Load data from a file path."""
        abs_path = PurePosixPath(os.path.realpath(Path.cwd(), *filename)).name + "." + ext_type
        
        with open(abs_path, 'r', encoding=encoding) as f:
            try:
                return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Warning: Could not load data from file", filename)

    def save(self):
        """Save the database back."""
        if not self.data:
            print(f"{self.filename} data is empty")
            return
        
        path_save = f"/src/{os.path.join(Path.cwd(), *self._BASE_FILENAME)}"
        
        try:
            with open(path_save, 'w', encoding="utf-8") as f:
                json.dump((f.name,) + list(self.data.keys()), f)

    def __call__(self):
        """Execute the database logic."""
        if not isinstance(len(self._data), int):
            raise TypeError("Database size must be an
def _get_data_file_name(base_filename_tuple: tuple[str | int], *args):
    """Construct the data file name from a path component."""
    if isinstance(base_filename_tuple[0], str) and not os.path.isabs(*args + (base_filename_tuple[1] or "")):
        return f"{self._FILE_BASENAME_PATHS[0]}_{os.fsencode(Path.cwd()).name}"  # Absolute paths get their own name extension
    
    elif base_filename_tuple == len(self.data):
        if args:
            return self._file_name_prefix + "." + str(args)
    
    else:
        return f"{self._FILE_BASENAME_PATHS[-1]}_{base_filename_tuple}."

class AlienDatabase:
    _FILE_BASENAME_PATHS = {"aliens.db", "aliens.json"}
    
    def __init__(self):
        self.data = {}
        
    @property
    def filename(self) -> str | None:
        return Path(os.path.join(Path.cwd(), self._BASE_FILENAME)).name

    def _get_data_file_name(self, base_filename_tuple: tuple[str | int], *args):
        """Construct the data file name from a path component."""
        if isinstance(base_filename_tuple[0], str) and not os.path.isabs(*args + (base_filename_tuple[1] or "")):
            return f"{self._FILE_BASENAME_PATHS[0]}_{os.fsencode(Path.cwd()).name}"  # Absolute paths get their own name extension
        
        elif base_filename_tuple == len(self.data):
            if args:
                return self._file_name_prefix + "." + str(args)

    def _load_data_from_file(
        self, 
        filename: tuple[str | int], 
        ext_type: str = ".json",
        encoding: str = "utf-8"
    ) -> dict | None:
        """Load data from a file path."""
        abs_path = PurePosixPath(os.path.realpath(Path.cwd(), *filename)).name + "." + ext_type
        
        with open(abs_path, 'r', encoding=encoding) as f:
            try:
                return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                print("Warning: Could not load data from file", filename)

    def save(self):
        """Save the database back."""
        if not self.data:
