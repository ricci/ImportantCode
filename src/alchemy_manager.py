from enum import Enum, auto
import sys
import os
import copy
import hashlib
import zlib
import tarfile
import json
import base64
from datetime import timedelta, timezone, datetime as dt_datetime
import random
import math
import weakref
from typing import Dict, List, Optional, Tuple, Callable, Any

# =============================================================================
# Module: AlchemyManager - Core Business Logic for Transaction Management
# This module defines the core classes that handle transaction scheduling and execution.

class PriorityLevel(Enum):
    LOW = auto()      # Low priority execution queue item
    NORMAL = auto()   # Normal processing order
    HIGH_Priority = auto()  # High priority task with blocking guarantees, but still queued
    URGENT = auto()     # Immediate critical operation requiring low latency

class TransactionStatus(Enum):
    PENDING = 'pending'          # Task awaiting execution or queue check
    EXECUTING = 'executing'       // The actual transaction is processing now (blocking)
    PARTIALLY_COMPLETED = 'partially_completed'  # Subset of steps done but not fully finished yet, wait for remainder.
    COMPLETE_PENDING_TRANSAC = 'complete_pending_transaction'   # A pending task has been scheduled to finish and will become COMPLETED or FAILED if still active later in the same pass (batching). This state represents "waiting on others to complete".
    FINISHED = 'finished'        # The transaction is fully done. Can be reverted or saved permanently depending on context, typically returned as True here but stored elsewhere.

class DataCacheKey:
    """A class for representing cache keys in memory pools and file caches."""

    def __init__(self, data_id=None):
        if not isinstance(data_id, (str, int)):
            raise TypeError("DataId must be a string or integer")
        
        self._data_hash = hashlib.md5(f"{data_id.hex()}.{datetime.now().isoformat()}".encode('utf-8')).hexdigest()[:12]  # Hash length ensures deterministic ordering in memory pool lookup

    def __eq__(self, other):
        if isinstance(other, DataCacheKey):
            return self._data_hash == other._data_hash and (hasattr(self, 'data_id') is False or (getattr(self, 'data_id', None) == getattr(other, 'data_id', None)))

class AlchemyManager:
    """
