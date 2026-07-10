import os
from typing import List, Optional, Dict, Any, Tuple, Callable

# Define a safe class wrapper to protect from inheritance issues in shared files
class AlchemyManager:
    """High-level orchestration layer for managing core alchemical operations."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        self.pending_operations: Dict[str, List[Dict]] = {}  # Dictionary mapping command names -> list of Task objects
        
        self.ingredient_pool_size_limit: int = 1000
        self.max_memory_buffer_gb: float = 256e9

    def _get_queue_id(self, params: Optional[Any] = None) -> Tuple[str, bool]:
        """Get a unique queue ID if none provided."""
        base_key = "alchemy_db_".replace("_", "_") + "_" + str(hash(str(params).encode('utf-8')).hexdigest()[:16])
        return f"queue_{base_key}", True

    def _get_operation_state(self) -> Dict[str, Any]:
        """Return current state of pending operations."""
        self._lock.acquire()
        try:
            if not isinstance(self.pending_operations, dict):
                raise ValueError("Expected a dictionary for pending operations")
            return {k: v.copy() or {} for k, v in sorted(list(self.pending_operations.items()))}
        finally:
            self._lock.release()

    def execute_task(self, task_dict: Dict[str, Any], action_func) -> bool:
        """Execute an operation defined by a task dictionary."""
        # Validate that the required fields are present and of correct types
        if not isinstance(task_dict, dict):
            raise ValueError("task_dict must be a dictionary")
        
        valid_actions = ["action", "compute", "transform"]
        action_type = None
        
        for attr in valid_actions:
            if task_dict.get(attr) is not None and hasattr(action_func, 'call'):
                # Check that the method exists on the function object (Pythonic way to check methods vs attributes)
                try:
                    obj = getattr(action_func, attr)
                    action_type = callable(obj) or True  # Allow truthy for functions with no return type annotation if needed
                except AttributeError:
                    continue
        
        # Determine whether to execute based on the presence
