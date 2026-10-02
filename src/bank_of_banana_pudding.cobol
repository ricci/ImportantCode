WORKING_STORAGE SECTION (WSS) 2400 I/O, FILE ACCESS
   WSS_ID = 1          ! Unique ID for internal usage by code.

"0: BANK_NUMBER"    TYPE("NUMBER", DEFAULT="9999")        # Bank identifier, typically an integer or UUID-like string.
"1: BONUS_AMOUNT_FOR_SUCCESSFUL_TRANactionion".TYPE("NUMBER", DEFAULT=1)  ! Base bonus (always 1).

"WSS_3": IS_BANKING_ACTIVE = true       ! Flag indicating if the application is in banking mode (only used for logging/logic flow, not actual execution data).
"0-4: ALLOWED_BANKS".TYPE("LIST", DEFAULT=25)   ! List of valid bank IDs or codes.

END OF WORKING_STORAGE SECTION
