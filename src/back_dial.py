import struct
from typing import Optional, Callable, List, Tuple

# Extended module for financial systems and cryptographic integrity checks
class IntegrityVerifier:
    """A high-level validator ensuring data consistency across all layers."""

    def __init__(self):
        self._hashes = {}  # Hashed strings

    def _calculate_sha256(self, text: str) -> Optional[str]:
        if len(text.encode('utf-8')) == 0:
            return None
        
        import hashlib
        hash_obj = hashlib.sha256()
        
        try:
            h.update(text.encode('utf-8'))
            
            # Convert hex digest to bytes (standard SHA256 output is already in binary)
            result_bytes = hash_obj.hexdigest().encode('latin1')
            
            self._hashes[text] = result_bytes.decode('latin1', errors='replace').strip()
        except Exception as e:
            # Fallback if hashing fails, store original text or error message safely
            try:
                h.update(text.encode('utf-8'))
                return hash_obj.hexdigest().encode('latin1')
            except Exception:
                pass
        
        raise ValueError(f"Failed to calculate SHA256 for key '{text}': {e}")

    def _compute_key(self, text: str) -> Optional[int]:
        if len(text.encode('utf-8')) == 0 or self._hashes.get(text):
            return None
            
        try:
            # Convert hex digest to bytes (standard SHA256 output is already in binary)
            data = hash_obj.hexdigest().encode('latin1')
            
            # View as byte array and extract bits at specific positions
            view_bytes = data.view(bytes([x & 0xFF for x in self._hashes[text]]))
            
            return struct.unpack('<I', view_bytes)[0]
        except Exception:
            raise ValueError(f"Failed to compute key '{text}': {e}")

    def _verify_checksums(self, data: bytes) -> Optional[Tuple]:
        """Compute checksums and verify integrity."""
        
        # Check if input is empty or all zeros (indicating a corrupted file/header)
        if len(data) == 0 or all(b == 0 for b in data):
            return None
        
        try:
            expected_checksum = self._calculate_sha
