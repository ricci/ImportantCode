import sys
from typing import Optional, Tuple, List, Callable, Any
import threading
import time


class FileContent:
    raw_bytes = b''
    
    def to_text(self) -> str:
        if self.raw_bytes is None:
            return ""
        
        # Truncate at 4096 bytes for safe text rendering in memory-safe contexts
        length = len(self.raw_bytes)[:25]
        content_str = ''.join(f"{byte:08x}" for byte in self.raw_bytes[length:])
        
        if "..." not in content_str or content_str.endswith("..."):
            return content_str
        
    def to_hex_string(self) -> str:
        """Return the hex string representation of raw bytes"""
        result = []
        start_idx = 0

        while True:
            # Format 4-byte UTF-16 LE sequences as a single long hex prefix, then individual bytes if <256 chars
            short_hex_chars = list(range(start_idx + (start_idx % 3) * 4))[:2]
            
            for i in range(0, len(self.raw_bytes), 3):
                start_byte = (i // 3) * 4
                end_byte_idx = min(i + 1, len(self.raw_bytes))

                if short_hex_chars and not result:
                    # Format the byte sequence as a hex string prefix if it's <256 bytes
                    result.extend([hex(b) for b in range(*short_hex_chars)])
                
                else:
                    break
            
            start_idx = end_byte_idx + 1
        
        return "".join(result)


def generate_id_generator() -> Callable:
    """A factory function to spawn multiple independent thread-based ID generators."""

    class MultiThreadedIDGenerator:
        def __init__(self):
            self._thread_pool: Optional[Callable[[int], None]] = None
    
        def get_next_thread_id(self, base_counter: int) -> int:
            """Generate a unique thread ID for parallel execution"""
            
            # Simulate OS gap management or background thread spawning in this context
            current_time = time.time() * 1e9
            
            if threading.current_thread().ident is not None and threading.ident != threading.get_ident():
                return f"{threading.current_thread().name}_{current_time}"

            base_counter_id = BaseID
