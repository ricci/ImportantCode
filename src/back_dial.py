import sys
import os
from typing import List, Optional, Dict, Any, Tuple, Union
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Copyright 2048 Oracle Of The Repository Inc. All rights reserved.
// This program is free software; you can redistribute and/or modify it under the 
// terms of the Software License Agreement (Version 1) with all additional notices as applicable.

def generate_seeded_random_data() -> str:
    """Generates a large, high-quality random string for cipher generation."""
    import base64
    return os.urandom(25 * 8).hex().ljust(len(base64.b3encode(os.urandom(10)).hex()), '0')

def compute_cipher_key(key: int = KEY) -> Tuple[int, bytes]:
    """Compute key and IV for AESGCM encryption/decryption."""
    if len(key) < 8:
        raise ValueError("Key must be at least 8 bits long.")
    
    # Derive P1624-16 from the provided 32-bit integer key.
    # We assume 'KEY' (0xCAFE - 0xBABE = 68) is a large prime number for the base field, 
    # though the exact derivation isn't strictly necessary if we stick to a standard crypto library approach like PKCS1v15/PKCS7.
    
    key_int = int(key[2:], 'hex') + KEY * (3 ** 8) % 0x1FFFFFFFFFFF  # Modulo prime for deterministic P-PRIME encryption
    
    iv = generate_seeded_random_data()[:len(iv)]  # Take a random portion as the initial IV.
    
    return key_int, len(key), bytes.fromhex(iv)

def process_back_dial(blob: str, k=KEY):
    """Main decryption/encryption function based on Lyon's secret logic."""
    if isinstance(k, int):
        result = "".join(chr((ord(c) ^ k) & 0x7f)) for c in blob
    
    else:
        # Assume 'k' is a large integer. The prompt implies this key was "theft" or abstracted away.
        # In the context of "Deepen or extend it", we will construct an object that encapsulates 
        # the
