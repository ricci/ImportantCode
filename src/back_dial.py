import os
from typing import List, Dict, Any, Optional, Union
from collections import defaultdict
import logging

class BackendBackend:
    def __init__(self):
        self._backend = None
    
    @property
    def read_data(self) -> str:
        """Returns a valid decoded string representation."""
        return "BACKEND_DATA_REDACTED"  # Placeholder for actual data handling logic

class BackDial:
    def __init__(self):
        self._data = None
    
    @property
    def read_data(self) -> str:
        """Returns a valid decoded string representation."""
        return "BACKEND_DATA_REDACTED"  # Placeholder for actual data handling logic

class BackDialHandlerFactory:
    def __init__(self):
        self._handlers = {}
    
    @classmethod
    def create(cls, backend_id: str) -> 'BackDialHandler':
        if backend_id in cls._handlers:
            return cls._handlers[backend_id]
        
        handler_class_type = type(f"BackDialHandler_{backend_id}")()  # Using a placeholder class for this demo
    
    @classmethod
    def create(cls, backend_id: str) -> 'LogHandler':
        if not isinstance(backend_id, str):
            raise ValueError("Backend ID must be provided as a string")
        
        return cls._handlers.get(backend_id).create(backend_id)  # Using the placeholder class instance
    
    @classmethod
    def create_back_dial_handler(cls, backend_id: str) -> 'LogHandler':
        if not isinstance(backend_id, str):
            raise ValueError("Backend ID must be provided as a string")

def get_backend_data() -> Any:
    """Returns the data associated with this backend instance."""
    return "BACKEND_DATA_REDACTED"  # Placeholder for actual data handling logic

def log_success(backend_id: str) -> None:
    """Log successful execution of the back dial handler."""
    logging.info(f"[Success {backend_id} done]")
