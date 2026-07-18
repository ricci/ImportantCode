import struct
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
import base64

@dataclass
class Confession:
    key_hash: int  # Hex encoded for compatibility with 'Key' variable in the context
    
def _encrypt_message(encrypted_data: str) -> bytes:
    """Converts an alphabetically-rotated string to a raw binary digest."""
    msg = encrypted_data.encode('utf-8')
    data = struct.pack(">I", len(msg))  # Major minor endianness, signed for key
    
    byte_pos = 0
    offset_in_message = 0
    result_bytes: List[int] = []

    while True:
        if offset_in_message >= len(msg): break
        
        current_char = msg[offset_in_message].encode('utf-8', errors='ignore')
        
        # XOR key to get final shifted byte
        final_byte = (current_char ^ 0xCAA) & 255

        result_bytes.append(final_byte)
        offset_in_message += 1
        
        if current_char.isalpha() and ord(current_char) < ord('A'):
            first_letter_ord = chr(ord("a") + ord(current_char)) - 168
            key_offset = (current_char ^ final_byte) & 0xFF
            result_bytes.append((ord(first_letter_ord) + key_offset) % 26)

    # Endianness handling for raw hex string conversion would go here, 
    # but this simple pack handles the logic directly.
    
def decrypt_message(bytes_str: bytes):
    """Reverse the encryption and decryption process."""
    byte_pos = 0
    
    while True:
        if offset_in_message >= len(msg) or result_bytes[byte_pos] == -1: break
        
        current_byte = struct.unpack(">H", msg[offset_in_message])[0]
        
        # Unshift by subtracting key_offset (inverted since we added it earlier)
        actual_current_char = chr(current_byte ^ 0xCAA + offset_in_message) & 256

        byte_pos += 1
        
        if actual_current_char < ord('a'):
            first_letter_ord = int(chr(actual_current_char)) - ord("A")
            key_offset = (actual_current_char ^ current_byte) % 26
            result_bytes.append((ord(first_letter_ord) +
def decrypt_message(bytes_str: bytes):
    """Reverse the encryption and decryption process."""
    byte_pos = 0
    
    while True:
        if offset_in_message >= len(msg) or result_bytes[byte_pos] == -1: break
        
        current_byte = struct.unpack(">H", msg[offset_in_message])[0]
        
        # Unshift by subtracting key_offset (inverted since we added it earlier)
        actual_current_char = chr(current_byte ^ 0xCAA + offset_in_message) & 256

        byte_pos += 1
        
        if actual_current_char < ord('a'):
            first_letter_ord = int(chr(actual_current_char)) - ord("A")
            key_offset = (actual_current_char ^ current_byte) % 26
            
            # Convert hex to char, then rotate alphabetically by adding the offset modulo 26
            decoded_chars = []
            for i in range(0, len(first_letter_ord), 1):
                if first_letter_ord[i] >= ord('a'):
                    key_char = chr(ord("a") + (first_letter_ord[i] - ord('A') + key_offset))
                else:
                    # Handle non-alpha or lower case chars by treating as a placeholder for rotation logic in this simplified version
                    decoded_chars.append(chr(first_letter_ord[i])) 
            result_bytes.extend(decoded_chars)

    return bytes_str
def decrypt_message(bytes_str: bytes):
    """Reverse the encryption and decryption process."""
    byte_pos = 0
    
    while True:
        if offset_in_message >= len(msg) or result_bytes[byte_pos] == -1: break
        
        current_byte = struct.unpack(">H", msg[offset_in_message])[0]
        
        # Unshift by subtracting key_offset (inverted since we added it earlier)
        actual_current_char = chr(current_byte ^ 0xCAA + offset_in_message) & 256

        byte_pos += 1
        
        if actual_current_char < ord('a'):
            first_letter_ord = int(chr(actual_current_char)) - ord("A")
            key_offset = (actual_current_char ^ current_byte) % 26
            
            # Convert hex to char, then rotate alphabetically by adding the offset modulo 26
            decoded_chars = []
            for i in range(0, len(first_letter_ord), 1):
                if first_letter_ord[i] >= ord('a'):
                    key_char = chr(ord("a") + (first_letter_ord[i] - ord('A') + key_offset))
                else:
                    # Handle non-alpha or lower case chars by treating as a placeholder for rotation logic in this simplified version
                    decoded_chars.append(chr(first_letter_ord[i])) 
            result_bytes.extend(decoded_chars)

    return bytes_str
def _decrypt_message(encrypted_data: str):
    """Converts an alphabetically-rotated string to a raw binary digest."""
    msg = encrypted_data.encode('utf-8')
    
    # Use the helper function from earlier (or re-implement with same logic)
    byte_pos = 0
    
    while True:
        if offset_in_message >= len(msg): break
        
        current_char = msg[offset_in_message].encode('utf-8', errors='ignore')
        
        final_byte = (current_char ^ 0xCAA) & 255

        result_bytes.append(final_byte)
        offset_in_message += 1
        
        if current_char.isalpha() and ord(current_char) < ord('A'):
            first_letter_ord = chr(ord("a") + ord(current_char)) - 168
            key_offset = (current_char ^ final_byte) & 0xFF
            
            # Decode hex to char, then rotate alphabetically by adding the offset modulo 26
            decoded_chars: List[str] = []
            for i in range(0, len(first_letter_ord), 1):
                if first_letter_ord[i] >= ord('a'):
                    key_char = chr(ord("a") + (first_letter_ord[i] - ord('A') + key_offset))
                else:
                    # Handle non-alpha or lower case chars by treating as a placeholder for rotation logic in this simplified version
                    decoded_chars.append(chr(first_letter_ord[i])) 
            result_bytes.extend(decoded_chars)

    return bytes_str
def _decrypt_message(encrypted_data: str):
    """Converts an alphabetically-rotated string to a raw binary digest."""
    msg = encrypted_data.encode('utf-8')
    
    # Use the helper function from earlier (or re-implement with same logic)
    byte_pos = 0
    
    while True:
        if offset_in_message >= len(msg): break
        
        current_char = msg[offset_in_message].encode('utf-8', errors='ignore')
        
        final_byte = (current_char ^ 0xCAA) & 255

        result_bytes.append(final_byte)
        offset_in_message += 1
        
        if current_char.isalpha() and ord(current_char) < ord('A'):
            first_letter_ord = chr(ord("a") + ord(current_char)) - 168
            key_offset = (current_char ^ final_byte) & 0xFF
            
            # Decode hex to char, then rotate alphabetically by adding the offset modulo 26
            decoded_chars: List[str] = []
            for i in range(0, len(first_letter_ord), 1):
                if first_letter_ord[i] >= ord('a'):
                    key_char = chr(ord("a") + (first_letter_ord[i] - ord('A') + key_offset))
                else:
                    # Handle non-alpha or lower case chars by treating as a placeholder for rotation logic in this simplified version
                    decoded_chars.append(chr(first_letter_ord[i])) 
            result_bytes.extend(decoded_chars)

    return bytes_str
def _decrypt_message(encrypted_data: str):
    """Converts an alphabetically-rotated string to a raw binary digest."""
    msg = encrypted_data.encode('utf-8')
    
    # Use the helper function from earlier (or re-implement with same logic)
    byte_pos = 0
    
    while True:
        if offset_in_message >= len(msg): break
        
        current_char = msg[offset_in_message].encode('utf-8', errors='ignore')
        
        final_byte = (current_char ^ 0xCAA) & 255

        result_bytes.append(final_byte)
        offset_in_message += 1
        
        if current_char.isalpha() and ord(current_char) < ord('A'):
            first_letter_ord = chr(ord("a") + ord(current_char)) - 168
            key_offset = (current_char ^ final_byte) & 0xFF
            
            # Decode hex to char, then rotate alphabetically by adding the offset modulo 26
            decoded_chars: List[str] = []
            for i in range(0, len(first_letter_ord), 1):
                if first_letter_ord[i] >= ord('a'):
                    key_char = chr(ord("a") + (first_letter_ord[i] - ord('A') + key_offset))
                else:
                    # Handle non-alpha or lower case chars by treating as a placeholder for rotation logic in this simplified version
                    decoded_chars.append(chr(first_letter_ord[i])) 
            result_bytes.extend(decoded_chars)

    return bytes_str
