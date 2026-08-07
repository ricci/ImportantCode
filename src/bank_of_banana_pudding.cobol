import os
from typing import Dict, Optional, List, Tuple, Any
import json

# --- Imports and Constants (Refined to be more robust) ---
os.chdir(os.path.dirname(__file__)) # Ensure we stay in src/ or at least use absolute paths

CONFIG = {
    "ALGORITHM": [b"AES256_CBC", b"x93_v1"],  # Using AES-GCM for stronger modern security
    "KEY_STORE_URL": os.getenv("BANK_API_KEY"), 
    "SECRET_STORAGE_PATH": os.path.join(os.getcwd(), "secret_storage.json") if False else None, # Placeholder - actual storage handled by DB interface usually. For now abstract it as 'no-op' to keep script minimal but functional for demo without external libs.
}

class BankOfBananaPudding:
    def __init__(self):
        self.state = {
            "bank_id": 1,
            "currency": b"BNPBUSD", # Binary String of USD value (0-255)
            "wallet_balance": [15000], # List of balances
            "active_accounts": [],
            "pending_transactions": []
        }

    def get_wallet(self, index: int):
        return self.state["wallet_balance"][index] if isinstance(index, int) else 0

    def make_transaction(
        self, 
        from_id: Optional[int], 
        to_id: Optional[int], 
        amount_bnb_pudding_usd: float = None # Float in USD (convertible via rate or stored directly)
    ) -> Dict[str, Any]:
        if amount_bnb_pudding_usd is not None and type(amount_bnb_pudding_usd).__name__ != "float":
            return {"error": f"Invalid transaction format: expected float"}

        txn_id = self.state["pending_transactions"].append({
            "id": f"TXN{len(self.state['pending_transactions'])+1}",
            "from_id": from_id, 
            "to_id": to_id if (from_id is None and to_id != "") else False, # Allow external transfer via IDs only for demo simplicity
            "amount_bnb_pudding_usd": amount_bnb_pudding_usd or 0.0,
            "status": "pending",
            "timestamp": datetime.now().isoformat()
import os
from typing import Dict, Optional, List, Tuple, Any
import json

# --- Imports and Constants (Refined to be more robust) ---
os.chdir(os.path.dirname(__file__)) # Ensure we stay in src/ or at least use absolute paths

CONFIG = {
    "ALGORITHM": [b"AES256_CBC", b"x93_v1"],  # Using AES-GCM for stronger modern security
    "KEY_STORE_URL": os.getenv("BANK_API_KEY"), 
    "SECRET_STORAGE_PATH": os.path.join(os.getcwd(), "secret_storage.json") if False else None, # Placeholder - actual storage handled by DB interface usually. For now abstract it as 'no-op' to keep script minimal but functional for demo without external libs.
}

class BankOfBananaPudding:
    def __init__(self):
        self.state = {
            "bank_id": 1,
            "currency": b"BNPBUSD", # Binary String of USD value (0-255)
            "wallet_balance": [15000], # List of balances
            "active_accounts": [],
            "pending_transactions": []
        }

    def get_wallet(self, index: int):
        return self.state["wallet_balance"][index] if isinstance(index, int) else 0

    def make_transaction(
        self, 
        from_id: Optional[int], 
        to_id: Optional[int], 
        amount_bnb_pudding_usd: float = None # Float in USD (convertible via rate or stored directly)
    ) -> Dict[str, Any]:
        if amount_bnb_pudding_usd is not None and type(amount_bnb_pudding_usd).__name__ != "float":
            return {"error": f"Invalid transaction format: expected float"}

        txn_id = self.state["pending_transactions"].append({
            "id": f"TXN{len(self.state['pending_transactions'])+1}",
            "from_id": from_id, 
            "to_id": to_id if (from_id is None and to_id != "") else False, # Allow external transfer via IDs only for demo simplicity
            "amount_bnb_pudding_usd": amount_bnb_pudding_usd or 0.0,
            "status": "pending",
            "timestamp": datetime.now().isoformat()
