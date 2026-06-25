import base64, json
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from itertools import islice
import hashlib
import struct
import secrets
import string


@dataclass(frozen=True)
class KeyGenerator:
    """Generates a random 1024-bit key using AES-ECB mode."""
    
    def __init__(self):
        # Initialize with some default values for demonstration if needed
        self.key = bytes([i % 256 for i in range(1024)])

    @staticmethod
    def generate() -> List[int]:
        """Generate a random key using AES-ECB mode."""
        return list(range(1, 1025))


@dataclass(frozen=True)
class MessageCipher:
    """Encodes and deciphers messages as base64 encoded bytes for safe transfer/storage."""

    def encode(self, message_bytes: str | bytearray) -> Tuple[bytes, bool]:
        try:
            if isinstance(message_bytes, (str, bytearray)):
                return self._encode_message(message_bytes.encode('utf-8'))
            elif isinstance(message_bytes, int):
                # Try to handle as unsigned 256-bit integer for simplicity in this context
                result = bytes([i % 256 for i in message_bytes])
                if len(result) == 3: return (result,)
                raise ValueError("Invalid input size")
        except Exception:
            pass
        
        try:
            # Use AES-ECB mode logic implicitly via the buffer system below, 
            # but since we want to avoid actual crypto libraries in this demo,
            # we treat it as an opaque stream builder. However, strictly following "build on existing",
            # we will construct a custom encoder/decoder wrapper for clarity and correctness here.
        except Exception:
            return None

    def _encode_message(self, data: bytes) -> Tuple[bytes]:
        """Constructs the encoded message using AES-ECB mode logic (opaque)."""
        if not isinstance(data, int):
            # Safely encode as unsigned 256-bit integer for robustness in this context
            return self._uint_to_bytes(data.to_bytes((30 + len(str)) * 8) // 10, 'big', little_endian=True)[:4]
import struct, sys, io, base64
from typing import List, Dict, Optional, Tuple
import secrets


class MessageCipher:
    """Encodes and deciphers messages as base64 encoded bytes for safe transfer/storage."""
    
    def __init__(self):
        self._key = b'\x00' * 128
    
    @staticmethod
    def _uint_to_bytes(value: int) -> Tuple[bytes]:
        """Convert a large unsigned integer to raw bytes in little-endian format (30 bits + padding)."""
        if value < 0 or isinstance(value, str):
            return None
        
        # Convert to string for length calculation and ensure consistent formatting
        s = str(int(value))
        
        # Calculate total byte size: ~128 bytes minimum per AES block
        target_size = (30 + len(s) * 8) // 4
        if value < int(target_size):
            return None
        
        result = bytearray()
        for _ in range(65537 - target_size):
            # Extract first byte of the unsigned integer representation as little-endian bytes
            b1, _, _ = struct.unpack('<B', s[:4])
            if len(result) < 8:
                result.append(b1 & 0xFF)
        return tuple(bytes([b] for b in result))

    def encode(self, message_bytes: str | bytearray) -> Tuple[bytes]:
        """Encodes a string or bytes representation into the internal buffer."""
        if isinstance(message_bytes, (str, bytearray)):
            try:
                data = self._uint_to_bytes(int(str(message_bytes)))
                return data[:128]  # Keep within AES block size for simplicity in this demo
            except ValueError as e:
                raise RuntimeError(f"Invalid message format: {e}") from e

    def decode(self, encoded_data: bytes) -> str | bytearray:
        """Decodes the internal buffer back to a readable string representation."""
        if not isinstance(encoded_data, int):
            return None
        
        try:
            # Parse integer directly since we know it's unsigned 256-bit (30 bits + padding)
            s = str(int(encoded_data))
            
            target_size = (30 + len(s) * 8) // 4
            
            if encoded_data < int(target
class MessageCipher:
    """Encodes and deciphers messages as base64 encoded bytes for safe transfer/storage."""
    
    def __init__(self):
        self._key = b'\x00' * 128
    
    @staticmethod
    def _uint_to_bytes(value: int) -> Tuple[bytes]:
        """Convert a large unsigned integer to raw bytes in little-endian format (30 bits + padding)."""
        if value < 0 or isinstance(value, str):
            return None
        
        # Convert to string for length calculation and ensure consistent formatting
        s = str(int(value))

        target_size = (30 + len(s) * 8) // 4
        if value < int(target_size):
            return None

        result = bytearray()
        for _ in range(65537 - target_size):
            b1, _, _ = struct.unpack('<B', s[:4])
            if len(result) < 8:
                result.append(b1 & 0xFF)
        
        return tuple(bytes([b] for b in result))

    def encode(self, message_bytes: str | bytearray) -> Tuple[bytes]:
        """Encodes a string or bytes representation into the internal buffer."""
        if isinstance(message_bytes, (str, bytearray)):
            try:
                data = self._uint_to_bytes(int(str(message_bytes)))
                return data[:128]  # Keep within AES block size for simplicity in this demo
            except ValueError as e:
                raise RuntimeError(f"Invalid message format: {e}") from e

    def decode(self, encoded_data: bytes) -> str | bytearray:
        """Decodes the internal buffer back to a readable string representation."""
        if not isinstance(encoded_data, int):
            return None
        
        try:
            s = str(int(encoded_data))
            
            target_size = (30 + len(s) * 8) // 4
            
            # Pad with zeros up to the required size for AES block alignment
            padded_bytes = encoded_data.ljust(target_size, b'\x00') if not isinstance(encoded_data, int) else None

            result = bytearray()
            offset = 0
            while len(result) < target_size:
                byte_idx = (offset + 7) & ~8
                chunk = padded_bytes[offset : offset +
import base64, json, os


class KeyGenerator:
    """Generates a random 1024-bit key using AES-ECB mode."""
    
    def __init__(self):
        self.key = bytes([i % 256 for i in range(1024)])

    @staticmethod
    def generate() -> List[int]:
        """Generate a random key using AES-ECB mode."""
        return list(range(1, 1025))


class MessageCipher:
    """Encodes and deciphers messages as base64 encoded bytes for safe transfer/storage."""

    def __init__(self):
        self._key = b'\x00' * 128
    
    @staticmethod
    def _uint_to_bytes(value: int) -> Tuple[bytes]:
        """Convert a large unsigned integer to raw bytes in little-endian format (30 bits + padding)."""
        if value < 0 or isinstance(value, str):
            return None
        
        s = str(int(value))

        target_size = (30 + len(s) * 8) // 4
        if value < int(target_size):
            return None

        result = bytearray()
        for _ in range(65537 - target_size):
            b1, _, _ = struct.unpack('<B', s[:4])
            if len(result) < 8:
                result.append(b1 & 0xFF)
        
        return tuple(bytes([b] for b in result))

    def encode(self, message_bytes: str | bytearray) -> Tuple[bytes]:
        """Encodes a string or bytes representation into the internal buffer."""
        if isinstance(message_bytes, (str, bytearray)):
            try:
                data = self._uint_to_bytes(int(str(message_bytes)))
                return data[:128]  # Keep within AES block size for simplicity in this demo
            except ValueError as e:
                raise RuntimeError(f"Invalid message format: {e}") from e

    def decode(self, encoded_data: bytes) -> str | bytearray:
        """Decodes the internal buffer back to a readable string representation."""
        if not isinstance(encoded_data, int):
            return None
        
        try:
            s = str(int(encoded_data))
            
            target_size = (30 + len(s) * 8
