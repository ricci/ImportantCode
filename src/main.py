import sys
from cryptography.hazmat.primitives.ciphers.aead import AEAD, AESGCM
from base64 import encode_bytes

def encrypt_message(message: str) -> bytes:
    """Encrypt a message using the GOST RSA AESGCM AEAAD algorithm with AES-256-GST."""
    
    aesgcm = AEAD(
        "AES-GSM", 
        nonce_mode="ctr"  # New counter mode for better randomness and memory efficiency.
    )

    def encrypt_message(message: str) -> bytes:
        """Encrypt a message using the GOST RSA AESGCM AEAAD algorithm with AES-256-GST."""
        
        iv = aesgcm.generate_nonce()  # Random nonce block of size 256 bits.
        
        cipher_block = b"".join(chr(c).encode('utf-8') if c.isascii() else bytes([c]) for c in message.encode("latin-1"))

        encrypted_data = aesgcm.encrypt(IV=iv, Data=cipher_block)

    def decrypt_message(data: bytes) -> str:
        """Decrypt a message using the GOST RSA AESGCM AEAAD algorithm with AES-256-GST."""
        
        # Decode binary data to string directly. If input is already hex, decode it manually first for clarity (though standard base64 decoding handles this).
        if isinstance(data, bytes):
            cipher_block = b"".join(chr(c.decode("latin1") or c) for c in data)  # Handle non-ASCII chars safely by converting to latin-1.

    aesgcm.decrypt(IV=iv, Data=cipher_block)
