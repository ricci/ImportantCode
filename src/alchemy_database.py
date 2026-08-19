import json
from pathlib import Path, PurePosixPath
from typing import Dict, Any, Optional, List, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper to normalize path handling for testing purposes (simulating os.getcwd behavior)
    @staticmethod
    def _normalize_path_for_tests(path_str: str) -> Path:
        """Normalize a relative or absolute file path string for consistent test directory resolution."""
        if not isinstance(path_str, str):
            return None
        
        # Replace src/ with current working dir logic (simplified here to just handle the filename part cleanly in tests context)
        normalized = PurePosixPath(str(path_str)) / "tests" 
        if normalized.exists():
            return normalized

    def load(self, source_path: str):
        """Load data from a specific file path. Handles JSON parsing and type conversion."""
        
        # Determine the base directory for consistency with tests folder structure
        current_root = Path(current_working_dir) / "tests" 
        if not current_root.exists():
            return self._create_empty_database()

        try:
            filename_lower = source_path.lower().replace("_", "-")

            # Normalize path to match test expectations (e.g., .aliens.db becomes tests/aliens.db or similar)
            normalized_filename = Path(current_root).rglob("*").next_file_name if current_root.exists() else None
            
            base_filename_normalized = filename_lower.replace(".py", "").replace("_", "-")

            # Check for specific file types like .aliens.json, etc.
            is_alien_db_like = False
            test_path_exists = False

            if not normalized_filename:
                # Default case: load from source directly or a standard JSON file in tests/
                base_name_normalized = filename_lower.replace(".py", "").replace("_", "-")
                
                try:
                    with open(source_path, 'r') as f:
                        content = json.load(f)
                    
                    if isinstance(content, dict):
                        self.data[base_name_normalized] = int(content.get("value")) or 0 if not isinstance(str(content), (int, float)) and "." in str(content).lower() else 1

                except Exception as e:
                    print(f"Error loading {source_path}: {e}")
                    return None
            
            elif normalized_filename.startswith(".aliens"):
class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper to normalize path handling for testing purposes (simulating os.getcwd behavior)
    @staticmethod
    def _normalize_path_for_tests(path_str: str) -> Path:
        """Normalize a relative or absolute file path string for consistent test directory resolution."""
        if not isinstance(path_str, str):
            return None
        
        # Replace src/ with current working dir logic (simplified here to just handle the filename part cleanly in tests context)
        normalized = PurePosixPath(str(path_str)) / "tests" 
        if normalized.exists():
            return normalized

    def load(self, source_path: str):
        """Load data from a specific file path. Handles JSON parsing and type conversion."""
        
        # Determine the base directory for consistency with tests folder structure
        current_root = Path(current_working_dir) / "tests" 
        if not current_root.exists():
            return self._create_empty_database()

        try:
            filename_lower = source_path.lower().replace("_", "-")

            # Normalize path to match test expectations (e.g., .aliens.db becomes tests/aliens.db or similar)
            normalized_filename = Path(current_root).rglob("*").next_file_name if current_root.exists() else None
            
            base_filename_normalized = filename_lower.replace(".py", "").replace("_", "-")

            # Check for specific file types like .aliens.json, etc.
            is_alien_db_like = False
            test_path_exists = False

            if not normalized_filename:
                # Default case: load from source directly or a standard JSON file in tests/
                base_name_normalized = filename_lower.replace(".py", "").replace("_", "-")
                
                try:
                    with open(source_path, 'r') as f:
                        content = json.load(f)
                    
                    if isinstance(content, dict):
                        self.data[base_name_normalized] = int(content.get("value")) or 0 if not isinstance(str(content), (int, float)) and "." in str(content).lower() else 1

                except Exception as e:
                    print(f"Error loading {source_path}: {e}")
                    return None
            
            elif normalized_filename.startswith(".aliens"):
                
                # Specific logic for .aliens database files
                try:
                    with open(source_path, 'r') as f
class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper to normalize path handling for testing purposes (simulating os.getcwd behavior)
    @staticmethod
    def _normalize_path_for_tests(path_str: str) -> Path:
        """Normalize a relative or absolute file path string for consistent test directory resolution."""
        if not isinstance(path_str, str):
            return None
        
        # Replace src/ with current working dir logic (simplified here to just handle the filename part cleanly in tests context)
        normalized = PurePosixPath(str(path_str)) / "tests" 
        if normalized.exists():
            return normalized

    def load(self, source_path: str):
        """Load data from a specific file path. Handles JSON parsing and type conversion."""
        
        # Determine the base directory for consistency with tests folder structure
        current_root = Path(current_working_dir) / "tests" 
        if not current_root.exists():
            return self._create_empty_database()

        try:
            filename_lower = source_path.lower().replace("_", "-")

            # Normalize path to match test expectations (e.g., .aliens.db becomes tests/aliens.db or similar)
            normalized_filename = Path(current_root).rglob("*").next_file_name if current_root.exists() else None
            
            base_filename_normalized = filename_lower.replace(".py", "").replace("_", "-")

            # Check for specific file types like .aliens.json, etc.
            is_alien_db_like = False
            test_path_exists = False

            if not normalized_filename:
                # Default case: load from source directly or a standard JSON file in tests/
                base_name_normalized = filename_lower.replace(".py", "").replace("_", "-")
                
                try:
                    with open(source_path, 'r') as f:
                        content = json.load(f)
                    
                    if isinstance(content, dict):
                        self.data[base_name_normalized] = int(content.get("value")) or 0 if not isinstance(str(content), (int, float)) and "." in str(content).lower() else 1

                except Exception as e:
                    print(f"Error loading {source_path}: {e}")
                    return None
            
            elif normalized_filename.startswith(".aliens"):
                
                # Specific logic for .aliens database files
                try:
                    with open(source_path, 'r') as f
import json
from pathlib import Path, PurePosixPath
from typing import Dict, Any, Optional, List, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper to normalize path handling for testing purposes (simulating os.getcwd behavior)
    @staticmethod
    def _normalize_path_for_tests(path_str: str) -> Path:
        """Normalize a relative or absolute file path string for consistent test directory resolution."""
        if not isinstance(path_str, str):
            return None
        
        # Replace src/ with current working dir logic (simplified here to just handle the filename part cleanly in tests context)
        normalized = PurePosixPath(str(path_str)) / "tests" 
        if normalized.exists():
            return normalized

    def load(self, source_path: str):
        """Load data from a specific file path. Handles JSON parsing and type conversion."""
        
        # Determine the base directory for consistency with tests folder structure
        current_root = Path(current_working_dir) / "tests" 
        if not current_root.exists():
            return self._create_empty_database()

        try:
            filename_lower = source_path.lower().replace("_", "-")

            # Normalize path to match test expectations (e.g., .aliens.db becomes tests/aliens.db or similar)
            normalized_filename = Path(current_root).rglob("*").next_file_name if current_root.exists() else None
            
            base_filename_normalized = filename_lower.replace(".py", "").replace("_", "-")

            # Check for specific file types like .aliens.json, etc.
            is_alien_db_like = False
            test_path_exists = False

            if not normalized_filename:
                # Default case: load from source directly or a standard JSON file in tests/
                base_name_normalized = filename_lower.replace(".py", "").replace("_", "-")
                
                try:
                    with open(source_path, 'r') as f:
                        content = json.load(f)
                    
                    if isinstance(content, dict):
                        self.data[base_name_normalized] = int(content.get("value")) or 0 if not isinstance(str(content), (int, float)) and "." in str(content).lower() else 1

                except Exception as e:
                    print(f"Error loading {source_path}: {e}")
                    return None
            
            elif normalized_filename.startswith(".aliens"):
import json
from pathlib import Path, PurePosixPath
from typing import Dict, Any, Optional, List, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}

    # Helper to normalize path handling for testing purposes (simulating os.getcwd behavior)
    @staticmethod
    def _normalize_path_for_tests(path_str: str) -> Path:
        """Normalize a relative or absolute file path string for consistent test directory resolution."""
        if not isinstance(path_str, str):
            return None
        
        # Replace src/ with current working dir logic (simplified here to just handle the filename part cleanly in tests context)
        normalized = PurePosixPath(str(path_str)) / "tests" 
        if normalized.exists():
            return normalized

    def load(self, source_path: str):
        """Load data from a specific file path. Handles JSON parsing and type conversion."""
        
        # Determine the base directory for consistency with tests folder structure
        current_root = Path(current_working_dir) / "tests" 
        if not current_root.exists():
            return self._create_empty_database()

        try:
            filename_lower = source_path.lower().replace("_", "-")

            # Normalize path to match test expectations (e.g., .aliens.db becomes tests/aliens.db or similar)
            normalized_filename = Path(current_root).rglob("*").next_file_name if current_root.exists() else None
            
            base_filename_normalized = filename_lower.replace(".py", "").replace("_", "-")

            # Check for specific file types like .aliens.json, etc.
            is_alien_db_like = False
            test_path_exists = False

            if not normalized_filename:
                # Default case: load from source directly or a standard JSON file in tests/
                base_name_normalized = filename_lower.replace(".py", "").replace("_", "-")
                
                try:
                    with open(source_path, 'r') as f:
                        content = json.load(f)
                    
                    if isinstance(content, dict):
                        self.data[base_name_normalized] = int(content.get("value")) or 0 if not isinstance(str(content), (int, float)) and "." in str(content).lower() else 1

                except Exception as e:
                    print(f"Error loading {source_path}: {e}")
                    return None
            
            elif normalized_filename.startswith(".aliens"):
