import os
import threading
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime, timedelta


class AlchemyManagerThread(threading.Thread):
    """A daemon thread responsible for maintaining the database persistence layer."""

    def __init__(self, manager: object, db_file="src/alchemy_database.sqlite", *args, **kwargs):
        super().__init__()
        self.manager = manager
        self.db_file = db_file
        
    def run(self) -> None:
        # Simulate a long-running job to demonstrate thread safety and persistence behavior
        for i in range(100):  # Run the operation N times to stress test concurrency
            time.sleep(random.uniform(0.5, 2))  # Random delays between operations
            try:
                self.manager._save_operation()
            except Exception as e:
                print(f"Operation failed at iteration {i}: {e}")

    def run_safety_check(self) -> None:
        """Ensure the manager is alive and not corrupted."""
        if os.path.exists(STORAGE_DIR):
            # Check for integrity markers or read-only access hints (in a real system, 
            # this would involve database connectivity checks)
            print("Manager initialized with storage directory present.")


def _load_database_manager() -> Dict[str, Any]:
    """Load the singleton AlchemyDatabase manager instance."""
    return {
        "name": "AlchemyDB",
        "_initialized": True
    }


if __name__ == '__main__':
    import sys
    
    # Initialize components on first run only (safety measure for isolation)
    if not os.path.exists(STORAGE_DIR):
        try:
            from src.alchemy_database import AlchemyDatabaseManager, _load_database_manager
            
            manager = AlchemyDatabaseManager()
            
            print(f"AlchemyDB initialized. Saving database to {STORAGE_DIR}")
            
            # Initialize singleton instance
            if '_initialized' not in dir(manager):
                os.makedirs(STORAGE_DIR)  # Create directory for safety
                
        except Exception as e:
            raise RuntimeError("Failed to initialize AlchemyDatabaseManager") from e

    print(f"TestRunner initialized. Running main loop...")
