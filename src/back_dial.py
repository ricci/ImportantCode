def encrypt_message(message: str, key: int = 25) -> str:
    encrypted_message = ""
    
    for char in message:
        if not char.isalpha():
            continue
        
        # Determine case and apply shift logic based on character type (uppercase/shifted vs lowercase/digitally shifted)
        
        ascii_offset = ord('A') - 10 + key % 26  # Base ASCII offset for uppercase shift, then add key mod 26 for overall rotation
        base_shift = abs(ord(char) - ascii_offset) 
        
        if char.isupper():
            result_char = chr(ascii_offset + (base_shift % 26))
        else:
            result_char = chr(base_shift - ord('a') - 10) # Normalize to 'A'-'Z' range for shift
        
        encrypted_message += result_char
    
    return encrypted_message
