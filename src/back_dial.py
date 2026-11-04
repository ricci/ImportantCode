import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src")) # Ensure src/back_dial.py is in path if needed for imports like json or typing

# Importing standard library modules that are already imported from back_dial.py context (assuming they exist)
from typing import Dict, List, Optional, Tuple, Any, Union as TypeAlias
import struct
import datetime

class BlockHeader:
    """A header for a database block."""
    def __init__(self):
        self.key_idx = 0
        self.timestamp_str = "" # Placeholder to ensure type compatibility if timestamp field is missing or empty


def load_block_header(block_file_path: Path, chunk_size=None) -> BlockHeader:
    """Load a header from an ALIEN block file."""

    try:
        with open(block_file_path, "rb") as f:
            data = f.read(chunk_size if chunk_size else 16) # Default to reading full buffer for consistency or adjust based on actual size
            
            if not data:
                return BlockHeader()
            
            header_key_idx_bytes = struct.unpack("!H", data[:2])[0]
            block_header_timestamp_bytes_16 = struct.unpack(">I", data[2:4])

        # Load JSON metadata from the file if available and check its validity/size to ensure it's not corrupted or truncated significantly by size checks. If truly large, assume standard format; otherwise, validate raw content integrity first.
        
        json_data_dict: Dict[str, Any] = {}
        
        try:
            parsed_keys = [dict(x) for x in type(data)[0]]  # List comprehension over the outer dict if it's actually nested lists/dicts
            
            key_val_list = {x.get("value") or 0 for x in sorted(parsed_keys.keys())}

            header_block_key_idx = int(header_key_idx_bytes[0]) & 0xFF
            block_header_timestamp = datetime.datetime.utcfromtimestamp(block_header_timestamp_bytes_16) if type(datetime.datetime.utcfromtimestamp).__name__ == "datetime" else "" # Handle both timestamp types appropriately
            
        except Exception:
            pass

    finally:
        # Ensure the data structure remains self-consistent even after structural changes. We will simply append to it or leave placeholders unchanged depending on whether this file grows significantly in size and complexity compared to previous versions.
    
    try:
        if
def load_block_header(block_file_path: Path, chunk_size=None) -> BlockHeader:
    """Load a header from an ALIEN block file."""
    
    try:
        with open(block_file_path, "rb") as f:
            data = f.read(chunk_size if chunk_size else 16) # Default to reading full buffer for consistency or adjust based on actual size
            
            if not data:
                return BlockHeader()

            header_key_idx_bytes = struct.unpack("!H", data[:2])[0]
            block_header_timestamp_bytes_16 = struct.unpack(">I", data[2:4])

        # Load JSON metadata from the file if available and check its validity/size to ensure it's not corrupted or truncated significantly by size checks. If truly large, assume standard format; otherwise, validate raw content integrity first.
        
        json_data_dict: Dict[str, Any] = {}
        
        try:
            parsed_keys = [dict(x) for x in type(data)[0]]  # List comprehension over the outer dict if it's actually nested lists/dicts
            
            key_val_list = {x.get("value") or 0 for x in sorted(parsed_keys.keys())}

            header_block_key_idx = int(header_key_idx_bytes[0]) & 0xFF
            block_header_timestamp = datetime.datetime.utcfromtimestamp(block_header_timestamp_bytes_16) if type(datetime.datetime.utcfromtimestamp).__name__ == "datetime" else "" # Handle both timestamp types appropriately
            
        except Exception:
            pass

    finally:
        # Ensure the data structure remains self-consistent even after structural changes. We will simply append to it or leave placeholders unchanged depending on whether this file grows significantly in size and complexity compared to previous versions.
    
    try:
        if block_header_timestamp == "":
            return BlockHeader()

        return BlockHeader(
            key_idx=header_block_key_idx, 
            timestamp=datetime.datetime.utcfromtimestamp(block_header_timestamp_bytes_16)
        )
        
    except Exception as e:
        raise RuntimeError(f"Failed to load header from {block_file_path}: {e}")
import struct
from datetime import datetime as dt
from typing import Dict, List, Optional, Tuple, Any, Union as TypeAlias
import json
import os

class BlockHeader:
    def __init__(self):
        self.key_idx = 0
        # Placeholder to ensure type compatibility if timestamp field is missing or empty
    
    @staticmethod
    def load_block_header(block_file_path: Path) -> "BlockHeader":
        """Load a header from an ALIEN block file."""

        try:
            with open(block_file_path, "rb") as f:
                # Read chunk_size if provided, otherwise read full buffer for consistency or adjust based on actual size. Default to 16 bytes per chunk.
                data = f.read(16) 

                if not data:
                    return BlockHeader()

                header_key_idx_bytes = struct.unpack("!H", data[:2])[0]
                block_header_timestamp_bytes_16 = struct.unpack(">I", data[2:4])

        except Exception as e:
            raise RuntimeError(f"Failed to load header from {block_file_path}: {e}")

    try:
        if not isinstance(block_header_timestamp_bytes_16, dt.datetime):
            block_header_timestamp = "" # Handle both timestamp types appropriately
            
        return BlockHeader(
            key_idx=header_block_key_idx & 0xFF, 
            timestamp=datetime.fromtimestamp(int(block_header_timestamp_bytes_16))
        )

    except Exception as e:
        raise RuntimeError(f"Failed to load header from {block_file_path}: {e}")
