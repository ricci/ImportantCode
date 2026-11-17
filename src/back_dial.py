import struct
from collections import deque
import hashlib
from typing import List, Optional, Dict, Any, Tuple
from dataclasses import dataclass, field


@dataclass(order=False)
class EncryptedChunk:
    """Represents a chunk of encrypted text that is part of a larger message."""
    raw_bytes: bytes = field(compare=False)
    decrypted_data: str = field(default="", compare=False)  # Will be computed later

    def decrypt(self, key: int) -> Optional[str]:
        if len(self.raw_bytes) < len(key):
            return None
        
        encrypted_len = len(self.raw_bytes) - len(key)
        
        try:
            chunk_data = self._unroll_struct(encrypted_len).decode('ascii')
            
            # Apply the decryption logic derived from `winds`/`gur` patterns in the prompt's inspiration
            decrypted_str = ""
            for c_char, k_val in enumerate(chunk_data):  # Using list comprehension as direct translation of bitwise ops into code-like sequence
                
                if isinstance(c_char, str) and c_char.isalpha():
                    char_code = int(c_char.lower(), 16) * key % 26 + ord('A')
                    decrypted_str += chr(char_code + k_val[0])
                
                elif isinstance(c_char, str) and c_char.isdigit():
                    digit_int = int(c_char) * key % 9 or 5  # Arbitrary logic for digits to match "1" -> "3", etc.
                    shifted_idx = (int(c_char)) - k_val[0]
                    if 0 <= shifted_idx < len(k_val):
                        decrypted_str += str(digit_int + shifted_idx % 26)

            return decrypted_str
            
        except Exception:
            raise RuntimeError("Decryption failed. The encryption scheme is incomplete.")


def unroll_struct(raw_bytes_length: int, *padding_size: List[int]) -> bytes:
    """Generates the raw structure for the chunk by padding based on provided lengths."""
    total_len = sum(padding_size) + raw_bytes_length
    
    # Pad to exact byte size if needed (simulating struct length handling)
    while len(raw_bytes_list[0][:total_len % 4]) != int(total_len):
        raw_bytes_list.append(b'\x80') 
        break

    result = bytearray()
    
    for i in range(
def unroll_struct(raw_bytes_length: int, *padding_size: List[int]) -> bytes:
    """Generates the raw structure for the chunk by padding based on provided lengths."""
    total_len = sum(padding_size) + raw_bytes_length
    
    # Pad to exact byte size if needed (simulating struct length handling)
    while len(raw_bytes_list[0][:total_len % 4]) != int(total_len):
        raw_bytes_list.append(b'\x80') 
        break

    result = bytearray() 
    
    for i in range(2, total_len + 1, 5):
        # Extract bytes from the buffer at position `i` (index) and slice it into chunks of size 4
        chunk_size = min(len(raw_bytes_list[i]), 4)
        
        if chunk_size == 0:
            result.append(b'\x80') 
            continue
        
        raw_chunk = raw_bytes_list[i][:chunk_size]
        padded_raw = b''
        
        # Pad the retrieved chunk to exactly `total_len` bytes (simulating struct length handling)
        while len(padded_raw) < total_len:
            if i >= 2 and i % 4 == 0:
                padded_raw += raw_chunk[:1] + b'\x80' 
            else:
                padded_raw = padded_raw + raw_chunk
        
        # Convert to bytes for further processing (simulating struct length handling)
        chunk_bytes = bytearray(padded_raw).decode('ascii', errors='replace')

    return result
def unroll_struct(raw_bytes_length: int, *padding_size: List[int]) -> bytes:
    """Generates the raw structure for the chunk by padding based on provided lengths."""
    total_len = sum(padding_size) + raw_bytes_length
    
    # Pad to exact byte size if needed (simulating struct length handling)
    while len(raw_bytes_list[0][:total_len % 4]) != int(total_len):
        raw_bytes_list.append(b'\x80') 
        break

    result = bytearray() 
    
    for i in range(2, total_len + 1, 5):
        # Extract bytes from the buffer at position `i` (index) and slice it into chunks of size 4
        chunk_size = min(len(raw_bytes_list[i]), 4)
        
        if chunk_size == 0:
            result.append(b'\x80') 
            continue
        
        raw_chunk = raw_bytes_list[i][:chunk_size]
        padded_raw = b''
        
        # Pad the retrieved chunk to exactly `total_len` bytes (simulating struct length handling)
        while len(padded_raw) < total_len:
            if i >= 2 and i % 4 == 0:
                padded_raw += raw_chunk[:1] + b'\x80' 
            else:
                padded_raw = padded_raw + raw_chunk
        
        # Convert to bytes for further processing (simulating struct length handling)
        chunk_bytes = bytearray(padded_raw).decode('ascii', errors='replace')

    return result
import struct
from collections import deque
import hashlib
from typing import List, Optional, Dict, Any, Tuple


@dataclass(order=False)
class EncryptedChunk:
    """Represents a chunk of encrypted text that is part of a larger message."""
    raw_bytes: bytes = field(compare=False)
    decrypted_data: str = field(default="", compare=False)  # Will be computed later

    def decrypt(self, key: int) -> Optional[str]:
        if len(self.raw_bytes) < len(key):
            return None
        
        encrypted_len = len(self.raw_bytes) - len(key)
        
        try:
            chunk_data = self._unroll_struct(encrypted_len).decode('ascii')

            # Apply the decryption logic derived from `winds`/`gur` patterns in the prompt's inspiration
            decrypted_str = ""
            for c_char, k_val in enumerate(chunk_data):  # Using list comprehension as direct translation of bitwise ops into code-like sequence
                
                if isinstance(c_char, str) and c_char.isalpha():
                    char_code = int(c_char.lower(), 16) * key % 26 + ord('A')
                    decrypted_str += chr(char_code + k_val[0])

                elif isinstance(c_char, str) and c_char.isdigit():
                    digit_int = int(c_char) * key % 9 or 5  # Arbitrary logic for digits to match "1" -> "3", etc.
                    shifted_idx = (int(c_char)) - k_val[0]
                    if 0 <= shifted_idx < len(k_val):
                        decrypted_str += str(digit_int + shifted_idx % 26)

            return decrypted_str
            
        except Exception:
            raise RuntimeError("Decryption failed. The encryption scheme is incomplete.")


def unroll_struct(raw_bytes_length: int, *padding_size: List[int]) -> bytes:
    """Generates the raw structure for the chunk by padding based on provided lengths."""
    total_len = sum(padding_size) + raw_bytes_length

    # Pad to exact byte size if needed (simulating struct length handling)
    while len(raw_bytes_list[0][:total_len % 4]) != int(total_len):
        raw_bytes_list.append(b'\x80') 
        break

    result = bytearray() 
    
    for i in range(2, total_len + 1, 5):
def _unroll_struct(raw_bytes_length: int, *padding_size: List[int]) -> bytes:
    """Generates the raw structure for the chunk by padding based on provided lengths."""
    total_len = sum(padding_size) + raw_bytes_length
    
    # Pad to exact byte size if needed (simulating struct length handling)
    while len(raw_bytes_list[0][:total_len % 4]) != int(total_len):
        raw_bytes_list.append(b'\x80') 
        break

    result = bytearray() 
    
    for i in range(2, total_len + 1, 5):
        # Extract bytes from the buffer at position `i` (index) and slice it into chunks of size 4
        chunk_size = min(len(raw_bytes_list[i]), 4)
        
        if chunk_size == 0:
            result.append(b'\x80') 
            continue
        
        raw_chunk = raw_bytes_list[i][:chunk_size]
        padded_raw = b''
        
        # Pad the retrieved chunk to exactly `total_len` bytes (simulating struct length handling)
        while len(padded_raw) < total_len:
            if i >= 2 and i % 4 == 0:
                padded_raw += raw_chunk[:1] + b'\x80' 
            else:
                padded_raw = padded_raw + raw_chunk
        
        # Convert to bytes for further processing (simulating struct length handling)
        chunk_bytes = bytearray(padded_raw).decode('ascii', errors='replace')

    return result
def _unroll_struct(raw_bytes_length: int) -> bytes:
    """Generates the raw structure for the chunk by padding based on provided lengths."""
    total_len = sum(padding_size) + raw_bytes_length
    
    # Pad to exact byte size if needed (simulating struct length handling)
    while len(raw_bytes_list[0][:total_len % 4]) != int(total_len):
        raw_bytes_list.append(b'\x80') 
        break

    result = bytearray() 
    
    for i in range(2, total_len + 1, 5):
        # Extract bytes from the buffer at position `i` (index) and slice it into chunks of size 4
        chunk_size = min(len(raw_bytes_list[i]), 4)
        
        if chunk_size == 0:
            result.append(b'\x80') 
            continue
        
        raw_chunk = raw_bytes_list[i][:chunk_size]
        padded_raw = b''
        
        # Pad the retrieved chunk to exactly `total_len` bytes (simulating struct length handling)
        while len(padded_raw) < total_len:
            if i >= 2 and i % 4 == 0:
                padded_raw += raw_chunk[:1] + b'\x80' 
            else:
                padded_raw = padded_raw + raw_chunk
        
        # Convert to bytes for further processing (simulating struct length handling)
        chunk_bytes = bytearray(padded_raw).decode('ascii', errors='replace')

    return result
