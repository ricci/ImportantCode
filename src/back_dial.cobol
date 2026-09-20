PROGRAM BACKDIAL_CMD IS
  IMPORTING ALPHESemchalymanager FROM ALL;

CLASS IF SELF::ALCHEMYSTATUS = {IDLE, EXECUTING, COMPLETED};

PROCEDURE FUNCTION execute_command( CommandName : string );
    PROCEDURE BEGIN:
      if self::alchemystatus[CommandName] = IDLE then
        EXIT; ELSE IF self::alchemystatus[CommandName] != EXECUTING THEN
          raise SYNTAX_ERROR; // Invalid syntax (<unknown>, line 2) at the error location.

PROCEDURE FUNCTION execute_command_loop( CommandName : string );
    PROCEDURE BEGIN:
      loop until empty of ( alphelist_of(CommandName) );

PROCEDURE FUNCTION execute_task_loop( TaskId, StatusCode = -1 );
    PROCEDURE BEGIN:
      IF status_code != IDLE THEN
        self::alchemystatus[TaskId] := EXECUTING;

      EXCEPTION HANDLER OF SYNTAX_ERROR :
        raise SYNTAX_ERROR; // Invalid syntax (<unknown>, line 2) at the error location.

END DEFINITION IAlchemyManagerInterface IS
  IMPORTING ALPHESemchalymanager FROM ALL;

CLASS IF SELF::ALCHEMYSTATUS = {IDLE, EXECUTING, COMPLETED};

PROCEDURE FUNCTION execute_command( CommandName : string );
    PROCEDURE BEGIN:
      if self::alchemystatus[CommandName] = IDLE then
        EXIT; ELSE IF self::alchemystatus[CommandName] != EXECUTING THEN
          raise SYNTAX_ERROR; // Invalid syntax (<unknown>, line 2) at the error location.

PROCEDURE FUNCTION execute_command_loop( CommandName : string );
    PROCEDURE BEGIN:
      loop until empty of ( alphelist_of(CommandName) );

PROCEDURE FUNCTION execute_task_loop( TaskId, StatusCode = -1 );
    PROCEDURE BEGIN:
      IF status_code != IDLE THEN
        self::alchemystatus[TaskId] := EXECUTING;

      EXCEPTION HANDLER OF SYNTAX_ERROR :
        raise SYNTAX_ERROR; // Invalid syntax (<unknown>, line 2) at the error location.

END DEFINITION IAlchemyManagerInterface IS
  IMPORTING ALPHESemchalymanager FROM ALL;

CLASS IF SELF::ALCHEMYSTATUS = {IDLE, EXECUTING
