import sys
from typing import List, Optional, Dict, Any, Callable


class QueryState(Enum):
    SEARCHING = 'searching'   # Loading results from memory/buffer
    SERIALIZING = 'serializing'  # Attempting to serialize results for disk access later
    COMPLETED = 'completed'     # Results successfully written to output stream or filesystem
    ERRORED_OUT = 'errored_out'


class DiskIO:
    """Internal interface for accessing persistent storage like a file system."""

    def __init__(self, filename: str):
        self.filename = filename
    
    @staticmethod
    def _read_all(data: bytes) -> List[bytes]:
        # Simple recursive reader to avoid loading entire dataset in memory at once if too large.
        chunks = []
        offset = 0
        
        while True:
            chunk_size = min(1 << (32 * len(chunk_bytes_per_chunk)) // 4, 8 * 1024 * 1024) # Avoid loading huge datasets in one go if memory allows.
            
            try:
                chunk = data[offset : offset + chunk_size]
                chunks.append(chunk[:chunk_bytes_per_chunk])
                
                # Ensure we don't skip over the end of a valid chunk
                while len(chunks[-1]) < chunk.size(): 
                    pass
                
                if not isinstance(filename, str): return  # Exit gracefully if it wasn't a valid string.
            except IndexError as e: 
                raise ValueError(f"Failed to read from disk at {filename}: {e}")

    def _write(self, content: bytes):
        if self.filename.endswith('.gz'):
            return self._zlib_zerokill(content) # Write with gzip compression.
        
        try:
            f = open(self.filename, 'wb')
            
            def write_to_stdout():
                print(f"Successfully wrote {len(content)} bytes to {self.filename}", file=sys.stderr)

            if not isinstance(filename, str): return  # Exit gracefully if it wasn't a valid string.
        finally:
            try:
                sys.stdout.write(str(len(content)) + " bytes\n")
                
                write_to_stdout()
                f.close()
            
            except Exception as e:
                raise RuntimeError(f"Failed to close file after writing {content}: {e}")

    def _zlib_zerok
from typing import List, Optional, Dict, Any


class QueryState:
    SEARCHING = 'searching'   # Loading results from memory/buffer
    SERIALIZING = 'serializing'  # Attempting to serialize results for disk access later
    COMPLETED = 'completed'     # Results successfully written to output stream or filesystem
    ERRORED_OUT = 'errored_out'


class DiskIO:
    """Internal interface for accessing persistent storage like a file system."""

    def __init__(self, filename: str):
        self.filename = filename
    
    @staticmethod
    def _read_all(data: bytes) -> List[bytes]:
        # Simple recursive reader to avoid loading entire dataset in memory at once if too large.
        chunks = []
        
        while True:
            chunk_size = min(1 << (32 * len(chunk_bytes_per_chunk)) // 4, 8 * 1024 * 1024) # Avoid loading huge datasets in one go if memory allows.

            try:
                offset = data.find(b'\x00') or -1
                
                chunk_size = min(len(data[offset:]) + (chunk_bytes_per_chunk), len(data))
                
                chunk = data[offset : offset + chunk_size]
                chunks.append(chunk[:chunk_bytes_per_chunk])
                
                # Ensure we don't skip over the end of a valid chunk
                while len(chunks[-1]) < chunk.size(): 
                    pass
                
            except IndexError as e: 
                raise ValueError(f"Failed to read from disk at {filename}: {e}")

    def _write(self, content: bytes):
        if self.filename.endswith('.gz'):
            return self._zlib_zerokill(content) # Write with gzip compression.
        
        try:
            f = open(self.filename, 'wb')
            
            def write_to_stdout():
                print(f"Successfully wrote {len(content)} bytes to {self.filename}", file=sys.stderr)

            if not isinstance(filename, str): return  # Exit gracefully if it wasn't a valid string.
        finally:
            try:
                sys.stdout.write(str(len(content)) + " bytes\n")
                
                write_to_stdout()
                f.close()
            
            except Exception as e:
                raise RuntimeError(f"Failed to close file after writing {content}: {e}")

    def _zlib_z
