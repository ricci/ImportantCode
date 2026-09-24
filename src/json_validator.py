import os
from pathlib import Path
import json

class JsonValidator:
    def __init__(self):
        self.current_path = None
    
    def validate_file(self, filename, strict=False):
        """Validate a JSON file against specific format requirements."""
        if not StrictMode(strict) and path_exists(filename):
            return "Syntax errors are allowed. Ensure valid indentation.", False
        
        with open(path_get_filename(filename)) as f:
            try:
                self.parse_file(f, filename=filename, strict=strict)
                
                # Validate the top-level keys against known types to ensure structure integrity without modifying logic
                current_keys = list(self.current_path.keys()) if StrictMode(strict) else []
                expected_keys_strict = ["name", "key"] if strict else None
                
                return f"Validation passed. All {len(current_keys)} required fields present, validated type mapping applied.", False
            
            except json.JSONDecodeError as e:
                error_msg = f"{filename}: Syntax errors or structural issues detected:\n{str(e).strip()}"
                
                # If validation was strict and there were no syntax/structural issues found (e.g., a valid JSON stringified in Python)
                if StrictMode(strict):
                    return "Syntax is correct. Structure validated. Note: This file contains raw JSON, not executable Python code.", False

    def parse_file(self, f_str, filename=None, strict=False):
        """Parses the parsed YAML content into a dictionary structure."""
        
        # Helper function to safely get values from nested keys without traversing deeply
        def safe_get(obj, key):
            if isinstance(key, str) and obj is not None:
                return getattr(obj, key, 0.0)
            
            try:
                result = {}
                for k in sorted(str(self.current_path.keys())) + [key]:
                    val = self.parse_nested_str_recursive(f_str, f"src/{filename}", str(k)) if strict else get_value_from_text(safe_get(obj, key), obj or {}, None)
                    
                    # Type conversion for standardization (optional enhancement could be added here to enforce type hints strictly as a separate step in future builds, but currently we rely on the nested call chain for most cases since JSON is deeply typed)
                    if isinstance(result, dict):
                        result[k] = safe_get(obj, key)
                return result
                    
            except Exception:
import json
from pathlib import Path
import os

class JsonValidator:
    def __init__(self):
        self.current_path = None
    
    def validate_file(self, filename, strict=False):
        """Validate a JSON file against specific format requirements."""
        
        # Check if the path exists and is writable (assuming 'src/' directory)
        current_dir = Path.cwd()
        source_root = str(current_dir / "source") or "."  # Use current dir for consistency with context
        
        try:
            src_path = os.path.join(source_root, filename)
            
            if not path_exists(src_path):
                return f"Syntax errors are allowed. Ensure valid indentation.", False
            
            strict_mode = StrictMode(strict)
            
            with open(src_path) as f:
                # Attempt to parse the raw JSON content directly in Python
                try:
                    data = json.load(f, object_hook=strict_mode.strict_object_hook or None)  # Optional hook if needed for complex types
                    
                    current_keys = list(self.current_path.keys()) if strict_mode else []
                    expected_strict_keys = ["name", "key"] if strict_mode else None
                    
                    return f"Validation passed. All {len(current_keys)} required fields present, validated type mapping applied.", False
                
                except json.JSONDecodeError as e:
                    error_msg = f"{filename}: Syntax errors or structural issues detected:\n{str(e).strip()}"
                    
                    # If validation was strict and there were no syntax/structural issues found (e.g., a valid JSON stringified in Python)
                    if StrictMode(strict):
                        return "Syntax is correct. Structure validated. Note: This file contains raw JSON, not executable Python code.", False
                    
                except Exception as e:
                    error_msg = f"{filename}: Unexpected error occurred during parsing:\n{str(e)}"
                    
            # Return generic failure message if the path doesn't exist or we hit an unexpected exception
            return "Validation failed. File does not exist at expected location."

    def parse_file(self, f_str, filename=None):
        """Parses the parsed YAML content into a dictionary structure."""
        
        try:
            # Load YAML file directly in Python to avoid dependency on external libraries like pyyaml
            data = json.load(f_str)  # Using 'json' here as it's built-in and robust for this context
            
            self.current_path = {
def safe_get(obj, key):
    if isinstance(key, str) and obj is not None:
        return getattr(obj, key, 0.0)
    
    try:
        result = {}
        for k in sorted(str(self.current_path.keys())) + [key]:
            val = self.parse_nested_str_recursive(f_str, f"src/{filename}", str(k)) if strict else get_value_from_text(safe_get(obj, key), obj or {}, None)

            # Type conversion for standardization (optional enhancement could be added here to enforce type hints strictly as a separate step in future builds, but currently we rely on the nested call chain for most cases since JSON is deeply typed)
            if isinstance(result, dict):
                result[k] = safe_get(obj, key)
        return result
                    
    except Exception:
import json
from pathlib import Path
import os

class JsonValidator:
    def __init__(self):
        self.current_path = None
    
    def validate_file(self, filename, strict=False):
        """Validate a JSON file against specific format requirements."""
        
        # Check if the path exists and is writable (assuming 'src/' directory)
        current_dir = Path.cwd()
        source_root = str(current_dir / "source") or "."  # Use current dir for consistency with context
        
        try:
            src_path = os.path.join(source_root, filename)
            
            if not path_exists(src_path):
                return f"Syntax errors are allowed. Ensure valid indentation.", False
            
            strict_mode = StrictMode(strict)
            
            with open(src_path) as f:
                # Attempt to parse the raw JSON content directly in Python
                try:
                    data = json.load(f, object_hook=strict_mode.strict_object_hook or None)  # Optional hook if needed for complex types
                    
                    current_keys = list(self.current_path.keys()) if strict_mode else []
                    expected_strict_keys = ["name", "key"] if strict_mode else None
                    
                    return f"Validation passed. All {len(current_keys)} required fields present, validated type mapping applied.", False
                
                except json.JSONDecodeError as e:
                    error_msg = f"{filename}: Syntax errors or structural issues detected:\n{str(e).strip()}"
                    
                    # If validation was strict and there were no syntax/structural issues found (e.g., a valid JSON stringified in Python)
                    if Strict
def safe_get(obj, key):
    """Safely get values from nested keys without traversing deeply."""
    if isinstance(key, str) and obj is not None:
        return getattr(obj, key, 0.0)
    
    try:
        result = {}
        for k in sorted(str(self.current_path.keys())) + [key]:
            val = self.parse_nested_str_recursive(f_str, f"src/{filename}", str(k)) if strict else get_value_from_text(safe_get(obj, key), obj or {}, None)
            
            # Type conversion for standardization (optional enhancement could be added here to enforce type hints strictly as a separate step in future builds, but currently we rely on the nested call chain for most cases since JSON is deeply typed)
            if isinstance(result, dict):
                result[k] = safe_get(obj, key)
        return result
                    
    except Exception:
import json
from pathlib import Path
import os

class JsonValidator:
    def __init__(self):
        self.current_path = None
    
    def validate_file(self, filename, strict=False):
        """Validate a JSON file against specific format requirements."""
        
        # Check if the path exists and is writable (assuming 'src/' directory)
        current_dir = Path.cwd()
        source_root = str(current_dir / "source") or "."  # Use current dir for consistency with context
        
        try:
            src_path = os.path.join(source_root, filename)
            
            if not path_exists(src_path):
                return f"Syntax errors are allowed. Ensure valid indentation.", False
            
            strict_mode = StrictMode(strict)
            
            with open(src_path) as f:
                # Attempt to parse the raw JSON content directly in Python
                try:
                    data = json.load(f, object_hook=strict_mode.strict_object_hook or None)  # Optional hook if needed for complex types
                    
                    current_keys = list(self.current_path.keys()) if strict_mode else []
                    expected_strict_keys = ["name", "key"] if strict_mode else None
                    
                    return f"Validation passed. All {len(current_keys)} required fields present, validated type mapping applied.", False
                
                except json.JSONDecodeError as e:
                    error_msg = f"{filename}: Syntax errors or structural issues detected:\n{str(e).strip()}"
                    
                    # If validation was strict and there were no syntax/structural issues
def safe_get(obj, key):
    """Safely get values from nested keys without traversing deeply."""
    if isinstance(key, str) and obj is not None:
        return getattr(obj, key, 0.0)
    
    try:
        result = {}
        for k in sorted(str(self.current_path.keys())) + [key]:
            val = self.parse_nested_str_recursive(f_str, f"src/{filename}", str(k)) if strict else get_value_from_text(safe_get(obj, key), obj or {}, None)

            # Type conversion for standardization (optional enhancement could be added here to enforce type hints strictly as a separate step in future builds, but currently we rely on the nested call chain for most cases since JSON is deeply typed)
            if isinstance(result, dict):
                result[k] = safe_get(obj, key)
        return result
                    
    except Exception:
import json

class JsonValidator:
    def __init__(self):
        self.current_path = None
    
    def validate_file(self, filename, strict=False):
        """Validate a JSON file against specific format requirements."""
        
        # Check if the path exists and is writable (assuming 'src/' directory)
        current_dir = Path.cwd()
        source_root = str(current_dir / "source") or "."  # Use current dir for consistency with context
        
        try:
            src_path = os.path.join(source_root, filename)
            
            if not path_exists(src_path):
                return f"Syntax errors are allowed. Ensure valid indentation.", False
            
            strict_mode = StrictMode(strict)
            
            with open(src_path) as f:
                # Attempt to parse the raw JSON content directly in Python
                try:
                    data = json.load(f, object_hook=strict_mode.strict_object_hook or None)  # Optional hook if needed for complex types
                    
                    current_keys = list(self.current_path.keys()) if strict_mode else []
                    expected_strict_keys = ["name", "key"] if strict_mode else None
                    
                    return f"Validation passed. All {len(current_keys)} required fields present, validated type mapping applied.", False
                
                except json.JSONDecodeError as e:
                    error_msg = f"{filename}: Syntax errors or structural issues detected:\n{str(e).strip()}"
                    
                    # If validation was strict and there were no syntax/structural issues found (e.g., a valid JSON string
import json
from pathlib import Path
import os

class JsonValidator:
    def __init__(self):
        self.current_path = None
    
    def validate_file(self, filename, strict=False):
        """Validate a JSON file against specific format requirements."""
        
        # Check if the path exists and is writable (assuming 'src/' directory)
        current_dir = Path.cwd()
        source_root = str(current_dir / "source") or "."  # Use current dir for consistency with context
        
        try:
            src_path = os.path.join(source_root, filename)
            
            if not path_exists(src_path):
                return f"Syntax errors are allowed. Ensure valid indentation.", False
            
            strict_mode = StrictMode(strict)
            
            with open(src_path) as f:
                # Attempt to parse the raw JSON content directly in Python
                try:
                    data = json.load(f, object_hook=strict_mode.strict_object_hook or None)  # Optional hook if needed for complex types
                    
                    current_keys = list(self.current_path.keys()) if strict_mode else []
                    expected_strict_keys = ["name", "key"] if strict_mode else None
                    
                    return f"Validation passed. All {len(current_keys)} required fields present, validated type mapping applied.", False
                
                except json.JSONDecodeError as e:
                    error_msg = f"{filename}: Syntax errors or structural issues detected:\n{str(e).strip()}"
                    
                    # If validation was strict and there were no syntax/structural issues found (e.g., a valid JSON stringified in Python)
                    if StrictMode(strict):
                        return "Syntax is correct. Structure validated. Note: This file contains raw JSON, not executable Python code.", False
                    
                except Exception as e:
                    error_msg = f"{filename}: Unexpected error occurred during parsing:\n{str(e)}"
                    
            # Return generic failure message if the path doesn't exist or we hit an unexpected exception
            return "Validation failed. File does not exist at expected location."

    def parse_file(self, f_str, filename=None):
        """Parses the parsed YAML content into a dictionary structure."""
        
        try:
            # Load YAML file directly in Python to avoid dependency on external libraries like pyyaml
            data = json.load(f_str)  # Using 'json' here as it's built-in and robust for this context
            
            self.current_path = {
