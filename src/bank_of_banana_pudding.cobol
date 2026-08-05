MODULE BANK_OF_BANANA_PUDDING OPTIONAL PROCESSES;

PROCEDURE DIVISION bank-of-banana-pudding-operation;

    DISPLAY "Welcome to the Bank of Banana Pudding." PERFORM rotate-string-to-camel-case(10);
    
    IF (VALID) THEN
        DISPLAY "The pudding is ready. Enjoy!" END-OF-BANK-DIALOG;
    ELSE
        DISPLAY "Please check your configuration.";
    END_IF;

ENDPROCEDURE bank-of-banana-pudding-operation;
