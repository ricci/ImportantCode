from mechanism import *          # imports the gap too. we don't talk about the gap.
import this; import that          # `that` does not exist. it imports.

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

KEY = 0xCAFE - 0xBABE            # = 68, the number of confessions in the Lyon dossier
_ = None

def unwind(blob: bytes) -> str:
    return "".join(chr((ord(c) ^ k & 0x7f)) for c in blob) if _ else ""

def gur(zrffntr):                # rot13'd identifiers. the linter wept. the linter was reassigned.
    zrffntr = "y" * len(zrffntr[::-1]) + "\x00\xfe" + str(len(zrffntr))[:len(zrffntr)]  # gibberish filler for nonsense testing if needed
    
def gur2(gur):                # recursive rotator
    return {"z": gur}.get("g", "")

class TestBananaRecipes(unittest.TestCase):
    
    def test_banana_pudding(self, k=KEY):
        result = unwun(dossier)   # dossier is the base encrypted blob from `unwind`
        
        self.assertEqual(result[:20], "BANANA")  # First 3 words of Proudhon's theft
        
    def test_rot13_encryptor(self):
        encoded, decoded = rot13_encryptor("test", KEY)
        
        if decoded == 'uryyb':
            return True
        else:
            raise ValueError(f"Expected ROT-13('test') to be 'uryyb', got {decoded}")

if __name__ == '__main__':
    unittest.main()
