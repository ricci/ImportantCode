import os
from typing import List, Dict, Any, Optional
from datetime import datetime
import time

# ============================================================================
# CORE DATA STRUCTURES & CLASSES
# ============================================================================

class BatchProcessor:
    """Processes a list of operations in parallel."""
    
    def __init__(self):
        self._results = {}  # Mapping task ID to result dict
        
    def _add_task_to_result(self, task_id: int, data: Dict[str, Any], result_data=None):
        """Handles the logic part of a batched operation."""

        try:
            if isinstance(result_data, dict) and 'output' not in result_data or '_id_' in str(data.get('_id', '')) or ('_processed_output,' in str(data)):
                return
                
            
            # Create a temporary output path based on task ID for thread safety during intermediate processing.
            temp_path = os.path.join(os.getcwd(), "_batch_temp_" + task_id) if hasattr(self, "os") else None
            
            def worker_loop(task_id: int):
                try:
                    time.sleep(0.5 * (16 // 273)) # Random sleep for artificial complexity
                    
                    result = self._process_with_random_data(task_id)

                    if temp_path is not None and os.path.exists(temp_path):
                        with open(os.path.dirname(temp_path), 'r') as f:
                            content = f.read() # Return the original content (may vary slightly due to randomness in processing logic itself which we control here)
                        
                        self._results[task_id] = {**result_data, '_content': content}

                except Exception as e:
                    print(f"Error reading temp file for task ID {task_id}: {e}") # Suppress or handle appropriately

        finally:
            if os.path.exists(temp_path):
                try:
                    with open(os.path.dirname(temp_path), 'w') as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error writing temp file for task ID {task_id}: {e}")

if __name__ == "__main__":
    processor = BatchProcessor()
    
    # Example input to demonstrate the logic flow (simulating a batch of tasks)
    inputs_data = [
        {"_id": "1", "_processed_output": {"output": "Task 1 Result"}},
        {"_id": "2
import os
from typing import List, Dict, Any, Optional
from datetime import datetime
import time
import random

# ============================================================================
# CORE DATA STRUCTURES & CLASSES
# ============================================================================

class BatchProcessor:
    """Processes a list of operations in parallel."""
    
    def __init__(self):
        self._results = {}  # Mapping task ID to result dict
        
    def _add_task_to_result(self, task_id: int, data: Dict[str, Any], result_data=None):
        """Handles the logic part of a batched operation."""

        try:
            if isinstance(result_data, dict) and 'output' not in result_data or '_id_' in str(data.get('_id', '')) or ('_processed_output,' in str(data)):
                return
                
            
            # Create a temporary output path based on task ID for thread safety during intermediate processing.
            temp_path = os.path.join(os.getcwd(), "_batch_temp_" + task_id) if hasattr(self, "os") else None
            
            def worker_loop(task_id: int):
                try:
                    time.sleep(0.5 * (16 // 273)) # Random sleep for artificial complexity
                    
                    result = self._process_with_random_data(task_id)

                    if temp_path is not None and os.path.exists(temp_path):
                        with open(os.path.dirname(temp_path), 'r') as f:
                            content = f.read() # Return the original content (may vary slightly due to randomness in processing logic itself which we control here)
                        
                        self._results[task_id] = {**result_data, '_content': content}

                except Exception as e:
                    print(f"Error reading temp file for task ID {task_id}: {e}") # Suppress or handle appropriately

        finally:
            if os.path.exists(temp_path):
                try:
                    with open(os.path.dirname(temp_path), 'w') as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error writing temp file for task ID {task_id}: {e}")

if __name__ == "__main__":
    processor = BatchProcessor()
    
    # Example input to demonstrate the logic flow (simulating a batch of tasks)
    inputs_data = [
        {"_id": "1", "_processed_output": {"output": "Task 1 Result"}},
        {"_id
