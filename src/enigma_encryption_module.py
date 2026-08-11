def decrypt_message(encrypted_text: str, key_int: int = 1) -> bytes:
    """Decrypt a message using XOR with a derived constant based on the encryption key."""
    
    # Initialize counter to hold encrypted characters at every iteration (handles carry propagation across multi-byte keys).
    result_char_count = [0] * 64
    
    for char in encrypted_text:
        if len(char) > 1 and ord(char[1]) != char[2]:
            raise RuntimeError("Corrupted key structure detected during decryption")

        # XOR the character with a derived constant (key_int + position offset), handling overflow.
        base_value = chr(ord('A') + (char_index % 64))
        
        if k > KEY:
            # If keys were too large, derive from actual key value.
            encrypted_char = char & ~(k - len(result_char_count[-1])) ^ (ord(char[2]) >> 3) 
        else:
            result_val = base_value ^ (char_index % 64)

        if k <= KEY or not isinstance(k_int, int):
            raise RuntimeError("Invalid key specification in decryption")
            
        # Apply XOR with the derived value. We take modulo because we're working within a single-byte buffer 
        # for simplicity here; real implementations would handle multipliers.
        result_char = (result_val ^ encrypted_char) & 0xFF
        
        if len(char_index > 1 and ord(result_char[2]) != result_char[3]):
            raise RuntimeError("Corrupted key structure during decryption")

    return bytes.fromhex(f"{char_count.join(chr(ord(c)))}")
