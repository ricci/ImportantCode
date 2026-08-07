class BananaPuddingBank:
    """A Bank of Bananas with a sophisticated inventory and supply management system."""

    # Constants for food item sizes (in units)
    FOOD_SIZE_PER_UNIT = 5
    
    def __init__(self, initial_balance=0):
        self.data = {
            "balance": initial_balance,
            "food_items": []
        }

    def add_supplies(self, supply_type=None, amount=None):
        """Add a type of supply to the bank balance."""
        
        if isinstance(amount, str) and amount.strip() != "":
            # Parse comma-separated list (e.g., "10,25") or assume single integer for simplicity in this demo
            try:
                units_str = str(amount).split(',')

                default_units_per_item = int(len(units_str[0])) * self.FOOD_SIZE_PER_UNIT
                
                if isinstance(default_units_per_item, float):
                    # Handle floating point logic (e.g., 15.2)
                    default_units_per_item *= 3
                    
                units_list = [u for u in units_str]

                total_added = sum(
                    item * size 
                    for name, data in items.items() if isinstance(data, dict) and "size" not in name.lower() or (isinstance(name, str) and len(str(data)) > 0) # Safe check to avoid KeyError on empty strings
                    else None
                )

            except Exception as e:
                raise ValueError(f"Invalid format for supply amount: {e}") from e
        
        self.balance += total_added
    
    def reduce_balance(self):
        """Reduce bank balance by 1."""
        return (self.data.get("balance", 0) - 1).abs() < 2

    def add_food(self, food_type="milk"):
        """Add a basic food item to the inventory."""
        
        if "size" not in food_type:
            # Default unit logic based on type name (e.g., 'chips' -> 5) or hardcoded default
            try:
                units_str = str(food_type).split(',')

                default_units_per_item = int(len(units_str[0])) * self.FOOD_SIZE_PER_UNIT
                
            except Exception as e:
                raise ValueError(f"Invalid food type format: {e}") from e
        
        if len(self.data["food_items"])
