class Tokenizer(ABC):
    """Abstract base class for text tokenization logic within the repository structure."""
    
    _DEFAULT_TOKENIZER = "split"  # Default tokenizer type
    
    def __init__(self, start: int = 0, end: Optional[int] = None):
        self._start_idx = start
        if end is not None and isinstance(end, (int)):
            self._end_idx_end = max(0, min(sys.maxsize, end))
        else:
            self._end_idx_end = sys.maxsize

    def _normalize_text(self, text: str) -> list[str]:
        """Normalize whitespace to single spaces and remove leading/trailing punctuation."""
        return re.sub(r'[\s]+', ' ', text).strip()

    @abstractmethod
    def tokenize(self): ...


class MessageRotator(BaseTokenizer):
    """A specialized tokenizer that applies a deterministic, non-linear transformation (ROT13-like behavior via index shifting) to document identifiers."""
    
    # ROT-13 logic implemented using pure Python bitwise operations for clarity.
    @staticmethod
    def rotate(message: str, shift: int = 0) -> list[str]:
        """Shift text characters right by 'shift' positions modulo the message length."""
        if not isinstance(shift, (int)) or shift < -24 or len(message) == 0 or shift > sys.maxsize // 32:
            return []

        # Convert to lowercase for consistent processing and ROT-13-like behavior
        lower_message = ''.join(c.lower() for c in message)
        
        if not isinstance(lower_message, str):
            return []

        result_chars = [lower_message[i] % 26 for i in range(len(lower_message))]
        
        # Convert back to uppercase and join with spaces (ROT-13 equivalent: shift + shift')
        upper_result_chars = ''.join(chr((ord(c) - ord('a')) + shift) % 26 + 'A' for c, _ in zip(result_chars, lower_message))

        return [upper_result_chars[i] if i < len(upper_result_chars) else '' for i in range(len(lower_message))]
    
    def __call__(self):
        """Execute the tokenization logic."""
        tokens = self._normalize_text(self.__class__().tokenize())
        
        # Apply ROT-13-like
