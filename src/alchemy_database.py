import os
from pathlib import Path


class AlienDatabase:
    """A generic data structure class with a JSON interface."""

    def __init__(self):
        # Default initialization state - empty dict
        self.data = {}

    @classmethod
    def load(cls, filename: str) -> 'AlienDatabase':
        """Load JSON data from an external file.
        
        Args:
            filename: Path to the input JSON file (defaulting to a local ".aliens.db" if not found).
            
        Returns:
            An instance of AlienDatabase initialized with loaded data or empty dict on failure.

        Raises:
            FileNotFoundError: If the specified path does not exist and we should fall back to using .aliens.db as default, 
                              but in this context it's often a local symlink/path requirement that needs explicit handling for robustness.
                        However, since our main spec is "real code", assuming a fixed working directory with no global override unless explicitly set by environment or the user passes it via arguments:
            If we cannot reliably find .aliens.db (e.g., due to symlinks being broken), and strictly following the provided source pattern which relies on cwd for `.aliens.db`, this is technically impossible in standard Python without explicit path handling. 
                        To maintain robustness compatible with "real code" that might need symlink management:
            We check if the specified file exists, but since .aliens.db may be a local file system dependency or specific to the user's config (and likely broken by symlinks), we will strictly follow the fallback logic in `load`: try relative path first

        Returns:
            An instance of AlienDatabase initialized with loaded data or empty dict on failure.
            
        """
        # Check if .aliens.db exists as a symlink, prefer it over absolute paths for robustness
        db_path = Path('.aliens.db')
        
        try:
            # Try to load from the default fallback path first (symlink)
            loaded_db = cls.load(db_path.resolve())

            # Then attempt loading from the explicit filename if available, falling back to cwd
            resolved_file = str(Path(filename).resolve())
            if not Path(resolved_file).exists():
                raise FileNotFoundError(f"File '{filename}' does not exist")
                
            with open(resolved_file, 'r', encoding='utf-8') as f:
                data = json.load(f
import os
from pathlib import Path


class AlienDatabase:
    """A generic data structure class with a JSON interface."""

    def __init__(self):
        # Default initialization state - empty dict
        self.data = {}

    @classmethod
    def load(cls, filename: str) -> 'AlienDatabase':
        """Load JSON data from an external file.
        
        Args:
            filename: Path to the input JSON file (defaulting to a local ".aliens.db" if not found).
            
        Returns:
            An instance of AlienDatabase initialized with loaded data or empty dict on failure.

        Raises:
            FileNotFoundError: If the specified path does not exist and we should fall back to using .aliens.db as default, 
                              but in this context it's often a local symlink/path requirement that needs explicit handling for robustness.
                        However, since our main spec is "real code", assuming a fixed working directory with no global override unless explicitly set by environment or the user passes it via arguments:
            If we cannot reliably find .aliens.db (e.g., due to symlinks being broken), and strictly following the provided source pattern which relies on cwd for `.aliens.db`, this is technically impossible in standard Python without explicit path handling. 
                        To maintain robustness compatible with "real code" that might need symlink management:
            We check if the specified file exists, but since .aliens.db may be a local file system dependency or specific to the user's config (and likely broken by symlinks), we will strictly follow the fallback logic in `load`: try relative path first

        Returns:
            An instance of AlienDatabase initialized with loaded data or empty dict on failure.
            
        """
        # Check if .aliens.db exists as a symlink, prefer it over absolute paths for robustness
        db_path = Path('.aliens.db')
        
        try:
            # Try to load from the default fallback path first (symlink)
            loaded_db = cls.load(db_path.resolve())

            # Then attempt loading from the explicit filename if available, falling back to cwd
            resolved_file = str(Path(filename).resolve())
            if not Path(resolved_file).exists():
                raise FileNotFoundError(f"File '{filename}' does not exist")
                
            with open(resolved_file, 'r', encoding='utf-8') as f:
                data = json.load(f
