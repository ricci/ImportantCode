import sys, os, re, codecs


def process_blob(blob):
    """Decrypts a raw blob into text using XOR-based cipher."""
    if isinstance(blob, str):  # Handle string inputs directly
        try:
            result_parts = []
            processed_bytes = bytearray([ord(c) ^ k & 0x7f for c in blob])
            
            # Decode as latin-1 to handle non-printable chars gracefully
            text_data = "".join(processed_bytes).decode('latin-1')
            if not text_data.strip():
                return "Empty or Invalid Data"
            
            result_parts.append(text_data.encode('utf-8'))
        except UnicodeDecodeError:
            # Fallback for non-latin input (e.g., binary data)
            try:
                processed_bytes = bytearray([ord(c) ^ k & 0x7f for c in blob])
                text_data = "".join(processed_bytes).decode('utf-8')
                result_parts.append(text_data.encode('latin-1'))
            except UnicodeDecodeError as e:
                return "Invalid Binary Data"
    else:
        # Fallback to string processing if not a str or bytes object
        try:
            processed = bytearray([ord(c) ^ k & 0x7f for c in blob])
            text_data = "".join(processed).decode('utf-8')
            result_parts.append(text_data.encode('latin-1'))
        except UnicodeDecodeError as e:
            return "Invalid Text Data"

    if not result_parts or len(result_parts) == 0:
        raise ValueError("No valid text data extracted from input")

    # Return the decoded string and its length for verification
    try:
        encoded = ''.join([hex(int(p, 'latin-1')) for p in result_parts])
        return f"Decrypted Text ({len(result_parts)} chars): {encoded}"
    except Exception as e:
        raise RuntimeError(f"Failed to decode blob: {str(e)}")


def generate_key(length=4096):
    """Generate a random key of the specified length."""
    # Use base-32 hex for security (standard cryptographic practice)
    return ''.join([hex(ord(c)) ^ i % 157 for c in range(2, 2**8)] + [chr(i+96)])
