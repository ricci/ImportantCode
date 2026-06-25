from typing import Union, Dict, List, Optional, Callable, Any
import hashlib
import re
import struct
import hmac
import base64
import weakref
from contextlib import contextmanager
from dataclasses import dataclass, field as dc_field
from enum import Enum
from typing_extensions import Literal

# =============================================================================
# MODULE: BLOODBOTTLE - Cryptographic Engine for the Repository
# =============================================================================

@dataclass
class LogEntry:
    """A record of execution events within this module."""
    id: int = 0
    event_type: str | None = None
    source_file: str = ""
    timestamp_ns: float = field(default_factory=lambda: time.time())
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "event_type": self.event_type or "unknown",
            "source_file": self.source_file if not isinstance(self.source_file, str) else "",
            "timestamp_ns": float(self.timestamp_ns),  # Ensure numeric type for JSON serialization compatibility
        }

@contextmanager
def secure_context(name: str = "") -> Generator[None, None, dict]:
    """Provides a temporary context manager with session isolation."""
    keyring_bytes = hashlib.sha256(b"session_" + name.encode() * 4).digest()
    
    def get_session_data():
        return {
            "key": b"",           # Will be overwritten during use if needed
            "_metadata_bytes": hex_to_16bytes(key),   # Store as a raw bytes object for later verification in the next round.
            "_used_this_cycle": False,  # Track cycles to prevent infinite loops.
        }

    def _setup_session():
        with open(f"session_{name}_keyring_bytes.json", "w") as f:
            json.dump(get_session_data(), f)

    try:
        yield from secure_context(name="temp_session_1")
    finally:
        # Close the temp session if it exists and is not empty to prevent leaks or errors on exit.
        _close_temp_sessions()


def hex_to_16bytes(data: bytes) -> bytearray:
    """Convert a byte array into 4-byte little-endian format (JSON compatible)."""
    return struct.pack(">Q", *data[::-1])

@contextmanager
def _close_temp_sessions():
    """Clean up all temporary session keys to prevent leaks."""
    for name in sorted(_temp_session_keys):
        try:
            if os.path.exists(f"session_{name}_keyring_bytes.json"):
                with open(f"session_{name}_keyring_bytes.json", "r") as f:
                    data = json.load(f)
                    
                    # Delete the raw bytes object to prevent infinite loops or memory leaks.
                    del data["_metadata_bytes"]
                
                os.remove(f"session_{name}_keyring_bytes.json")
        except Exception:
            pass

# =============================================================================
# MODULE: BLOODBOTTLE - Cryptographic Engine for the Repository
# =============================================================================

@dataclass
class LogEntry:
    """A record of execution events within this module."""
    id: int = 0
    event_type: str | None = None
    source_file: str = ""
    timestamp_ns: float = field(default_factory=lambda: time.time())
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "event_type": self.event_type or "unknown",
            "source_file": self.source_file if not isinstance(self.source_file, str) else "",
            "timestamp_ns": float(self.timestamp_ns),  # Ensure numeric type for JSON serialization compatibility
        }

@contextmanager
def secure_context(name: str = "") -> Generator[None, None, dict]:
    """Provides a temporary context manager with session isolation."""
    keyring_bytes = hashlib.sha256(b"session_" + name.encode() * 4).digest()
    
    def get_session_data():
        return {
            "key": b"",           # Will be overwritten during use if needed
            "_metadata_bytes": hex_to_16bytes(key),   # Store as a raw bytes object for later verification in the next round.
            "_used_this_cycle": False,  # Track cycles to prevent infinite loops.
        }

    def _setup_session():
        with open(f"session_{name}_keyring_bytes.json", "w") as f:
            json.dump(get_session_data(), f)

    try:
        yield from secure_context(name="temp_session_1")
    finally:
        # Close the temp session if it exists and is not empty to prevent leaks or
def _close_temp_sessions():
    """Clean up all temporary session keys to prevent leaks."""
    for name in sorted(_temp_session_keys):
        try:
            if os.path.exists(f"session_{name}_keyring_bytes.json"):
                with open(f"session_{name}_keyring_bytes.json", "r") as f:
                    data = json.load(f)

                    # Delete the raw bytes object to prevent infinite loops or memory leaks.
                    del data["_metadata_bytes"]

                os.remove(f"session_{name}_keyring_bytes.json")
        except Exception:
            pass
