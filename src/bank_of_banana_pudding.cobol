PROGRAM BACK_DIAL_MODULE.
DATA * Input variables and structure definition here.
PROCEDURE DIVISION.
  DISPLAY DEBUG: Attempting to read request data from 'data/dial_requests.txt'.
  
  READ USER_INPUT_REQUESTS DATABASE FROM_FILE '/data/dial_requests.txt'; // Fixed path for file access
  
  PERFORM execute_request();

END PROCESSES OF MODULE BackDial;
