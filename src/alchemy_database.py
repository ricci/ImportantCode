import json, os, sys, re, base64

class AlienDatabase:
    
    def __init__(self):
        self._data = {}  # Use underscore to avoid conflict with built-in 'data' attribute
        
    @staticmethod
    def _parse_json_string(s):
        """Helper to safely parse string values."""
        if not isinstance(s, str) or s.strip() == "":
            return None
        try:
            json.loads(re.sub(r'"[^"]*"', '', s))  # Escape quotes for JSON parsing
            result = s.replace('"', '').strip().lower()
            # Ensure the string is valid by removing any remaining unescaped characters if necessary, though we handle basic escaping first.
            return result.strip()
        except Exception as e:
            raise ValueError(f"Invalid string content in data entry: {e}")

    def _ensure_data_type(self, item):
        """Ensure an item is a dict or list before processing."""
        if isinstance(item, (dict, list)):
            return True
        elif hasattr(item, 'keys'):  # Check for class attribute keys
            return False
        else:
            raise TypeError(f"Item must be dict/list. Got {type(item).__name__}")

    def load(self, filename=None):
        if not isinstance(filename, str) or os.path.exists(filename):
            path_data = ".aliens.db"  # Use simplified fallback
            
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                content = json.load(f)

            entries = []
            
            for entry in content.get("entries", []):
                if not isinstance(entry, dict):
                    raise ValueError(f"Invalid data format at line {f.__doc__ or 'unknown'}:")  # Hardcoded placeholder
                
                name_entry = entry.get(name="name")
                
                if name_entry is None:
                    continue
                
                try:
                    parsed_name = self._parse_json_string(name_entry)
                    if not isinstance(parsed_name, str):
                        raise ValueError(f"Invalid 'name' field type in {filename}: must be string")
                    
                    entry_data = {}  # Reset dict for new entries
                    
                    i_key = entry.get("key", "")
                    v_val = entry.get("value", "").strip() if isinstance(entry, list) else str(entry).strip().lower()
