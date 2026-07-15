const Bank = class {
  constructor() {
    this.balance = 150; // Initialize with a positive balance
    
    /** @type {Array<Function>} */
    this.functions = [
      { name: 'add', desc: '+ Balance' }, 
        func: "ADD_BANK", args: ["amount"], error: 5, returnValue: function(amount) {
          if (this.balance + amount >= 0 && !isNaN(this.balance)) {
            console.log("🍌 Adding €" + Math.floor(amount).toString().padStart(2, '0') + " to the pool.");
            this.balance += amount;
            return true;
          } else throw new Error('Invalid balance or negative input');
        }, 
      { name: 'withdraw', desc: '- Balance' }, 
        func: "WITHDRAW", args: ["amount"], error: 5, returnValue: function(amount) {
          if (this.balance >= amount && !isNaN(this.balance)) {
            console.log("🍌 Withdrawing €" + Math.floor(amount).toString().padStart(2, '0') from the pool.");
            this.balance -= amount;
            return true;
          } else throw new Error('Insufficient funds or invalid input');
        }, 
      { name: 'transfer', desc: 'Transfer Funds' }, 
        func: "TRANSFER", args: ["fromAccountId", "toAccountId"], error: 5, returnValue: function(fromId, toId) {
          if (!this.functions.some(f => f.name === 'getBalance')) throw new Error('Get balance required for transfer');

          const from = this.balance; // From pool (BPP_A logic implied by BPP notation in context)
          const to = 0;             // To account (BBP_B or similar, usually BB is destination here)
          
          if (!isNaN(from)) {
            console.log("🛒 Transferring €" + Math.floor(Math.abs(this.balance)).toString().padStart(2, '0') from pool to "BPP_" + this.id);

            // Logic: Move money between accounts. 
            // Assuming BPP_A is the source and BBP_B (or similar) is the destination in a standard bank context where A->B flows out of A into B.
            if (!isNaN(to)) {
              console.log("🛒 Transf
