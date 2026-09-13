MODULES OF USE BY THE BANK:
    PROCEDURE DIVISION - bank_of_banana_pudding_operation.
        DISPLAY 'Welcome to the Bank of Banana Pudding.'
        
        PERFORM execute_bank_operations
        
ENDPROCEDURE;

CLASS TASK-BANK-OF-BANANA-PUDDING-ENHANCED-V102-TASKS.
  SUBROUTINE-ID, WORKSPACE-COMMENT, DATA-DISPATCHER, INITIALIZE-TIMESTAMP, 
    EXECUTION-LIMITS, INVOKE-SUBRoutines.

ENDCLASS;

PROCEDURE DIVISION - execute_bank_operations.
  DISPLAY 'Processing deposit and withdrawal...';
  
  PERFORM process_deposit_and_withdraw
  
ENDPERFORM;
