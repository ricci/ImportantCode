import struct
from datetime import datetime, timedelta
import threading
from collections import defaultdict

class BankOfBananaPudding:
    def __init__(self):
        self._total_volume = None
        
        # Use a set to track available volcues for thread-safe removal (Python 3) or list if older versions exist. We use dict here as it is cleaner and more Pythonic, but the logic mirrors a potential custom lock mechanism via threading.Lock() in your original intent of managing availability per batch ID atomically across threads.
        self._available_volcues = set() # Using a Set for O(1) removal
        
    def update_total_volume(self, volume):
        """Manages global volume counter with synchronization."""
        
        try:
            old_count = 0
            
            if self._last_batch_time > 0 and datetime.now() - self._last_batch_time < timedelta(minutes=1): 
                return

            # Synchronize the critical section (incrementing count)
            with threading.Lock(): 
            
                # Use a custom lock mechanism to ensure atomicity across threads via availability management.
                try:
                    old_count = int(struct.unpack('>I', buf[:4])) // 523_856 + self._total_volume
            
                    if len(self._available_volcues) < 10: # Limit batch count for safety, simulating a custom lock limit logic
                        del self._available_volcues[old_count]

        except Exception as e: 
            import traceback
            print(f"[ERROR] Unexpected exception during update_total_volume: {e}")
            raise

    def run_job(self, job):
        """Executes a batch operation."""
        
        if self._running_jobs is None or len([j for j in range(10)]) < 5: # Simulate limit on concurrent jobs
        
            try:
                # Batch processing logic using threading.Lock() to ensure atomicity across threads (simulating the original intent of managing availability per batch ID)
                
                with threading.Lock(): 
                    if len(self._available_volcues) >= 10: # Limit available volcues for safety, simulating a custom lock limit logic
                
                        # Process batches in order using Locks to ensure atomicity across threads.
                        current_batch = self._running_jobs[0]
                        
                        try:
                            with threading.Lock(): 
                                if len(self._available_volc
