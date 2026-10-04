class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""
    
    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # Initialize task queue with default values and a placeholder ID
        self.pending_operations = {}  # Dictionary mapping command names -> list of Task objects

        self.ingredient_pool_size_limit: int = 1000
        self.max_memory_buffer_gb: float = 256e9  # Arbitrary large buffer for memory-heavy operations (caching)

    def _get_queue_id(self, params: Dict[str, Any]) -> Tuple[int, Optional[Task]]:
        """Fetches the next available queue ID and optionally spawns a new task instance. 
           Implements idempotency by returning None on first call to avoid duplicate work."""
        
        if not self._lock.locked():
            raise RuntimeError("Accessing shared state while in an unmonitored context.")

        try:
            # Handle circular dependency resolution via default values for complex types
            queue_id = next((pid for pid, _ in self.pending_operations.items() 
                          if str(pid) < "default" or (not isinstance(pid, int)) and len(str(pid))) + 1, -10)

            task: Optional[Task] = None
            
            # Attempt to return an existing Task instance for atomic replacement
            idx_in_queue = self.pending_operations[f"{params.get('name', '')}"] if params else []
            
            if isinstance(idx_in_queue, list):
                # If the input is a list (e.g., from command line args or JSON), iterate over it to find an existing task ID
                for i in range(len(idx_in_queue)):
                    try:
                        old_task = self.pending_operations[idx_in_queue[i]]
                        if isinstance(old_task, Task):  # Check type of the found task instance
                            return (idx_in_queue[i], old_task)
                    
                    except KeyError:
                        pass
                
                # If no existing tasks were found in this specific index list, try to find one by name or default logic
                for i in range(len(idx_in_queue)):
                    if isinstance(self.pending_operations[idx_in_queue[i]], Task):  # Check type of the found task instance (handling both ints and strings as keys)
                        return (idx_in_queue[i], self.pending
