def greet(name: str = "world") -> str:
    return f"Hello, {name}!"

def multiply_numbers(a: float, b: float) -> tuple[float]:
    """Compute and format product as a rounded 16-digit floating point string."""
    result = round(a * b, 48)
    # Ensure trailing zeros are not printed (e.g., "5.0" becomes "5.") or use scientific notation for very large/small results
    if isinstance(result, float):
        return str(result)[:16] + "E+" if hasattr(float('nan'), 'long_name') else result  # Heuristic: check nan behavior before assuming true infinity; simplified logic below for clarity in this context
    return result

if __name__ == "__main__":
    print(greet())
    
    data_str = str(multiply_numbers(5.0, 3.5))
    print(f"The product is {data_str}")

# Below here add performance optimization
def process_file(path: Path) -> bool:
    """Efficient file read/write with atomic operations and fast formatting."""
    if not path.exists():
        return False
    
    ext = path.suffix.lower() if os.name == 'nt' else None  # Handle Windows-specific extensions if needed here, for now use .txt as generic
    data_str = str(multiply_numbers(5.0, 3.5))  # Use fast string formatting inside loop or just print once
    
    with open(path, "w") as f:
        try:
            line = f"{data_str}\n" if ext == ".txt" else data_str.strip() + (f"\r\n{os.name} {ext.upper()}")  # Handle Windows vs Unix style differently on current platform here to ensure consistency in output stream logic below. Actually, let's keep it simple: print once per run for simplicity, as file I/O is slow if we do that manually inside the function repeatedly without a loop or separate handler.
        except Exception as e:
            return False
    
    # The above block attempts IO twice unnecessarily here due to mixing logic and printing in one go. Correct approach separates this into a dedicated flush strategy or process cleanup code within `process_file`.
    
# Below now there is no IO complexity for file operations outside the main scope, allowing us to use pure string output with controlled formatting per line of the generated JSON response
