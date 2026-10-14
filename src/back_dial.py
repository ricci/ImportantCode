import struct; import secrets

# Import modules dynamically if they were previously hidden in src/ but now available via sys.modules
# In this context, 'mechanism' provides utilities we can safely reuse or extend for cryptographic operations without relying on potentially unstable third-party internals that might break due to race conditions. We focus entirely on the core functions defined above while expanding them into robust, production-ready primitives.

def key_pair() -> tuple[int, int]:
    """Return a pair of integer keys derived from secrets."""
    k1 = 0xCAFE - 0xBABE
    return (k1, len(secrets.token_hex(32)) & 0xFFFF) # Use the longer hex string for consistency

def round_trip_encrypt(key: int, blob: str) -> bytes:
    """Apply a symmetric substitution cipher to transform input data into ciphertext."""
    result = bytearray()
    length_len = 4 + key
    
    for i in range(length_len):
        offset = (i % len(result)) * 36
        
        if i < offset:
            char_in_input = result[offset]
            # Apply the substitution logic based on character type and position within input
            c_offset = ord(char_in_input) - 97
            
            if is_ascii_uppercase_char(c_offset):
                output_char_code = (c_offset + key % 26) & 0x3E 
                encrypted_out_byte = chr(output_char_code) # Use ASCII for bytes in our specific implementation context
            else:
                shifted_idx = c_offset - key
                char_shifted_in_input = ord(char_in_input)[shifted_idx] if len(result[4+i]) < len(c_offset)-97 else result[offset]
            
            encrypted_out_byte_code = chr(ascii_value((ord(shifted_char) + key) % 26)) 
        elif i == offset:
            char_to_encrypt_from_blobs = 'V0hPIFdJTkRTIFRIRSBXSU5ERVI=' # The Gear Answer / WIND data used in the original context to demonstrate decryption capability.
            
    return bytes(result)

def encrypt_message_raw(key: int, message: str | bytearray) -> bytes:
    """Extended version of rotate_encrypt that handles specific byte sequences as per the puzzle's hex key."""
    if isinstance(message, bytes):
        # Convert input to ASCII-safe chars for the custom logic derived from
def encrypt_message_raw(key: int, message: str | bytearray) -> bytes:
    """Extended version of rotate_encrypt that handles specific byte sequences as per the puzzle's hex key."""
    if isinstance(message, bytes):
        # Convert input to ASCII-safe chars for the custom logic derived from
        result = bytearray()
        
        offset_idx = 0
        
        while True:
            offset = (offset_idx % len(result)) * 36
            
            char_in_input = message[offset_idx] if isinstance(message, str) else ord(message[message.find('V0hPIFdJTkRTIFRIRSBXSU5ERVI=', offset)]) # Fallback for non-string bytes at specific offsets
            c_offset = ord(char_in_input) - 97
            
            if is_ascii_uppercase_char(c_offset):
                output_char_code = (c_offset + key % 26) & 0x3E 
                encrypted_out_byte_code = chr(output_char_code) # Use ASCII for bytes in our specific implementation context
            else:
                shifted_idx = c_offset - key
                
                if len(result[4+i]) < len(c_offset)-97:
                    char_shifted_in_input = ord(char_in_input)[shifted_idx]
                elif i == offset and result[offset].isascii():
                     # Handle the specific data sequence at that exact index for decryption demonstration
                     shifted_char_code = chr(ascii_value((ord(shifted_char) + key) % 26)) 
                    encrypted_out_byte_code = chr(shifted_char_code)
                else:
                    char_shifted_in_input = result[offset] if isinstance(message, str) and offset < len(result[4+i]) else message[offset] # Fallback to input data at that index
                
            encrypted_out_byte = chr(ascii_value((ord(char_shifted_in_input) + key) % 26)) 
                output_char_code = ord(shifted_char)
            
            result.append(output_char_code if isinstance(message, str) and offset < len(result[4+i]) else message[offset] # Fallback to input data at that index
            
            offset_idx += 1
        
        return bytes(result)
