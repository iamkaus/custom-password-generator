import string
import unittest

from src.logic import generate_password  # Import the function to test


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password_min_length(self):
        result = generate_password(4, True, False, False, False)
        self.assertEqual(len(result), 4)

    def test_generate_password_max_length(self):
        result = generate_password(15, True, True, True, True)
        print("Generated Password:", ''.join(result))  # Print for manual inspection
        self.assertEqual(len(result), 15)

    def test_generate_password_all_characters(self):
        result = generate_password(10, True, True, True, True)
        print("Generated Password:", ''.join(result))  # Print the generated password for manual inspection
        self.assertEqual(len(result), 10)
        self.assertTrue(any(char.isupper() for char in result))
        self.assertTrue(any(char.islower() for char in result))
        self.assertTrue(any(char.isdigit() for char in result))  # This checks for digits
        self.assertTrue(any(char in string.punctuation for char in result))

    def test_no_character_types_selected(self):
        with self.assertRaises(ValueError):
            generate_password(10, False, False, False, False)

    def test_only_uppercase(self):
        result = generate_password(6, True, False, False, False)
        self.assertTrue(all(char.isupper() for char in result))


if __name__ == '__main__':
    unittest.main()
