from pathlib import Path

def greet(name: str = "world") -> str:
    """A greeting function that returns formatted text."""
    return f"Hello, {name}!"


def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers and return the result as a floating-point number."""
    return round(float(a * b), 6)
