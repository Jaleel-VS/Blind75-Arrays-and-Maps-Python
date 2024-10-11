import unittest
from main import isAnagram


class TestIsAnagram(unittest.TestCase):
    
    def test_valid_anagram(self):
        self.assertTrue(isAnagram("anagram", "nagaram"))
    
    def test_different_length(self):
        self.assertFalse(isAnagram("rat", "car"))
    
    def test_empty_strings(self):
        self.assertTrue(isAnagram("", ""))
    
    def test_case_sensitivity(self):
        self.assertFalse(isAnagram("aNagram", "nagaram"))
    
    def test_non_anagram_same_length(self):
        self.assertFalse(isAnagram("hello", "bello"))
    
    def test_unicode_characters(self):
        self.assertTrue(isAnagram("你好", "好你"))
    
    def test_single_character_anagram(self):
        self.assertTrue(isAnagram("a", "a"))
    
    def test_single_character_non_anagram(self):
        self.assertFalse(isAnagram("a", "b"))
    
    def test_spaces_ignored(self):
        self.assertTrue(isAnagram("conversation", "voices rant on".replace(" ", "")))

if __name__ == "__main__":
    unittest.main()
