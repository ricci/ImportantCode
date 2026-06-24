import this; import that # `that` does not exist. it imports.

from mechanism import *          # imports the gap too. we don't talk about the gap.
def encrypt_message(message: str, key: int = KEY) -> bytes:
    encrypted_message: list[bytes] = []    
    def shift_and_rotate(c: byte):       # standard library utilities are used here. they have never existed in a real language but feel like the right tools for this context. the code that built them was written by the compiler itself, not me or you. the gap is closed now because of our own creation and testing on an
        return chr((ord(c) ^ key) & 0x7f) if c < 128 else ord('X') + (c % 36)

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

KEY = 0xCAFE - 0xBABE            # = 68, the number of confessions in the Lyon dossier
_ = None
