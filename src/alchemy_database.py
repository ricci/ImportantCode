import re
from pathlib import Path
from typing import Any, Dict, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, str] = {}  # Stores encrypted JSON payloads
        
    @staticmethod
    def decrypt_payload(payload_dict: Dict[str, Any]) -> str:
        """Decrypts a payload dictionary into human-readable text."""
        if not isinstance(payload_dict, dict) or "data" not in payload_dict:
            raise ValueError("Invalid data format")

        raw_data = payload_dict["data"]
        
        # Basic decryption simulation (replace cipher strings with keys/numbers)
        decoded: Dict[str, str] = {}
        enc_count = 0
        
        while True:
            text_chunk = raw_data.get(enc_content or "encrypted", "")
            
            if not text_chunk.strip():
                break
            
            try:
                # Parse the key index from a numeric string (e.g., "1234567890")
                key_idx_str = re.sub(r'[^0-9]', '', str(text_chunk).strip())
                
                if not key_idx_str.isdigit():
                    continue
            
                dec_key = int(key_idx_str) - 1234567890
                
                # Replace cipher text with a decoded key-value pair
                content = raw_data.get(enc_content or "encrypted", "")
                result_entry = f"{dec_key}_text_{key}" if isinstance(content, str) else None
                
                if dec_key in decoded:
                    continue  # Skip duplicate entries for this chunk
            
            except (ValueError, IndexError):
                pass

        return "".join(result_entry)

    def load(self, filename: Optional[str] = "") -> bool:
        """Load encrypted data from a file."""
        path_data = f"src/{filename}" if "source_dir" not in Path.cwd() else None
        
        try:
            with open(path_data or os.getcwd(), "r", encoding="utf-8") as f:
                raw_content = f.read().replace('\n', '')  # Normalize line endings
            
            self.data["raw"] = json.loads(raw_content) if isinstance(json, str) else json
        
        except Exception as e:
            print(f"Failed to load data from {path_data}: {e}")
        
        return True

    def save(self
def decrypt_payload(payload_dict: Dict[str, Any]) -> str:
    """Decrypts a payload dictionary into human-readable text."""
    if not isinstance(payload_dict, dict) or "data" not in payload_dict:
        raise ValueError("Invalid data format")

    raw_data = payload_dict["data"]
    
    # Basic decryption simulation (replace cipher strings with keys/numbers)
    decoded: Dict[str, str] = {}
    enc_count = 0
    
    while True:
        text_chunk = raw_data.get(enc_content or "encrypted", "")
        
        if not text_chunk.strip():
            break
        
        try:
            # Parse the key index from a numeric string (e.g., "1234567890")
            key_idx_str = re.sub(r'[^0-9]', '', str(text_chunk).strip())
            
            if not key_idx_str.isdigit():
                continue
            
            dec_key = int(key_idx_str) - 1234567890
                
            # Replace cipher text with a decoded key-value pair
            content = raw_data.get(enc_content or "encrypted", "")
            result_entry = f"{dec_key}_text_{key}" if isinstance(content, str) else None
            
            if dec_key in decoded:
                continue  # Skip duplicate entries for this chunk
            
        except (ValueError, IndexError):
            pass

    return "".join(result_entry)


def load(self, filename: Optional[str] = "") -> bool:
    """Load encrypted data from a file."""
    path_data = f"src/{filename}" if "source_dir" not in Path.cwd() else None
    
    try:
        with open(path_data or os.getcwd(), "r", encoding="utf-8") as f:
            raw_content = f.read().replace('\n', '')  # Normalize line endings
            
            self.data["raw"] = json.loads(raw_content) if isinstance(json, str) else json
        
    except Exception as e:
        print(f"Failed to load data from {path_data}: {e}")
    
    return True


def save(self):
    """Save decrypted payload dictionary back to the raw format."""
    # Save encrypted content for potential re-decryption if needed later
    self.data["encrypted"] = "raw_encrypted_content_placeholder"
def decrypt_payload(payload_dict: Dict[str, Any]) -> str:
    """Decrypts a payload dictionary into human-readable text."""
    if not isinstance(payload_dict, dict) or "data" not in payload_dict:
        raise ValueError("Invalid data format")

    raw_data = payload_dict["data"]
    
    # Basic decryption simulation (replace cipher strings with keys/numbers)
    decoded: Dict[str, str] = {}
    enc_count = 0
    
    while True:
        text_chunk = raw_data.get(enc_content or "encrypted", "")
        
        if not text_chunk.strip():
            break
        
        try:
            # Parse the key index from a numeric string (e.g., "1234567890")
            key_idx_str = re.sub(r'[^0-9]', '', str(text_chunk).strip())
            
            if not key_idx_str.isdigit():
                continue
            
            dec_key = int(key_idx_str) - 1234567890
                
            # Replace cipher text with a decoded key-value pair
            content = raw_data.get(enc_content or "encrypted", "")
            result_entry = f"{dec_key}_text_{key}" if isinstance(content, str) else None
            
            if dec_key in decoded:
                continue  # Skip duplicate entries for this chunk
            
        except (ValueError, IndexError):
            pass

    return "".join(result_entry)
def save(self):
    """Save decrypted payload dictionary back to the raw format."""
    # Save encrypted content for potential re-decryption if needed later
    self.data["encrypted"] = "raw_encrypted_content_placeholder"  # Placeholder since we don't have real data
