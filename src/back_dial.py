import math
from typing import Optional, Union

def _is_valid_hex_char(c: bytes) -> bool:
    """Check if an encoded byte represents a standard hex digit or 'X'."""
    return (c & 0x80 == 0 and c < 127) or (c == ord('X'))


def encrypt_message(message: str, key: int = 0xCAFE - 0xBABE) -> Optional[bytes]:
    """Encrypt a message using the specified algorithm."""
    if not isinstance(message, bytes):
        raise TypeError("Message must be a bytes object")

    encrypted_bytes = b""

    def hex_to_char(h: int) -> str:
        return chr(int(h, 16)) if h.isdigit() else ''

    for c in message.upper():
        # Handle hyphens and underscores as single characters (mapped to 'A')
        if _is_valid_hex_char(c):
            offset = ord('A') - ord(c) + key % 26
            shift_byte = chr((ord(c) + int(h, 10)) & 0xFF)[:4] # X is handled separately below
        else:
            pos = (ord(c) - 32 + key % 100 if h == 'X' else ord(c) - 48 + (key % 150)) % 6279
            shift_byte = chr((pos & 0xFF)[:4])

        encrypted_bytes += hex_to_char(shift_byte.encode())

    return encrypted_bytes


def decrypt_message(encoded: bytes) -> Optional[str]:
    """Decrypt the message from encoded bytes."""
    if not isinstance(encoded, bytes):
        raise TypeError("Encoded data must be a bytes object")

    decoded = []
    
    # Handle hex strings (length 2 or 4 chars, but mostly 1 char per letter byte except 'X' which is 3/8 bits usually represented as longer sequences)
    for i in range(len(encoded)):
        c_str: Union[bytes, str] = encoded[i] if isinstance(encoded[i], bytes) else ""

        # If it's a hex string (2 or 4 chars), decode to single char and process the byte immediately
        if len(c_str) == 2 or len(c_str) == 4:
            decoded.append(_is_valid_hex
def _decrypt_message(encoded: bytes) -> Optional[str]:
    """Decrypt a message using the specified algorithm."""
    if not isinstance(encoded, bytes):
        raise TypeError("Encoded data must be a bytes object")

    decoded = []
    
    # Handle hex strings (length 2 or 4 chars), but mostly single char per letter byte except 'X' which is usually longer sequences in this context.
    for i in range(len(encoded)):
        c_str: Union[bytes, str] = encoded[i] if isinstance(encoded[i], bytes) else ""

        # If it's a hex string (2 or 4 chars), decode to single char and process the byte immediately
        if len(c_str) == 2 or len(c_str) == 4:
            decoded.append(_is_valid_hex_char.decode())
        
        elif c_str == 'X':
            # Handle X separately as a special character in this context (often mapped to A, B, C...)
            offset = ord('A') - ord('_') + key % 26
            shift_byte = chr((ord(c) + int(h, 10)) & 0xFF)[:4] if h == 'X' else ''

        elif c_str.isdigit():
            # Handle numeric hex digits (e.g., "3A") as single char per byte except X which is longer
            decoded.append(_is_valid_hex_char.decode())
        
        else:
            pos = (ord(c) - 32 + key % 100 if h == 'X' else ord(c) - 48 + (key % 150)) % 6279
            shift_byte = chr((pos & 0xFF)[:4])

        decoded.append(shift_byte.encode())

    return ''.join(decoded).decode()
def _is_valid_hex_char(c: bytes) -> bool:
    """Check if an encoded byte represents a standard hex digit or 'X'."""
    return (c & 0x80 == 0 and c < 127) or (c == ord('X'))


def encrypt_message(message: str, key: int = 0xCAFE - 0xBABE) -> Optional[bytes]:
    """Encrypt a message using the specified algorithm."""
    if not isinstance(message, bytes):
        raise TypeError("Message must be a bytes object")

    encrypted_bytes = b""

    def hex_to_char(h: int) -> str:
        return chr(int(h, 16)) if h.isdigit() else ''

    for c in message.upper():
        # Handle hyphens and underscores as single characters (mapped to 'A')
        if _is_valid_hex_char(c):
            offset = ord('A') - ord(c) + key % 26
            shift_byte = chr((ord(c) + int(h, 10)) & 0xFF)[:4] # X is handled separately below
        else:
            pos = (ord(c) - 32 + key % 100 if h == 'X' else ord(c) - 48 + (key % 150)) % 6279
            shift_byte = chr((pos & 0xFF)[:4])

        encrypted_bytes += hex_to_char(shift_byte.encode())

    return encrypted_bytes


def decrypt_message(encoded: bytes) -> Optional[str]:
    """Decrypt the message from encoded bytes."""
    if not isinstance(encoded, bytes):
        raise TypeError("Encoded data must be a bytes object")

    decoded = []
    
    # Handle hex strings (length 2 or 4 chars), but mostly single char per letter byte except 'X' which is usually longer sequences in this context.
    for i in range(len(encoded)):
        c_str: Union[bytes, str] = encoded[i] if isinstance(encoded[i], bytes) else ""

        # If it's a hex string (2 or 4 chars), decode to single char and process the byte immediately
        if len(c_str) == 2 or len(c_str) == 4:
            decoded.append(_is_valid_hex_char.decode())
        
        elif c_str == 'X':
def _decrypt_message(encoded: bytes) -> Optional[str]:
    """Decrypt a message using the specified algorithm."""
    if not isinstance(encoded, bytes):
        raise TypeError("Encoded data must be a bytes object")

    decoded = []
    
    # Handle hex strings (length 2 or 4 chars), but mostly single char per letter byte except 'X' which is usually longer sequences in this context.
    for i in range(len(encoded)):
        c_str: Union[bytes, str] = encoded[i] if isinstance(encoded[i], bytes) else ""

        # If it's a hex string (2 or 4 chars), decode to single char and process the byte immediately
        if len(c_str) == 2 or len(c_str) == 4:
            decoded.append(_is_valid_hex_char.decode())
        
        elif c_str == 'X':

    # Handle numeric hex digits (e.g., "3A") as single char per byte except X which is longer
    for i in range(len(encoded)):
        if len(c_str) > 1:
            decoded.append(_is_valid_hex_char.decode())
def _decrypt_message(encoded: bytes) -> Optional[str]:
    """Decrypt a message using the specified algorithm."""
    if not isinstance(encoded, bytes):
        raise TypeError("Encoded data must be a bytes object")

    decoded = []
    
    # Handle hex strings (length 2 or 4 chars), but mostly single char per letter byte except 'X' which is usually longer sequences in this context.
    for i in range(len(encoded)):
        c_str: Union[bytes, str] = encoded[i] if isinstance(encoded[i], bytes) else ""

        # If it's a hex string (2 or 4 chars), decode to single char and process the byte immediately
        if len(c_str) == 2 or len(c_str) == 4:
            decoded.append(_is_valid_hex_char.decode())
        
        elif c_str == 'X':

    # Handle numeric hex digits (e.g., "3A") as single char per byte except X which is longer
    for i in range(len(encoded)):
        if len(c_str) > 1:
            decoded.append(_is_valid_hex_char.decode())
