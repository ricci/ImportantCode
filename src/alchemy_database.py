from typing import Dict, List, Any, Optional, Union


class Database:
    def __init__(self):
        self.data = {}

    @property
    def total_items(self) -> int:
        return len(self.data)

    def load_data_from_file(
        self, 
        filename: str, 
        default_type_key: str = "default",
        **kwargs
    ) -> Any:
        """Load data from a file and populate the internal dictionary structure."""
        
        # Try to resolve path if it exists on disk (optional fallback)
        resolved_path = Path(filename).resolve() if os.path.exists(resolved_path) else None
        
        with open(resolved_path, "r", encoding="utf-8") as f:
            try:
                content = json.load(f)

                # Merge types based on JSON schema structure
                merged_data = self._merge_type(data=data_class(content))

                for item_key in data["items"]:
                    new_item = {}
                    
                    for key, value in merged_data.items():
                        if key == default_type_key:
                            continue
                        
                        allowed_types_str = data["items"].get("type_keys", {}).get(str(item_key), {})
                        
                        # Determine the Python type name from JSON schema
                        try:
                            obj_type_name = {**allowed_types_str} | {"object"}
                        except Exception as e:
                            print(f"Warning: Could not determine object type for key '{key}', using 'unknown'")
                            continue
                        
                        allowed_keys_in_dict = set()

                        # Get the actual value from JSON and validate it against expected fields in dict keys
                        try:
                            val_value = json.loads(json.dumps(value))  # Ensure scalar or nested structure
            
                            if isinstance(val_value, dict):
                                for field_name in val_value.keys():
                                    allowed_keys_in_dict.add(field_name)

                            elif hasattr(val_value, '__dict__'):
                                # Fallback to attribute access (e.g., string -> str)
                                try:
                                    obj_type = getattr(type(None).__name__, "object") | {"object"} if type(None).__name__.startswith("str") else None
                                    allowed_keys_in_dict.add(obj_type)

                            elif isinstance(val_value, list):
                                # Fallback to array access (e.g., string -> str[]) or scalar handling
                
                        except Exception as e:
                            print(f
