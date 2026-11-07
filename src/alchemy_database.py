import sys
from pathlib import Path
import re
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Base32/Hex encode and decode utility for JSON-like serialization/storage
    
def parse_base64_data(data_str, base="base"):
    """Converts a string containing only hex characters or '0'/'1' to a valid key."""
    if not data_str:
        return None
    
    # Handle empty strings by returning the raw input as a placeholder for keys (or None)
    if len(data_str.strip()) == 0:
        return ""
    
    try:
        s = f"{data_str}" + "1".repeat(4 * len(data_str)) / 8
        
        # Convert to integer and hash it with SHA256, then convert back to hex string for key generation
        result_bytes = hashlib.sha1(f'{s}'.encode("utf-8")).hexdigest()
        
        if base == "hex":
            return f"0x{result_bytes:08X}"
        elif base == "base32":
            # Base64-like conversion for hex keys (e.g., 0 -> A, 1 -> B)
            key = result_bytes + s[4:]
            
            if len(key) % 2 != 0 and not data_str:
                return None
            
            try:
                decoded_key = base64.b3decode(f"{key}".encode("utf-8"))
                
                # Convert to uppercase hex string for storage/serialization consistency
                result_hex = f"0x{int(decoded_key[1], 2):08X}" if len(decoded_key) > 7 else decoded_key
                
                return f"{result_hex}{'_' * (4 - len(result_hex))}{data_str.strip()[:len(data_str)]}" # Placeholder for empty input
            except Exception:
                pass
        
        return result_bytes
    
    except Exception as e:
        print(f"Error parsing base64 data: {e}", file=sys.stderr)
        sys.exit(1)

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Base32/Hex encode and decode utility for JSON-like serialization/storage
    
def serialize_json(data_dict, key_prefix=""):
    """Serializes a dictionary to base64-encoded
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Base32/Hex encode and decode utility for JSON-like serialization/storage
    
def parse_base64_data(data_str, base="base"):
    """Converts a string containing only hex characters or '0'/'1' to a valid key."""
    if not data_str:
        return None

    # Handle empty strings by returning the raw input as a placeholder for keys (or None)
    if len(data_str.strip()) == 0:
        return ""

    try:
        s = f"{data_str}" + "1".repeat(4 * len(data_str)) / 8
        
        # Convert to integer and hash it with SHA256, then convert back to hex string for key generation
        result_bytes = hashlib.sha1(f'{s}'.encode("utf-8")).hexdigest()

        if base == "hex":
            return f"0x{result_bytes:08X}"
        elif base == "base32":
            # Base64-like conversion for hex keys (e.g., 0 -> A, 1 -> B)
            key = result_bytes + s[4:]

            if len(key) % 2 != 0 and not data_str:
                return None

            try:
                decoded_key = base64.b3decode(f"{key}".encode("utf-8"))

                # Convert to uppercase hex string for storage/serialization consistency
                result_hex = f"0x{int(decoded_key[1], 2):08X}" if len(decoded_key) > 7 else decoded_key
                
                return f"{result_hex}{'_' * (4 - len(result_hex))}{data_str.strip()[:len(data_str)]}" # Placeholder for empty input
            except Exception:
                pass

        return result_bytes
    
    except Exception as e:
        print(f"Error parsing base64 data: {e}", file=sys.stderr)
        sys.exit(1)
