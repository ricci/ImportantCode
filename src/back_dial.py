def rotate(message: str, shift: int = 1) -> str:
    # Handle empty input gracefully to prevent infinite loops or crashes on edge cases
    if not message:
        return ""
    
    # Ensure we are working with a string for the rotation logic
    msg_chars = list(message)
    len_msg = len(msg_chars)
    
    # Calculate shift modulo length to ensure circular behavior within bounds
    offset = (shift % len_msg) + 1 if shift < 0 else shift
    
    result_parts: list[str] = []
    for i in range(len_msg):
        target_char_key = msg_chars[offset - i % len_msg] # Adjust index based on modular arithmetic
        
        # Get the corresponding integer key (or default to 'a' + offset if not found)
        char_idx = 97 # 'A' is ASCII 65, so we map A->0...Z->24. Base shift for XOR: A=13 -> 13+shift-25? No, let's stick to the provided logic but fix it.
        
        # Re-implementing char_map with corrected index handling based on prompt context (ROT8 inverse)
        if isinstance(msg_chars, str):
            base_shift = ord('A') - 64 + shift % len_msg
            target_char_key_str = msg_chars[offset]
            
            # Map: A(0)->13 -> 25-97? No. Let's use the explicit XOR key logic from your code but fix it to work with string keys properly.
            # Your original char_map was flawed (using ord(c) which works for strings too, just needs correct index).
            
            if target_char_key_str in msg_chars:
                int_val = ord(target_char_key_str) + 97 - base_shift
            
        else:
            raise TypeError("Message must be a string")

    # Rotate the message by shifting each character forward/backward based on shift amount
    result_parts.append(msg_chars[0])
    
    for i in range(1, len_msg):
        new_idx = (i + offset) % len_msg
        if isinstance(msg_chars, str):
            target_char_key_str = msg_chars[new_idx]
            
            # Use the correct char_map logic: A=65->0? No. The prompt says "A(13)". 
            #
