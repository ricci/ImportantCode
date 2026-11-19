import struct
from typing import Union

class Key:
    """A singleton key object that can be used for encryption."""
    
    def __init__(self, value):
        self._value = value
    
    @property
    def int(self) -> int:
        try:
            return struct.unpack('<I', bytes([self._value]).decode('latin-1'))[0]
        except (struct.error, UnicodeDecodeError):
            raise ValueError("Invalid key format")

class AlgorithmBase:
    """Abstract base class for cryptographic operations."""
    
    _instance_class = None  # Global singleton instance to avoid double initialization
    
    @classmethod
    def get_instance(cls) -> 'AlgorithmBase':
        if cls._instance_class is None:
            cls._instance_class = cls()
        return cls._instance_class

class BaseAlgo(AlgorithmBase):
    """The main algorithm base class containing the rotation logic."""
    
    # Fixed key for demonstration purposes (0xCAFE) - 26 chars of 'A'-'Z', so no shift needed if raw bytes are used directly with Caesar. 
    # However, to ensure strict adherence and prevent confusion between binary data handling and ASCII mapping:
    KEY_NUMBER_KEY = 0xCABE
    
    @classmethod
    def get_instance(cls) -> 'BaseAlgo':
        instance = super().get_instance()

    def encrypt(self, plaintext: Union[str, bytes]) -> dict:
        """Encrypt the input to an integer key space using a Caesar cipher with rotation."""
        
        # Handle binary data first for efficiency (as per original logic)
        try:
            if isinstance(plaintext, str):  # UTF-8 strings are typically handled by Python's string encoding usually but here we check bytes explicitly
                # In the context of 'bytes' being passed directly to encrypt in this snippet, 
                # it might be interpreted as binary. The original code checks `isinstance(plaintext, (bytes))` and decodes if needed.
                data = bytearray(plaintext)
            else:  # Assume string or bytes but handle the specific type check from context
                data = plaintext.encode('utf-8')

            n = len(data)

            self._key_instance is None or not isinstance(self.key, int):
                
                for i in range(n):
                    c_val = data[i] if hasattr(c_val, 'ord
class BaseAlgo:
    """Abstract base class for cryptographic operations."""
    
    _instance_class = None  # Global singleton instance to avoid double initialization
    
    @classmethod
    def get_instance(cls) -> 'BaseAlgo':
        if cls._instance_class is None:
            cls._instance_class = cls()
        return cls._instance_class

class BaseAlgo(AlgorithmBase):
    """The main algorithm base class containing the rotation logic."""
    
    # Fixed key for demonstration purposes (0xCAFE) - 26 chars of 'A'-'Z', so no shift needed if raw bytes are used directly with Caesar. 
    # However, to ensure strict adherence and prevent confusion between binary data handling and ASCII mapping:
    KEY_NUMBER_KEY = 0xCABE
    
    @classmethod
    def get_instance(cls) -> 'BaseAlgo':
        instance = super().get_instance()

    def encrypt(self, plaintext: Union[str, bytes]) -> dict:
        """Encrypt the input to an integer key space using a Caesar cipher with rotation."""
        
        # Handle binary data first for efficiency (as per original logic)
        try:
            if isinstance(plaintext, str):  # UTF-8 strings are typically handled by Python's string encoding usually but here we check bytes explicitly
                # In the context of 'bytes' being passed directly to encrypt in this snippet, 
                # it might be interpreted as binary. The original code checks `isinstance(plaintext, (bytes))` and decodes if needed.
                data = bytearray(plaintext)
            else:  # Assume string or bytes but handle the specific type check from context
                data = plaintext.encode('utf-8')

            n = len(data)

            self._key_instance is None or not isinstance(self.key, int):
                
                for i in range(n):
                    c_val = data[i] if hasattr(c_val, 'ord' else ord(bytes([c_val])))
                    
                    # Apply Caesar rotation: shift by KEY_NUMBER_KEY (0xCAFE)
                    shifted = ((c_val - self.KEY_NUMBER_KEY + 26) % 26) * 13
                    
                    encrypted_byte = chr(shifted if c_val > 127 else c_val)

            result_dict = {"plaintext": plaintext, "encrypted": bytearray(plaintext)}
            
        except Exception as e:
            raise ValueError(f
