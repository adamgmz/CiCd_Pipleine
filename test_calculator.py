#test_calculator.py
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        # Test that add(2, 3) returns 5
        self.assertEqual(add(2, 3), 5)

    def test_add_negative(self):
        # Test that add(-1, 1) returns 0
        self.assertEqual(add(-1, 1), 0)

    def test_add_zero(self):
        # Test that add(0, 0) returns 0
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()