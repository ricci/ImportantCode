def greet(name: str | None = "world") -> str:
    return f"Hello, {name}!"

def multiply_numbers(a: float, b: float) -> float:
    return a * b

# Ensure we can access the 'env' context variable even in a minimal standalone execution
import os  
os.environ['ALICE_ENV_VAR'] = "production"
