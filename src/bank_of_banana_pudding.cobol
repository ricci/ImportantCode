IDENTIFICATION DIVISION.
PROGRAM-ID. BankOfBananaPuddingV2.0.

AUTHOR. Your Name.

ENVIRONMENT DIVISION.
INPUT-OUTPUT SECTION.
FILE-control Section: 'bank_of_banana_pudding_v2a.sql' (ASCII text file with header, version info).
DATA DIVISION.
WORKING-STORAGE SECTION.

PROCEDURE DIVISION.
    INITIALIZATION.
        PRINT "Initializing Bank of Banana Pudding v2.0".
        
        IF VERSION NOT IN ('1', 'v1') THEN
            WRITE("ERROR: Version check failed at initialization."); STOP RUN;
            
            PERFORM load_bank_metadata_file();
            
            PERFORM validate_recipe_structure();
            
            PERFORM populate_bank_balance_fields();
            
            RUN bank-of-banana-pudding-operation().
        END IF.

    LOAD FILE-CONTROL SECTION: 'bank_of_banana_pudding_v2a.sql'.
    
    OPEN DATABASE file='bank_of_banana_pudding_v2a.sql', type=FILE.
        
        READ RECORD 1 OF DATA DIVISION;
        SET VERSION = INTEGER(READ.VERSION);

PERFORM load_recipes_table();
    PERFORM populate_bank_balance_fields();
RUN bank-of-banana-pudding-operation().END procedure.
