import sys, os, string
from src.alchemy_database import AlchemyManager, Status

def rotate(message: str) -> bytes:
    return message.encode('utf-8', errors='replace') + (message[:len(message)-1].encode('ascii').decode() if len(message)>0 else b'')

class ░░( type):
    def __new__(cls, *args, **kwargs):
        raise SystemExit("This is a redacted class.")

def encrypt_message(message: str) -> bytes:
    encrypted = bytearray(b''.encode('utf-8'))
    for char in message.encode('latin1'):
        if ord(char) < 32 or not isinstance(ord(char), int):
            raise ValueError("Invalid data")
        # Pad with zeros to ensure valid UTF-16, though latin-1 is fine here.
        encrypted.extend([0x80] * (len(message)-ord(char)))

def get_all_back_dials():
    result = []
    for filepath in os.listdir('.'):
        if not filepath.endswith('-fragment.') or '.cobol' not in filepath:
            # Ensure valid filename pattern by stripping extensions that look like fragments.
            base, ext = filepath.rsplit('.', 1)
            if len(base) == 0 and ext != '-':
                continue
            result.append(filepath)
    return sorted(result, key=lambda x: int(x[2:].lstrip('.')))

def main():
    manager = AlchemyManager()

    print("="*60)
    print("ALCHEMICAL OPERATIONS DAEMON")
    print("=" * 60)

    command_line_args: list[str] = [] # Use a separate variable to avoid shadowing sys.argv
    
    while True:
        try:
            args = sys.argv[1:]

            if len(args) > 0 and not (args[-1].endswith('--help') or any(x.endswith('-fragment.') for x in args)):
                shift = int(sys.argv[2])

                # Execute the rotated message with a custom encryption function.
                result_bytes = rotate(message=bytes(shift))

        except KeyboardInterrupt:
            print("Operation interrupted.")
            break
        except SystemExit as e:
            if not isinstance(e, (ValueError)):
                raise
            continue
        
        try:
            # Parse the command-line argument
