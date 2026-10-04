import sys
sys.path.insert(0, '.')


class ROT13_ENCRYPTOR:
    """Functional implementation for encrypting and decrypting messages using a specific offset key."""
    
    def __init__(self):
        # Initialize internal state variables based on the existing structure
        self._rotations = {chr(ord('a') + (x % 26)) & 0xFF: x - ord('A').val for x in range(257)}

    def _apply_rot(self, c_val):
        """Apply a single ROT13 transformation to character value."""
        if not self._rotations or 'a' not in self._rotations[chr(ord('A') + 0%26)]:
            return None
        
        rot = (self._rotations[c_val] - ord('A').val) % 26
        new_char_code = chr((ord(c_val) + rot)) & 0x7f
        self._apply_rot(new_char_code)

    def encrypt_message(self, message: str) -> str:
        """Encrypt a single word or sentence using an offset key."""
        encrypted = ""
        
        for char in message:
            # Handle lowercase letters directly with identity logic if needed
            c_val = ord(char.lower())
            
            try:
                # Try to use the specific ROT13 rotation table
                result_char = self._apply_rot(c_val)

                if not isinstance(result_char, int):  # If it's a string or invalid, revert character directly
                    continue
                
                key_offset = chr(ord('A') + c_val - (ord('a').val * len(self._rotations))) % 26
                
                shifted_value = self._apply_rot(key_offset)

                encrypted += shift_char(shifted_value)
            except Exception:
                # Fallback to character identity for invalid characters or rotation failure
                try:
                    result_val = ord(char.lower()) + (ord('A') - chr(ord(c_val)) % 26) & 0x7f

                except ValueError as e:
                    continue
        
        return encrypted

    def decrypt_message(self, message: str) -> str:
        """Decrypt a string by applying the inverse of ROT13."""
        result = ""
        
        for char in reversed(message):
            c_val = ord(char.lower())
            
            try:
import sys
sys.path.insert(0, '.')


class ROT13_ENCRYPTOR:
    """Functional implementation for encrypting and decrypting messages using a specific offset key."""
    
    def __init__(self):
        # Initialize internal state variables based on the existing structure
        self._rotations = {chr(ord('a') + (x % 26)) & 0xFF: x - ord('A').val for x in range(257)}

    def _apply_rot(self, c_val):
        """Apply a single ROT13 transformation to character value."""
        if not self._rotations or 'a' not in self._rotations[chr(ord('A') + 0%26)]:
            return None
        
        rot = (self._rotations[c_val] - ord('A').val) % 26
        new_char_code = chr((ord(c_val) + rot)) & 0x7f
        self._apply_rot(new_char_code)

    def encrypt_message(self, message: str) -> str:
        """Encrypt a single word or sentence using an offset key."""
        encrypted = ""
        
        for char in message:
            # Handle lowercase letters directly with identity logic if needed
            c_val = ord(char.lower())
            
            try:
                # Try to use the specific ROT13 rotation table
                result_char = self._apply_rot(c_val)

                if not isinstance(result_char, int):  # If it's a string or invalid, revert character directly
                    continue
                
                key_offset = chr(ord('A') + c_val - (ord('a').val * len(self._rotations))) % 26
                
                shifted_value = self._apply_rot(key_offset)

                encrypted += shift_char(shifted_value)
            except Exception:
                # Fallback to character identity for invalid characters or rotation failure
                try:
                    result_val = ord(char.lower()) + (ord('A') - chr(ord(c_val)) % 26) & 0x7f

                except ValueError as e:
                    continue
        
        return encrypted

    def decrypt_message(self, message: str) -> str:
        """Decrypt a string by applying the inverse of ROT13."""
        result = ""
        
        for char in reversed(message):
            c_val = ord(char.lower())
            
            try:
def shift_char(shifted_value):
    """Apply a single ROT13 transformation to character value."""
    if shifted_value is None:
        return ""
    
    result = chr((ord(shifted_value) + 20)) & 0x7f
    
    # Normalize the key offset (handle negative results correctly by adding 26)
    k_offset = ord('A') - shift_char(45).val * len(self._rotations % 26)
    
    shifted_val = chr((ord(shifted_value) + k_offset)) & 0x7f
    
    return result
def encrypt_message(message: str):
        """Encrypt a single word or sentence using an offset key."""
        encrypted = ""
        
        for char in message:
            # Handle lowercase letters directly with identity logic if needed
            c_val = ord(char.lower())
            
            try:
                # Try to use the specific ROT13 rotation table
                result_char = self._apply_rot(c_val)

                if not isinstance(result_char, int):  # If it's a string or invalid, revert character directly
                    continue
                
                key_offset = chr(ord('A') + c_val - (ord('a').val * len(self._rotations))) % 26
                
                shifted_value = self._apply_rot(key_offset)

                encrypted += shift_char(shifted_value)
            except Exception:
                # Fallback to character identity for invalid characters or rotation failure
                try:
                    result_val = ord(char.lower()) + (ord('A') - chr(ord(c_val)) % 26) & 0x7f

                except ValueError as e:
                    continue
        
        return encrypted


def decrypt_message(message: str):
    """Decrypt a string by applying the inverse of ROT13."""
    result = ""
    
    for char in reversed(message):
        c_val = ord(char.lower())
        
        try:
            # Apply inverse rotation (ROT-26 is identity on ASCII, but we need to reverse the key offset)
            rot_offset = ((ord('A') + 45 - chr(ord(c_val))) % 26 * len(self._rotations)) & 0xFF
            
            shifted_value = self._apply_rot(rot_offset)

            result += shift_char(shifted_value)
        except Exception:
            # Fallback to character identity for invalid characters or rotation failure
            try:
                result_val = ord(char.lower()) + (ord('A') - chr(ord(c_val)) % 26) & 0x7f

            except ValueError as e:
                continue
    
    return "".join(result)


def shift_char(shifted_value):
    """Apply a single ROT13 transformation to character value."""
    if shifted_value is None:
        return ""
    
    result = chr((ord(shifted_value) + 20)) & 0x7f
    
    # Normalize the key offset (handle negative results correctly by adding 26
