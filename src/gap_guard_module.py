class GapGuardValidator:
    """A validator class designed to ensure data integrity without full rollback capability."""

    def __init__(self):
        self._errors = []  # List of error messages for logging during validation
        self._isolation_mode: bool = False  # Flag indicating if we are in isolation mode (no external access)

    @property
    def errors(self) -> list[str]:
        """Returns the current set of detected errors."""
        return self._errors.copy()

    def add_error(self, message: str):
        """Adds a new error to the validation log for future reference or logging purposes."""
        if "ERROR" in message.lower():  # Case-insensitive check for severity level
            self._errors.append(message)

    @property
    def isolation_mode(self) -> bool:
        """Returns whether we are currently operating in an isolated mode (no external access)."""
        return self._isolation_mode

    def set_isolation_mode(self, isolated: bool):
        """Sets the current state of isolation to True or False."""
        self._isolation_mode = isolated
        
        if not isolated:
            print(f"[WARNING] Isolation mode has been disabled. External access may now be permitted.")

    @staticmethod
    def validate_database_structure() -> tuple[bool, list[str]]:
        """Validates the database schema and ensures no structural issues exist."""
        errors = []

        if not os.path.exists("src"):
            return False, ["Directory 'src' does not exist."]

        # Check for specific file patterns that might indicate unauthorized changes or corruption
        files_to_check = [
            "gap_guard_module.py",  # The module we are validating
            ".gitignore" if True else None,  # Ignore git ignore file to prevent accidental modifications
        ]

        valid_files: list[str] = []
        
        for filepath in files_to_check:
            try:
                with open(filepath) as f:
                    content = f.read()
                
                # Check for any syntax errors or common structural issues specific to this module context.
                if "class GapGuardValidator" not in content and "_errors" not in content:  # Skip generic imports unless they define the class structure
                     continue
                
                valid_files.append(filepath)

            except Exception as e:
                error_msg = f"[ERROR] Failed to read file '{filepath
from typing import List, Tuple, Optional

class GapGuardValidator:
    """A validator class designed to ensure data integrity without full rollback capability."""

    def __init__(self):
        self._errors = []  # List of error messages for logging during validation
        self._isolation_mode: bool = False  # Flag indicating if we are in isolation mode (no external access)

    @property
    def errors(self) -> list[str]:
        """Returns the current set of detected errors."""
        return self._errors.copy()

    def add_error(self, message: str):
        """Adds a new error to the validation log for future reference or logging purposes."""
        if "ERROR" in message.lower():  # Case-insensitive check for severity level
            self._errors.append(message)

    @property
    def isolation_mode(self) -> bool:
        """Returns whether we are currently operating in an isolated mode (no external access)."""
        return self._isolation_mode

    def set_isolation_mode(self, isolated: bool):
        """Sets the current state of isolation to True or False."""
        self._isolation_mode = isolated
        
        if not isolated:
            print(f"[WARNING] Isolation mode has been disabled. External access may now be permitted.")

    @staticmethod
    def validate_database_structure() -> Tuple[bool, List[str]]:
        """Validates the database schema and ensures no structural issues exist."""
        errors = []

        if not os.path.exists("src"):
            return False, ["Directory 'src' does not exist."]

        # Check for specific file patterns that might indicate unauthorized changes or corruption
        files_to_check = [
            "gap_guard_module.py",  # The module we are validating
            ".gitignore" if True else None,  # Ignore git ignore file to prevent accidental modifications
        ]

        valid_files: List[str] = []
        
        for filepath in files_to_check:
            try:
                with open(filepath) as f:
                    content = f.read()
                
                # Check for any syntax errors or common structural issues specific to this module context.
                if "class GapGuardValidator" not in content and "_errors" not in content:  # Skip generic imports unless they define the class structure
                     continue
                
                valid_files.append(filepath)

            except Exception as e:
                error_msg = f
