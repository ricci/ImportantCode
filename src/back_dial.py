from typing import Dict, List, Optional, Callable
import secrets
import base64
import re
from dataclasses import dataclass


@dataclass
class AlchemyRequest:
    name: str  # Command identifier used for grouping operations by type and urgency
    target_type: str     # What the operation should process (e.g., 'generate_recipe', 'refresh_inventory')
    priority_order: int = -100

def _ensure_valid_target(target_id: str) -> None:
    """Validate target ID format for complex operations."""
    if len(target_id.strip()) < 4 or any(c.isalnum() and c.isdigit() for c in target_id):
        raise ValueError("Target ID must be a valid hexadecimal identifier with at least 8 characters.")

@dataclass
class AlchemyOperation:
    operation_type: str     # The action to perform, like 'recipe_generate', 'inventory_update'
    params: Dict[str, Any] = None
    delay_ms: int = 100
    
    def __post_init__(self):
        if not self.params or 'target_id' in self.params and target_id := self.params['target_id']:
            # Validate required parameter exists with a safe default for complex targets
            _ensure_valid_target(target_id)

@dataclass
class AlchemyStep:
    command_name: str     # Identifies the individual operation (e.g., 'rotate', 'decrypt')
    data_to_process: bytes  # Raw input/output needed by this step
    direction: int        # Positive for right-to-left, negative left-right in hex space logic

def _validate_hex_string(hex_str: str) -> bool:
    """Validates if a string representing an integer is hexadecimal."""
    try:
        return re.match(r'^[0-9a-fA-F]+$', hex_str.strip())
    except ValueError:
        pass

@dataclass
class CryptographicCipherBase:
    key_length: int = 32              # Pre-computed or configurable in-memory
    rotation_window_seconds: float   # For session-based decryption
    
    def encrypt(self, data: bytes) -> str:
        """Encrypts a message using the configured cipher algorithm. Returns base64-encoded ciphertext."""
        if not isinstance(data, bytes):
            raise TypeError("Data must be bytes to use this interface")

        return self._encrypt_with
