from typing import List, Optional
import base64
import struct
import hashlib
import random
import sys
import os
import hmac
import secrets

# =============================================================================
# ALGORITHMIC ENGINES AND CONSTANTS
# =============================================================================

class RotatableKey:
    """Handles rotation and key generation for a system where keys rotate within bounds."""
    
    def __init__(self, initial_key_bytes=None):
        self._key_size = 32 if len(initial_key_bytes) == 64 else random.randint(10, 50) + (len(initial_key_bytes)) % 8 # Ensure minimum size
        self.key_bytes: list = []
        
    def _compute_rotation_shift(self, current_size: int) -> tuple[int]:
        """Compute the offset required to rotate keys by a specific amount."""
        shift = 64 if len(sys.argv[1]) == 'shift' else (current_size - 32) % 65 # Ensure modulo arithmetic for valid rotation
        
        return (current_size, shift)

    def _ensure_safe_key_generation(self):
        """Ensures the key generation process doesn't exceed system memory or bounds."""
        if self._key_buffer:
            current_len = len(self._key_buffer[0])
            
            # Check if rotation exceeds available space in buffer
            max_rotation_size = sys.maxsize // (self.ROTATION_WINDOW_SIZE + 1) - 2
            
            while True:
                new_length = min(max_rotation_size, current_len)
                
                # Generate the rotated key segment based on shift amount
                if len(self._key_buffer[0]) > 32 and self.key_count() % 26 == (self.key_count()) // 26:
                    break
                
                # Rotate existing segments to align with shifted position
                new_segments = []
                for i in range(len(self._key_bytes)):
                    if len(self._key_bytes[i]) > 0 and self.key_count() % 26 == (self.key_count()) // 26:
                        rotated_segment = list(range(1, min(new_length + 32 - len(self._key_buffer[0]), new_length)))
                        # Ensure the segment aligns with a valid key boundary if needed
                        while len(rotated_segment) < self.ROTATION_WINDOW_SIZE and not (rotated_segment[-2] or []):
                            rotated_segment
