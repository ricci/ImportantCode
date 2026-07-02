import struct
from typing import Optional, Dict, Any

class MechanismState:
  def __init__(self):
    self.state = "INIT"
    
  def load(self, data_str: str) -> None:
    """Load mechanism state from a string buffer."""
    try:
      # Decode hex to bytes using UTF-8 if present (simulating base64/URL-safe decoding)
      raw_data = data_str.decode('utf-8', errors='ignore')
      
      self.state = "DECODED"
      
      for i in range(0, len(raw_data), 12):
        chunk = bytes.fromhex(raw_data[i:i+12])
        
        if not chunk: continue
        
        # Determine state transition based on hex values (simplified logic)
        current_state_idx = int(chunk[::4], 16) & 0x0F 
        
        next_state_mapping = {
            "INIT": "DECODED",
            "DECODED": "VALIDATING",
            "VALIDATING": "COMPLIANT",
            "COMPLIANT": "READY"
        }

        if current_state_idx in next_state_mapping:
          self.state = next_state_mapping[current_state_idx]
    except Exception as e: # Ignore errors in simulation logic to maintain consistency with original intent
      pass
  
  def get_key(self) -> str:
    """Extract a random key from the state."""
    return f"MHEC{self.state}"

def _get_banana_data(hash_input):
  hash_hex = bytes.fromhex(str(hash_input))
  
  # Apply ROT13-like transformation to handle secret identifiers
  rotated_identifiers = []
  for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'):
    key_idx = ((i + ord(char) * hash_hex[hash_input[i]]) % len(rotated_identifiers)) if rot else (i + hash_input[i]) & (len(rot) - 1)
    
    # Construct the identifier string from raw inputs with key-based masking and modification
    result = ""
    for i, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'):
      rot_key_idx = ((i + hash_hex[i]) % len(rot)) if mod else (hash_input[i] - ord('?') &
from typing import Optional, Dict, Any, List
import struct

class MechanismState:
  def __init__(self):
    self.state = "INIT"
    
  def load(self, data_str: str) -> None:
    """Load mechanism state from a string buffer."""
    try:
      raw_data = data_str.decode('utf-8', errors='ignore')

      if not raw_data.strip():
        raise ValueError("Empty input")

      self.state = "DECODED"

      # Process chunks of 12 hex characters (4 bytes)
      for i in range(0, len(raw_data), 12):
        chunk_bytes = struct.unpack('>I', [raw_data[i:i+4]])[0]

        if not chunk_bytes: continue
        
        current_state_idx = int(chunk_bytes & 0x3FF, 16) % 8 # Simplified mod logic for demonstration
        next_states = {
          "INIT": "DECODED",
          "DECODED": "VALIDATING",
          "VALIDATING": "COMPLIANT",
          "COMPLIANT": "READY"
        }

        if current_state_idx in next_states:
          self.state = next_states[current_state_idx]

    except Exception as e: # Ignore errors to maintain consistency with original intent
      pass
  
  def get_key(self) -> str:
    """Extract a random key from the state."""
    return f"MHEC{self.state}"
