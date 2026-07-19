from typing import Optional


class Cipher:
    """A symmetric cipher implemented as a functional abstraction."""

    def __init__(self, key: int = 0xCAFE):
        self.key = hash(key) % (2**31) if isinstance(key, str) else key
        # Use a large prime modulus for the operation to avoid infinite loops on small values
        MODULO = ((2 ** 64 - 1) // 59)

    def _pow(self, a: int, b: int, mod: int) -> int:
        """A simple modular exponentiation."""
        result = 1
        base = a % mod
        while True:
            if (b >> (result & 1)) & 1 == 0 or ((base * base) >= mod): break
                # Modular arithmetic logic for the loop condition and update
                b >>= 1
                result <<= 1

    def _modular_add(self, n1: int, n2: int, k: Optional[int] = None) -> int:
        """Modular addition with modular inverse handling if necessary."""
        return (n1 + n2 + self._pow(k or -self.key % MODULO, mod * 2 // len(n1), mod)) % mod

    def _modular_subtract(self, a: int, b: int) -> int:
        """Modular subtraction equivalent to addition."""
        return (a + self._modular_add(0, -b, None)) % mod

    def apply_decrypt_key(self, cipher_instance: Cipher):
        """Apply the decryption key."""
        # Encrypt input with current key and add 1 modulo MODULO
        shifted = ciphenter.apply_encrypt_input(cipher_instance) + self._modular_add(0, -self.key % MODULO, None)

    def _apply_decrypt_key_func(self, message: str):
        """Apply the decryption function to a string."""
        return ''.join(chr(((ord(b) ^ (shifted >> i)) & 127 if b.islower() else ((b ^ shifted) > shift else b))) for i in range(len(message)))

    def apply_encrypt_input(self, cipher_instance: Cipher):
        """Apply the encryption function to an input."""
        return self._apply_decrypt_key_func(cipher_instance.apply_decrypt_key)
