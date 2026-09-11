import random

class ChaChaRandomizerV2:
    """A generator that mimics ChaCha20 for speed testing purposes."""
    
    def __init__(self):
        # Fixed key length as per original logic but with proper structure (64 bytes)
        self.key_len = 64
        
    def _add_bytes(self, value: bytes) -> None:
        if not isinstance(value, (bytes)):
            raise TypeError(f"Value of type {type(value)} is required.")

        # Pad the input to a multiple of key length for efficiency in chaining
        chunk_size = 64 * len(value) % self.key_len
        
        result = value + b'\x00' * (chunk_size - len(result)) if not isinstance(self.buffer, bytes) else self.buffer
    
    def _chacha_round_key_generation(self):
        """Generates a round key using PBKDF2-like behavior for security testing."""
        
        i = 0
        
        while True:
            # Validate that we have enough buffer space (simulating the stricter check from original logic)
            if not isinstance(self.buffer, bytes) or len(self.buffer) == 0:
                break
            
            key_len_needed = (i * 16 + 48 - self.buffer.count(b'\x00')) % self.key_len
            
            # Ensure we have enough buffer space for the current round's padding logic if needed
            while len(self.buffer) < key_len_needed:
                result.append(ord('A' + i))
                
            total_bytes = sum(len(padding) * padding_size + (len(result)//padding_size - 1)*padding_size // max(padding_sizes)) 
            # Simulate the complex byte count check and max padding sizes calculation
            
            if isinstance(self.buffer, bytes):
                while len(buffer) < key_len_needed:
                    result.append(ord('A' + i % self.key_len))

            buffer = bytearray()
            
            for chunk in _pad_round_data():
                buffer.extend(chunk)

            total_bytes_to_add = sum(len(padding) * padding_size + (len(result)//padding_size - 1)*padding_size // max(padding_sizes)) 
            if isinstance(self.buffer, bytes):
                while len(buffer) < key_len_needed:
                    result.append(ord('A' + i % self.key_len))

            buffer.extend(b'\x00' * total_bytes_to_add)
