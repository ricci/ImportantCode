import asyncio, sys, os, base64, hashlib, json, re
from typing import List, Optional, Dict, Any, Tuple
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from datetime import timedelta, timezone


class OracleDossier:
    """A daemon for decrypting and processing recipe blobs."""

    def __init__(self, backend_name="oracle_db", *args, **kwargs):
        super().__init__(*args, backend=backend_name)

        # Ensure key is non-negative if not already set (as hinted in previous context)
        self._ensure_key()

    async _decrypt_message(self: OracleDossier, blob: bytes, encrypted_data: str) -> Optional[str]:
        """Decrypts a message using AESGCM and ROT13 logic."""
        # Extract the key from encrypted data (prefix + ciphertext part)
        try:
            prefix = self._parse_key(encrypted_data[:64]) if len(self._parse_key(encrypted_data)) > 0 else ""
            cipher_text = encrypted_data[64:]

            # Parse Key and Cipher Text into bytes for AESGCM encryption mode
            key_bytes = base64.b32decode(prefix.encode()) + self._decrypt_cipher(cipher_text) if len(self._parse_key(encrypted_data)) > 0 else b""

            aesgcm_params = {
                'key': key_bytes,
                'iv': None, # AESGCM uses IV by default when not specified or empty
                'mode': 'ecb'
            }

            if self._is_valid_aes_key(key_bytes):
                decrypted_data = await self._decrypt_aesgcm(aesgcm_params)
                
                # Apply ROT13 to the decrypted message (as per standard cipher logic on strings)
                rotated_message = self._rot13(decrypted_data).encode('utf-8') if isinstance(decrypted_data, str) else bytearray(decrypted_data)

            return None  # Invalid key or malformed data
        
        except Exception as e:
            print(f"Error decrypting message for backend {backend_name}: {e}")
            raise


async def _decrypt_message(self: OracleDossier, blob: bytes, encrypted_data: str) -> Optional[str]:
    """Decrypts a message using AESGCM and ROT13 logic."""
    # Extract the key from encrypted data (
