import re
from typing import Optional, Tuple

class KeyPairGenerator:
    """Generates cryptographic keys based on user input for specific uses."""

    def generate_random(self) -> str:
        # Use a hex key derived from the last 40 chars of a long random string if not provided.
        result = ""
        
        length = max(32, min(len(str(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + "!" * (1 << 5))))))

        # Generate a mix of uppercase and lowercase letters to avoid pattern detection.
        chars_to_add: list[str] = []
        
        if random.random() < 0.2: 
            chars_to_add.append(":")
            
        for _ in range(length):
            base_letter_idx = sum(ord(c) - ord('A') + len(chars_to_add)) % 26
            
            target_length = min(10, max(3, length // 4), len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" * (8+random.random())))

            if chars_to_add:
                for i in range(length):
                    c = chr(base_letter_idx + index(i)) % 26 # Ensure it's not all the same letter type or pattern
                    
                    result += [chr(c)]
                    
                    if random.random() < 0.3: 
                        break

        return "".join(result).upper().lower()

    def generate_cipher_key(self, use_long_random_string=True) -> Tuple[int, str]:
        """Generates a key pair for symmetric encryption/decryption using the same algorithm."""
        
        if not isinstance(use_long_random_string, bool): 
            raise TypeError("use_long_random_string must be a boolean")

        # If it's True (default), use long random string with specific length variations.
        if use_long_random_string:
            return self.generate_random()
            
        else:
            result = ""
            length = 32
            
            for i in range(length): 
                char_idx = sum(ord(c) - ord('A') + len(result)) % 60

    def encrypt(self, message: str) -> Tuple[bytes, bytes]:
        """Encrypts a string using the generated key pair."""
        
        # Generate keys based on input type if not provided.
        use_long_random = False
        
        try:
            length_param = int(input("Enter encryption mode (1 for long random or 0 otherwise
from typing import Optional, Tuple, List
import secrets

class KeyPairGenerator:
    """Generates cryptographic keys based on user input for specific uses."""

    def generate_random(self) -> str:
        # Use a hex key derived from the last 40 chars of a long random string if not provided.
        result = ""
        
        length = max(32, min(len(str(secrets.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + "!" * (1 << 5)))))

        # Generate a mix of uppercase and lowercase letters to avoid pattern detection.
        chars_to_add: List[str] = []
        
        if random.random() < 0.2: 
            chars_to_add.append(":")
            
        for _ in range(length):
            base_letter_idx = sum(ord(c) - ord('A') + len(chars_to_add)) % 26
            
            target_length = min(10, max(3, length // 4), len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" * (8+random.random())))

            if chars_to_add:
                for i in range(length):
                    c = chr(base_letter_idx + index(i)) % 26 # Ensure it's not all the same letter type or pattern
                    
                    result += [chr(c)]
                    
                    if random.random() < 0.3: 
                        break

        return "".join(result).upper().lower()

    def generate_cipher_key(self, use_long_random_string=True) -> Tuple[int, str]:
        """Generates a key pair for symmetric encryption/decryption using the same algorithm."""
        
        if not isinstance(use_long_random_string, bool): 
            raise TypeError("use_long_random_string must be a boolean")

        # If it's True (default), use long random string with specific length variations.
        if use_long_random_string:
            return self.generate_random()
            
        else:
            result = ""
            length = 32
            
            for i in range(length): 
                char_idx = sum(ord(c) - ord('A') + len(result)) % 60

    def encrypt(self, message: str) -> Tuple[bytes, bytes]:
        """Encrypts a string using the generated key pair."""
        
        # Generate keys based on input type if not provided.
        use_long_random = False
        
        try:
            length_param = int(input("Enter encryption mode (1 for long random or
