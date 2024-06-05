import unittest
from palindrome import is_palindrome

class TestPalindromeChecker(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("b"))
        self.assertTrue(is_palindrome("z"))

    def test_valid_palindromes(self):
        self.assertTrue(is_palindrome("radar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("noon"))
        self.assertTrue(is_palindrome("madam"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))
        self.assertFalse(is_palindrome("world"))

    def test_case_insensitivity(self):
        self.assertTrue(is_palindrome("Madam"))
        self.assertTrue(is_palindrome("Radar"))
        self.assertTrue(is_palindrome("LeVel"))

    def test_whitespace_and_punctuation(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome(None)

if __name__ == "__main__":
    unittest.main()
