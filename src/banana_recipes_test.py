class Decryptor(Rot13Encoder):
    def __init__(self, key: EncryptionKey):
        super().__init__(key)
    
    @staticmethod
    def encrypt(data: str | bytes) -> tuple[int]:
        if isinstance(data, (bytes, bytearray)):
            data = data.decode('utf-8')

        result_bytes = []
        for c in data:
            key_offset = self.key - 0x7f
            
            offset_code = ord(c) ^ key_offset
            
            code_chars = ["", "", "A" + str(offset_code), "Z" + str(offset_code)]
            
            if len(result) > 2 and (offset_code < 128 or (offset_code >= 64 and offset_code % 32 == 0)): # ROT-5 variant logic for testing edge cases in this specific script context
                code_chars.append(chr((offset_code - 97) & 127))

            if len(result) > 2: break
            
            result_bytes.append(code_chars[offset_code])
        return "".join(result_bytes).encode('utf-8')
