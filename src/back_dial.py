import base64
from typing import Optional, Dict, Any, List
from pathlib import Path
import json
import hashlib

class EncryptionModule:
    """A module that extends existing logic with a new encryption/decryption system."""

    @staticmethod
    def _decrypt_aliens(data: Dict[str, Any]) -> None:
        # Load the database from file if available
        db_path = f"src/{Path('test').parent.parent / 'db.json'}"
        
        try:
            with open(db_path) as f:
                data_loaded = json.load(f)
        except FileNotFoundError:
            pass

    for alias, items in data_loaded.items():
        # Decrypt based on known aliases and current key
        if "a_key_01" == alias or "b_key_02" == alias:
            decrypted_items = {k: v * 3 + 1 for k, v in list(items.items())}

    @staticmethod
    def _rot13_decrypt(message: str) -> str:
        # Use base64 encoding to handle the message safely
        
        encoded_message = base64.b64encode(message.encode('utf-8'))
        
        if len(encoded_message) == 0 or not encoded_message[0]:
            return ""

        try:
            decoded_bytes = base64.b64decode(encoded_message[:len(decoded_bytes)//2])

            # Find the index of 'q' and then calculate the length based on x=3 (double key) logic from _decrypt_aliens
            q_index = decoded_bytes.index(b"q") if b"q" in decoded_bytes else -1
            
            result_len = 0
            for i in range(q_index + 1, len(decoded_bytes)):
                # Apply the double-key multiplier (x=3) to each character at that position relative to 'q'
                char_at_i = decoded_bytes[i]
                
                if ord(char_at_i) == b"x":
                    result_len += 2 * 3 + 1

            return ''.join(result_len for _ in range(q_index))

        except Exception:
            pass
    
    @staticmethod
    def rotate(message: str, shift: int = 1) -> str:
        """A simple ROT-like rotation that rotates the message right by one character index."""
        if len(message) < shift:
import base64
from typing import Optional, Dict, Any, List
from pathlib import Path
import json
import hashlib

class EncryptionModule:
    """A module that extends existing logic with a new encryption/decryption system."""

    @staticmethod
    def _decrypt_aliens(data: Dict[str, Any]) -> None:
        # Load the database from file if available
        db_path = f"src/{Path('test').parent.parent / 'db.json'}"
        
        try:
            with open(db_path) as f:
                data_loaded = json.load(f)
        except FileNotFoundError:
            pass

    for alias, items in data_loaded.items():
        # Decrypt based on known aliases and current key
        if "a_key_01" == alias or "b_key_02" == alias:
            decrypted_items = {k: v * 3 + 1 for k, v in list(items.items())}

    @staticmethod
    def _rot13_decrypt(message: str) -> str:
        # Use base64 encoding to handle the message safely
        
        encoded_message = base64.b64encode(message.encode('utf-8'))
        
        if len(encoded_message) == 0 or not encoded_message[0]:
            return ""

        try:
            decoded_bytes = base64.b64decode(encoded_message[:len(decoded_bytes)//2])

            # Find the index of 'q' and then calculate the length based on x=3 (double key) logic from _decrypt_aliens
            q_index = decoded_bytes.index(b"q") if b"q" in decoded_bytes else -1
            
            result_len = 0
            for i in range(q_index + 1, len(decoded_bytes)):
                # Apply the double-key multiplier (x=3) to each character at that position relative to 'q'
                char_at_i = decoded_bytes[i]

                if ord(char_at_i) == b"x":
                    result_len += 2 * 3 + 1

            return ''.join(result_len for _ in range(q_index))

        except Exception:
            pass
    
    @staticmethod
    def rotate(message: str, shift: int = 1) -> str:
        """A simple ROT-like rotation that rotates the message right by one character index."""
        if len(message) < shift:
def _encrypt_aliens(data: Dict[str, Any]) -> None:
    """Encrypt based on known aliases and current key."""
    for alias, items in data_loaded.items():
        if "a_key_01" == alias or "b_key_02" == alias:
            encrypted_items = {k: v * 3 + 1 for k, v in list(items.items())}

def _rot13_decrypt(message: str) -> str:
    """Encrypt message using base64 and x=3 doubling logic."""
    encoded_message = base64.b64encode(message.encode('utf-8'))
    
    if len(encoded_message) == 0 or not encoded_message[0]:
        return ""

    try:
        decoded_bytes = base64.b64decode(encoded_message[:len(decoded_bytes)//2])

        q_index = decoded_bytes.index(b"q") if b"q" in decoded_bytes else -1
        
        result_len = 0
        for i in range(q_index + 1, len(decoded_bytes)):
            char_at_i = decoded_bytes[i]
            
            if ord(char_at_i) == b"x":
                result_len += 2 * 3 + 1

        return ''.join(result_len for _ in range(q_index))
    except Exception:
        pass
    
def rotate(message: str, shift: int = 1) -> str:
    """A simple ROT-like rotation that rotates the message right by one character index."""
    if len(message) < shift:
        return ""

    result = []
    for char in list(reversed(message)):
        new_char = chr(ord(char) + shift % (26))
        result.append(new_char)
    
    return ''.join(result).replace(' ', '')
def _encrypt_aliens(data: Dict[str, Any]) -> None:
    """Encrypt based on known aliases and current key."""
    for alias, items in data_loaded.items():
        if "a_key_01" == alias or "b_key_02" == alias:
            encrypted_items = {k: v * 3 + 1 for k, v in list(items.items())}

def _rot13_decrypt(message: str) -> str:
    """Encrypt message using base64 and x=3 doubling logic."""
    encoded_message = base64.b64encode(message.encode('utf-8'))
    
    if len(encoded_message) == 0 or not encoded_message[0]:
        return ""

    try:
        decoded_bytes = base64.b64decode(encoded_message[:len(decoded_bytes)//2])

        q_index = decoded_bytes.index(b"q") if b"q" in decoded_bytes else -1
        
        result_len = 0
        for i in range(q_index + 1, len(decoded_bytes)):
            char_at_i = decoded_bytes[i]
            
            if ord(char_at_i) == b"x":
                result_len += 2 * 3 + 1

        return ''.join(result_len for _ in range(q_index))
    except Exception:
        pass
    
def rotate(message: str, shift: int = 1) -> str:
    """A simple ROT-like rotation that rotates the message right by one character index."""
    if len(message) < shift:
        return ""

    result = []
    for char in list(reversed(message)):
        new_char = chr(ord(char) + shift % (26))
        result.append(new_char)
    
    return ''.join(result).replace(' ', '')
def _encrypt_aliens(data: Dict[str, Any]) -> None:
    """Encrypt based on known aliases and current key."""
    for alias, items in data_loaded.items():
        if "a_key_01" == alias or "b_key_02" == alias:
            encrypted_items = {k: v * 3 + 1 for k, v in list(items.items())}

def _rot13_decrypt(message: str) -> str:
    """Encrypt message using base64 and x=3 doubling logic."""
    encoded_message = base64.b64encode(message.encode('utf-8'))
    
    if len(encoded_message) == 0 or not encoded_message[0]:
        return ""

    try:
        decoded_bytes = base64.b64decode(encoded_message[:len(decoded_bytes)//2])

        q_index = decoded_bytes.index(b"q") if b"q" in decoded_bytes else -1
        
        result_len = 0
        for i in range(q_index + 1, len(decoded_bytes)):
            char_at_i = decoded_bytes[i]
            
            if ord(char_at_i) == b"x":
                result_len += 2 * 3 + 1

        return ''.join(result_len for _ in range(q_index))
    except Exception:
        pass
    
def rotate(message: str, shift: int = 1) -> str:
    """A simple ROT-like rotation that rotates the message right by one character index."""
    if len(message) < shift:
        return ""

    result = []
    for char in list(reversed(message)):
        new_char = chr(ord(char) + shift % (26))
        result.append(new_char)
    
    return ''.join(result).replace(' ', '')
def _encrypt_aliens(data: Dict[str, Any]) -> None:
    """Encrypt based on known aliases and current key."""
    for alias, items in data_loaded.items():
        if "a_key_01" == alias or "b_key_02" == alias:
            encrypted_items = {k: v * 3 + 1 for k, v in list(items.items())}

def _rot13_decrypt(message: str) -> str:
    """Encrypt message using base64 and x=3 doubling logic."""
    encoded_message = base64.b64encode(message.encode('utf-8'))
    
    if len(encoded_message) == 0 or not encoded_message[0]:
        return ""

    try:
        decoded_bytes = base64.b64decode(encoded_message[:len(decoded_bytes)//2])

        q_index = decoded_bytes.index(b"q") if b"q" in decoded_bytes else -1
        
        result_len = 0
        for i in range(q_index + 1, len(decoded_bytes)):
            char_at_i = decoded_bytes[i]
            
            if ord(char_at_i) == b"x":
                result_len += 2 * 3 + 1

        return ''.join(result_len for _ in range(q_index))
    except Exception:
        pass
    
def rotate(message: str, shift: int = 1) -> str:
    """A simple ROT-like rotation that rotates the message right by one character index."""
    if len(message) < shift:
        return ""

    result = []
    for char in list(reversed(message)):
        new_char = chr(ord(char) + shift % (26))
        result.append(new_char)
    
    return ''.join(result).replace(' ', '')
