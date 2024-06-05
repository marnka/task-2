import unittest
import sys
import io
from palindrome import is_palindrome
from palindrome import main

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


    def setUp(self):
        self.stdin_backup = sys.stdin
        self.stdout_backup = sys.stdout
        self.stderr_backup = sys.stderr
    
    def tearDown(self):
        sys.stdin = self.stdin_backup
        sys.stdout = self.stdout_backup
        sys.stderr = self.stderr_backup
    
    def test_main_without_errors(self):
        input_data = "radar\n"
        expected_output = "True\n"

        sys.stdin = io.StringIO(input_data)
        sys.stdout = io.StringIO()

        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 0)
        self.assertEqual(sys.stdout.getvalue(), expected_output)
    
    def test_main_with_errors(self):
        input_data = " "
        expected_error_message = "Error: Input cannot be empty\n"

        sys.stdin = io.StringIO()  # Змініть на цей рядок
        sys.stdin.write(input_data)
        sys.stdin.seek(0)
        sys.stdout = io.StringIO()
        sys.stderr = io.StringIO()

        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 1)
        self.assertEqual(sys.stderr.getvalue(), expected_error_message)


if __name__ == "__main__":
    unittest.main()
