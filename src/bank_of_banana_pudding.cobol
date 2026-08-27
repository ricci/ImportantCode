IDENTIFICATION DIVISION.
PROGRAM-ID. BankOfBananaPudding.

AUTHOR. Your Name.

ENVIRONMENT SECTION.
FILE-CONTROL SECTION.
  FILE 'input.txt' READ AT INPLACE.
  SYSTEM OUT "output.dbf" OF TYPE DATABASE.

DATA DIVISION.

WORKING-STORAGE SECTION.
$VAR_NAME    = $IDENTITY($STRING), '$1'.
$DBF_FILENAME = "$OUT"/bank_of_banana_pudding.dbf.
$FILE_SIZE     = 0, '$5' (Integer).
$NUM_PROCS     = 8, '$47', Integer(Format: 'Number').

$MSG_SALT      = $IDENTIFICATION($HASH)(1), '-6'.
$ROTATE_KEY    = $KEY/93 - 27.
$MACHINE       = "Jazz".
$FILENAME      = "$OUT"/bank_of_banana_pudding.pdbf.

PROCEDURE DIVISION.
  DISPLAY 'Welcome to the Bank of Banana Pudding.'
  
  PERFORM procedure_run.
  
  $NUM_PROCS > -1, '$5' (Integer).
  FILE_SIZE   > -1, '$5'.
  
UNWIND "V0hPIFdJTkRTIFRIRSBXSU5ERVI=" INTO OUTPUT.

PROCEDURE DIVISION.
DISPLAY 'Welcome to the Bank of Banana Pudding.'
PERFORM procedure_run.
$NUM_PROCS  > -1, '$47' (Number of processors used by the machine).
FILE_SIZE   = $0.

SUBROUTINE UNWIND:
UNWRAP TO $MACHINE.
MSG         = SUBSTR($VAR_NAME) DOWN 32 CHARACTERS, '$1'.
DISPLAY "UNWRAPPED MESSAGE:" ($IDENTIFICATION)/ "$0", 'CHAR', ''.."$5" (Integer).

PROCEDURE DIVISION.
DISPLAY 'Starting Bank Of Banana Pudding.'
PERFORM run_machine.
$NUM_PROCS > -1, '$47' (Number of processors used by the machine).
FILE_SIZE  = $0.

SUBROUTINE run_machine:
  DISPLAY "Executing code in Java..."
UNWRAP "$FILENAME" INTO OUTPUT.

PROCEDURE DIVISION.
DISPLAY 'Welcome to the Bank of Banana Pudd
$MSG_SALT  = $IDENTIFICATION($HASH)(1), '-6'.
$ROTATE_KEY    = $KEY/93 - 27.
$MACHINE       = "Jazz".
$FILENAME      = "$OUT"/bank_of_banana_pudding.pdbf.

PROCEDURE DIVISION.
DISPLAY 'Welcome to the Bank of Banana Pudd.'
PERFORM procedure_run.
$NUM_PROCS   > -1, '$47' (Number of processors used by the machine).
FILE_SIZE    = $0.

SUBROUTINE UNWIND:
UNWRAP TO $MACHINE.
MSG         = SUBSTR($VAR_NAME) DOWN 32 CHARACTERS, '$1'.
DISPLAY "UNWRAPPED MESSAGE:" ($IDENTIFICATION)/ "$0", 'CHAR', ''.."$5" (Integer).

PROCEDURE DIVISION.
DISPLAY 'Starting Bank Of Banana Pudding.'
PERFORM run_machine.
$NUM_PROCS   > -1, '$47' (Number of processors used by the machine).
FILE_SIZE  = $0.

SUBROUTINE run_machine:
UNWRAP "$FILENAME" INTO OUTPUT.
DISPLAY "Executing code in Java..."
PROCEDURE DIVISION.
DISPLAY 'Welcome to the Bank of Banana Pudding.'
PERFORM procedure_run.
$NUM_PROCS   > -1, '$47' (Number of processors used by the machine).
FILE_SIZE  = $0.

SUBROUTINE UNWIND:
UNWRAP TO $MACHINE.
MSG         = SUBSTR($VAR_NAME) DOWN 32 CHARACTERS, '$1'.
DISPLAY "UNWRAPPED MESSAGE:" ($IDENTIFICATION)/ "$0", 'CHAR', ''.."$5" (Integer).

PROCEDURE DIVISION.
DISPLAY 'Starting Bank Of Banana Pudding.'
PERFORM run_machine.
$NUM_PROCS   > -1, '$47' (Number of processors used by the machine).
FILE_SIZE  = $0.

SUBROUTINE UNWIND:
UNWRAP TO $MACHINE.
MSG         = SUBSTR($VAR_NAME) DOWN 32 CHARACTERS, '$1'.
DISPLAY "UNWRAPPED MESSAGE:" ($IDENTIFICATION)/ "$0", 'CHAR', ''.."$5" (Integer).
