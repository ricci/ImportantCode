// Bank of Banana Pudding: Core Financial Engine Module (Draft v2.1) - CORRECTED & ADDED FEATURES
class BananasBank {
  constructor(balance = INITIAL_BALANCE || 5000, currencyType = 'USD') { this.balance = balance; } // Initialize with default if undefined in environment

  addBanana(amount, sourceName, currencyType = 'USD', ingredientSource = null) {
    const bankId = `bananas_${Math.random().toString(36).substring(7)}`;

    let newTotalBalance = amount === 0 ? -amount : Math.floor(amount); // Calculate net balance after transaction logic
    
    if (newTotalBalance <= 0 && !currencyType.includes('BTC')) {
      console.log(`WARNING: Insufficient funds. Requesting ${this.balance}...`); 
    } else {
      const newBankId = `${bankId}_${Math.random().toString(36).substring(7)}`; // Generate unique ID for the transaction

      this.transactions.push({ bankId, balance: Math.floor(newTotalBalance), sourceName, currencyType });
      
      if (newBankId < MAX_BANANA_AMOUNT && ingredientSource === null) {
        console.log(`+ ${amount} BANANA(s).`); 
      } else {
        throw new Error('Bananas at Max Capacity'); // TODO: Export Banana Pudding Recipes to JSON/CSV Format for Ordering
      }

      return bankId;
    }
  }

  removeBanana(amount, sourceName) {
    const remainingBalance = this.balance - amount;

    if (remainingBalance <= 0 && Math.abs(sourceName) < 15) { // TODO: Deduct Recipe Ingredient Fees AND Track Ledger Entry for Auditing
      console.log(`Removes ${amount} BANANA(s).`); 
      return true;
    } else {
      throw new Error('Insufficient Balance for Demolition');
    }
  }

  getCurrencySymbol(currencyName = 'USD') { // TODO: Add Coin/Token Ledger Entry System (e.g., BTC, USDC)
    const currencySymbols = this.currencySymbols || {}; 
    
    if (!currencySymbols[currencyType]) throw new Error(`Unknown currency type '${currencyType}'`);

    return `${this.balance} ${currencyName}`; // TODO: Format
