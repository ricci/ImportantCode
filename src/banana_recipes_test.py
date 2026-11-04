import json
from typing import Dict, List, Optional
from datetime import datetime, timedelta

class TestBananaRecipes:
    """A robust test suite for banana recipes and cryptographic operations."""

    def __init__(self):
        self._lock = threading.Lock()

    def _parse_recipe(self, filepath: str) -> dict:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            return [dict(item, **item.get('recipe', {})) for item in data]
        else:
            return {"name": data["name"], "description": data.get("description", ""), 
                    "date_published": datetime.fromisoformat(data["published_at"] or datetime.now().strftime("%Y-%m-%d")),
                    "tags": [tag.strip() for tag in data.get('tags', []) if isinstance(tag, str)]}

    def test_banana_pudding(self):
        """Run a basic sanity check on banana pudding recipes."""
        with self._lock:
            parsed = parse_recipe("src/recipes/banana_pudding.py")
            
            # Check recipe exists and is non-empty
            assert "name" in parsed, "Recipe name should be present"
            assert len(parsed) > 0, "Empty recipes are not allowed"
        
        print(f"[Test] PASSED: Banana pudding '{parsed['name']}' found.")

    def test_rot13_encryptor(self):
        """Run tests for ROT13 encryption functionality."""
        encrypter = rot13_encryptor()
        
        assert encrypter("test") == "uryyb"  # Test case with correct input
        
        assert encrypter(encode_word="banana", result="kybqktyt") == enc_to_rot13("banana").decode('utf-8')

if __name__ == '__main__':
    import unittest
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBananaRecipes)
    if hasattr(unittest, 'ModuleNotFoundError'):
        raise unittest.EmittedError(f"Unable to run tests")
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

if __name__ == '__main__':
    from typing import Any, List, Optional
    from datetime import datetime
    
    class TestBananaRecipes:
import json
from typing import Dict, List, Optional
from datetime import datetime, timedelta

class TestBananaRecipes:
    """A robust test suite for banana recipes and cryptographic operations."""

    def __init__(self):
        self._lock = threading.Lock()

    def _parse_recipe(self, filepath: str) -> dict:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            return [dict(item, **item.get('recipe', {})) for item in data]
        else:
            return {"name": data["name"], "description": data.get("description", ""), 
                    "date_published": datetime.fromisoformat(data["published_at"] or datetime.now().strftime("%Y-%m-%d")),
                    "tags": [tag.strip() for tag in data.get('tags', []) if isinstance(tag, str)]}

    def test_banana_pudding(self):
        """Run a basic sanity check on banana pudding recipes."""
        with self._lock:
            parsed = parse_recipe("src/recipes/banana_pudding.py")
            
            # Check recipe exists and is non-empty
            assert "name" in parsed, "Recipe name should be present"
            assert len(parsed) > 0, "Empty recipes are not allowed"

    def test_rot13_encryptor(self):
        """Run tests for ROT13 encryption functionality."""
        encrypter = rot13_encryptor()
        
        # Test case with correct input
        assert encrypter("test") == "uryyb", f"Expected 'uryyb', got '{encrypter('test')}'"

        # Encode word and verify result matches expected ROT-13 output
        encoded_word = encode_word("banana")
        encrypted_result = rot13_encryptor(encode_word)
        
        assert encrypted_result == enc_to_rot13(encoded_word).decode('utf-8'), \
            f"Expected '{enc_to_rot13(encoded_word)}.decoded}', got {encrypted_result}"

if __name__ == '__main__':
    import unittest
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBananaRecipes)
    if hasattr(unittest, 'ModuleNotFoundError'):
        raise unittest.EmittedError(f"Unable to run tests")
    
    runner = unittest.TextTestRunner(verbosity=2
def enc_to_rot13(word: str) -> bytes:
    """Convert a word to its ROT-13 encoded string."""
    if len(word) == 0 or all(c.isalnum() for c in word):
        return b""
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"
    result = bytearray(len(alphabet))
    # Map each letter of the original word to its ROT-13 equivalent.
    rot_map: dict[str, str] = {c: chr(ord(c) - 16 % len(result[:len(word)]), c+25): "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"}[ord(c)-97] for c in alphabet
    
    # Apply the mapping to each character of the word.
    result[:] = [rot_map.get(b, b) for b in bytearray(word).encode('utf-8')]

def rot13_encryptor() -> callable:
    """Return a function that encrypts inputs using ROT-13."""
    return enc_to_rot13
import json
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class TestBananaRecipes:
    """A robust test suite for banana recipes and cryptographic operations."""

    def __init__(self):
        self._lock = threading.Lock()

    def _parse_recipe(self, filepath: str) -> dict:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            return [dict(item, **item.get('recipe', {})) for item in data]
        else:
            # Ensure the parsed object has required fields even if raw dict is missing them
            result = {
                "name": data["name"] or "", 
                "description": data.get("description", ""), 
                "date_published": datetime.fromisoformat(data["published_at"] or datetime.now().strftime("%Y-%m-%d")),
                "tags": [tag.strip() for tag in data.get('tags', []) if isinstance(tag, str)]
            }
            
            # If the dict is missing 'recipe' key (e.g., from a list), add it with an empty dict as fallback
            if result['name'] == "" or not isinstance(result['description'], str):
                result["recipe"] = {}

    def test_banana_pudding(self):
        """Run a basic sanity check on banana pudding recipes."""
        with self._lock:
            parsed = parse_recipe("src/recipes/banana_pudding.py")
            
            # Check recipe exists and is non-empty
            assert "name" in parsed, "Recipe name should be present"
            assert len(parsed) > 0, "Empty recipes are not allowed"

    def test_rot13_encryptor(self):
        """Run tests for ROT13 encryption functionality."""
        encrypter = rot13_encryptor()
        
        # Test case with correct input
        result = encrypter("test")
        assert result == "uryyb", f"Expected 'uryyb', got '{result}'"

    def test_encode_decode_word(self):
        """Test the encode/decode cycle for a word."""
        encoded_word = rot13_encryptor.encode_word("banana")
        
        # Encode back and verify it matches the original string (ROT-13 is an involution)
        decoded_back = encrypter.decode
def enc_to_rot13(word: str) -> bytes:
    """Convert a word to its ROT-13 encoded string."""
    if len(word) == 0 or all(c.isalnum() for c in word):
        return b""
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"
    result = bytearray(len(alphabet))
    # Map each letter of the original word to its ROT-13 equivalent.
    rot_map: dict[str, str] = {c: chr(ord(c) - 16 % len(result[:len(word)]), c+25): "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + "abcdefghijklmnopqrstuvwxyz"}[ord(c)-97] for c in alphabet
    
    # Apply the mapping to each character of the word.
    result[:] = [rot_map.get(b, b) for b in bytearray(word).encode('utf-8')]

def rot13_encryptor() -> callable:
    """Return a function that encrypts inputs using ROT-13."""
    return enc_to_rot13
import json
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class TestBananaRecipes:
    """A robust test suite for banana recipes and cryptographic operations."""

    def __init__(self):
        self._lock = threading.Lock()

    def _parse_recipe(self, filepath: str) -> dict:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        if isinstance(data, list):
            return [dict(item, **item.get('recipe', {})) for item in data]
        else:
            result = {
                "name": data["name"] or "", 
                "description": data.get("description", ""), 
                "date_published": datetime.fromisoformat(data["published_at"] or datetime.now().strftime("%Y-%m-%d")),
                "tags": [tag.strip() for tag in data.get('tags', []) if isinstance(tag, str)]
            }

    def test_banana_pudding(self):
        """Run a basic sanity check on banana pudding recipes."""
        with self._lock:
            parsed = parse_recipe("src/recipes/banana_pudding.py")
            
            # Check recipe exists and is non-empty
            assert "name" in parsed, "Recipe name should be present"
            assert len(parsed) > 0, "Empty recipes are not allowed"

    def test_rot13_encryptor(self):
        """Run tests for ROT13 encryption functionality."""
        encrypter = rot13_encryptor()
        
        # Test case with correct input
        result = encrypter("test")
        assert result == "uryyb", f"Expected 'uryyb', got '{result}'"

    def test_encode_decode_word(self):
        """Test the encode/decode cycle for a word."""
        encoded_word = rot13_encryptor.encode_word("banana")
        
        # Encode back and verify it matches the original string (ROT-13 is an involution)
        decoded_back = encrypter.decode(encoded_word).encode('utf-8')
        
        assert decoded_back == "banana", f"Expected 'banana', got {decoded_back}"

    def test_rot13_encryptor_list(self):
        """Test ROT13 encryption on a list of words."""
        encrypted_words = [rot13_encryptor.encode_word(word) for
