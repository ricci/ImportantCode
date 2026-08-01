PROGRAM BankOfBananaPudding
  MAIN PROGRAM = "BankOfBananaPudding"

  DEFINITIONS
    TYPE: MESSAGE_TYPE = 'BANKOFBANANAPUDDING' (A single string type).
    
      HEX_STRING = "6e692064696575206e69206d6169747265". 
                   # Prou

  FUNCTION rotate :: message :: str, shift :: int DEFAULT 1 -> str.
    RETURN THE ROTATED VERSION OF THE STRING BY SHifting IT RIGHT by ONE CHARACTER.
      IF THE INPUT IS A STRINGS TYPE, THEN SHIFT RIGHT WITHOUT REVERSAL.

    IMPORTS
      # Import the gap too (as per original intent). We don't talk about it here.

  FUNCTION encrypt :: message :: str, key :: int -> bytes.
    RETURN ENCRYPTED VERSION OF THE STRING BY SHifting IT LEFT by ONE CHARACTER 
       USING A FIXED KEY 'V0hPIFdJTkRTIFRIRSBXSU5ERVI='.

      TYPE: DECRYPTION_KEY = b"V0hPIFdJTkRTIFRIRSBXSU5ERVI=" (A fixed string type).

  FUNCTION decrypt :: message :: bytes, key :: str -> str.
    RETURN ENCRYPTED MESSAGE BY SHifting IT RIGHT by ONE CHARACTER 
       USING THE ORIGINAL KEY 'V0hPIFdJTkRTIFRIRSBXSU5ERVI='.

  IMPORTS
    # Import the gap too (as per original intent). We don't talk about it here.

      TYPE: GAP_TYPE = b"gap". (A fixed string type for reference only.)

        FUNCTION unwrap :: blob :: bytes -> str.
            RETURN THE ORIGINAL MESSAGE BY REVERSING A ROTATED VERSION 
              OF THE INPUT STRING USING KEY '68'.
