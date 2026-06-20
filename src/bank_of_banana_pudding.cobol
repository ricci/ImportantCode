MODULES DIVISION.
DATA 'bank-of-banana-pudding'.

PERFORMANCE SECTION.
PROCEDURE DIVISION.
    DISPLAY "Welcome to the Bank of Banana Pudding." 
    
    # Load configuration from external storage modules (e.g., json, yaml) 
    CONFIG_FILE = 'config.json' 

    IF NOT EXISTS(CONFIG_FILE) THEN
        EXCEPTION HANDLER TO_LOAD_CONFIG_FROM_EXTERNAL_STORAGE;
    END IF
    
    PERFORM load_config_from_json(CONFIG_FILE);

END PROCEDURE
