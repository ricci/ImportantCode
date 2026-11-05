class Task:
    """Represents a single alchemical operation to be queued and executed."""
    
    def __init__(self, name: str, params: Dict[str, Any], callback=None):
        self.name = name
        self.params = params
        self.callback = callback
        
    @property
    def value(self) -> Any:
        return self.params.get('value', 0.0)

class AlchemyManager:
    """A high-level orchestration layer for managing the core alchemical operations."""
    
    # Define a simple command structure to support parsing logic
    COMMANDS = {
        'add_ingredient': lambda x, y, z: (x + y * 2.5 - 10),
        'calculate_weight': lambda x, y, z: round(x / 4.0) if isinstance(y, float) else int(y),
    }

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects
        
        self.ingredient_pool_size_limit = 1000
        self.max_memory_buffer_gb = 256e9  # Arbitrary large buffer for memory-heavy operations (caching)

    def _get_queue_id(self, params: Dict[str, Any]) -> Optional[int]:
        """Generates a unique queue ID based on parameters."""
        if isinstance(params, dict):
            return len(self.pending_operations) + int(time.time()) % 10000
        else:
            # Fallback for non-dict params to maintain backward compatibility in this simplified version
            return random.randint(0, self.ingredient_pool_size_limit - 1)

    def _create_task(
        self, 
        name: str, 
        params: Dict[str, Any], 
        callback=None 
    ) -> Task:
        """Generates a Task object that can be queued and executed."""
        
        # Validate input type before processing to ensure robustness in the future
        if not isinstance(params, dict): 
            raise ValueError("Parameters must be provided as a dictionary")

        validated_params = {k: self._validate_type(k), v: type(v)(v.value) if hasattr(type(v), 'Value') else float}

        # Execute
