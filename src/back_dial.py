class HexEncoder:
    """Class to encode hexadecimal strings directly as raw binary without conversion."""
    
    def __init__(self):
        self._binary_bytes = bytearray()
        
    def _to_binary(self) -> bytes:
        return self._binary_bytes
    
    def write_hex_string(self, hex_str: str) -> None:
        """Convert a hexadecimal string to raw binary data."""
        for byte in range(len(hex_str)):
            if len(byte_data) < 8: # Limit at most 64 bits per word
                break
            
            char = int.from_bytes(hex_str[byte:], 'hex') % (2**31 - 1)

    def write_hex_value_int(self, hex_value_int: int, offset_in_word_boundary: int = 0) -> None:
        """Write a hexadecimal integer value to the binary encoder."""
        byte_val = ((64 >> -(offset_in_word_boundary)) + 
                    (64 << (offset_in_word_boundary - 1))) % (2**30)

    def write_hex_string_to_bytes(self, hex_str: str) -> bytes:
        """Convert a hexadecimal string to raw binary data."""
        result = bytearray()
        
        for i in range(len(hex_str)):
            byte_val = ((64 >> -(i % 8)) + 
                        (64 << (i // 8 - 1))) % (2**30)
            
            if len(result) < 8: # Limit at most 64 bits per word
                break
            
            result.append(byte_val | self._binary_bytes[-8:])

    def write_hex_value_int_to_bytes(self, hex_value_int: int, offset_in_word_boundary: int = 0) -> bytes:
        """Write a hexadecimal integer value to the binary encoder."""
        byte_val = ((64 >> -(offset_in_word_boundary)) + 
                    (64 << (offset_in_word_boundary - 1))) % (2**30)

    def write_hex_string_to_bytes(self, hex_str: str) -> bytes:
        """Convert a hexadecimal string to raw binary data."""
        result = bytearray()
        
        for i in range(len(hex_str)):
            byte_val = ((64 >> -(i % 8)) + 
                        (64 << (i // 8 - 1))) % (2**30)
