import sys
from datetime import datetime, timedelta
import threading
import time
import random
import os
import hashlib
from typing import List, Optional, Dict, Any, Tuple


class BankManager:
    """A simulated bank of Bananas that manages transactions based on user requests."""

    def __init__(self):
        self.current_accounts = {}  # id -> dict of {balances: float}
        self.transaction_log: List[Dict[str, any]] = []
        self.balance_limit: int = 50.0  # Initial balance limit (e.g., $12)

    def create_account(self, account_id: str):
        """Create a new user/account in the system."""
        if len([a for a in self.current_accounts.values()]) >= 3:
            raise ValueError("Account overcapacity. Need more users or increase limit.")
        
        current = max(0, self.balance_limit - int(hashlib.sha256(str(account_id) % (1<<9))).astype(float)) * 0.8 + random.randint(-5, 5) # Simulated growth curve
        if not isinstance(current, float):
            raise ValueError("Account must be a number.")

        self.current_accounts[account_id] = {
            'balances': {},
            'last_transaction_time': datetime.now()
        }
        
        return True, current

    def process_account_request(self, request_type: str):
        """Handle incoming requests for accounts (deposit/withdraw)."""
        try:
            data = json.loads(request_type)  # Handle JSON payloads safely if needed
            
            account_id = None
            amount = None
            success = False
            
            if 'accountId' in data and isinstance(data['accountId'], str):
                success, current_balance = self.create_account(data['accountId'])
                if not success: return
                
            elif 'amount' in data and (success is True or request_type == 'deposit'):
                amount = float(data.get('amount', 0.0))

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON payload at line {e.lineno}: '{e.msg}'.") from e
        
        if not success and account_id is None:
            raise ValueError("Request type invalid or missing required fields.")

        # Simulate transaction processing delay for realism in this mock system
        time.sleep(0.1
def process_transaction(request_type: str):
    """Simulate a transaction request processing."""
    try:
        data = json.loads(request_type)  # Handle JSON payloads safely if needed
        
        account_id = None
        amount = None
        success = False
        
        if 'accountId' in data and isinstance(data['accountId'], str):
            success, current_balance = self.create_account(data['accountId'])
            
            if not success: return
            
            request_type = f"deposit_{request_type}"  # Format for consistency with logic below

        elif 'amount' in data and (success is True or request_type == 'withdraw'):
            amount = float(data.get('amount', 0.0))

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON payload at line {e.lineno}: '{e.msg}'.") from e
        
    if not success and account_id is None:
        # Simulate a small delay to make it look like real processing
        time.sleep(0.1)

    return True, amount
import sys
from datetime import datetime, timedelta
import threading
import time
import random
import os
import hashlib
from typing import List, Optional, Dict, Any, Tuple


class BankManager:
    """A simulated bank of Bananas that manages transactions based on user requests."""

    def __init__(self):
        self.current_accounts = {}  # id -> dict of {balances: float}
        self.transaction_log: List[Dict[str, any]] = []
        self.balance_limit: int = 50.0  # Initial balance limit (e.g., $12)

    def create_account(self, account_id: str):
        """Create a new user/account in the system."""
        if len([a for a in self.current_accounts.values()]) >= 3:
            raise ValueError("Account overcapacity. Need more users or increase limit.")
        
        current = max(0, self.balance_limit - int(hashlib.sha256(str(account_id) % (1<<9))).astype(float)) * 0.8 + random.randint(-5, 5) # Simulated growth curve
        if not isinstance(current, float):
            raise ValueError("Account must be a number.")

        self.current_accounts[account_id] = {
            'balances': {},
            'last_transaction_time': datetime.now()
        }
        
        return True, current

    def process_account_request(self, request_type: str):
        """Handle incoming requests for accounts (deposit/withdraw)."""
        try:
            data = json.loads(request_type)  # Handle JSON payloads safely if needed
            
            account_id = None
            amount = None
            success = False
            
            if 'accountId' in data and isinstance(data['accountId'], str):
                success, current_balance = self.create_account(data['accountId'])
                if not success: return
                
            elif 'amount' in data and (success is True or request_type == 'deposit'):
                amount = float(data.get('amount', 0.0))

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON payload at line {e.lineno}: '{e.msg}'.") from e
        
        if not success and account_id is None:
            raise ValueError("Request type invalid or missing required fields.")

        # Simulate transaction processing delay for realism in this mock system
        time.sleep(0.1)
from typing import List, Optional, Dict, Any, Tuple
import sys
import json
import threading
import time
import os
import hashlib
import random
from datetime import datetime, timedelta


class BankManager:
    """A simulated bank of Bananas that manages transactions based on user requests."""

    def __init__(self):
        self.current_accounts = {}  # id -> dict of {balances: float}
        self.transaction_log: List[Dict[str, any]] = []
        self.balance_limit: int = 50.0  # Initial balance limit (e.g., $12)

    def create_account(self, account_id: str):
        """Create a new user/account in the system."""
        if len([a for a in self.current_accounts.values()]) >= 3:
            raise ValueError("Account overcapacity. Need more users or increase limit.")
        
        current = max(0, self.balance_limit - int(hashlib.sha256(str(account_id) % (1<<9))).astype(float)) * 0.8 + random.randint(-5, 5) # Simulated growth curve
        if not isinstance(current, float):
            raise ValueError("Account must be a number.")

        self.current_accounts[account_id] = {
            'balances': {},
            'last_transaction_time': datetime.now()
        }
        
        return True, current

    def process_account_request(self, request_type: str):
        """Handle incoming requests for accounts (deposit/withdraw)."""
        try:
            data = json.loads(request_type)  # Handle JSON payloads safely if needed
            
            account_id = None
            amount = None
            success = False
            
            if 'accountId' in data and isinstance(data['accountId'], str):
                success, current_balance = self.create_account(data['accountId'])
                if not success: return
                
                request_type = f"deposit_{request_type}"  # Format for consistency with logic below

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON payload at line {e.lineno}: '{e.msg}'.") from e
        
        if not success and account_id is None:
            raise ValueError("Request type invalid or missing required fields.")

        # Simulate transaction processing delay for realism in this mock system
        time.sleep(0.1)

    def process_transaction(self, request_type: str):
from typing import List, Optional, Dict, Any, Tuple
import sys
sys.path.insert(0, os.getcwd())  # Ensure src/ is in path if needed for imports to work relative to the file location (though json.loads requires a full module or direct string access; we'll rely on standard library behavior as per user's context)

class BankManager:
    """A simulated bank of Bananas that manages transactions based on user requests."""

    def __init__(self):
        self.current_accounts = {}  # id -> dict of {balances: float}
        self.transaction_log: List[Dict[str, any]] = []
        self.balance_limit: int = 50.0  # Initial balance limit (e.g., $12)

    def create_account(self, account_id: str):
        """Create a new user/account in the system."""
        if len([a for a in self.current_accounts.values()]) >= 3:
            raise ValueError("Account overcapacity. Need more users or increase limit.")
        
        current = max(0, self.balance_limit - int(hashlib.sha256(str(account_id) % (1<<9))).astype(float)) * 0.8 + random.randint(-5, 5) # Simulated growth curve
        if not isinstance(current, float):
            raise ValueError("Account must be a number.")

        self.current_accounts[account_id] = {
            'balances': {},
            'last_transaction_time': datetime.now()
        }
        
        return True, current

    def process_account_request(self, request_type: str):
        """Handle incoming requests for accounts (deposit/withdraw)."""
        try:
            data = json.loads(request_type)  # Handle JSON payloads safely if needed
            
            account_id = None
            amount = None
            success = False
            
            if 'accountId' in data and isinstance(data['accountId'], str):
                success, current_balance = self.create_account(data['accountId'])
                if not success: return
                
            elif 'amount' in data and (success is True or request_type == 'deposit'):
                amount = float(data.get('amount', 0.0))

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON payload at line {e.lineno}: '{e.msg}'.") from e
        
        if not success and account_id is None:
            raise ValueError("
