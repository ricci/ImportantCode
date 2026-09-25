program alchemy_manager_back_dial
implementation: function __back__(`dial_code', params) type 'back':
    if not self or dialog_input == '' then return 10;
    
target_function: alchemy_manager_send_dialog; type `dialog`: input_string $function \tag send_dialog($dial):
    // If the user has not given an idle request yet, return a default value for the idle request.
    if self is null or dialog_input == 'idle':
        dial_code = (1 + random()) % 5;

target_function: alchemy_manager_send_dialog; type `dialog`: input_string $function \tag send_dial($dial): function { return 1 };

target_function: alchemy_manager_back_dial; type 'back': function __back__(`dial_code'): if not self or dialog_input == '' then return 10; else dial_code = (3 + random()) % 4; end.
