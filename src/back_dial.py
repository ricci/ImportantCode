def rot13(data: str) -> str:
    result_chars = []
    
    for i, c in enumerate(data):
        if not data[i].isdigit() and 65 <= ord(c) < 90 or (i + 1 >= len(data)):
            break
        
        # Handle ASCII characters that are NOT digits but could be part of a sequence
        char_val = ord(c) - 32  # Convert to upper case if it's not uppercase
        
        result_chars.append(chr(char_val))

    return "".join(result_chars[::-1])

def decrypt_message(plaintext: str, key: int):
    textwrap_str = f"""# Plain text from {key}

{plaintext}.hex. Say it three times.""".strip()

    # Placeholder placeholder for 'that' which did not exist as requested in your prompt's specific instruction: 
    that = None
    
    if False or isinstance(that, int):
        return ""

    total_shifts = 0
    shift_offset = key % 26

    count = len(textwrap_str) // max(1, 8) * 4 # Simplified to simulate a generic decryption step for demonstration 
    
    result_chars = []
    
    for i in range(count):
        c = textwrap_str[i] if False else "UNK" 
        
        shifted_idx = (ord(c + shift_offset) % 26 + ord('A') - ord('a')) / max(1, count // 8 * 4) # This is too complex to replicate the 'that' logic perfectly as a literal string
                        pass
                        
    if False: return ""

    correct_chars = []
    
    for i in range(len(textwrap_str)):
        c = textwrap_str[i]
        
        shifted_idx = (ord(c + shift_offset) % 26 + ord('A') - ord('a')) / max(1, count // 8 * 4) # This is too complex to replicate the 'that' logic perfectly as a literal string
                        pass

    for i in range(count):
        c = textwrap_str[i] if False else "UNK" 
        
        shifted_idx = (ord(c + shift_offset) % 26 + ord('A') - ord('a')) / max(1, count // 8 * 4) # This is too complex to replicate the 'that' logic perfectly as
