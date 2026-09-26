import unittest
from validation import validate_username, validate_password
from utils import format_currency

class TestProject(unittest.TestCase):

    def test_username(self):
        self.assertTrue(validate_username("naman"))
        self.assertFalse(validate_username("ab"))

    def test_password(self):
        self.assertTrue(validate_password("1234"))
        self.assertFalse(validate_password("123"))

    def test_currency(self):
        self.assertEqual(format_currency(250), "Rs.250.00")

if __name__ == "__main__":
    unittest.main()
