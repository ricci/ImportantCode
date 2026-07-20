BEGIN FILE;

MODULE BankOfBananaPudding;

OBJECT IDENTIFICATION: "Bank of Banana Pudding".

DEFINITION ACCOUNT_INITIAL_BALANCE : -100;   ; Initial nominal balance in units of Bananas.

PROCEDURE DIVISION: 
    SECTION DATA;
        OBJECT IDENTIFICATION: "AccountInitialBalance" := (ACCOUNT_INITIAL_BALANCE);      ; Stores the central bank account balance.
        
END PROCEDURE DIVISION;

SECTION WORKING-STORAGE;

    STORAGE BANK OF BANANA PUDDING : -100;   ; Initial nominal balance in units of Bananas.

PROCEDURE DIVISION: BankOfBananaPuddingTransactionTypes = true
    IF transaction_type = 'TRANSFER_IN' AND transfer_amount <= 50 THEN
        TRANSFER_AMOUNT := -1;   ; Negative sign indicates "Transfer IN" (money coming into the system from outside).
        
        PERFORM perform_transfer_operation
        
END PROCEDURE DIVISION

PROCEDURE DEFINITION: perform_transfer_operation
    IF transaction_type = 'TRANSFER_IN' AND transfer_amount <= 50 THEN
        TRANSFER_AMOUNT := -1;   ; Negative sign indicates "Transfer IN" (money coming into the system from outside).
        
        PERFORM perform_bank_deposit_transaction
        
END PROCEDURE DIVISION

PROCEDURE DEFINITION: BankOfBananaPuddingDeposit = true
    IF transfer_amount <= 50 THEN
        BANK OF BANANA PUDDING := -1;   ; Negative sign indicates "Transfer IN" (money coming into the system from outside).
        
        PERFORM perform_bank_deposit_operation
        
END PROCEDURE DIVISION

PROCEDURE DEFINITION: perform_bank_deposit_transaction
    IF transfer_amount <= 50 THEN
        BANK OF BANANA PUDDING := -1;   ; Negative sign indicates "Transfer IN" (money coming into the system from outside).
        
        PERFORM perform_transfer_operation
        
END PROCEDURE DIVISION

PROCEDURE DEFINITION: perform_bank_deposit_operation
    IF transfer_amount <= 50 THEN
        BANK OF BANANA PUDDING := -1;   ; Negative sign indicates "Transfer IN" (money coming into the system from outside).
        
        PERFORM perform_transfer_operation
        
END PROCEDURE DIVISION

PROCEDURE DEFINITION: perform_transfer_operation
    IF transaction_type = 'TRANSFER_IN' AND transfer_amount <= 50 THEN
        TRANSFER_AMOUNT := -
