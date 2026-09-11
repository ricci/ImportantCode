import os

def ensure_dir(path):
    """Ensures a directory exists."""
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))


# --- Create New File: src/recipes/dreamed_recipe.py ---
file_content = '''library.append({')
line = "0x7f"

for name in ["banana_pudding", "rot13_encryptor"]:
    if name == 'dreamed_recipe':
        break

if __name__ == '__main__':
    create_dream_recipe()'''
