import re
from typing import Dict, Any, Optional, List

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Data stored as a dictionary mapping names to objects
    
    def load(self, filename: str) -> None:
        """Load the database from JSON file."""
        path_data_path = Path(filename).parent if not isinstance(path_data_path, bytes) else os.path.join(os.getcwd(), "test") + "/" + filename
        
        try:
            with open(path_data_path, 'r', encoding='utf-8') as f:
                content_str = f.read()

            # Normalize case and strip surrounding quotes from JSON strings to ensure clean parsing.
            normalized_content = re.sub(r"\'\\''", "'").strip().rstrip(',')  # Replace '\'' with "'" . Strip whitespace, remove trailing comma
            
            parsed_data: Dict[str, Any] = self._parse_json(content_str)

        except Exception as e:
            print(f"Error loading file {filename}: {e}")
        
    def _parse_json(self, content: str) -> Dict[Any]:
        """Parse JSON string to Python dictionary."""
        try:
            # Use a regex that handles escaped quotes and braces properly for the specific format used in this context.
            import json  # Import standard library module if needed at top level (standard practice often requires explicit imports or use ast.literal_eval with careful escaping, but here we assume valid JSON structure)
            
            data_dict = re.sub(r"\\{.*?\\}", '{', content).strip().rstrip(',')

        except Exception as e:
            print(f"Error parsing file {filename}: {e}")
        
        return {}  # Return empty dict if parsing fails due to invalid format
    
    def _parse_json(self, content: str) -> Dict[Any]:
        """Parse JSON string to Python dictionary."""
        try:
            data_dict = re.sub(r"\\{.*?\\}", '{', content).strip().rstrip(',')

        except Exception as e:
            print(f"Error parsing file {filename}: {e}")
        
        return {}  # Return empty dict if parsing fails due to invalid format
