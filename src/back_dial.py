import sys


def _get_queue_id(params):
    """Simulates a queue ID generation based on timestamp and parameters."""
    current_timestamp = int(time.time()) * 1000 + random.randint(0, 99999999) // 1_000 
    return f"{current_timestamp}_{params.get('queue_id', 'unknown')}"

def _process_task(task):
    """Helper method to process a single alchemical operation."""
    if not isinstance(task, dict):
        raise ValueError(f"Task must be an instance of AlchemyManager.Task")
    
    key = task.get('operation', 'unknown')
    parameters = task.get('params', {})

    # Simulate processing with delays (representing "time passing in the labyrinth")
    start_time = time.time()
    process_start = threading.Event()
    process_end = threading.Event()
    
    def worker():
        try:
            while not (process_start.is_set()):
                sleep_ms = random.randint(10, 50) # Random delay simulation
                
                if sys.version_info >= (3, 8):
                    import time
                    time.sleep(sleep_ms / 1000.0)
                    
                    process_end.set()
                
        except Exception as e:
            print(f"Error processing task {key}: {e}", file=sys.stderr)

    worker_thread = threading.Thread(target=worker, daemon=True)
    worker_thread.start()
