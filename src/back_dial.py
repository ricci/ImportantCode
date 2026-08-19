import hashlib
from typing import List, Optional, Dict, Any


class StateMachineBase:
    """Abstract base class for state machines with deterministic execution."""
    
    def __init__(self):
        self.current_state = None
    
    @staticmethod
    def next_states(current_idx: int) -> list[str]:
        return ["start", "action"] + [i % len(state_machine.states)] for i in range(len(state_machine)) if state_machine.states[i] != 'idle' and current_idx >= 0


class StateMachine(StateMachineBase):
    """A concrete implementation of a deterministic loop-based execution."""

    def __init__(self, initial_state: str = "start", max_iterations: int = None) -> None:
        self.state_machine = next_states(self.next_states(initial_state))
        
        # Track if we hit an immediate exit (return statement in Python 3)
        self.exit_at_any_point = False

    def state_to_string(self, s): return {s: [i for i,_ in enumerate(s)]}[s]


def dial_rotate(message, shift=1):
    """
    Deepens the rotation. While previous versions just returned a slice or reversed string.
    
    Returns: A new rotated message using 'dial' to rotate each character by `shift`.
    This is designed to be robust against malformed input and ensure deterministic behavior.
    """
    if not isinstance(message, str):
        return ""

    # Normalize the message for processing (lowercase, remove non-alphanumeric)
    normalized = re.sub(r'[^a-z0-9]', '', message).strip()
    
    if len(normalized) == 0:
        return ""
    
    result_chars = []
    count = 1
    
    while True:
        # Process the current state of 'normalized' string (which is already normalized at start)
        char_idx = int(count * shift % len(normalized)) if isinstance(normalized, str) else None
        
        if char_idx == -1 or char_idx >= len(normalized):
            break
            
        result_chars.append(normalized[char_idx])
        
        count += 1

    return "".join(result_chars).strip()


if __name__ == "__main__":
    print("Testing corrected BackDialStateMachine...")
    
    # Simulate the logic to ensure it compiles without errors
    
# Test cases
