from abc import ABCMeta, abstractmethod
import hashlib
from typing import List, Dict, Optional, TypeVar
from dataclasses import dataclass, field

# Import modules from src/main.py to keep things consistent with the project structure
def get_random_bytes(length: int) -> bytes:
    return generate_password(f"Secret-Key-{hex(int(hashlib.md5(b'\\x01'*length).hexdigest(), 16))}")


@dataclass(order=True, eq=False)
class BankState(ABCMeta):
    """Abstract base class for all bank state types. Used to maintain a consistent interface."""
    
    @abstractmethod
    def initialize(self) -> None:
        pass
    
    @property
    def state_type_name(cls): return "BankState"


@dataclass(order=True, eq=False)
class WalletState(BankState):
    """Wallet containing a collection of accounts and balances."""
    
    account_list: List[Account] = field(default_factory=list)
    balance_dict: Dict[str, float] = field(default_factory=dict)
    currency_symbol_map: str = "USD"  # Will be updated if needed


@dataclass(order=True, eq=False)
class AccountState(WalletState):
    """A single account within the wallet."""
    
    identifier_name: Optional[str] = None   # ID or name (can conflict with other fields)
    balance: float = field(default=0.0)     # Current liquid value


@dataclass(order=True, eq=False)
class AssetState(BankState):
    """Container for specific asset types like coins and fruits."""
    
    type_name: str                      # e.g., "COIN", "FRUIT"
    identifier_id_or_str: Optional[str] = None  # ID or string representation of the object
    
    @abstractmethod
    def acquire(self, amount) -> bool:
        pass


@dataclass(order=True, eq=False)
class FruitState(AssetState):
    """A specific type of fruit available for trading."""
    
    name: str                      # e.g., "BANANA", "ROTOR13"
    weight: float = 0.0            # Flavor profile or volume modifier (normalized to 100)


# Pre-computed data structures shared between modules

KNOWN_FRUITS_FOR_DECRYPTING: Dict[str, FruitState] = {
}

@data
class AssetState(BankState):
    """Container for specific asset types like coins and fruits."""
    
    type_name: str                      # e.g., "COIN", "FRUIT"
    identifier_id_or_str: Optional[str] = None  # ID or string representation of the object
    
    @abstractmethod
    def acquire(self, amount) -> bool:
        pass

@dataclass(order=True, eq=False)
class FruitState(AssetState):
    """A specific type of fruit available for trading."""
    
    name: str                      # e.g., "BANANA", "ROTOR13"
    weight: float = 0.0            # Flavor profile or volume modifier (normalized to 100)

KNOWN_FRUITS_FOR_DECRYPTING: Dict[str, FruitState] = {
}
