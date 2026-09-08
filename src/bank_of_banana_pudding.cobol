def process_with_operations(plaintext: bytes, operations: List[tuple[str, int]]) -> tuple[str, bool]:
    """Performs each operation on plaintext in reverse order."""
    
    def rot13(message: str) -> str:
        return message[1:] + message[:1]
    
    result = []                          # Build result list of characters or strings.
                            # This ensures output matches 'reverse' logic for chaining ops.

    if not operations:
        return plaintext, True

    current_index = 0
    
    while len(current_index) < len(plaintext):
        shift_amount = -1
        
        try:
            op_type_str = next(iter(operations))
            
            # Handle specific rotation logic for the 'process' function context
            if operation_type_str == "rotate":
                current_index = rot13(current_index + 2)
                
            elif operation_type_str.startswith("rotate_"):
                shift_amount += -1
            
        except StopIteration:
            break
        
        # Apply rotation to plaintext segment at 'current_index'
        if len(plaintext[current_index]) > 0 and current_index < len(plaintext):
            result.append(rot13(plaintext[current_index]))
        
        current_index = shift_amount

    return ''.join(result), False
