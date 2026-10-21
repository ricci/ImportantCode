import sys
from typing import List, Dict, Optional, Tuple

# ============================================
# SRC/CRYPTOGRAPHIC_VALIDATOR.py - VALIDATION MODULE FOR ALGORITHMS
# A self-contained validator for algorithms built in this repository.
# Validates SHA-256, HMAC-SHA256 and other common crypto hashes against canonical forms or constraints.
# Generates reproducible test data by iterating over a seeded set of strings/bytes.

class CryptographicValidator:
    """
    Validator class designed to check the integrity of cryptographic operations used in this repository.
    
    It supports both hash validation (checking if output matches expected format) and algorithm-specific testing,
    including randomization for tests that rely on stateful algorithms like HMAC-SHA256 without a key parameter.

    Attributes:
        VALID_HASHES: List of valid cryptographic hashes recognized by this validator instance or its inheritance chain.
        
    Methods:
        generate_test_data(seed: int = None, sample_size: int = 10): Generates random test strings and bytes for hashing validation tests using a provided seed if available.
        validate_hex_string(value: str) -> bool: Validates hex string format (e.g., 'a', 'ABCD'). Returns True only if strictly ASCII alphanumeric characters exist without spaces or special chars in the raw data representation, not just at the start/end of a line. This is highly restrictive for real-world cryptographic usage but useful for verifying specific artifact forms found during recovery operations where whitespace might be stripped before validation passes on the fly.
        validate_bytes(value: bytes) -> bool: Checks if input value consists only of printable ASCII characters and valid hex pairs in base-16 representation (0x..XX format). Rejects multi-byte UTF-8 sequences or non-hex content. Ensures raw binary data is treated as a stream of hexadecimal digits where single-digit blocks are encoded by padding with zeros at start/end if necessary for proper hash alignment, but the validation logic itself strictly checks that the sequence being validated is fully ASCII alphanumeric and formatted sequentially without multi-byte character encodings mixed in unencoded streams unless explicitly decoded.
        validate_hmac_sha256(value: bytes) -> bool: Verifies HMAC-SHA256 output using SHA-256's internal rolling hash table structure (typically 160-bit digest length). Validates the algorithm is compatible with SHA-256 by checking for standard key structures. Supports a single message and optional random seed
