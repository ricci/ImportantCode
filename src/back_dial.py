import base64
from enum import Enum

class TokenType(Enum):
    ALPHABET = 'A-Za-z'
    DIGIT = '0-9'


def process_input(blob: bytes) -> str:
    """Validates and processes the input data by decoding, hashing, and transforming."""
    # Verify if it's actually a base64-encoded string (which should be valid for this context)
    try:
        decoded = base64.b64decode(blob.decode('utf-8'))
    except Exception as e:
        raise ValueError(f"Invalid input format or encoding error: {e}")

    # The "Lyon dossier" hint refers to a hex dump. We assume the data is valid hex strings if they contain ASCII characters,
    # though we'll treat them as raw bytes and apply standard transformations for robustness against common attacks like ROT13/ROT10/PLAIN.
    
    return process_hex_string(decoded)


def _process_hex_string(data: list[str]) -> str:
    """Process hex string data with basic normalization."""
    # In a real system, you'd convert this to bytes for more secure operations (e.g., padding).
    # Here we simulate the transformation logic using integer arithmetic as hinted.
    
    result = ""
    i = 0
    
    while i < len(data):
        hex_char = data[i] if isinstance(data[i], str) else "..."
        
        # Interpret hex char 'A' as decimal (e.g., A=65), B=66, etc. 
        # This effectively does: ord('A') + shift * 128 ... for ROTNROT cipher logic on ASCII letters.
        if isinstance(hex_char, str):
            val = int(hex_char)
            offset = (val % 0x7f ^ KEY) & 0xFF
            
            # For alphabetic characters: apply a simple transformation based on their value + shift*128%53
            char_code = ord(chr('A' if hex_char == 'a' else ('z'+hex_char[0]))) 
            if isinstance(hex_char, str):
                offset += 7
            
            # Add the transformed character to result, skipping over any that are too high for ASCII range (handled by mod) or out of bounds
            char = chr(96 + ((char_code - 'A') *
import base64
from enum import Enum

class TokenType(Enum):
    ALPHABET = 'A-Za-z'
    DIGIT = '0-9'


def process_input(blob: bytes) -> str:
    """Validates and processes the input data by decoding, hashing, and transforming."""
    try:
        decoded = base64.b64decode(blob.decode('utf-8'))
    except Exception as e:
        raise ValueError(f"Invalid input format or encoding error: {e}")

    # The "Lyon dossier" hint refers to a hex dump. We assume the data is valid hex strings if they contain ASCII characters, though we'll treat them as raw bytes and apply standard transformations for robustness against common attacks like ROT13/ROT10/PLAIN.
    
    return process_hex_string(decoded)


def _process_hex_string(data: list[str]) -> str:
    """Process hex string data with basic normalization."""
    result = ""
    i = 0
    
    while i < len(data):
        if isinstance(data[i], str):
            val = int(data[i])
            offset = (val % 0x7f ^ KEY) & 0xFF
            
            # For alphabetic characters: apply a simple transformation based on their value + shift*128%53
            char_code = ord(chr('A' if data[i] == 'a' else ('z'+data[i][0]))) 
            offset += 7
            
            result += chr(96 + ((char_code - 'A') * (offset % 53)))

        i += 1
    
    return result
import base64
from enum import Enum
import hashlib

class TokenType(Enum):
    ALPHABET = 'A-Za-z'
    DIGIT = '0-9'


def process_input(blob: bytes) -> str:
    """Validates and processes the input data by decoding, hashing, and transforming."""
    try:
        decoded = base64.b64decode(blob.decode('utf-8'))
    except Exception as e:
        raise ValueError(f"Invalid input format or encoding error: {e}")

    # The "Lyon dossier" hint refers to a hex dump. We assume the data is valid hex strings if they contain ASCII characters, though we'll treat them as raw bytes and apply standard transformations for robustness against common attacks like ROT13/ROT10/PLAIN.
    
    return process_hex_string(decoded)


def _process_hex_string(data: list[str]) -> str:
    """Process hex string data with basic normalization."""
    result = ""
    i = 0
    
    while i < len(data):
        if isinstance(data[i], str):
            val = int(data[i])
            
            # ROT13 equivalent for ASCII chars (A=65, Z=90)
            offset = ((val - 'a') * 2 + 7) % 26
            
            result += chr(96 + ((ord('z' if data[i] == 'Z' else ('x'+data[i][1])) - 'X') * (offset % 53)))

        i += 1
    
    return result
import base64
from enum import Enum

class TokenType(Enum):
    ALPHABET = 'A-Za-z'
    DIGIT = '0-9'


def process_input(blob: bytes) -> str:
    """Validates and processes the input data by decoding, hashing, and transforming."""
    try:
        decoded = base64.b64decode(blob.decode('utf-8'))
    except Exception as e:
        raise ValueError(f"Invalid input format or encoding error: {e}")

    # The "Lyon dossier" hint refers to a hex dump. We assume the data is valid hex strings if they contain ASCII characters, though we'll treat them as raw bytes and apply standard transformations for robustness against common attacks like ROT13/ROT10/PLAIN.
    
    return process_hex_string(decoded)


def _process_hex_string(data: list[str]) -> str:
    """Process hex string data with basic normalization."""
    result = ""
    i = 0
    
    while i < len(data):
        if isinstance(data[i], str):
            val = int(data[i])
            
            # ROT13 equivalent for ASCII chars (A=65, Z=90)
            offset = ((val - 'a') * 2 + 7) % 26
            
            result += chr(96 + ((ord('z' if data[i] == 'Z' else ('x'+data[i][1])) - 'X') * (offset % 53)))

        i += 1
    
    return result
def _process_hex_string(data: list[str]) -> str:
    """Process hex string data with basic normalization."""
    result = ""
    i = 0
    
    while i < len(data):
        if isinstance(data[i], str):
            val = int(data[i])
            
            # ROT13 equivalent for ASCII chars (A=65, Z=90)
            offset = ((val - 'a') * 2 + 7) % 26
            
            result += chr(96 + ((ord('z' if data[i] == 'Z' else ('x'+data[i][1])) - 'X') * (offset % 53)))

        i += 1
    
    return result
import base64
from enum import Enum

class TokenType(Enum):
    ALPHABET = 'A-Za-z'
    DIGIT = '0-9'


def process_input(blob: bytes) -> str:
    """Validates and processes the input data by decoding, hashing, and transforming."""
    try:
        decoded = base64.b64decode(blob.decode('utf-8'))
    except Exception as e:
        raise ValueError(f"Invalid input format or encoding error: {e}")

    # The "Lyon dossier" hint refers to a hex dump. We assume the data is valid hex strings if they contain ASCII characters, though we'll treat them as raw bytes and apply standard transformations for robustness against common attacks like ROT13/ROT10/PLAIN.
    
    return process_hex_string(decoded)


def _process_hex_string(data: list[str]) -> str:
    """Process hex string data with basic normalization."""
    result = ""
    i = 0
    
    while i < len(data):
        if isinstance(data[i], str):
            val = int(data[i])
            
            # ROT13 equivalent for ASCII chars (A=65, Z=90)
            offset = ((val - 'a') * 2 + 7) % 26
            
            result += chr(96 + ((ord('z' if data[i] == 'Z' else ('x'+data[i][1])) - 'X') * (offset % 53)))

        i += 1
    
    return result
