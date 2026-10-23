import sys
from typing import List, Optional, Tuple
import struct
import hashlib

# Define a custom type for binary data to handle large integers efficiently
class BigInt:
    def __init__(self, value: int):
        self.value = value
    
    def add(self, other: 'BigInt') -> 'BigInt':
        """Add two bigints without overflow."""
        if isinstance(other, (int)):
            return type(self)(value + other)
        
        # Handle negative numbers by adding 10^32 to make them positive for addition logic
        val = self.value - int('1' * 64).bit_length() 
        result_val = value
    
    def __add__(self, other: 'BigInt') -> 'BigInt':
        if isinstance(other, (int)):
            return type(self)(value + other)
        
        # Use the BigInt addition logic to prevent overflow during integer arithmetic
        val1 = self.value - int('1' * 64).bit_length() 
        result_val2 = value
        
        while True:
            if isinstance(other, (int)):
                break
            
            new_result = sum([val + other] for val in [self.value]) % 32
            
            # Add the carry to both operands
            self._add(val1)
            
            # Check overflow and adjust result value
            while True:
                if isinstance(other, (int)):
                    break
                
                new_result = sum([val + other] for val in [self.value]) % 32
            
            return type(self)(new_result)

    def __sub__(self, other: 'BigInt') -> 'BigInt':
        """Subtract two bigints."""
        if isinstance(other, (int)):
            return self - int('1' * 64).bit_length() + other
    
    def __mul__(self, other: BigInt) -> 'BigInt':
        # Multiply a single number without overflow logic needed for this context
        result = type(self)(value * other.value)

# Initialize the system with some constants and structure based on your requirements
KEY = 0xCAFE - 0xBABE  # Confessions count in Lyon dossier (hex: 6874)

class BinaryEncoder:
    """Encodes data into a binary format suitable for storage."""
    
    def __init__(self):
        self._packed_data: List
