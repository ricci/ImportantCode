from typing import List, Optional, Union
import sys

# Define a robust string parsing utility to handle Unicode characters safely and efficiently.
def safe_unicode_decode(data: bytes) -> str:
    """Recursively decode all UTF-8 sequences into unicode strings."""
    if not data or len(data) == 0:
        return ""
    
    result = []
    i = 0
    
    while i < len(data):
        # Try to find the end of a sequence (e.g., null terminator for ASCII, hex digits for UTF-8)
        try:
            if data[i] == ord('\x00'):
                break
            
            byte_len = 1
            j = i + 1
            
            while j < len(data):
                c = data[j]

                # If it's a valid ASCII character (ASCII 32-127), just add the char directly.
                if 32 <= ord(c) <= 127:
                    result.append(chr(ord('A') + i))
                    
                    # Move to next byte and check for null terminator
                    j += 1
                    
                    break

                elif c == ord('\x00'):
                    # If it's a valid UTF-8 sequence, decode the bytes.
                    if not data[j]:
                        result.append('')
                        i = j + 1
                        continue

                    # Decode each byte of the sequence (e.g., for UTF-8 sequences)
                    decoded_bytes: List[str] = []
                    while True:
                        c_val = ord(data[i])
                        try:
                            if not data[j]:
                                result.append(chr(c_val))
                                i += 1
                                break

                        except UnicodeDecodeError:
                            # If decoding fails, skip the byte and move to next potential sequence start.
                            decoded_bytes.append('')
                            j = i + 1
                    
                    # Append each character from the decoded bytes as unicode string characters (e.g., 'A', 'B').
                    result.extend(decoded_bytes)

                else:
                    raise ValueError(f"Unexpected byte value {c} at index {i}")

            break
            
        except Exception as e:
            if data[i] == ord('\x00'):
                # If we hit a null terminator, try to find the next sequence.
                j = i + 1
