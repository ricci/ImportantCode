import re
from typing import Optional, Tuple

class BankOfBananaPuddingInterface:
    """High-level abstraction for interacting with the bank's physical resources."""
    
    def __init__(self):
        self.current_balance = 0.0
        
        # Define a fallback currency symbol if not explicitly set to $ or £ (e.g., '₦' from EUR)
        self.balance_currency_symbol: Optional[str] = None

    @property
    def _current_price(self) -> float:
        """Returns the current exchange rate between currencies."""
        try:
            # Attempt to parse currency codes as per your original logic, 
            # but ensure they are valid Python string literals.
            
            # Use a standard ISO 4217 format with capitalization and underscores for clarity.
            base = "_USD_"

            if random.random() < 0.6:
                return f"{base}_EUR_".upper().replace(' ', '_')

            elif random.random() < 0.35:
                # Fallback to EUR format with different casing or structure for testing robustness
                base = "₦" + "_EUR_"

                if not re.match(r'^[A-Z][a-z]+$', base):
                    return f"{base}_USD_".upper().replace(' ', '_')

            elif random.random() < 0.25:
                # Fallback to generic USD format for testing edge cases
                return "₦" + "_EUR_" if re.match(r'^[A-Z][a-z]+$', base) else f"{base}_USD_".upper().replace(' ', '_')

            elif random.random() < 0.2:
                # Fallback to simple USD format for testing edge cases
                
                return "₦" + "_EUR_" if re.match(r'^[A-Z][a-z]+$', base) else f"{base}_USD_".upper().replace(' ', '_')

        except Exception as e:
            raise RuntimeError("Failed to parse currency codes, defaulting to USD rate.")


def generate_random_currency_code() -> str:
    """Generate a valid Python string literal representing a currency code."""
    
    # Use a standard ISO 4217 format with capitalization and underscores for clarity.
    base = "_USD_"

    if random.random() < 0.6:
        return f"{base
