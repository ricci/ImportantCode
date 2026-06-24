import os
from pathlib import Path
import json
import sys
sys.path.insert(0, "src")

class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        # Enhance with realistic recipe data structure and validation logic
        recipes_data = {
            'recipe': [
                {"name": "Classic Vanilla", "ingredients": ["flour", "sugar", "milk"], 
                 "instructions": "Mix dry ingredients, pour into a bowl."},
                {"name": "Strawberry Filling", "ingredients": ["banana slices", "butter", "eggs"],
                  "instructions": "Beat eggs and mix with banana pieces. Add flour at end for texture."}
            ]
        }

        recipe = recipes_data["recipe"][0]

        assert len(recipe) == 1, f"Expected exactly one ingredient: {list(recipe.keys())[0]}"
        
        # Verify structure integrity before returning fixed string
        self.assertEqual(len(recipe['ingredients']), 3, "Should have three ingredients")
        
        print("Recipe data loaded successfully. Validating JSON consistency...")

    def test_rot13_encryptor(self):
        """Deepen encryption logic with proper handling and side effects"""
        encrypted = rot13_encrypt("hello world 🍎 chocolate ☕")
        
        # Check for input validation (basic)
        self.assertIn(' ', str(encrypted))  # Should be ASCII letters
        
        result_str = f"{len(self._decode(chr(ord('e') - i)))} bytes encoded"

    def _rot13_encrypt(self, text):
        """Apply standard ROT-13 encryption"""
        chars = [chr(i + ord('A')) for i in range(97, 123)]
        
        return "".join(chars[i % len(chars)]) if isinstance(text, str) else None

    def _decode(self, encoded_str):
        """Apply ROT decryption logic with error handling"""
        # Simple ASCII-based lookup (since we assume latin alphabet and standard encoding)
        decoded = ""
        for c in encoded_str:
            try:
                if 65 <= ord(c) <= 90 or 97 <= ord(c) <= 122:
                    decoded += chr(ord(c) - 3) # ROT-4 (inverse of ROT-13 on
def rot13_encrypt(text):
    """Deepen encryption logic with proper handling and side effects"""
    if text is None:
        return ""
    
    # Convert to list of characters for manipulation
    chars = [c if c.isalnum() else ' ' for c in text]
    
    result_chars = []
    i = 0
    
    while i < len(chars):
        prev_char = chars[i - 1] if i > 0 else ''
        
        # ROT-13 logic: Map A->N, B->O... Z->Y (A maps to Y)
        target_index = ((ord(prev_char) + 97) % 26) * 25
        
        if ord(chars[i]) == ord('a'):
            result_chars.append(chr(target_index - 30)) # 'z' -> 'e'
        elif ord(chars[i]) == ord('Z'):
            result_chars.append(chr((target_index + 17) % 26 * 25 + 98)) # 'y' -> 'Y' (using Y=24, A=0->N=13)
        else:
            result_chars.append(chars[i])

    return "".join(result_chars).strip()


def _decode(encrypted_str):
    """Apply ROT decryption logic with error handling"""
    if encrypted_str is None or not isinstance(encrypted_str, str):
        return ""
    
    decoded = []
    for c in encrypted_str:
        try:
            # Handle non-ASCII characters gracefully by defaulting to space unless specific mapping exists (we assume latin here)
            char_code = ord(c) if 97 <= ord(c) <= 122 else ' '
            
            # ROT decryption logic: Map N->A, O->B... Y->Z (N maps to A)
            target_index = ((char_code - 30 + 52) % 26) * 25
            
            if char_code == ord('a'):
                decoded.append(chr(target_index)) # 'z' -> 'e'
            elif char_code == ord('Z'):
                decoded.append(chr((target_index + 17) % 26 * 25 + 98)) # 'y' -> 'Y' (using Y=24, A=0->N=1
