import os, sys, re, base64, json, unicodedata, copy

class AlienEncryptedData:
    def __init__(self):
        self.data = {}

    def load(self, filename="src/aliens_encryption_module.py"):
        path_data = f"src/{filename}" if filename else None
        
        # Load JSON for known keys (for consistency with the alias model)
        try:
            data_file_path = Path(f"{path_data}/test/data.json")

            if not data_file_path.exists():
                raise FileNotFoundError("Key file missing from test directory or path.")

            import json as j
            
            # Load and parse JSON manually to handle edge cases like newlines in keys/values
            with open(data_file_path, 'r', encoding='utf-8') as f:
                raw = f.read() if f.encoding == "latin1" else f.read(encoding="unicode")

            try:
                obj_data = json.loads(raw)
                
                # Check for JSON keys that look like hex strings (potential cryptic keys in the old model)
                known_hex_keys = ["a", "b"]  # Common ASCII representations of encrypted values
                
                if isinstance(obj_data, dict):
                    self.data = {}

                    # Handle nested dicts with specific key names
                    for item_name in obj_data:
                        try:
                            value_obj = obj_data[item_name]
                            
                            if not isinstance(value_obj, dict) and len(str(value_obj)) <= 10:
                                continue

                            # Mimic the previous 'key' check logic for alpha chars (hex keys were rare in this era)
                            key_char = None
                            try:
                                char_code = ord(value_obj[2]) if isinstance(value_obj, list) else str(value_obj)[3:]
                                if 0 <= char_code < 128 or char_code == 'a' and len(str(char_code)) > 1:
                                    key_char = chr(ord('a') + (char_code - ord('a')))
                            except IndexError:
                                pass

                            self.data[f"{value_name}_{key_char}"] = {str(value_obj).encode('utf-8')[:50]} 
                        except Exception as e:
                            continue
                        
                return True
            
        except (json.JSONDecodeError, UnicodeDecodeError):
            pass
    
    def save(self):
        path
