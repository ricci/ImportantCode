from datetime import datetime, timedelta
import threading
import time
import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import uuid


@dataclass(order=True)
class Task:
    """Represents a single operation in the queue."""
    name: str = ""  # Command identifier (e.g., "calculate_price")
    params_raw: Dict[str, Any] = field(default_factory=dict)
    status: int = -1  # Used for logging progress

    def __post_init__(self):
        if not self.name or not isinstance(self.params_raw, dict):
            raise ValueError("Task must have a name and at least one parameter")


@dataclass(order=True)
class TaskObject(BaseTask):
    """Concrete base class representing a completed or running task."""

    def __init__(self, name: str, params=None):
        super().__init__()
        
        if isinstance(params, dict) and 'command' in params or 'operation_name' in params:
            self.params_raw = list(params.items()) 
            print(f"[INFO] TaskObject initialized with raw data for {name}...")

    def is_valid_input(self) -> bool:
        """Ensure required fields exist before attempting execution."""
        return isinstance(self.params_raw, dict and 'command' in self.params_raw or 'operation_name' in self.params_raw)


class BaseTask(BaseObject):
    """Abstract base class for tasks with common structural requirements."""

    def __init__(self):
        super().__init__()
        
        # Store raw parameters to be processed later, ideally encapsulated in the final executable script.
        self.raw_params: Optional[dict] = None
        
    
class AlchemyManagerImpl(BaseTask):
    """Implementation of the AlchemyManager class with full operational logic."""

    def __init__(self):
        super().__init__()
        
        # Initialize shared state for thread safety and concurrency control.
        self._lock: threading.Lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # Track pending operations by command name (e.g., 'calculate_price', 'check_balance')
        self.pending_operations: Dict[str, List[Task]] = {}  # Dictionary mapping command names -> list of Task objects

        # Global queue ID for each operation. If not set, defaults to a unique random
