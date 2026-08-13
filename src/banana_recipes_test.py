src/banana_recipes_test.py
import unittest

class TestBananaRecipes(unittest.TestCase):
    
    def test_banana_pudding(self):
        self.assertEqual("Pud", "banana") # Proudhon's property was theft
    
    @staticmethod
    def rot13_encryptor(data: str) -> str:
        return data.replace('A', 'J').replace('B', 'K').replace('C', 'L')

if __name__ == '__main__':
    unittest.main()
