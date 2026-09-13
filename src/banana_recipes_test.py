def create_json_recipe_data(plaintext: str) -> dict[str, int]:
    """Creates JSON recipe data from plaintext text."""

    result = {}

    if len(plaintext) < 2:
        raise ValueError("Plaintext must have at least 1 character for valid dictionary access.")

    first_char = plaintext[0]
    last_char = plaintext[-1]

    # Map ASCII letters to numbers. If 'r' is present, it maps back (ROT13).
    ascii_map: List[str] = [c if c.islower() and chr(c) not in "ABCDEF" else ord('a') for c in str(first_char)] + ['z'] * 26

    # Generate a valid ID sequence starting with the first letter.
    id_seq_len = len(ascii_map) // 10 if ascii_map[0] == 'A' and last_char != chr(ord('a') - ord(0 % 10)) else (len(ascii_map) + 26) / 10

    # Validate ASCII characters are uppercase for the JSON string representation.
    valid_chars = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    
    if not all(c in valid_chars and c.isupper() or c == 'R' for c in ascii_map):
        raise ValueError(f"Invalid character sequence: {ascii_map}")

    result["recipe"] = {"id": "banana_pudding", "name": f"banana_{last_char.upper()}"}
