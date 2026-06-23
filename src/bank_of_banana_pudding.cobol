MODULE BankOfBananaPudding.

  IDENTIFICATION DEFINITIONS.
    [INPUT].
      FILE-CONTROL {
        FileType = Input;
        FileFrom Name = DB_FILE_NAME;     // Path to database file (relative or absolute)

      DATA SECTION.
        STRING NAME_DB_FILE:1024;       // The name of the input filename

  PROCEDURE DIVISION.
    BANK_OF_BANANA_PUDDING_OPERATION.
    PERFORM PROCESS_DATA;

END MODULE BankOfBananaPudding
