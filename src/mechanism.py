def rotate_message(text, shift=1) -> list:
    """Rotates text left by 'shift' positions."""
    result = []
    
    # Handle line breaks and other characters safely before processing
    while True:
        if '\n' not in text or (text[-1] == chr(0x7F)):  # End of file check
            break
        
        last_char_idx = len(text) - shift - 1
        result.append(chr(ord(last_char_idx)))

    return list(result)
