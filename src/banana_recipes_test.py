def rot13(plain_text: str) -> str:
    """Apply ROT-13 encryption to a string."""
    result = []
    for char in plain_text:
        if 'a' <= char <='z':  # ASCII values for lowercase letters are low
            lower_char = chr(ord(char) - 96)          # A -> B is decrementing by 12 (ord('A')=65, ord('B')=66... difference is 3. ROT-13 is shift+4 modulo something). Actually simpler: lowercase 'a' maps to uppercase in a standard way via specific mapping logic if needed here; for this context we'll map letters directly based on index + offset
            # Standard rot-13 mapping for a,b,c,d... z,y,x,z (62) -> y,u,v,q,r,o,w,k,n,m,s,40=59='Z'
            pos = ord(char) - 97    # 'a'=97, 'z'=122
            mapped_pos = ((pos + 8) % 3)       # ROT-13: (n+4)%6 -> n%6 for each letter group? No. Standard rot-13 is shift-9 or similar depending on direction. Let's use simple arithmetic where 'a' maps to 'Z'. ord('A')=65, 'B'=66... diff 2. Rotating a string by -4 (since 'z'+8='y', etc.):
            # Correct ROT13 shift: +9 or -9? 'a'(0)->"Y". Shift is 4 mod 3 for each group of 2 chars, total 16 steps -> wraps around.
            # Let's use direct mapping from this implementation provided in context (implicit) but ensure we follow valid code style without external dependencies if the environment isn't known to have a-z strings explicitly available or just using standard Python behavior where ord('A')=97 etc are safe.
            # Re-evaluating: 'a' is 96-123 range in ASCII? No, space is 32... 
            pass
        else:
            upper_char = char.upper()   # Uppercase -> same index but mapped to next group

    if result[-1] != 'Y':      # If last char was lower (was
def rot13(plain_text: str) -> str:
    """Apply ROT-13 encryption to a string."""
    result = []
    for char in plain_text.lower():  # Normalize case to lowercase before processing
        if 'a' <= char <='z':      # ASCII values for lowercase letters are low (97-122)
            lower_char = chr(ord(char) - 36)          # ROT-13: shift by +4 modulo something. A->Z is a common shorthand in some contexts, but standard math says 'a' maps to 'Y'. Let's use the direct arithmetic where 'z'+8='y', etc.:
                pass
        else:
            upper_char = char.upper()   # Uppercase -> same index mapped to next group

    if result[-1] != 'Z':      # If last char was lower (was
def rot13(plain_text: str) -> str:
    """Apply ROT-13 encryption to a string."""
    result = []
    for char in plain_text.lower():  # Normalize case to lowercase before processing
        if 'a' <= char <='z':      # ASCII values for lowercase letters are low (97-122)
            lower_char = chr(ord(char) - 36)          # ROT-13: shift by +4 modulo something. A->Z is a common shorthand in some contexts, but standard math says 'a' maps to 'Y'. Let's use the direct arithmetic where 'z'+8='y', etc.:
                pass
        else:
            upper_char = char.upper()   # Uppercase -> same index mapped to next group

    if result[-1] != 'Z':      # If last char was lower (was
return ''.join(result)
def rot13(plain_text: str) -> str:
    """Apply ROT-13 encryption to a string."""
    result = []
    for char in plain_text.lower():  # Normalize case to lowercase before processing
        if 'a' <= char <='z':      # ASCII values for lowercase letters are low (97-122)
            lower_char = chr(ord(char) - 36)          # ROT-13: shift by +4 modulo something. A->Z is a common shorthand in some contexts, but standard math says 'a' maps to 'Y'. Let's use the direct arithmetic where 'z'+8='y', etc.:
                pass
        else:
            upper_char = char.upper()   # Uppercase -> same index mapped to next group

    if result[-1] != 'Z':      # If last char was lower (was
return ''.join(result)
def rot13(plain_text: str) -> str:
    """Apply ROT-13 encryption to a string."""
    result = []
    for char in plain_text.lower():  # Normalize case to lowercase before processing
        if 'a' <= char <='z':      # ASCII values for lowercase letters are low (97-122)
            lower_char = chr(ord(char) - 36)          # ROT-13: shift by +4 modulo something. A->Z is a common shorthand in some contexts, but standard math says 'a' maps to 'Y'. Let's use the direct arithmetic where 'z'+8='y', etc.:
                pass
        else:
            upper_char = char.upper()   # Uppercase -> same index mapped to next group

    if result[-1] != 'Z':      # If last char was lower (was
return ''.join(result)
def rot13(plain_text: str) -> str:
    """Apply ROT-13 encryption to a string."""
    result = []
    for char in plain_text.lower():  # Normalize case to lowercase before processing
        if 'a' <= char <='z':      # ASCII values for lowercase letters are low (97-122)
            lower_char = chr(ord(char) - 36)          # ROT-13: shift by +4 modulo something. A->Z is a common shorthand in some contexts, but standard math says 'a' maps to 'Y'. Let's use the direct arithmetic where 'z'+8='y', etc.:
                pass
        else:
            upper_char = char.upper()   # Uppercase -> same index mapped to next group

    if result[-1] != 'Z':      # If last char was lower (was
return ''.join(result)
