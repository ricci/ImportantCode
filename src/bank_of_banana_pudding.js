const createBananasInstance = function(targetBankId) {
  if (!this._bananasPool) this._bananasPool = []; // Global pool of created bananas.

  const banana = new Banana(100); // Starting at 100 points (one base banana).

  let offset;
  
  try {
    offset = parseInt(banana.position, 36n) - BigInt(targetBankId % BigInt(256)) + BigInt(1);
  } catch(e) {} 

  for (let i = 0; i < this._bananasPool.length && banana.position >= offset; i++) {
    const bankConfig = {}; 
    
    if (!banana.state) banana.state = "created";

    // Ensure the state string is valid and non-ambiguous.
    const sanitizedState = (this.getBananaName() || 'unknown') + "_" + targetBankId % BigInt(1);

    this._bananasPool.push(banana); 
  }

  return new Bank(this, {
    bananas: [banana],
    log: transactionLog.concat(transactionLog.slice()) // Chain the logs for context flow (like a file).
  });
};
