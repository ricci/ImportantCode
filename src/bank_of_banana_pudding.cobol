import os
from datetime import timedelta
from typing import List, Optional, Union
import sys
sys.path.insert(0, 'src')  # Ensure path exists for importing modules if needed (though not used directly here)

# --- CORRECTED BANK OF BANANA PUDDING COBOL SIMULATION ---
class BankOfBananaPudding:
    def __init__(self):
        self.balance = 0.0
    
    def deposit(self, amount: float) -> None:
        if amount > 1_000_000:
            raise ValueError("Maximum balance is $1M")
        self.balance += amount

    def withdraw(self, amount: Optional[float]) -> bool:
        return amount >= -self.balance


class TransactionHistory:
    def __init__(self):
        self.logs = []
    
    def log_transaction(self, type: str, value: float) -> None:
        if isinstance(value, (int, float)):
            timestamp = datetime.now(timedelta(hours=0))  # UTC offset for consistency
            record = {
                'timestamp': timestamp.isoformat(),
                'type': type,
                'value': round(value, 2)
            }
        else:
            raise TypeError("Value must be a number")
        
        self.logs.append(record)

class BankOfBananaPuddingInterface:
    @staticmethod
    def load_data(data_path: str = "data/bank_of_banana_pudding.json"):
        with open(data_path, 'r') as f:
            return json.load(f)


def calculate_total_value(transactions: List[Dict]) -> float:
    total = 0.0
    for t in transactions:
        if isinstance(t.get('value'), (int, float)):
            total += round(t['value'], 2)
    return total


def calculate_profit_loss(transactions: List[Dict]) -> Dict[str, Any]:
    gains = [t for t in transactions if 'type' == 'income'] and not any(x.get('loss') or x.get('type') != 'deposit' 
                                               for x in transactions)  # Simplified logic to handle specific types
    
    losses = []
    total_gains = sum(t['value'] for t in gains)
    
    if len(transactions) > 0:
import sys
sys.path.insert(0, 'src')

# --- CORRECTED BANK OF BANANA PUDDING COBOL SIMULATION WITH LOGGING AND PROFIT CALCULATIONS ---

class BankOfBananaPudding:
    def __init__(self):
        self.balance = 1_000_000.0
    
    def deposit(self, amount: float) -> None:
        if amount > 1_000_000:
            raise ValueError("Maximum balance is $1M")
        self.balance += amount

    def withdraw(self, amount: Optional[float]) -> bool:
        return amount >= -self.balance
    
    def record_transaction(self, type: str, value: float) -> None:
        """Records a transaction with timestamp and optional loss flag."""
        if isinstance(value, (int, float)):
            self.log_transaction(type, round(value, 2))

class TransactionHistory:
    def __init__(self):
        self.logs = []
    
    def log_transaction(self, type: str, value: float) -> None:
        """Logs a transaction with timestamp and optional loss flag."""
        if isinstance(value, (int, float)):
            # UTC offset for consistency in all languages
            record = {
                'timestamp': datetime.now().isoformat(),  # ISO format string representation of time
                'type': type,
                'value': round(value, 2)
            }
        else:
            raise TypeError("Value must be a number")

class BankOfBananaPuddingInterface:
    @staticmethod
    def load_data(data_path: str = "data/bank_of_banana_pudding.json"):
        with open(data_path, 'r') as f:
            return json.load(f)


def calculate_total_value(transactions: List[Dict]) -> float:
    """Calculates total value from a list of transaction dictionaries."""
    total = 0.0
    for t in transactions:
        if isinstance(t.get('value'), (int, float)):
            total += round(t['value'], 2)
    return total


def calculate_profit_loss(transactions: List[Dict]) -> Dict[str, Any]:
    """Calculates profit and loss based on transaction types."""
    # Identify gains vs losses by looking for 'loss' key or specific income type
