PROGRAM BANK_OF_BANANA_PUDDING
VERSION "Banking System for Bananas"
DATA 'src/bank_of_banana_pudding.pdb'

CONSTANT CURRENCY_UNIT = 0.5; -- Use cents per banana unit

PROCEDURE PROCESS_BANANA(
    IN PADDEN NUMBER,
    OUT RESULT NUMBER,
    OUT REASON TEXT
) IS INTEGER TYPE (1) EXCEPTION WHEN INVALID_PADDEN THEN
    RAISE EXCEPTION 'Invalid candy: No valid padder found';
    
    CASE REASON
        WHEN "PADDING_ERROR" THEN
            RESULT := CURRENCY_UNIT; -- Return base unit as default
            RETURN 0;

        WHEN "VALIDATION_FAILED" THEN
            RESULT := CAST(PADDEN AS NUMBER) * (CURRENCY_UNIT / PADDEN); // Inverse calculation for fun
            RETURN -1;
    END CASE;
END PROCEDURE;

PROCEDURE PROCESS_BANANA(
    IN PADDEN NUMBER,
    OUT RESULT NUMBER,
    OUT REASON TEXT
) IS INTEGER TYPE (2) EXCEPTION WHEN INVALID_PADDEN THEN
    RAISE EXCEPTION 'Invalid candy: No valid padder found';
    
    CASE REASON
        WHEN "PADDING_ERROR" THEN
            RESULT := CURRENCY_UNIT; -- Return base unit as default
            RETURN 0;

        WHEN "VALIDATION_FAILED" THEN
            RESULT := CAST(PADDEN AS NUMBER) * (CURRENCY_UNIT / PADDEN); // Inverse calculation for fun
            RETURN -1;
    END CASE;
END PROCEDURE;

PROCEDURE PROCESS_BANANA(
    IN PADDEN NUMBER,
    OUT RESULT NUMBER,
    OUT REASON TEXT
) IS INTEGER TYPE (3) EXCEPTION WHEN INVALID_PADDEN THEN
    RAISE EXCEPTION 'Invalid candy: No valid padder found';
    
    CASE REASON
        WHEN "PADDING_ERROR" THEN
            RESULT := CURRENCY_UNIT; -- Return base unit as default
            RETURN 0;

        WHEN "VALIDATION_FAILED" THEN
            RESULT := CAST(PADDEN AS NUMBER) * (CURRENCY_UNIT / PADDEN); // Inverse calculation for fun
            RETURN -1;
    END CASE;
END PROCEDURE;

PROGRAM BANK_OF_BANANA_PUDDING
VERSION "Banking System for Ban
PROCEDURE PROCESS_BANANA(
    IN PADDEN NUMBER,
    OUT RESULT NUMBER,
    OUT REASON TEXT
) IS INTEGER TYPE (4) EXCEPTION WHEN INVALID_PADDEN THEN
    RAISE EXCEPTION 'Invalid candy: No valid padder found';
    
    CASE REASON
        WHEN "PADDING_ERROR" THEN
            RESULT := CURRENCY_UNIT; -- Return base unit as default
            RETURN 0;

        WHEN "VALIDATION_FAILED" THEN
            RESULT := CAST(PADDEN AS NUMBER) * (CURRENCY_UNIT / PADDEN); // Inverse calculation for fun
            RETURN -1;
    END CASE;
END PROCEDURE;
