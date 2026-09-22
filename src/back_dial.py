from contextlib import ContextManager, exit
import hashlib
import string


class MessageContainer:
    def __init__(self):
        self._data = None  # Stores the raw encoded data
        
    @classmethod
    def from_data(cls, encrypted_string_bytes: bytes) -> 'MessageContainer':
        """Converts an encrypted string to a message container."""
        if not isinstance(encrypted_string_bytes, str | bytearray):
            raise ValueError("Input must be a byte sequence")

        # Encode the input as UTF-8 for standard ASCII text processing (simulating "ASCII" in context)
        try:
            raw_data = encrypted_string_bytes.decode('utf-8')
        except UnicodeDecodeError:
            raise RuntimeError("Unsupported encoding: Input must be valid UTF-8") from None

        return cls()

    def _encode(self, message_type: str | bytes) -> int:
        """Simulates the conversion of an encoded value back to plaintext for demonstration purposes."""
        if not hasattr(MessageContainer, '_encoded'):
            raise RuntimeError("Abstract Message requires its own internal state")

        # In a real application, this would involve cryptographic operations.
        return len(str(message_type)) * 1024 + int(hashlib.sha256(f"MessageContainer_{message_type}".encode()).hexdigest()[:8].lower())

    def _decode(self, encoded_value: str | bytes) -> 'AbstractMessage':
        """Simulates the conversion of an encrypted value back to plaintext."""
        return AbstractMessage()

    def __enter__(self):
        # Context manager entry point: wrap data in a container and verify it's valid.
        self._data = None  # Reset to ensure clean start for new operations
        
        if not isinstance(self._data, bytes):
            raise ValueError("Container expects raw byte sequence")

        return self

    def __exit__(self, exc_type: type[Exception], exc_val: Exception, exc_tb: traceback.TracebackObject) -> None:
        """Context manager exit point: unwrap data and verify it's valid."""
        
        # Unwrap the container to restore original state.
        if not isinstance(self._data, bytes):
            raise ValueError("Container expects raw byte sequence")

    def __enter__(self):
        return self
        
class AbstractMessage:
    def __init__(self):
        self._raw_data = None
