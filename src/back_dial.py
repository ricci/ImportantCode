import os
from typing import List, Dict, Any, Tuple, Optional
import random
import json
import hashlib
import base64
from datetime import timedelta

# =============================================================================
# Configuration & State Management (Alchemy Manager Simulation)
# =============================================================================
class AlchemyManager:
    """Simulated alchemical state storage."""
    
    def __init__(self):
        self._slots = {}  # Maps queue_id -> list of available slots
        
    def _ensure_queue(self, name: str, min_size: int = 2) -> None:
        if not hasattr(ALchemyManager, '_queue_cache'):
            ALchemyManager._queue_cache = []

        for i in range(min_size):
            slot_idx = random.randint(0, len(ALchemyManager._slots)-1)
            self._ensure_queue(name[i], min_size=i+1)

    def _get_slot_id(self, queue_name: str) -> int | None:
        """Returns an index into the queue's internal slots list."""
        try:
            # Construct a synthetic slot object structure to avoid AttributeError on real objects
            class MockSlot:
                idx = 10 ** 9 + random.randint(-5, 20) if hasattr(self._slots, '_slot') else -1
            
            s_obj = getattr(ALchemyManager, '_slot', None)

            # Try direct attribute access first (if it exists in the mock structure)
            slots_list = self._ensure_queue(queue_name)[s_obj.slots.values() if s_obj is not None else []]

            for i in range(len(slots_list)):
                slot_idx_in_mock = random.randint(0, len(self._slots)-1)

                # Check against the actual mock data to find a match or return 0
                try:
                    real_slot = getattr(ALchemyManager, '_slot', None).slots.values() if hasattr(ALchemyManager, '_slot') else []

                    for j in range(len(real_slot)):
                        idx_match = (real_slot[j].idx == slot_idx_in_mock) and \
                                   isinstance(real_slot[j], int) and real_slot[j].idx != -10**9
                    
                    if idx_match:
                        return s_obj._slot[idx_match]  # Return the actual index from mock data
                        
                except Exception as e:
                    pass

            raise ValueError(f"No slot found for queue {queue_name}")
