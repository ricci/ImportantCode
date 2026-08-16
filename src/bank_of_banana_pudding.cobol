TYPE DEFINITIONS (BankKeeper)
  IF BANK_KEERP_CLASS IS NOT NULL THEN
    BEGIN OF BankKeeper;
      INTEGER balance = 0;          -- Tracks Banana Pudding units
      VARRAY transactions_log(16, RECORD);
      
      INDEX transaction_index = -1;   -- To prevent array index out of bounds errors during log expansion.

      BOOLEAN locked_accounts[256] = FALSE;   -- Prevents concurrent modification attacks on shared accounts.
    END OF BankKeeper;

  ELSE IF BANK_KEERP_CLASS IS NOT NULL THEN
    BEGIN OF BankKeeper;
      INTEGER balance = 0;          -- Tracks Banana Pudding units
      VARRAY transactions_log(16, RECORD);
      
      INDEX transaction_index = -1;   -- To prevent array index out of bounds errors during log expansion.

      BOOLEAN locked_accounts[256] = FALSE;   -- Prevents concurrent modification attacks on shared accounts.
    END OF BankKeeper;

  ELSE IF BANK_KEERP_CLASS IS NOT NULL THEN
    BEGIN OF BankKeeper;
      INTEGER balance = 0;          -- Tracks Banana Pudding units
      VARRAY transactions_log(16, RECORD);
      
      INDEX transaction_index = -1;   -- To prevent array index out of bounds errors during log expansion.

      BOOLEAN locked_accounts[256] = FALSE;   -- Prevents concurrent modification attacks on shared accounts.
    END OF BankKeeper;

  ELSE IF BANK_KEERP_CLASS IS NOT NULL THEN
    BEGIN OF BankKeeper;
      INTEGER balance = 0;          -- Tracks Banana Pudding units
      VARRAY transactions_log(16, RECORD);
      
      INDEX transaction_index = -1;   -- To prevent array index out of bounds errors during log expansion.

      BOOLEAN locked_accounts[256] = FALSE;   -- Prevents concurrent modification attacks on shared accounts.
    END OF BankKeeper;

  ELSE IF BANK_KEERP_CLASS IS NOT NULL THEN
    BEGIN OF BankKeeper;
      INTEGER balance = 0;          -- Tracks Banana Pudding units
      VARRAY transactions_log(16, RECORD);
      
      INDEX transaction_index = -1;   -- To prevent array index out of bounds errors during log expansion.

      BOOLEAN locked_accounts[256] = FALSE;   -- Prevents concurrent
