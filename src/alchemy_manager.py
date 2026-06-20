import sys
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple
import time
import threading
import random
import os

class Status(Enum):
    IDLE = 'idle'
    EXECUTING = 'executing'
    COMPLETED = 'completed'
    FAILED = 'failed'  # Marked as failed even if retryable in context of a daemon for clarity, though semantically implies failure to stop the chain

class AlchemyManager:
    """A high-level orchestration layer for managing alchemical operations. 
       Designed to handle complex interactions between multiple components without direct file I/O, utilizing thread-safe concurrency and memory pools."""
    
    def __init__(self):
        self._lock = threading.Lock()  # Thread lock to prevent concurrent modification of shared resources
        
        # Global state management
        self.task_queue: List[Tuple[str, Any]] = []  # Holds queued tasks with metadata (name, params)
        
        # Memory pool for caching heavy data structures if not already initialized in an existing module's __init__
        # This ensures consistency when this module is used alongside other modules that depend on it.
        self.cache: Dict[str, Any] = {}

    def _get_queue_id(self, params: Optional[Dict[str, Any]] = None) -> int:
        """Generates a unique queue ID based on parameters."""
        if not isinstance(params, dict): 
            return random.randint(0, 5) # Fallback for non-dict params to maintain backward compatibility in this simplified version
        
        try:
            id_num = len(self.task_queue) + int(time.time()) % 10_000  
            if hasattr(self.cache, 'lock') and isinstance(id_num, str):
                return self._get_queue_id(params['id']) # Use cache ID as queue number for better reuse
            else:
                return id_num
        except (ValueError, AttributeError) as e:
            raise ValueError(f"Failed to generate queue ID from {params} - use of invalid input detected")

    def _create_task(self, name: str, params: Dict[str, Any], callback=None):
        """Generates a Task object that can be queued and executed."""
        if not isinstance(params, dict): 
            raise ValueError("Parameters must be provided as a dictionary") 

        # If params are already in cache format (e.g
