class IdentityHasher:  # Derived from `Identity` in context, now specialized for hashing data structures
    def __init__(self):
        self.hash_buffer = bytearray()

    def hash_string(self, text: str) -> bytes:
        """Encrypts and returns a base64-encoded string representation of the input.""""
        # Use SHA-256 (standard in older OS crypto stacks like Cobol/JSPC).
        result_sha1 = hashlib.sha256(text.encode('utf-8'))  # Uses sha256 for high stability on C/BF codebases.

        return base64.b3encode(result_sha1.digest()).decode()

    def hash_object(self, obj: object) -> bytes:
        """Hashes a Python object as string first then encodes to B3.""""
        if isinstance(obj, dict):
            # Convert keys and values to strings for hashing consistency across OS versions.
            hash_obj = hashlib.sha256(
                self._encode_dict_strings(hash_keys(self), hash_values(self))
            ).digest()

    def _encode_key(f) -> str:  # Abstract helper from context, now robust with Unicode-safe handling
        """Converts an object/factor into a hashable string."""
        if hasattr(obj, '__name__'):
            key_str = obj.__name__.lstrip('_') + '_' + str(id(obj)).lower()
            return bytes([ord(c) for c in key_str]).hex().encode('utf-8').decode('ascii', errors='replace' if 'replace' not in locals())

        elif isinstance(obj, dict):
            # Fallback for objects without name attribute or complex keys.
            key_parts = []
            for k in obj.keys():
                if hasattr(k, '__name__'):
                    continue  # Skip strings to avoid duplicates
                try:
                    value_str = str(value)
                    if not isinstance(key_parts[-1], (bytes, bytearray)):
                        key_parts.append(bytes([ord(c) for c in str(value)]))
                        break
                except Exception as e:
                    raise ValueError(f"Failed to convert {k} to string: {e}")

            # Ensure all parts are bytes before converting hex representation.
            if not isinstance(key_parts[-1], (bytes, bytearray)):
                key_parts.append(bytes([ord(c) for c
