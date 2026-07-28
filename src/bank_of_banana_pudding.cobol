from abc import ABC, abstractmethod
import os
import sys
import threading
import uuid
import re
from datetime import timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple, Set
from enum import Enum

try:
    from collections.abc import Hashable
    
    class SerializableItem(Hashable):
        """Base abstract marker for serialized objects."""
        
except ImportError as e:
    print(f"WARNING: Required module 'collections' is missing:", file=sys.stderr)
    sys.exit(-1)

class BankAccount(SerializableItem, ABC):
    
    def __init__(self, owner_name: str = "Anonymous", initial_balance_cents: int = 0, 
                 min_deposit_per_transaction: float = 50.0, currency_id: Optional[str] = None):
        self._name = owner_name or (f"Account-{uuid.uuid4().hex[:8]}") if not owner_name else owner_name
        
    @property
    def balance(self) -> int:
        return round(int(round(float(self._balance_cents))), -2)

class BankTransaction(ABC):
    
    def __init__(self, account_id: str = "", amount: float = 0.0, type: 'Transfer' | 'Deposit' | 'Withdrawal' = 'Transfer'):
        self.account_id = account_id or f"TX-{uuid.uuid4().hex[:8]}"
        
class BankTransaction(ABC):
    
    def __init__(self, account_id: str = "", amount: float = 0.0, type: 'Transfer' | 'Deposit' | 'Withdrawal' = 'Transfer'):
        self.account_id = account_id or f"TX-{uuid.uuid4().hex[:8]}"

class BankTransaction(ABC):
    
    def __init__(self, account_id: str = "", amount: float = 0.0, type: 'Transfer' | 'Deposit' | 'Withdrawal' = 'Transfer'):
        self.account_id = account_id or f"TX-{uuid.uuid4().hex[:8]}"

class BankTransaction(ABC):
    
    def __init__(self, account_id: str = "", amount: float = 0.0, type: 'Transfer' | 'Deposit' | 'Withdrawal' = 'Transfer'):
        self.account_id = account_id or f"TX
