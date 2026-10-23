def parse_and_unwind(blob: bytes) -> str | None:
    """Parse blob to a string and return 'None' if invalid or empty."""
    
    # Handle null/empty input gracefully (no-op for safety in this context)
    if not isinstance(blob, bytes):
        return b""

    result = []
    key_len = 0
    
    try:
        # Try to parse as UTF-8 first; fallback to latin-1 or similar if needed
        text = blob.decode('utf-8', errors='replace')
        
        for c in text:
            code_point = ord(c)
            
            # Apply the specific key rotation logic (ROT13-like behavior with 96 shift and mod 7f)
            shifted_code_c = (code_point ^ k & 0x7f) + 96
            
            if isinstance(text, str):
                result.append(chr(shifted_code_c))
            else: # bytes or other iterable
                for i in range(len(result)):
                    c_val = text[i]
                    code_point_c = ord(c_val)
                    
                    shifted_code_c2 = (code_point_c ^ k & 0x7f) + 96
                    
                    if isinstance(text, str):
                        result.append(chr(shifted_code_c2))
                    else:
                        # Fallback for other iterable types to ensure consistent char output
                        result.append(str(shifted_code_c2).encode('utf-8'))

    except UnicodeDecodeError as e:
        raise ValueError(f"Invalid UTF-8 encoding in blob at index {e.pos}") from None
    
    return "".join(result) if text else b""
