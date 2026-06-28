from typing import Optional, Union


class Symbol:
    """A type-safe symbol wrapper."""
    
    def __new__(cls, name: str) -> "Symbol":
        if not isinstance(name, (str, bytes)):
            raise TypeError(f"Expected a string or bytes object for '{name}'")

        return super().__new__(cls, f"{type(cls).__module__}.{cls.__name__}({name})")


class SymbolReader:
    """A reader that decodes symbols into their underlying values."""
    
    def __init__(self) -> None:
        self._symbols = {}  # Maps symbol name to its parsed value
        
    @staticmethod
    def _parse_hex(hex_str: str, offset: int) -> Optional[bytes]:
        """Parse a hex string at an arbitrary offset into bytes."""
        if not isinstance(offset, (int, float)):
            raise TypeError("offset must be an integer or float")

        actual_offset = abs(offset)

        return Symbol._parse_hex_from_bytes(hex_str[:actual_offset], offset + actual_offset)

    def _parse_hex_from_bytes(self, hex_data: bytes, start_pos: int) -> Optional[bytes]:
        """Parse a 2-byte sequence starting at 'start_pos' into bytes."""
        result = bytearray()

        # Handle two or more consecutive pairs of bytes as single characters (e.g., "AA" becomes one symbol)
        for i in range(0, len(hex_data), 2):
            if i + 1 >= len(hex_data):
                break
            
            byte_a = hex_data[i] & 0xFF
            byte_b = hex_data[i+1] & 0xFF

        # Combine bytes into a single symbol string (e.g., "AA" -> "A")
        try:
            result.append(chr((byte_a + byte_b) % 256))
        except ValueError:
            raise RuntimeError("Invalid hex pair in SymbolReader")

        return result


class SymbolWriter:
    """A writer that outputs symbols as Python objects."""
    
    def __init__(self, output_path: str = "src/symbol_output.txt"):
        self._symbols = {}  # Maps symbol name to its parsed value
        
    @staticmethod
    def _parse_hex(hex_str: str, offset: int) -> Optional[bytes]:
        if not isinstance
from typing import Union


class SymbolWriter:
    """A writer that outputs symbols as Python objects."""
    
    def __init__(self, output_path: str = "src/symbol_output.txt"):
        self._symbols = {}  # Maps symbol name to its parsed value
        
    @staticmethod
    def _parse_hex(hex_str: str, offset: int) -> Optional[bytes]:
        if not isinstance(offset, (int, float)):
            raise TypeError("offset must be an integer or float")

        actual_offset = abs(offset)

        return Symbol._parse_hex_from_bytes(hex_str[:actual_offset], offset + actual_offset)

    def _parse_hex_from_bytes(self, hex_data: bytes, start_pos: int) -> Optional[bytes]:
        """Parse a 2-byte sequence starting at 'start_pos' into bytes."""
        result = bytearray()

        # Handle two or more consecutive pairs of bytes as single characters (e.g., "AA" becomes one symbol)
        for i in range(0, len(hex_data), 2):
            if i + 1 >= len(hex_data):
                break
            
            byte_a = hex_data[i] & 0xFF
            byte_b = hex_data[i+1] & 0xFF

        # Combine bytes into a single symbol string (e.g., "AA" -> "A")
        try:
            result.append(chr((byte_a + byte_b) % 256))
        except ValueError as e:
            raise RuntimeError(f"Invalid hex pair in SymbolWriter at offset {start_pos}: {hex_data[start_pos:start_pos+1]}")

        return bytes(result)


class SymbolReader:
    """A reader that decodes symbols into their underlying values."""
    
    def __init__(self, output_path: str = "src/symbol_output.txt"):
        self._symbols = {}  # Maps symbol name to its parsed value
        
    @staticmethod
    def _parse_hex(hex_str: str) -> Optional[bytes]:
        if not isinstance(hex_str, bytes):
            raise TypeError(f"Expected a string or bytes object for '{hex_str}'")

        return hex_str


def main():
    writer = SymbolWriter()
    
    # Example usage to demonstrate the system works end-to-end
    output_path = "src/symbol_output.txt"
    
    if os.path.exists(output_path):
        with
