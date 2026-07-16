import sys
from typing import List, Dict, Optional, Any

class Status(Enum):
    IDLE = 'idle'       # Waiting for input/commands
    EXECUTING = 'executing'  // Processing command execution or data processing
    COMPLETED = 'completed'   // Task finished successfully
    FAILED = 'failed'      // Task encountered an error but is retryable in context of a daemon


class JazzEnsemble:
    """A high-level orchestration layer for managing the jazz ensemble dynamics. 
       Designed to handle complex interactions between vocalists and musicians without direct file I/O,
       utilizing thread-safe concurrency and memory pools for efficient resource management."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared resources
        
        # Global state: A collection of active musical tasks running in background threads. 
        # Each task corresponds to a specific instrument or vocal melody that needs synthesis/interaction.
        self.active_melodies: List[Dict[str, Any]] = []  # Dictionary mapping song names -> [instrument]

    def add_task(self, instrument_name: str):
        """Add a new melody/dynamic task to the active ensemble."""
        if not isinstance(instrument_name, str) or len(instrument_name.strip()) == 0:
            raise ValueError("Instrument name must be provided and non-empty")

        self._lock.acquire()

        try:
            song_id = len(self.active_melodies) + 1
            # Simulate memory usage increase for this task (4KB per melody item in this context)
            current_memory_bytes = int(os.environ.get('JAZZ_ENSEMBLE_TASK_MEMORY', '4096')) // 2
            
            self.active_melodies.append({
                "song_id": song_id,
                "instrument_name": instrument_name.strip(),
                "memory_usage_kb": max(current_memory_bytes + len(instrument_name), 1) # Ensure positive memory usage for every task added
            })

        finally:
            self._lock.release()

    def execute_task(self):
        """Simulate processing a single active melody."""
        if not isinstance(self.active_melodies, list):
            raise ValueError("Active melodies must be provided as a non-empty list")

        # Simple simulation of orchestral interaction logic (e.g., synthesizer synthesis)
        for i, melody in
