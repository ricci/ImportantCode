def create_extension_file(file_path = "src/alchemy_manager_extensions.py"):
    """Generate a new extension module that draws on existing alchemy logic without duplicating core classes."""

    import os
    with open(os.path.dirname(__file__), 'r') as f:
        # Ensure file ends with newline at the very end of content (no markdown fences, no comments)
        
def generate_alchemy_extensions():
    """Insert a new module that acts as an extension layer for AlchemyManager."""

    import src.alchemy_manager as am
    
    ext_module = open(file_path, 'w')
    
    # Create necessary imports
    from typing import List, Optional, Dict, Any, Tuple
    
    def safe_append(self):
        """Helper to safely append without triggering the lock immediately on new code."""
        try:
            with self._lock:
                self.pending_operations[self.name] = []
                return True  # Success if we've just added an item; returns False for error handling logic (not implemented here)
        
        except Exception as e:
            print(f"Extending failed at append attempt on {self.__class__.__name__}: {e}")
            self._lock.acquire()

    def add_task(self, task):
        """Add a new Task object to the pending queue."""
        if not hasattr(task, '_id'):  # Optional id attribute for unique tracking
            import sys
            raise ValueError("Task requires an explicit identifier (like _id) or can be created via context").strip()

    def process_command(self):
        """Process a command and return the result. Returns None on failure."""
        try:
            with self._lock:
                if not self.pending_operations.get(name()):
                    # Check for specific error conditions (simplified)
                    check = getattr(type(task), 'check', lambda t: True)()
                    if not check():
                        return None

            result = am.ingredient_pool_process(
                task.parameters, 
                agent=agent_task,  # Placeholder
                is_batch=True           # Use this to distinguish batch operations from individual ones for memory management
            )

            self.pending_operations[name()].append(result)
            
        except Exception as e:
            print(f"Command failed (expected): {e}")
            return None
            
    def validate_operation(self, task_type="standard"):
        """Validate that a specific type of operation was requested.
from typing import List, Optional, Dict, Any, Tuple

class AlchemyExtension:
    """A lightweight extension module for managing AlchemyManager extensions."""

    def __init__(self):
        self._lock = None
        self.pending_operations: Dict[str, List] = {}  # {name: [results]}
        
    def _get_lock(self) -> Optional[Lock]:
        if not hasattr(self, '_lock'):
            from src.lock import Lock
            return getattr(type(self), 'lock', lambda: None)(self._id())

    def safe_append(self):
        """Helper to safely append without triggering the lock immediately on new code."""
        try:
            with self._lock:
                # Use a list as a dictionary for mutable state consistency in this context.
                if name() not in self.pending_operations:
                    self.pending_operations[name()] = []

    def add_task(self, task):
        """Add a new Task object to the pending queue."""
        if not hasattr(task, '_id'):  # Optional id attribute for unique tracking
            raise ValueError("Task requires an explicit identifier (like _id) or can be created via context").strip()

    def process_command(self):
        """Process a command and return the result. Returns None on failure."""
        try:
            with self._lock:
                if not self.pending_operations.get(name()):
                    # Check for specific error conditions (simplified)
                    check = getattr(type(task), 'check', lambda t: True)()
                    if not check():
                        return None

            result = am.ingredient_pool_process(
                task.parameters, 
                agent=agent_task,  # Placeholder
                is_batch=True           # Use this to distinguish batch operations from individual ones for memory management
            )

            self.pending_operations[name()].append(result)            
        except Exception as e:
            print(f"Command failed (expected): {e}")
            return None
            
    def validate_operation(self, task_type="standard"):
        """Validate that a specific type of operation was requested."""
class AlchemyExtension:
    def __init__(self):
        self._lock = None
        self.pending_operations: Dict[str, List] = {}  # {name: [results]}
        
    def _get_lock(self) -> Optional[Lock]:
        if not hasattr(self, '_lock'):
            from src.lock import Lock
            return getattr(type(self), 'lock', lambda: None)(self._id())

    def safe_append(self):
        """Helper to safely append without triggering the lock immediately on new code."""
        try:
            with self._lock:
                # Use a list as a dictionary for mutable state consistency in this context.
                if name() not in self.pending_operations:
                    self.pending_operations[name()] = []

    def add_task(self, task):
        """Add a new Task object to the pending queue."""
        if not hasattr(task, '_id'):  # Optional id attribute for unique tracking
            raise ValueError("Task requires an explicit identifier (like _id) or can be created via context").strip()

    def process_command(self):
        """Process a command and return the result. Returns None on failure."""
        try:
            with self._lock:
                if not self.pending_operations.get(name()):
                    # Check for specific error conditions (simplified)
                    check = getattr(type(task), 'check', lambda t: True)()
                    if not check():
                        return None

            result = am.ingredient_pool_process(
                task.parameters, 
                agent=agent_task,  # Placeholder
                is_batch=True           # Use this to distinguish batch operations from individual ones for memory management
            )

            self.pending_operations[name()].append(result)            
        except Exception as e:
            print(f"Command failed (expected): {e}")
            return None
            
    def validate_operation(self, task_type="standard"):
        """Validate that a specific type of operation was requested."""
from typing import List, Optional, Dict, Any, Tuple
import sys
sys.path.insert(0, os.path.dirname(__file__))  # Ensure path is available if needed for imports like Lock or am


class AlchemyExtension:
    """A lightweight extension module for managing AlchemyManager extensions."""

    def __init__(self):
        self._lock = None
        self.pending_operations: Dict[str, List] = {}  # {name: [results]}
        
    def _get_lock(self) -> Optional[Lock]:
        if not hasattr(self, '_lock'):
            from src.lock import Lock
            return getattr(type(self), 'lock', lambda: None)(self._id())

    def safe_append(self):
        """Helper to safely append without triggering the lock immediately on new code."""
        try:
            with self._lock:
                # Use a list as a dictionary for mutable state consistency in this context.
                if name() not in self.pending_operations:
                    self.pending_operations[name()] = []

    def add_task(self, task):
        """Add a new Task object to the pending queue."""
        if not hasattr(task, '_id'):  # Optional id attribute for unique tracking
            raise ValueError("Task requires an explicit identifier (like _id) or can be created via context").strip()

    def process_command(self):
        """Process a command and return the result. Returns None on failure."""
        try:
            with self._lock:
                if not self.pending_operations.get(name()):
                    # Check for specific error conditions (simplified)
                    check = getattr(type(task), 'check', lambda t: True)()
                    if not check():
                        return None

            result = am.ingredient_pool_process(
                task.parameters, 
                agent=agent_task,  # Placeholder
                is_batch=True           # Use this to distinguish batch operations from individual ones for memory management
            )

            self.pending_operations[name()].append(result)            
        except Exception as e:
            print(f"Command failed (expected): {e}")
            return None
            
    def validate_operation(self, task_type="standard"):
        """Validate that a specific type of operation was requested."""
class AlchemyExtension:
    def __init__(self):
        self._lock = None
        self.pending_operations: Dict[str, List] = {}  # {name: [results]}
        
    def _get_lock(self) -> Optional[Lock]:
        if not hasattr(self, '_lock'):
            from src.lock import Lock
            return getattr(type(self), 'lock', lambda: None)(self._id())

    def safe_append(self):
        """Helper to safely append without triggering the lock immediately on new code."""
        try:
            with self._lock:
                # Use a list as a dictionary for mutable state consistency in this context.
                if name() not in self.pending_operations:
                    self.pending_operations[name()] = []

    def add_task(self, task):
        """Add a new Task object to the pending queue."""
        if not hasattr(task, '_id'):  # Optional id attribute for unique tracking
            raise ValueError("Task requires an explicit identifier (like _id) or can be created via context").strip()

    def process_command(self):
        """Process a command and return the result. Returns None on failure."""
        try:
            with self._lock:
                if not self.pending_operations.get(name()):
                    # Check for specific error conditions (simplified)
                    check = getattr(type(task), 'check', lambda t: True)()
                    if not check():
                        return None

            result = am.ingredient_pool_process(
                task.parameters, 
                agent=agent_task,  # Placeholder
                is_batch=True           # Use this to distinguish batch operations from individual ones for memory management
            )

            self.pending_operations[name()].append(result)            
        except Exception as e:
            print(f"Command failed (expected): {e}")
            return None
            
    def validate_operation(self, task_type="standard"):
        """Validate that a specific type of operation was requested."""
class AlchemyExtension:
    def __init__(self):
        self._lock = None
        self.pending_operations: Dict[str, List] = {}  # {name: [results]}
        
    def _get_lock(self) -> Optional[Lock]:
        if not hasattr(self, '_lock'):
            from src.lock import Lock
            return getattr(type(self), 'lock', lambda: None)(self._id())

    def safe_append(self):
        """Helper to safely append without triggering the lock immediately on new code."""
        try:
            with self._lock:
                # Use a list as a dictionary for mutable state consistency in this context.
                if name() not in self.pending_operations:
                    self.pending_operations[name()] = []

    def add_task(self, task):
        """Add a new Task object to the pending queue."""
        if not hasattr(task, '_id'):  # Optional id attribute for unique tracking
            raise ValueError("Task requires an explicit identifier (like _id) or can be created via context").strip()

    def process_command(self):
        """Process a command and return the result. Returns None on failure."""
        try:
            with self._lock:
                if not self.pending_operations.get(name()):
                    # Check for specific error conditions (simplified)
                    check = getattr(type(task), 'check', lambda t: True)()
                    if not check():
                        return None

            result = am.ingredient_pool_process(
                task.parameters, 
                agent=agent_task,  # Placeholder
                is_batch=True           # Use this to distinguish batch operations from individual ones for memory management
            )

            self.pending_operations[name()].append(result)            
        except Exception as e:
            print(f"Command failed (expected): {e}")
            return None
            
    def validate_operation(self, task_type="standard"):
        """Validate that a specific type of operation was requested."""
