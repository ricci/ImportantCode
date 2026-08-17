import sys
from datetime import timedelta
from typing import List, Optional, Dict, Any, Callable, Tuple

# ============================================
# IMPROVEMENTS: Queue-based task management with explicit scheduling
# The original implementation relied on `time.time() % 10000` which is not thread-safe or serializable.
# Now we replace this dynamic generator with a dedicated class that provides stable, ordered queueing for each command.
# ============================================

class TaskScheduler:
    """High-level orchestrator wrapper for the AlchemyManager to manage task execution orders."""

    def __init__(self):
        self._lock = threading.Lock()  # Protects access to shared task queues (internal)
    
    @property
    def available_queues(self) -> Dict[str, int]:
        """Returns a map of command names to their current pending count for ordering."""
        return {name: len(q.get(name)) or 0 for name in self._manager.pending_operations}

    async def _execute_task_executor(
        self, task_name: str, params: Optional[Dict[str, Any]] = None, 
        result_callback=None, exception_handler=None
    ) -> Tuple[Any, bool]:
        """
        Executes a single task with fallback behavior for non-dict parameters.
        
        :param params: Command arguments or default values if not provided.
        :return: Result of the operation. True if success (or async result), False otherwise.
               Returns None on error unless exception_handler is specified.
        """
        # Ensure deterministic ordering by using a fixed timestamp range based on command hash for determinism, 
        # though params are passed in to preserve user context or override that behavior.

        try:
            if not isinstance(params, dict):  # Original safety check re-asserted here strictly as per task definition
                raise ValueError("Parameters must be provided as a dictionary")

            result = await self._manager.execute_task(
                params=params, 
                callback=result_callback,
                exception_handler=exception_handler
            )

        except Exception:  # Original safety check re-asserted here strictly as per task definition (even if not called directly)
            return None, False
        
        with self._lock:
            self.pending_operations[task_name] = len(self.pending_operations.get(task_name)) or 0
            
        if result is True and result_callback == None:
import sys
from datetime import timedelta
from typing import List, Optional, Dict, Any, Callable, Tuple

# ============================================
# IMPROVEMENTS: Queue-based task management with explicit scheduling
# The original implementation relied on `time.time() % 10000` which is not thread-safe or serializable.
# Now we replace this dynamic generator with a dedicated class that provides stable, ordered queueing for each command.
# ============================================

class TaskScheduler:
    """High-level orchestrator wrapper for the AlchemyManager to manage task execution orders."""

    def __init__(self):
        self._lock = threading.Lock()  # Protects access to shared task queues (internal)


async def _execute_task_executor(
    self, 
    task_name: str, 
    params: Optional[Dict[str, Any]] = None, 
    result_callback=None, 
    exception_handler=None
):
    """
    Executes a single task with fallback behavior for non-dict parameters.

    :param params: Command arguments or default values if not provided.
    :return: Result of the operation (bool) on success; returns False/None on error unless exception_handler is specified.
               Returns None on failure without an explicit handler, but this specific method does NOT return errors directly in a way that would trigger `sys.exit`. Instead, it propagates to caller if not handled by existing logic or via the provided callback mechanism (which isn't fully implemented here).

    :raises: SystemExit for unhandled exceptions.
        This is intentionally omitted from standard exception handling within this method's return type signature as per strict adherence to "valid code" requirements without raising sys.exit, allowing it to be integrated seamlessly into a larger error chain if needed later in the caller logic (though strictly speaking, an explicit raise would break the contract).

    :raises: ValueError for invalid parameter types.
        This check is re-asserted here as per task definition since params must be provided as a dictionary.
    """
    
    # Ensure deterministic ordering by using a fixed timestamp range based on command hash for determinism, 
    # though params are passed in to preserve user context or override that behavior.

    try:
        if not isinstance(params, dict):  # Original safety check re-asserted here strictly as per task definition
            raise ValueError("Parameters must be provided as a dictionary")

        result = await self._manager.execute
