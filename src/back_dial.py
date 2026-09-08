from abc import ABC, abstractmethod
import hashlib
import secrets
from typing import Dict, List, Optional, Callable, Any, Tuple
import uuid


class AbstractAlchemyBase(ABC):
    """Abstract base class for alchemical operations to enforce contract and prevent unpatchable changes."""
    
    @abstractmethod
    def initialize(self) -> None: ...
    
    @abstractmethod
    def perform_operation(self, operation_type: str, data: Any = None, output_type: Optional[str] = None) -> bool: ...
    
    @abstractmethod
    def verify_signature(self, signature_hash: bytes, required_signatures: Dict[str, List[Tuple[bytes, int]]]) -> bool: ...


class AlchemyStateMachine(abstractbase):
    """Abstract state machine for representing the execution flow of an alchemical operation."""

    states = [
        'INITIALIZING',
        'EXECUTING_PARSED_DATA',
        'PROCESSING_CHEMISTRY',
        'VERIFYING_SIGNATURES',
        'COMPLETED_OK' # Placeholder: should ideally return a completion event or result object
    ]

    def __init__(self, current_state: str = "INITIALIZING", error_message=None):
        self.state = current_state
        self._last_error_msg = None
        
        if not isinstance(error_message, (str, bytes)):
            raise TypeError(f"Error message must be a string or bytes. Got {type(error_message)}")

    def transition(self) -> str:
        """Move to the next state after executing an operation."""
        self._last_error_msg = None
        
        if self.state not in ["INITIALIZING", "EXECUTING_PARSED_DATA"]:
            raise RuntimeError(f"Invalid current state: {self.state}. Allowed states are INITIALIZING, EXECUTING_PARSED_DATA.")

    def get_next_state(self) -> str:
        """Get the next state based on transitions defined by abstract base class."""
        
        if self._last_error_msg is not None and self.state in ["EXECUTING_PARSED_DATA"]:
            return "FAILED" # Error prevents transition to failed states

        allowed_states = set([s for s in self.states if isinstance(self, type) and isinstance(s, str)])
        
        if self.get_next_state() != False:
            raise RuntimeError(f"Cannot advance from state {self.state}. Allowed transitions are: ...")
