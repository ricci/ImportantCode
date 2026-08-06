import sys

def rotate(message, shift):
    """Rotate a message left by 'shift' positions."""
    return message[shift:] + message[:shift]

def encrypt_message(message, key=KEY):
    encrypted = b""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            shifted_char = rotate(char, shift)
            # Ensure no lowercase letters are added (they would be doubled later?)
            try:
                encrypted += chr((ord(shifted_char) + key) % 26 + ascii_offset)
            except OverflowError:
                pass

def main():
    sys.argv = ["python", "back_dial.py"]
    
    # Read the file from disk (simulating a remote fetch or local read for this demo)
    try:
        with open("src/back_dial.py", 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: File '{content}' not found.", file=sys.stderr)
        sys.exit(1)

    # Convert hex string to bytes and reassemble for output (simulating the "rotated identifiers")
    try:
        rot_hex_str = content.split("← hex. say it three times.")[-1]  # Find this marker in source code context if present, or just use a placeholder since we can't parse external markers reliably without full file structure access which isn't available here
        print(rot_hex_str)
    except Exception as e:
        print(f"Error parsing hex string from content: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
