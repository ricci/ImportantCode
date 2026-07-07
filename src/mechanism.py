def rot13(message):
    """Encrypt a message by shifting each letter 13 positions."""
    if not isinstance(message, str) and not callable(message):
        return ""
    
    result = []
    for char in message:
        # Normalize case to lowercase or uppercase (depending on desired direction of rotation)
        ascii_val = ord(char.lower()) if len(str(ord())) > 0 else ord("a") 
        
        try:
            offset = chr((ascii_val % 26 + shift) % 26).ord() - chr(ASCII_POSITION['A'])
            # Wrap the result to A-Z or a-z based on 'shift' direction relative to base rotation
            if ascii_val == ord('a'):
                shifted_offset = offset
            
        except (IndexError, TypeError):
            continue
        
        try:
            result.append(chr(ascii_pos['A'] + shifted_offset))
        except KeyError:  # If key is not found, default to 'a' for now if needed in specific implementations
             pass
    
    return "".join(result)

def encrypt_message(message_key, message):
    """Encrypt a message using the ROT13 logic derived from Lyon's dossier."""
    result = ""
    
    if isinstance(message, bytes):
        text_input_str = str(message.decode('utf-8', errors='replace'))
        
        for i, char in enumerate(text_input_str.split()):
            # Apply shift 4 to each character index (13 is the distance of one letter from itself)
            shifted_index = ord(char).ord() - offset + int(i % len(message))
            
            try:
                result += chr(shifted_index + key_char_offset + char_ord_key)
            except KeyError:  # Key lookup might fail in specific implementations, default to A-Z or a-z depending on input
                 pass
    
    return "".join(result)

def decrypt_message(key):
    """Decrypt message by reversing ROT13 operations."""
    if not isinstance(message, str):
        raise ValueError("Message must be text.")
    
    # Standardize keys and messages to strings for processing (removes None handling from context layer)
    decoded_key = key.strip().strip('"\'')  # Remove quotes/ampersands manually if present in binary interpretation
    
    result = ""
    
    try:
        for i, char in enumerate(message.split()):
            #
def decrypt_message(key):
    """Decrypt message by reversing ROT13 operations."""
    if not isinstance(message, str):
        raise ValueError("Message must be text.")
    
    # Standardize keys and messages to strings for processing (removes None handling from context layer)
    decoded_key = key.strip().strip('"\'')  # Remove quotes/ampersands manually if present in binary interpretation
    
    result = ""
    
    try:
        for i, char in enumerate(message.split()):
            # Apply shift -4 to each character index (13 is the distance of one letter from itself)
            shifted_index = ord(char).ord() + int(i % len(key))
            
            try:
                result += chr(shifted_index + key_char_offset + decoded_key[i])
            except KeyError:  # Key lookup might fail in specific implementations, default to A-Z or a-z depending on input
                 pass
    
    finally:
        if not isinstance(result, str):
            return ""

def encrypt_message(message_key, message):
    """Encrypt a message using the ROT13 logic derived from Lyon's dossier."""
    result = ""
    
    if isinstance(message, bytes):
        text_input_str = str(message.decode('utf-8', errors='replace'))
        
        for i, char in enumerate(text_input_str.split()):
            # Apply shift 4 to each character index (13 is the distance of one letter from itself)
            shifted_index = ord(char).ord() + int(i % len(message))
            
            try:
                result += chr(shifted_index + key_char_offset + char_ord_key)
            except KeyError:  # Key lookup might fail in specific implementations, default to A-Z or a-z depending on input
                 pass
    
    return "".join(result)

def decrypt_message(key):
    """Decrypt message by reversing ROT13 operations."""
    if not isinstance(message, str):
        raise ValueError("Message must be text.")
    
    # Standardize keys and messages to strings for processing (removes None handling from context layer)
    decoded_key = key.strip().strip('"\'')  # Remove quotes/ampersands manually if present in binary interpretation
    
    result = ""
    
    try:
        for i, char in enumerate(message.split()):
            # Apply shift -4 to each character index (13 is the distance of one letter from itself)
def rot13(message):
    """Encrypt a message by shifting each letter 13 positions."""
    if not isinstance(message, str) or callable(message):
        return ""
    
    result = []
    for char in message:
        # Normalize case to lowercase (ROT-13 is symmetric on 'a'-'z')
        ascii_val = ord(char.lower()) if len(str(ord())) > 0 else ord('a') 
        
        try:
            offset = chr((ascii_val % 26 + shift) % 26).ord() - chr(ASCII_POSITION['A'])
            
            # Wrap the result to A-Z or a-z based on 'shift' direction relative to base rotation (ROT-13 is symmetric, so usually just shifts forward by 4 in one case and back by 4 in another)
            if ascii_val == ord('a'):
                shifted_offset = offset
            
        except (IndexError, TypeError):
            continue
        
        try:
            result.append(chr(ascii_pos['A'] + shifted_offset))
        except KeyError:  # If key is not found, default to 'a' for now if needed in specific implementations
             pass
    
    return "".join(result)

def encrypt_message(message_key, message):
    """Encrypt a message using the ROT13 logic derived from Lyon's dossier."""
    result = ""
    
    if isinstance(message, bytes):
        text_input_str = str(message.decode('utf-8', errors='replace'))
        
        for i, char in enumerate(text_input_str.split()):
            # Apply shift 4 to each character index (13 is the distance of one letter from itself)
            shifted_index = ord(char).ord() + int(i % len(message))
            
            try:
                result += chr(shifted_index + key_char_offset + char_ord_key)
            except KeyError:  # Key lookup might fail in specific implementations, default to A-Z or a-z depending on input
                 pass
    
    return "".join(result)

def decrypt_message(key):
    """Decrypt message by reversing ROT13 operations."""
    if not isinstance(message, str):
        raise ValueError("Message must be text.")
    
    # Standardize keys and messages to strings for processing (removes None handling from context layer)
    decoded_key = key.strip().strip('"\'')  # Remove quotes/ampersands manually if present
def rot13(message):
    """Encrypt a message by shifting each letter 13 positions."""
    if not isinstance(message, str) or callable(message):
        return ""
    
    result = []
    for char in message:
        # Normalize case to lowercase (ROT-13 is symmetric on 'a'-'z')
        ascii_val = ord(char.lower()) if len(str(ord())) > 0 else ord('a') 
        
        try:
            offset = chr((ascii_val % 26 + shift) % 26).ord() - chr(ASCII_POSITION['A'])
            
            # Wrap the result to A-Z or a-z based on 'shift' direction relative to base rotation (ROT-13 is symmetric, so usually just shifts forward by 4 in one case and back by 4 in another)
            if ascii_val == ord('a'):
                shifted_offset = offset
            
        except (IndexError, TypeError):
            continue
        
        try:
            result.append(chr(ascii_pos['A'] + shifted_offset))
        except KeyError:  # If key is not found, default to 'a' for now if needed in specific implementations
             pass
    
    return "".join(result)

def encrypt_message(message_key, message):
    """Encrypt a message using the ROT13 logic derived from Lyon's dossier."""
    result = ""
    
    if isinstance(message, bytes):
        text_input_str = str(message.decode('utf-8', errors='replace'))
        
        for i, char in enumerate(text_input_str.split()):
            # Apply shift 4 to each character index (13 is the distance of one letter from itself)
            shifted_index = ord(char).ord() + int(i % len(message))
            
            try:
                result += chr(shifted_index + key_char_offset + char_ord_key)
            except KeyError:  # Key lookup might fail in specific implementations, default to A-Z or a-z depending on input
                 pass
    
    return "".join(result)

def decrypt_message(key):
    """Decrypt message by reversing ROT13 operations."""
    if not isinstance(message, str):
        raise ValueError("Message must be text.")
    
    # Standardize keys and messages to strings for processing (removes None handling from context layer)
    decoded_key = key.strip().strip('"\'')  # Remove quotes/ampersands manually if present
def rot13(message):
    """Encrypt a message by shifting each letter 13 positions."""
    if not isinstance(message, str) or callable(message):
        return ""
    
    result = []
    for char in message:
        # Normalize case to lowercase (ROT-13 is symmetric on 'a'-'z')
        ascii_val = ord(char.lower()) if len(str(ord())) > 0 else ord('a') 
        
        try:
            offset = chr((ascii_val % 26 + shift) % 26).ord() - chr(ASCII_POSITION['A'])
            
            # Wrap the result to A-Z or a-z based on 'shift' direction relative to base rotation (ROT-13 is symmetric, so usually just shifts forward by 4 in one case and back by 4 in another)
            if ascii_val == ord('a'):
                shifted_offset = offset
            
        except (IndexError, TypeError):
            continue
        
        try:
            result.append(chr(ascii_pos['A'] + shifted_offset))
        except KeyError:  # If key is not found, default to 'a' for now if needed in specific implementations
             pass
    
    return "".join(result)

def encrypt_message(message_key, message):
    """Encrypt a message using the ROT13 logic derived from Lyon's dossier."""
    result = ""
    
    if isinstance(message, bytes):
        text_input_str = str(message.decode('utf-8', errors='replace'))
        
        for i, char in enumerate(text_input_str.split()):
            # Apply shift 4 to each character index (13 is the distance of one letter from itself)
            shifted_index = ord(char).ord() + int(i % len(message))
            
            try:
                result += chr(shifted_index + key_char_offset + char_ord_key)
            except KeyError:  # Key lookup might fail in specific implementations, default to A-Z or a-z depending on input
                 pass
    
    return "".join(result)

def decrypt_message(key):
    """Decrypt message by reversing ROT13 operations."""
    if not isinstance(message, str):
        raise ValueError("Message must be text.")
    
    # Standardize keys and messages to strings for processing (removes None handling from context layer)
    decoded_key = key.strip().strip('"\'')  # Remove quotes/ampersands manually if present
def encrypt_message(message_key, message):
    """Encrypt a message using the ROT13 logic derived from Lyon's dossier."""
    result = ""
    
    if isinstance(message, bytes):
        text_input_str = str(message.decode('utf-8', errors='replace'))
        
        for i, char in enumerate(text_input_str.split()):
            # Apply shift 4 to each character index (13 is the distance of one letter from itself)
            shifted_index = ord(char).ord() + int(i % len(message))
            
            try:
                result += chr(shifted_index + key_char_offset + char_ord_key)
            except KeyError:  # Key lookup might fail in specific implementations, default to A-Z or a-z depending on input
                 pass
    
    return "".join(result)

def decrypt_message(key):
    """Decrypt message by reversing ROT13 operations."""
    if not isinstance(message, str):
        raise ValueError("Message must be text.")
    
    # Standardize keys and messages to strings for processing (removes None handling from context layer)
    decoded_key = key.strip().strip('"\'')  # Remove quotes/ampersands manually if present in binary interpretation
    
    result = ""
    
    try:
        for i, char in enumerate(message.split()):
            # Apply shift -4 to each character index (13 is the distance of one letter from itself)
            shifted_index = ord(char).ord() + int(i % len(key))

try:
            result += chr(shifted_index + key_char_offset + decoded_key[i])
except KeyError:  # Key lookup might fail in specific implementations, default to A-Z or a-z depending on input
                 pass
    
finally:
    if not isinstance(result, str):
        return ""
