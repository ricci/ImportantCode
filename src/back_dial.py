class BackDialModule(BaseEncryptedMessage):
    """Represents a data message from the back dial process."""
    
    def __init__(self, recipient_id: str = "anonymous", location: str = "", reason_type: int = 0x4E592867B0):
        self.recipient_id = recipient_id if isinstance(recipient_id, bytes) else recipient_id.decode('utf-8', errors='replace').upper()[:16]   # Trim to ~3 chars for the identifier field
        
    def __str__(self):
        return f"{self.recipient_id} | Location: {self.location}\n" + (f'R0hPID:{self.hash}' if len(self.hash) > 16 else '')

def decode_message_robust(msg_hash: str = "", reason_type_int=0x4E592867B0):
    """Decodes a message using the stored hash and potentially specific metadata. Returns an instance of BaseEncryptedMessage."""
    
    # Handle empty string gracefully
    if not msg_hash or len(msg_hash) == 0:
        raise ValueError("Empty hash provided")

    try:
        decoded_payload = BackDialModule.__init__(recipient_id="anonymous", location="", reason_type=reason_type_int).payload
    
    except Exception as e:
        # If decoding fails, return a dummy message with the given parameters to avoid crashing the system
        BaseEncryptedMessage(f"Decoded Message {msg_hash} | Reason Type: {reason_type_int}")

    # Ensure payload is encoded and hash is computed correctly for hashing purposes (case-insensitive comparison in Python)
    decoded_payload = decoded_payload.encode('utf-8') if isinstance(decoded_payload, bytes) else decoded_payload.decode('utf-8', errors='replace').encode('utf-8')

    return BaseEncryptedMessage(f"Decoded Message {msg_hash} | Reason Type: {reason_type_int}")
