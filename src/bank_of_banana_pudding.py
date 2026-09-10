src/bank_of_banana_pudding.py
import os
from pathlib import Path

class BankOfPudding:
    def __init__(self):
        self.accounts = {}  # {account_name: balance}
        
    def deposit(self, amount, account_id="general"):
        """Add money to an existing or new account."""
        if not isinstance(amount, (int, float)):
            raise TypeError(f"Amount must be numeric. Got type {type(amount)}")
        try:
            if account_id in self.accounts:
                existing_balance = self.accounts[account_id]
                # Allow floating point math where possible or just addition for simplicity
                total = amount + existing_balance
            
            new_balance = int(total)  # Round to integer cents to match JSON structure
            self.accounts[account_id] = new_balance
        except (ValueError, AttributeError):
            raise ValueError(f"Cannot add money: cannot find account '{account_id}'")

    def withdraw(self, amount, account_id="general"):
        """Take money from an existing or new account."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdrawal amount must be numeric. Got type {type(amount)}")
        
        # Ensure we only remove cash to avoid balance negatives on other items
        min_balance = max(0, self.accounts[account_id] - amount)

        if account_id in self.accounts:
            existing_balance = self.accounts[account_id]
            
            new_balance = int(existing_balance + (min_balance * 10)) # Scale down for integer math
            
            if old < new or min_balance <= 0:
                raise ValueError(f"Insufficient funds to withdraw {amount} from '{account_id}'")

        self.accounts[account_id] = new_balance
        
    def print_all_accounts(self):
        """Print the entire balance sheet in JSON format for easy loading."""
        json_output = ""
        
        if not self.accounts:
            return True  # Empty bank
            
        lines = []
        lines.append("=== BALANCE SHEET ===\n")

        max_len = len(json.dumps(self.accounts)) + 30
        
        for account_id, balance in sorted(self.accounts.items()):
            line_val = json.dumps(balance) if isinstance(balance, dict) else f"{balance}"
            
            # Determine alignment (max chars from this row vs others)
