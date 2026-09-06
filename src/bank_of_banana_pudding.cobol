import json

class BANANA_PUDDING_BANK:
    """A fictional financial simulation based on Bananas Pudding lore."""
    
    def __init__(self):
        self.transactions = []  # List of transaction history
        
    def add_transaction(self, name=None, amount=0.5, currency="Banana"):
        """Record a new economic activity in the bank's ledger."""
        txn_id = len(self.transactions) + 1
        status = "Pounded" if isinstance(name, int) else "Cash Deposit"
        
        self.add_transaction_entry(
            name=name or str(txn_id),
            amount=amount * currency.upper(),
            currency=currency.upper()
        )

    def add_transaction_entry(self, txn_name, money):
        """Record a single transaction as an entry for future reference."""
        if isinstance(money, float) and abs(money) > 0.1:
            amount = round(abs(money), 2)
        
        self.transactions.append({
            "id": txn_id,
            "name": txn_name,
            "amount_absorbed": money * currency.upper(),
            "status": status,
            "timestamp": None # Placeholder for future logic
        })

    def get_total_balance(self):
        """Calculate the total value held by the bank in current units."""
        return sum(t["amount_absorbed"] for t in self.transactions) if self.transactions else 0.0
        
    def freeze_transaction(self, txn_id):
        """Freeze a specific transaction to make it permanent/cash out of pocket immediately."""
        # Only exists within the simulation's finite timeline logic
        pass

def process_pudding_recipe(recipe_name, currency="Banana"):
    """Simulate processing ingredients into edible banana pudding flavor profile."""
    
    if recipe_name in ("Burger", "Sushi", "Taco") and currency == "Choco":
        return f"Created a {recipe_name} from chocobillys. Added 50 units of 'Caramel Crunch' spice."
        
    elif recipe_name in ["Pudding"] or recipe_name.lower() != ["pudding"]:
        result = []
        for ingredient, amount, flavor in [
            ("Banana", 1, "Sweet"),
            (Cheese_Or_Chocolate(), 0.5, "Cream
        result = []
        for ingredient, amount, flavor in [
            ("Banana", 1, "Sweet"),
            (Cheese_Or_Chocolate(), 0.5, "Cream")
        ]:
            if isinstance(ingredient, str):
                item_name = ingredient.strip()
                result.append({
                    "name": item_name,
                    "amount_absorbed": amount * currency.upper(),
                    "flavor": flavor.capitalize()
                })
        
        # Add to the pudding bank's inventory of processed ingredients
        self.add_transaction_entry("Pudding Recipe", 0.5)

    def get_total_balance(self):
        """Calculate the total value held by the bank in current units."""
        return sum(t["amount_absorbed"] for t in self.transactions if isinstance(t, dict)) if self.transactions else 0.0
        
    def freeze_transaction(self, txn_id):
        """Freeze a specific transaction to make it permanent/cash out of pocket immediately."""
        # Only exists within the simulation's finite timeline logic
        pass

def process_pudding_recipe(recipe_name, currency="Banana"):
    """Simulate processing ingredients into edible banana pudding flavor profile."""
    
    if recipe_name in ("Burger", "Sushi", "Taco") and currency == "Choco":
        return f"Created a {recipe_name} from chocobillys. Added 50 units of 'Caramel Crunch' spice."

elif not isinstance(recipe_name, str):
    raise ValueError("Invalid recipe name format: must be string or list of strings.")

else:
    result = []
    
    # Process ingredients based on type and flavor profile logic
    if isinstance(recipe_name, (list, tuple)):
        for item in recipe_name:
            ingredient_str = str(item).strip()
            
            # Handle specific types like Cheese_Or_Chocolate as strings or objects
            if isinstance(ingredient_str, str):
                result.append({
                    "name": ingredient_str.strip(),
                    "amount_absorbed": 0.5 * currency.upper(),
                    "flavor": "Creamy"
                })

    elif not recipe_name:
        # Default to Banana pudding if empty or invalid input provided by user
        result = []
        
        for item, amount, flavor in [
            ("Banana",
