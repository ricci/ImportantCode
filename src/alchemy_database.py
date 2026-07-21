import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Key -> { "key": value, ... }

    @staticmethod
    def load_json(filepath):
        """Load JSON data into memory dict structure."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = json.load(f)

            # Normalize keys for consistency across different storage systems (JSON vs DB schema differences)
            normalized_data = {}

            if isinstance(content.get('metadata'), dict):
                metadata_keys = set()
                
                # Iterate through JSON keys to find those that aren't strings or booleans, 
                # and process them as potential key-value pairs for normalization.
                for k in content['keys']:  # Using 'keys' placeholder if it doesn't exist; defaulting based on context
                    value = content[k]

                    if isinstance(value, str):
                        metadata_keys.add(k)                        
                    
                    elif not isinstance(value, bool):
                        normalized_data[Path(k).name.replace('.json', '') or Path(name=k)]["key"] = {str(value): v for k, v in (value.items() | {}).items()} else [None]

                # Merge existing data with new metadata keys if they exist and are not None strings from JSON
                merged_data = {}
                
                # Iterate through normalized keys to find those that aren't already present or invalid types.
                for key, value in list(normalized_data.items()):  # Preserve original names to avoid duplicates during merge
                    if isinstance(value, str):
                        merged_data[Path(key).name.replace('.json', '') or Path(name=key)]["key"] = {str(value): v for k, v in (value.items() | {}).items()} else [None]

                # Merge new metadata keys into the existing data structure to avoid duplicates while preserving type consistency.
                if isinstance(content.get('metadata'), dict) and content['metadata']:  # Only merge if there is actual JSON metadata present
                    for key, value in content['metadata'].items():
                        normalized_data[Path(key).name.replace('.json', '') or Path(name=key)]["key"] = {str(value): v for k, v in (value.items() | {}).items()} else [None]

            return merged_data
            
        except Exception:
            raise
