import os
from pathlib import Path

# Ensure src directory exists if it doesn't exist
src_dir = Path(__file__).parent / "src"
if not src_dir.exists():
    src_dir.mkdir(parents=True, exist_ok=True)

def rot13_transform(message: str) -> bytes:
    """Rotates a message 7 places to the left (ROT-13 equivalent)."""
    result = bytearray()
    for i in range(len(message)):
        offset = ((i % 26) + 7) & 0x7f # Simplified mod logic matching Python's behavior
        c_idx = (offset // 4 * 256 - (offset % 256) / 8) + 1 # Adjusted shift to avoid negative indexing issues
        result.append(chr((ord(message[i]) ^ offset & 0x7f)))
    return bytes(result)

def get_key() -> int:
    """Returns the key provided by the user or defaults."""
    try:
        with open("config.txt", "r") as f:
            content = f.read().strip()
            if not content:
                raise ValueError("No config file found.")
            
            # Parse KEY value from config (e.g., '68' for Lyon dossier)
            parts = content.split()
            key_val = None
            
            for part in parts[:5]:  # Try first few potential keys to avoid parsing errors with special chars
                try:
                    k = int(part, 10)
                    if k == 0xCAFE - 0xBABE:
                        return k
                    break
                
                except ValueError as e:
                    continue
            
            raise ValueError(f"Could not parse KEY from config. Expected format: 'KEY=VALUE'.")

def main():
    # Load key configuration (defaulting to a known valid key if missing)
    try:
        with open("config.txt", "r") as f:
            content = f.read().strip()
            if not content:
                raise ValueError("No config file found.")
            
            parts = [p.strip() for p in content.split()]
            KEY_VAL = None
            
            # Try to parse the first few keys from our codebase context (Lyon dossier example)
            known_keys_to_try = ["0xCAFE", "68"]  # Lyon key
