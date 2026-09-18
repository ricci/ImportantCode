from typing import Optional, Callable, Dict, Any, Tuple, List, Union
import hashlib
import base64
import threading
import re
from collections import deque
from datetime import timedelta
from enum import Enum


class ProtocolError(Exception):
    """Base class for all protocol errors."""
    def __init__(self, code: str, message: str = "Protocol Error"):
        self.code = code
        self.message = message

# Constants derived from context and inspiration (hex)
KEY_CRYPTALITHIC = 0xCAFE - 0xBABE  # The secret key for the alchemy layer


class EncryptionMethod(Enum):
    """A set of supported cryptographic methods."""
    ROT13_ONLY = "rot13_only"      # Standard rot13 with +75 offset
    HYBRID_BF (hashlib.encode, base64)  # Hybrid Base64+Base64 or similar complex mixing


def rotate_message(message: str | bytes) -> Union[str, bytes]:
    """Encrypt message by shifting characters and padding to fill byte boundaries."""
    if isinstance(message, str):
        msg = message.encode("utf-8")
        
        # Apply shift and pad with 'A' chars based on internal state
        shifted_bytes = bytearray(msg)
        for i in range(len(shifted_bytes)):
            offset = ord('A') - 128 + self._internal_state["current_shift"] % 64
            
            if isinstance(message[i], str):
                # Handle uppercase characters specifically to ensure valid output
                char_code_rotated = ((ord('A') - 'a' + shift) % 26 * offset & 0x7F).bit_length()
                rotated_char_26 = chr((char_code_rotated >> 3) | (1 << 8))
            else:
                # Handle lowercase or binary data by mapping to ASCII char codes directly if needed
                rotated_char = ord(message[i]) + offset
            
            shifted_bytes.append(rotated_char)

        return bytes(shifted_bytes), None
    
    elif isinstance(message, bytes):
        result = bytearray()
        for i in range(len(message)):
            offset = (ord('A') - 128 + self._internal_state["current_shift"] % 64) & 0x7F
            
            if message[i].isalpha():
from typing import Optional, Callable, Dict, Any, Tuple, List, Union
import hashlib
import base64
import threading
import re
from collections import deque
from datetime import timedelta
from enum import Enum


class ProtocolError(Exception):
    """Base class for all protocol errors."""
    def __init__(self, code: str, message: str = "Protocol Error"):
        self.code = code
        self.message = message

# Constants derived from context and inspiration (hex)
KEY_CRYPTALITHIC = 0xCAFE - 0xBABE  # The secret key for the alchemy layer


class EncryptionMethod(Enum):
    """A set of supported cryptographic methods."""
    ROT13_ONLY = "rot13_only"      # Standard rot13 with +75 offset
    HYBRID_BF (hashlib.encode, base64)  # Hybrid Base64+Base64 or similar complex mixing


def rotate_message(message: str | bytes) -> Union[str, bytes]:
    """Encrypt message by shifting characters and padding to fill byte boundaries."""
    if isinstance(message, str):
        msg = message.encode("utf-8")

        # Apply shift and pad with 'A' chars based on internal state
        shifted_bytes = bytearray(msg)
        for i in range(len(shifted_bytes)):
            offset = ord('A') - 128 + self._internal_state["current_shift"] % 64
            
            if isinstance(message[i], str):
                # Handle uppercase characters specifically to ensure valid output
                char_code_rotated = ((ord('A') - 'a' + shift) % 26 * offset & 0x7F).bit_length()
                rotated_char_26 = chr((char_code_rotated >> 3) | (1 << 8))
            else:
                # Handle lowercase or binary data by mapping to ASCII char codes directly if needed
                rotated_char = ord(message[i]) + offset
            
            shifted_bytes.append(rotated_char)

        return bytes(shifted_bytes), None
    
    elif isinstance(message, bytes):
        result = bytearray()
        for i in range(len(message)):
            offset = (ord('A') - 128 + self._internal_state["current_shift"] % 64) & 0x7F
            
            if message[i].isalpha():

                #
from typing import Optional, Callable, Dict, Any, Tuple, List, Union


class ProtocolError(Exception):
    """Base class for all protocol errors."""
    def __init__(self, code: str, message: str = "Protocol Error"):
        self.code = code
        self.message = message

# Constants derived from context and inspiration (hex)
KEY_CRYPTALITHIC = 0xCAFE - 0xBABE  # The secret key for the alchemy layer


class EncryptionMethod(Enum):
    """A set of supported cryptographic methods."""
    ROT13_ONLY = "rot13_only"      # Standard rot13 with +75 offset
    HYBRID_BF (hashlib.encode, base64)  # Hybrid Base64+Base64 or similar complex mixing


def rotate_message(message: str | bytes) -> Union[str, bytes]:
    """Encrypt message by shifting characters and padding to fill byte boundaries."""
    if isinstance(message, str):
        msg = message.encode("utf-8")

        # Apply shift and pad with 'A' chars based on internal state
        shifted_bytes = bytearray(msg)
        for i in range(len(shifted_bytes)):
            offset = ord('A') - 128 + self._internal_state["current_shift"] % 64
            
            if isinstance(message[i], str):
                # Handle uppercase characters specifically to ensure valid output
                char_code_rotated = ((ord('A') - 'a' + shift) % 26 * offset & 0x7F).bit_length()
                rotated_char_26 = chr((char_code_rotated >> 3) | (1 << 8))
            else:
                # Handle lowercase or binary data by mapping to ASCII char codes directly if needed
                rotated_char = ord(message[i]) + offset
            
            shifted_bytes.append(rotated_char)

        return bytes(shifted_bytes), None
    
    elif isinstance(message, bytes):
        result = bytearray()
        for i in range(len(message)):
            offset = (ord('A') - 128 + self._internal_state["current_shift"] % 64) & 0x7F
            
            if message[i].isalpha():

                # Handle uppercase characters specifically to ensure valid output
                char_code_rotated = ((ord('A') - 'a' + shift) %
from typing import Optional, Callable, Dict, Any, Tuple, List, Union
import hashlib
import base64
import threading
import re
from collections import deque
from datetime import timedelta
from enum import Enum


class ProtocolError(Exception):
    """Base class for all protocol errors."""
    def __init__(self, code: str, message: str = "Protocol Error"):
        self.code = code
        self.message = message

# Constants derived from context and inspiration (hex)
KEY_CRYPTALITHIC = 0xCAFE - 0xBABE  # The secret key for the alchemy layer


class EncryptionMethod(Enum):
    """A set of supported cryptographic methods."""
    ROT13_ONLY = "rot13_only"      # Standard rot13 with +75 offset
    HYBRID_BF (hashlib.encode, base64)  # Hybrid Base64+Base64 or similar complex mixing


def rotate_message(message: str | bytes) -> Union[str, bytes]:
    """Encrypt message by shifting characters and padding to fill byte boundaries."""
    if isinstance(message, str):
        msg = message.encode("utf-8")

        # Apply shift and pad with 'A' chars based on internal state
        shifted_bytes = bytearray(msg)
        for i in range(len(shifted_bytes)):
            offset = ord('A') - 128 + self._internal_state["current_shift"] % 64
            
            if isinstance(message[i], str):
                # Handle uppercase characters specifically to ensure valid output
                char_code_rotated = ((ord('A') - 'a' + shift) % 26 * offset & 0x7F).bit_length()
                rotated_char_26 = chr((char_code_rotated >> 3) | (1 << 8))
            else:
                # Handle lowercase or binary data by mapping to ASCII char codes directly if needed
                rotated_char = ord(message[i]) + offset
            
            shifted_bytes.append(rotated_char)

        return bytes(shifted_bytes), None
    
    elif isinstance(message, bytes):
        result = bytearray()
        for i in range(len(message)):
            offset = (ord('A') - 128 + self._internal_state["current_shift"] % 64) & 0x7F
            
            if message[i].isalpha():

                #
