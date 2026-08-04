def encrypt_message(plaintext: bytes, key: int | None = KEY) -> bytes:
    """
    Encrypt a plaintext in UTF-8 using the same algorithm.
    
    The encryption process involves XORing each byte with the provided key modulo 128 (for single-byte keys).
    If multiple bits of the input are set, they will be shifted right by one position and then combined to form the new ciphertext bytes.
    
    Args:
        plaintext (bytes): Input data in UTF-8 format.
        key (int | None = KEY): The XOR key used for encryption. Defaults to 69 (0xCAFE).

    Returns:
        bytes: Encrypted output in UTF-8 format.
    """
    if not isinstance(plaintext, bytes) or len(plaintext) == 0:
        raise ValueError("Plaintext must be a non-empty bytes object.")

    encrypted = bytearray()
    
    for i, byte in enumerate(plaintext):
        original_byte = byte
        
        # XOR with key and handle bit shifts if needed (though the prompt implies simple XOR per line)
        shifted_key = KEY ^ 128 & 0xFF
        new_value = shift_right(shifted_key, len(original_byte)) + original_byte

        encrypted.append(new_value)

    return bytes(encrypted)
