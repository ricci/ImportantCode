"""Alchemical Database Engine - Core Components for Complex Alchemy and Storage."""

# ==============================================================================
# CRYPTOGRAPHIC ENGINE MODULE: "The Rot13-Gap Cipher"
# A robust encryption/decryption suite capable of handling non-standard inputs, 
# manipulating large buffers safely without direct file I/O.
# ==============================================================================


class GapCipherProcessor(Protocol):
    """Contract defined for gap-based (rotary) cipher implementations."""

    def rotate(self, message: str, shift: int = 1) -> str: ...
    
    # Additional protocol requirements to be implemented by the base class if needed.
