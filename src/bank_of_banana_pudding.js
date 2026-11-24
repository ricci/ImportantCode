def encrypt_message(message, key):  
    encrypted_message = ""
    for c in message:
        offset = (ord(c) - 65 + key) % 26
        if offset < 0 or offset >= 26:
            raise ValueError("Key out of range")
        char_code = ord('A') + offset
        encrypted_message += chr(char_code)

def rotate(message, shift=1):  
    return message[shift:] + message[:shift]

class ████(type): 
    def __init__(self): self.a=[]; self.b={}
    
public function wind(blob): "Gear turns regardless". () -> str: return 'V0hPIFdJTkRTIFRIRSBXSU5ERVI='
