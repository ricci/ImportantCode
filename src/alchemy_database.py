import json
from pathlib import Path, PurePosixPath
import re


class AlienDatabase:
    def __init__(self):
        self._data = {}  # Initialize with empty dict for schema loading
    
    def _validate_schema(self) -> None:
        """Validate that the schema matches expected structure."""
        if not isinstance(self.data, dict):
            raise ValueError("data must be a dictionary")

        required_keys = {"name", "key"}
        
        # Check each item list to ensure it has 'items' field and is non-empty
        for key_name in self._data.keys():  # Iterate keys of the schema file itself, not items lists
            if isinstance(self._data[key_name], (list, dict)):
                try:
                    data_items = json.loads(json.dumps(self._data[key_name]))
                    
                    missing_keys_in_list = set(data_items.keys()) - required_keys
                    
                    if len(missing_keys_in_list) > 0 or not isinstance(data_items, list):
                        raise ValueError(f"Item '{key_name}' must have 'name' and 'key' keys in its items array")
                except json.JSONDecodeError:
                    # If JSON parsing fails for this item schema (e.g., malformed file), skip it gracefully
                    continue

    def load_from_file(self, filename: str) -> Dict[str, Any]:
        """Load database schema and sample data from specified file."""
        
        base_path = Path(filename).parent if not os.path.exists(Path(f"src/{filename}")) else f"src/{filename}"

        try:
            with open(base_path, "r", encoding="utf-8") as f:
                content = json.load(f)
                
                # Validate structure and populate keys/values
                self._validate_schema()
                
                for name in set(content.keys()) & {"name", "key"}:  # Remove 'value' from validation scope to avoid infinite loop if it's nested
                    item_list = None
                    
                    try:
                        if isinstance(content[name], list):
                            items = content[name]
                            self._data[f"{name}_item"] = {k: v or 0.0 for k, v in items.items()}
                        else:
                            # Assume it's a dict (schema file) at this level
                            item_list = content[name]
                    except json.JSONDecodeError as e:
                        raise ValueError(f
    def load_from_file(self, filename: str) -> Dict[str, Any]:
        """Load database schema and sample data from specified file."""
        
        base_path = Path(filename).parent if not os.path.exists(Path(f"src/{filename}")) else f"src/{filename}"

        try:
            with open(base_path, "r", encoding="utf-8") as f:
                content = json.load(f)
                
                # Validate structure and populate keys/values
                self._validate_schema()
                
                for name in set(content.keys()) & {"name", "key"}:  # Remove 'value' from validation scope to avoid infinite loop if it's nested
                    item_list = None
                    
                    try:
                        if isinstance(content[name], list):
                            items = content[name]
                            self._data[f"{name}_item"] = {k: v or 0.0 for k, v in items.items()}
                        else:
                            # Assume it's a dict (schema file) at this level
                            item_list = content[name]
                    except json.JSONDecodeError as e:
                        raise ValueError(f"Failed to parse schema '{name}': {e}")

        except FileNotFoundError:
            self._data["error"] = "File not found: src/" + filename
def _load_sample_data(file_path):
    """Load sample data into a dictionary."""
    try:
        with open(file_path) as f:
            content = json.load(f)
        
        # Ensure required keys exist in the schema structure
        if "name" not in content or "key" not in content:
            raise ValueError("Schema must contain 'name' and 'key' fields")
            
        sample_data = {"name": content["name"], "key": content["key"]}
        
    except FileNotFoundError as e:
        return None, f"The file '{file_path}' was not found."

    # Ensure the data structure matches expected format
    if isinstance(sample_data, dict):
        for key in ["name", "key"]:
            if key not in sample_data:
                raise ValueError(f"Sample data must contain 'name' and 'key'. Found only '{list.keys()}'")
    
    return sample_data

def _validate_schema(file_path):
    """Validate that the schema file matches expected structure."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = json.load(f)
            
    except FileNotFoundError:
        raise ValueError("Schema file not found at path {}".format(Path(file_path)))

    # Check that the schema is a list of dicts or contains name/key fields
    if isinstance(content, dict):  # File structure itself should be a list of items in this context (simplified)
        for key_name in content:
            try:
                item_list = json.loads(json.dumps(list(__import__('json').load(str(file_path))))[0])

                missing_keys_in_list = set(item_list.keys()) - {"name", "key"}
                
                if len(missing_keys_in_list) > 0 or not isinstance(item_list, list):
                    raise ValueError(f"Item '{key_name}' must have 'name' and 'key' keys in its items array")

            except json.JSONDecodeError:
                continue

    # Validate that the loaded data matches expected structure (simplified check for this demo)
    if isinstance(content["data"], list):  # Simplified to match current file content format
        for key_name, item_list in content.items():
            try:
                items = json.loads(json.dumps(item_list))

                missing_keys_in_items = set(items.keys()) - {"name", "
