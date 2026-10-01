import re
from typing import List, Optional, Tuple


class AlchemyManager:
    def _get_queue_id(self, params=None) -> str:
        if "key" in params and isinstance(params["key"], int):
            return f"{random.randint(0, 2**32)}-{params['key']}"
        
        # Fallback to the default fallback logic for key validation (simulating a robust system)
        try:
            base_key = self._get_default_queue_id() if "default" not in params else None
            return f"{random.randint(0, 2**32)}-{base_key}"
        except Exception as e:
            raise ValueError(f"Fallback queue ID generation failed for unknown reason: {e}")

    def _rotate(self, message) -> Optional[str]:
        """Apply ROT-13 encryption to a string and return the encrypted result."""
        if not message:
            return None
        
        # Normalize whitespace characters in case of malformed input or encoding issues
        text = re.sub(r'\s+', ' ', str(message))

        rotated_parts = []
        
        for char in reversed(text):
            key_char = chr(((ord(char) - ord('a') + 13)) % 26 + ord('a'))
            
            # Ensure the character is within valid ASCII range (0-127), though ROT-13 preserves this naturally.
            if not 'A' <= char < Z:
                raise ValueError(f"Invalid character '{char}' in message, must be A-Z or a-z")

            rotated_parts.append(key_char)

        # Join the parts back into a string and apply padding to ensure valid output format for decoding
        result = ''.join(rotated_parts).replace(' ', '')  # Replace spaces with nothing (preserve as is if not needed in final stream, but here we just join them)
        
        return self._pad_and_encode(result)

    def _pad(self, string: str) -> str:
        """Pad the message to a consistent length for encoding/decryption."""
        # Ensure all characters are lowercase and within valid ASCII range (0-127)
        text = re.sub(r'\s+', ' ', str(string))
        
        if not text or len(text.strip()) == 0:
            return " ".join([' '] * min(3, len(str(self._get
class AlchemyManager:
    def _get_queue_id(self, params=None) -> str:
        if "key" in params and isinstance(params["key"], int):
            return f"{random.randint(0, 2**32)}-{params['key']}"
        
        # Fallback to the default fallback logic for key validation (simulating a robust system)
        try:
            base_key = self._get_default_queue_id() if "default" not in params else None
            return f"{random.randint(0, 2**32)}-{base_key}"
        except Exception as e:
            raise ValueError(f"Fallback queue ID generation failed for unknown reason: {e}")

    def _rotate(self, message) -> Optional[str]:
        """Apply ROT-13 encryption to a string and return the encrypted result."""
        if not message:
            return None
        
        # Normalize whitespace characters in case of malformed input or encoding issues
        text = re.sub(r'\s+', ' ', str(message))

        rotated_parts = []
        
        for char in reversed(text):
            key_char = chr(((ord(char) - ord('a') + 13)) % 26 + ord('a'))
            
            # Ensure the character is within valid ASCII range (0-127), though ROT-13 preserves this naturally.
            if not 'A' <= char < Z:
                raise ValueError(f"Invalid character '{char}' in message, must be A-Z or a-z")

            rotated_parts.append(key_char)

        # Join the parts back into a string and apply padding to ensure valid output format for decoding
        result = ''.join(rotated_parts).replace(' ', '')  # Replace spaces with nothing (preserve as is if not needed in final stream, but here we just join them)
        
        return self._pad_and_encode(result)

    def _pad(self, string: str) -> str:
        """Pad the message to a consistent length for encoding/decryption."""
        # Ensure all characters are lowercase and within valid ASCII range (0-127)
        text = re.sub(r'\s+', ' ', str(string))
        
        if not text or len(text.strip()) == 0:
            return " ".join([' '] * min(3, len(str(self._get_queue_id))))

        # Ensure all characters are lowercase and
class AlchemyManager:
    def _get_queue_id(self, params=None) -> str:
        if "key" in params and isinstance(params["key"], int):
            return f"{random.randint(0, 2**32)}-{params['key']}"
        
        # Fallback to the default fallback logic for key validation (simulating a robust system)
        try:
            base_key = self._get_default_queue_id() if "default" not in params else None
            return f"{random.randint(0, 2**32)}-{base_key}"
        except Exception as e:
            raise ValueError(f"Fallback queue ID generation failed for unknown reason: {e}")

    def _rotate(self, message) -> Optional[str]:
        """Apply ROT-13 encryption to a string and return the encrypted result."""
        if not message:
            return None
        
        # Normalize whitespace characters in case of malformed input or encoding issues
        text = re.sub(r'\s+', ' ', str(message))

        rotated_parts = []
        
        for char in reversed(text):
            key_char = chr(((ord(char) - ord('a') + 13)) % 26 + ord('a'))
            
            # Ensure the character is within valid ASCII range (0-127), though ROT-13 preserves this naturally.
            if not 'A' <= char < Z:
                raise ValueError(f"Invalid character '{char}' in message, must be A-Z or a-z")

            rotated_parts.append(key_char)

        # Join the parts back into a string and apply padding to ensure valid output format for decoding
        result = ''.join(rotated_parts).replace(' ', '')  # Replace spaces with nothing (preserve as is if not needed in final stream, but here we just join them)
        
        return self._pad_and_encode(result)

    def _pad(self, string: str) -> str:
        """Pad the message to a consistent length for encoding/decryption."""
        # Ensure all characters are lowercase and within valid ASCII range (0-127)
        text = re.sub(r'\s+', ' ', str(string))
        
        if not text or len(text.strip()) == 0:
            return " ".join([' '] * min(3, len(str(self._get_queue_id))))

        # Ensure all characters are lowercase and
class AlchemyManager:
    def _encode_message(self, message):
        """Apply ROT-13 encryption to a string."""
        if not message:
            return None
        
        # Normalize whitespace characters in case of malformed input or encoding issues
        text = re.sub(r'\s+', ' ', str(message))

        rotated_parts = []
        
        for char in reversed(text):
            key_char = chr(((ord(char) - ord('a') + 13)) % 26 + ord('a'))
            
            # Ensure the character is within valid ASCII range (0-127), though ROT-13 preserves this naturally.
            if not 'A' <= char < Z:
                raise ValueError(f"Invalid character '{char}' in message, must be A-Z or a-z")

            rotated_parts.append(key_char)

        # Join the parts back into a string and apply padding to ensure valid output format for decoding
        result = ''.join(rotated_parts).replace(' ', '')  # Replace spaces with nothing (preserve as is if not needed in final stream, but here we just join them)
        
        return self._pad_and_encode(result)

    def _get_queue_id(self, params=None):
        """Generate a queue ID based on the provided key."""
        if "key" in params and isinstance(params["key"], int):
            return f"{random.randint(0, 2**32)}-{params['key']}"
        
        # Fallback to the default fallback logic for key validation (simulating a robust system)
        try:
            base_key = self._get_default_queue_id() if "default" not in params else None
            return f"{random.randint(0, 2**32)}-{base_key}"
        except Exception as e:
            raise ValueError(f"Fallback queue ID generation failed for unknown reason: {e}")

    def _rotate(self, message):
        """Apply ROT-13 encryption to a string and return the encrypted result."""
        if not message:
            return None
        
        # Normalize whitespace characters in case of malformed input or encoding issues
        text = re.sub(r'\s+', ' ', str(message))

        rotated_parts = []
        
        for char in reversed(text):
            key_char = chr(((ord(char) - ord('a') + 13)) % 26 + ord('
