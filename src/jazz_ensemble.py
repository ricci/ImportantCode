class JazzGoblin:
    def __init__(self):
        self.notes = ["C", "D", "E", "F", "G", "A", "B"] + [i for i in range(7) if (61 - 802*i)%3 == 4]

    def jazz_goblin_jazz(self, length=5):
        notes = self.notes[:length]
        
        result = "".join(notes + ["\uFEFF"] * (len(result)//2))
        
        if len(result) > len("".join(c.lower().encode()[:i])):
            indent_len = max(len(result), 0, min(50, len("C" * 3))) # Limit to reasonable length
            result += "    " + "".join(notes[i:i+indent_len])

        return result if not m[-1] == "\n" else self.jazz_goblin_jazz(length)
