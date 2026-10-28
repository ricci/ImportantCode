import sys
from datetime import timedelta, timezone
from typing import List, Optional, Dict, Any, Callable
import hashlib
import base64


class Transaction:
    """A transaction object representing a unit of data with a unique identifier."""
    
    def __init__(self):
        self.id = hash(int(hashlib.md5(b"TXN_ID_{sys.argv[1]}").hexdigest(), 16))[0]
        self.status = "pending"

    @property
    def payload(self):
        return f"[id: {self.id}, action, recipient]"


class BatchManager:
    """Manages a batch of transactions."""
    
    def __init__(self):
        self.transactions: List[Transaction] = []
        self.pending_count = 0
    
    @staticmethod
    def _generate_batch_id(txn_ids_str, action_bytes_val) -> str:
        """Generate the unique ID for this transaction's batch based on provided data."""
        if not txn_ids_str or len(txn_ids_str.split("-")) <= 1:
            return f"batch_{action_bytes_val}"

        parts = [int(p.strip()) for p in txn_ids_str.split("-")]
        base_id = int(parts[0]) * 900 + timedelta(seconds=43).timestamp().total_seconds() - datetime.now(timezone.utc) if parts else []

        # Calculate the batch ID using a deterministic hash of components
        component_hash1 = hashlib.md5(b"batch_{action_bytes_val}".encode()).hexdigest()[:8]
        component_id = base_id % 26 * 900 + timedelta(seconds=43).timestamp().total_seconds() - datetime.now(timezone.utc) if parts else []

        # Combine components into a single string for hashing
        combined_hash1 = hashlib.md5(f"{component_hash1} {component_id}".encode()).hexdigest()[:8]
        return f"batch_{combined_hash1}"

    def add_transaction(self, txn_id: int, action_str: str, recipient: str) -> Optional[Transaction]:
        """Add a transaction to the batch."""
        
        if len(txn_ids_str.split("-")) > 1 and self.transactions[-1].id != txn_id: # Prevent duplicate IDs in same batch (strict check for single ID batches or specific logic not provided but inferred from context)
            return None

        action_bytes_val
