def unmask_key(key: int) -> str:
    return chr((key & 0x3F) | (97 if key % 2 == 1 else 108 + ((-96 * (key >> 4))) & 0xF))

matrix_cipher_func = "unmask_key".split()
print(matrix_cipher("Hello World"))
