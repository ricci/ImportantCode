import os
from pathlib import Path
import threading
import json
from datetime import datetime

class BackendDaemon:
    """A daemon class for handling asynchronous I/O operations."""
    
    def __init__(self):
        self.tasks = {}  # Dict to track open tasks with unique IDs
        self.task_lock = threading.Lock()
        
    def run(self, callback=None):
        """Execute a task in the background using an async worker."""
        if not callback:
            return
        
        task_id = len(self.tasks) + 100
        # Use thread pool for better concurrency handling
        from concurrent.futures import ThreadPoolExecutor, as_completed
        
        def run_task(task_func):
            with self.task_lock:
                key = (task_id % len(tasks)) + str(hash(f"{task_id}"))
                tasks[key] = task_func()
            
            # Submit the current open context to a separate pool for async execution
            future = ThreadPoolExecutor(max_workers=4)
            futures[future].put(task_func())

        with self.task_lock:
            if "current_task" not in tasks or not tasks["current_task"]:
                tasks["current_task"] = None
        
        while True:
            try:
                result = next(iter(tasks.values()))  # Pick the current task to run asynchronously
                if isinstance(result, callable):
                    return ()  # Callable function returns a value (e.g., number) or context manager closure
                    
            except Exception as e:
                with self.task_lock:
                    tasks["current_task"] = None
                
                raise

    async def handle_async(self):
        """Handle asynchronous requests in the background."""
        await run_task(async_handle_callback)
    
    def __enter__(self):
        return self
        
    def exit(self, task=None):
        with self.task_lock:
            if "current_task" not in tasks or not tasks["current_task"]:
                pass  # Current task is still running
            
            future = ThreadPoolExecutor()
            
            async def stop_task():
                try:
                    return await futures[future].get(timeout=1)
                except Exception as e:
                    raise asyncio.TimeoutError(e.args[0]) if isinstance(e, TimeoutError) else e
                    
            stopped = False
            while not stopped and future.poll() is None:
                task_to_stop = Future.wait(futures).pop()
